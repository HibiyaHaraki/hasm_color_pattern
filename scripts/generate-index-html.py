from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def extract_object_blocks(js_source: str) -> list[str]:
    array_start = js_source.find("[")
    array_end = js_source.rfind("];")
    if array_start == -1 or array_end == -1 or array_end <= array_start:
        raise ValueError("Could not find BASE_PATTERN_DEFINITIONS array in src/patterns.js")

    array_text = js_source[array_start:array_end]
    blocks: list[str] = []
    depth = 0
    start_index = -1

    for index, char in enumerate(array_text):
        if char == "{":
            if depth == 0:
                start_index = index
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0 and start_index != -1:
                blocks.append(array_text[start_index : index + 1])
                start_index = -1

    return blocks


def get_quoted_value(block: str, key: str) -> str | None:
    match = re.search(rf"\b{re.escape(key)}\s*:\s*\"([^\"]+)\"", block)
    return match.group(1) if match else None


def parse_patterns(patterns_path: Path) -> list[dict[str, str]]:
    source = patterns_path.read_text(encoding="utf-8")
    blocks = extract_object_blocks(source)

    parsed: list[dict[str, str]] = []
    for block in blocks:
        pattern_id = get_quoted_value(block, "id")
        main_color = get_quoted_value(block, "mainColor")
        text_color = get_quoted_value(block, "textColor")
        text_background_color = get_quoted_value(block, "textBackgroundColor")

        if not pattern_id or not main_color or not text_color or not text_background_color:
            continue

        label = (
            get_quoted_value(block, "label")
            or get_quoted_value(block, "markdownLabel")
            or pattern_id
        )

        parsed.append(
            {
                "id": pattern_id,
                "label": label,
                "mainColor": main_color,
                "textColor": text_color,
                "textBackgroundColor": text_background_color,
            }
        )

    if not parsed:
        raise ValueError("No patterns were parsed from src/patterns.js")

    return parsed


def build_html(patterns: list[dict[str, str]]) -> str:
    patterns_json = json.dumps(patterns, indent=6)
    template = """<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
  <title>Color Pattern Standalone</title>
  <style>
    :root {
      --main-color: #0a1561;
      --text-color: #d4d4d4;
      --text-bg-color: #1e1e1e;
    }

    * {
      box-sizing: border-box;
    }

    html,
    body {
      margin: 0;
      width: 100%;
      height: 100%;
    }

    body {
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      font-family: \"Avenir Next\", \"Segoe UI\", Tahoma, sans-serif;
      color: var(--text-color);
      background:
        radial-gradient(120% 90% at 10% 12%, color-mix(in srgb, var(--main-color) 40%, white), transparent 56%),
        radial-gradient(110% 95% at 88% 14%, color-mix(in srgb, var(--main-color) 30%, white), transparent 58%),
        radial-gradient(130% 110% at 48% 88%, color-mix(in srgb, var(--main-color) 20%, black), transparent 62%),
        linear-gradient(
          135deg,
          color-mix(in srgb, var(--text-bg-color) 90%, black) 0%,
          color-mix(in srgb, var(--text-bg-color) 76%, var(--main-color)) 48%,
          color-mix(in srgb, var(--text-bg-color) 88%, black) 100%
        );
      transition: background 560ms linear, color 560ms linear;
      overflow: hidden;
      position: relative;
      padding: 1.5rem;
    }

    .title {
      margin: 0;
      text-align: center;
      font-weight: 800;
      line-height: 1.2;
      font-size: clamp(1.6rem, 4.4vw, 4rem);
      letter-spacing: 0.015em;
      text-wrap: balance;
      transform: translateY(-0.6rem);
      transition: color 560ms linear, text-shadow 560ms linear;
      text-shadow: 0 12px 28px color-mix(in srgb, var(--main-color) 45%, transparent);
      position: relative;
      z-index: 2;
    }

    .pattern-name {
      display: inline-block;
      color: color-mix(in srgb, var(--main-color) 60%, var(--text-color));
      transition: color 560ms linear, opacity 0.6s ease, transform 0.6s ease;
      animation: nameReveal 0.65s ease;
      white-space: nowrap;
    }

    .copyright {
      position: fixed;
      bottom: 0.8rem;
      left: 50%;
      transform: translateX(-50%);
      margin: 0;
      font-size: clamp(0.74rem, 1.6vw, 0.9rem);
      letter-spacing: 0.03em;
      opacity: 0.8;
      color: color-mix(in srgb, var(--text-color) 90%, white 10%);
      transition: color 560ms linear;
      text-align: center;
      z-index: 2;
    }

    .pattern-sidebar {
      position: fixed;
      left: 1.15rem;
      top: 50%;
      transform: translateY(-50%);
      z-index: 2;
      width: min(34vw, 260px);
      max-height: 78vh;
      overflow: auto;
      padding: 0.85rem 0.8rem;
      border-radius: 12px;      
    }

    .pattern-list {
      margin: 0;
      padding: 0;
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.36rem;
    }

    .pattern-item {
      font-size: 0.8rem;
      letter-spacing: 0.02em;
      color: color-mix(in srgb, var(--text-color) 90%, white 10%);
      opacity: 0.2;
      transform: translateX(0);
      transition: opacity 560ms linear, transform 560ms linear, color 560ms linear;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .pattern-item.is-target {
      transform: translateX(4px);
    }

    body::before {
      content: \"\";
      position: absolute;
      inset: -18%;
      pointer-events: none;
      background:
        conic-gradient(
          from 150deg at 50% 50%,
          color-mix(in srgb, var(--main-color) 35%, transparent),
          color-mix(in srgb, var(--main-color) 16%, transparent),
          color-mix(in srgb, var(--main-color) 30%, transparent),
          color-mix(in srgb, var(--main-color) 12%, transparent),
          color-mix(in srgb, var(--main-color) 35%, transparent)
        );
      filter: blur(54px) saturate(110%);
      opacity: 0.36;
      transform: scale(1.04);
      transition: background 560ms linear, opacity 560ms linear;
      z-index: -1;
    }

    .title.switching .pattern-name {
      opacity: 0;
      transform: translateY(8px);
    }

    @keyframes nameReveal {
      from {
        opacity: 0;
        transform: translateY(8px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    @media (max-width: 640px) {
      .pattern-sidebar {
        width: calc(100% - 1rem);
        left: 0.5rem;
        top: auto;
        bottom: 3.1rem;
        transform: none;
        max-height: 26vh;
        padding: 0.55rem 0.6rem;
      }

      .pattern-item {
        font-size: 0.74rem;
      }

      .title {
        transform: translateY(-0.3rem);
      }

      .copyright {
        bottom: 0.65rem;
      }
    }
  </style>
</head>
<body>
  <aside class=\"pattern-sidebar\" aria-label=\"Color pattern list\">
    <ul id=\"pattern-list\" class=\"pattern-list\"></ul>
  </aside>
  <h1 id=\"title\" class=\"title\">This Color Pattern is <span id=\"pattern-name\" class=\"pattern-name\">Classic</span></h1>
  <p class=\"copyright\">Copyright (c) 2026 Hibiya Haraki</p>

  <script>
    const patterns = __PATTERNS_JSON__;

    const root = document.documentElement;
    const title = document.getElementById(\"title\");
    const patternName = document.getElementById(\"pattern-name\");
    const patternList = document.getElementById(\"pattern-list\");

    const STEP_PERCENT = 10;
    const STEP_INTERVAL_MS = 560;

    function hexToRgb(hex) {
      const normalized = hex.replace(\"#\", \"\");
      return {
        r: Number.parseInt(normalized.slice(0, 2), 16),
        g: Number.parseInt(normalized.slice(2, 4), 16),
        b: Number.parseInt(normalized.slice(4, 6), 16)
      };
    }

    function clamp(val) {
      return Math.max(0, Math.min(255, Math.round(val)));
    }

    function rgbToHex(r, g, b) {
      const toHex = (n) => clamp(n).toString(16).padStart(2, \"0\");
      return \"#\" + toHex(r) + toHex(g) + toHex(b);
    }

    function mixHex(firstHex, secondHex, ratio) {
      const first = hexToRgb(firstHex);
      const second = hexToRgb(secondHex);
      const r = Math.round(first.r + (second.r - first.r) * ratio);
      const g = Math.round(first.g + (second.g - first.g) * ratio);
      const b = Math.round(first.b + (second.b - first.b) * ratio);
      return rgbToHex(r, g, b);
    }

    function applyInterpolatedPattern(fromPattern, toPattern, progress) {
      const blendedMain = mixHex(fromPattern.mainColor, toPattern.mainColor, progress);
      const blendedText = mixHex(fromPattern.textColor, toPattern.textColor, progress);
      const blendedTextBg = mixHex(fromPattern.textBackgroundColor, toPattern.textBackgroundColor, progress);

      root.style.setProperty(\"--main-color\", blendedMain);
      root.style.setProperty(\"--text-color\", blendedText);
      root.style.setProperty(\"--text-bg-color\", blendedTextBg);
    }

    function setPatternName(label) {
      title.classList.add(\"switching\");
      window.setTimeout(() => {
        patternName.textContent = label;
        patternName.style.animation = \"none\";
        void patternName.offsetWidth;
        patternName.style.animation = \"nameReveal 0.45s ease\";
        title.classList.remove(\"switching\");
      }, 180);
    }

    if (patterns.length === 0) {
      throw new Error(\"No patterns available from src/patterns.js\");
    }

    const patternItems = patterns.map((pattern) => {
      const item = document.createElement(\"li\");
      item.className = \"pattern-item\";
      item.textContent = pattern.label;
      patternList.appendChild(item);
      return item;
    });

    let fromIndex = 0;
    let toIndex = patterns.length > 1 ? 1 : 0;
    let progressPercent = 0;

    root.style.setProperty(\"--main-color\", patterns[0].mainColor);
    root.style.setProperty(\"--text-color\", patterns[0].textColor);
    root.style.setProperty(\"--text-bg-color\", patterns[0].textBackgroundColor);
    setPatternName(patterns[fromIndex].label);

    function updatePatternListOpacity(fromIdx, toIdx, progress) {
      patternItems.forEach((item, idx) => {
        item.classList.remove(\"is-target\");

        if (idx === fromIdx && idx === toIdx) {
          item.style.opacity = \"1\";
          return;
        }

        if (idx === fromIdx) {
          const fromOpacity = 1 - progress * 0.72;
          item.style.opacity = String(Math.max(0.28, fromOpacity));
          return;
        }

        if (idx === toIdx) {
          const toOpacity = 0.28 + progress * 0.72;
          item.style.opacity = String(Math.min(1, toOpacity));
          item.classList.add(\"is-target\");
          return;
        }

        item.style.opacity = \"0.2\";
      });
    }

    function animateGradientBetweenPatterns() {
      const fromPattern = patterns[fromIndex];
      const toPattern = patterns[toIndex];
      const progress = progressPercent / 100;

      applyInterpolatedPattern(fromPattern, toPattern, progress);
      updatePatternListOpacity(fromIndex, toIndex, progress);

      if (progressPercent === 50) {
        setPatternName(patterns[toIndex].label);
      }

      progressPercent += STEP_PERCENT;
      if (progressPercent > 100) {
        progressPercent = 0;
        fromIndex = toIndex;
        toIndex = (toIndex + 1) % patterns.length;
        if (toIndex === fromIndex && patterns.length > 1) {
          toIndex = (toIndex + 1) % patterns.length;
        }
      }
    }

    animateGradientBetweenPatterns();
    window.setInterval(animateGradientBetweenPatterns, STEP_INTERVAL_MS);
  </script>
</body>
</html>
"""
    return template.replace("__PATTERNS_JSON__", patterns_json)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate standalone index.html from src/patterns.js"
    )
    parser.add_argument(
        "--patterns",
        type=Path,
        default=Path("src/patterns.js"),
        help="Path to src/patterns.js",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("index.html"),
        help="Output HTML path",
    )
    args = parser.parse_args()

    patterns = parse_patterns(args.patterns)
    html = build_html(patterns)
    args.output.write_text(html, encoding="utf-8")
    print(f"Generated {args.output} from {args.patterns} ({len(patterns)} patterns).")


if __name__ == "__main__":
    main()
