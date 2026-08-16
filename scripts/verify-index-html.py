from __future__ import annotations

import json
import importlib.util
import re
import sys
from pathlib import Path


def load_parse_patterns(script_path: Path):
    spec = importlib.util.spec_from_file_location("generate_index_html", script_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Failed to load generator module from {script_path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.parse_patterns


def extract_embedded_patterns(index_html: str) -> list[dict[str, str]]:
    match = re.search(
        r"const\s+patterns\s*=\s*(\[[\s\S]*?\]);",
        index_html,
        flags=re.MULTILINE,
    )
    if not match:
        raise ValueError("Could not find embedded patterns array in index.html")

    return json.loads(match.group(1))


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    generator_path = repo_root / "scripts" / "generate-index-html.py"
    patterns_path = repo_root / "src" / "patterns.js"
    index_path = repo_root / "index.html"

    parse_patterns = load_parse_patterns(generator_path)
    source_patterns = parse_patterns(patterns_path)
    index_text = index_path.read_text(encoding="utf-8")
    embedded_patterns = extract_embedded_patterns(index_text)

    source_ids = [pattern["id"] for pattern in source_patterns]
    embedded_ids = [pattern.get("id") for pattern in embedded_patterns]

    missing_ids = [pattern_id for pattern_id in source_ids if pattern_id not in embedded_ids]
    extra_ids = [pattern_id for pattern_id in embedded_ids if pattern_id not in source_ids]

    if missing_ids or extra_ids:
        print("Pattern mismatch between src/patterns.js and index.html")
        if missing_ids:
            print(f"Missing in index.html: {', '.join(missing_ids)}")
        if extra_ids:
            print(f"Unexpected in index.html: {', '.join(str(i) for i in extra_ids)}")
        return 1

    if len(embedded_patterns) != len(source_patterns):
        print(
            "Pattern count mismatch: "
            f"src={len(source_patterns)} index={len(embedded_patterns)}"
        )
        return 1

    print(
        "index.html contains all available color patterns "
        f"({len(source_patterns)} patterns)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
