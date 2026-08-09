# @hasm/color-patterns

Shared color pattern definitions and helpers for both hasm and hasm_markdown.

## Purpose

Single source of truth for selectable color patterns.

- hasm uses full theme token objects
- hasm_markdown uses lightweight pattern options and CSS variables

---

## Installation

```bash
npm install ../hasm_color_patterns
```

If the submodule location differs, adjust the relative path.

---

## Exports

| Export | Type | Description |
|---|---|---|
| `COLOR_PATTERNS` | `Array` | All resolved pattern objects (id, label, markdownLabel, colors) |
| `COLOR_PATTERN_OPTIONS` | `Array` | Lightweight list for UI dropdowns (id, label, markdownLabel) |
| `DEFAULT_COLOR_PATTERN` | `string` | The default pattern id (`"classic"`) |
| `isValidColorPattern(id)` | `function` | Returns `true` if the id matches a known pattern |
| `getPatternById(id, fallbackId?)` | `function` | Returns a full pattern object, falling back to `fallbackId` or `"classic"` |
| `getThemeVariables(id, fallbackId?)` | `function` | Returns CSS custom properties for use in a UI theme |
| `getMarkdownThemeVariables(id, fallbackId?)` | `function` | Returns the three core CSS variables used by the markdown renderer |
| `buildThemeClassCss(rootSelector?, fallbackId?)` | `function` | Generates a full CSS string with per-pattern class selectors |

---

## Available Patterns

| id | Label | Description |
|---|---|---|
| `classic` | Classic | Classic Blue (default) |
| `sunrise` | Sunrise | Sunrise Orange |
| `forest` | Forest | Forest Green |
| `dawn` | Dawn | Dawn |
| `copper` | Copper | Copper |
| `pine` | Pine | Pine |
| `ocean` | Ocean | Ocean Cyan |
| `arctic` | Arctic | Arctic |
| `slate` | Slate | Slate Gray |
| `charcoal` | Charcoal | Charcoal |
| `coffee` | Coffee | Coffee Brown |
| `sand` | Sand | Sand |
| `emerald` | Emerald | Emerald Teal |
| `teal-night` | Teal Night | Teal Night |
| `midnight` | Midnight | Midnight Navy |
| `royal` | Royal | Royal |
| `high-contrast` | High Contrast | High Contrast |

---

## Usage

### 1. Get all patterns for a UI dropdown

```js
import { COLOR_PATTERN_OPTIONS } from "@hasm/color-patterns";

// [{ id: "classic", label: "Classic", markdownLabel: "Classic Blue" }, ...]
console.log(COLOR_PATTERN_OPTIONS);
```

### 2. Validate a user-supplied pattern id

```js
import { isValidColorPattern } from "@hasm/color-patterns";

const userChoice = "ocean";
if (!isValidColorPattern(userChoice)) {
  throw new Error(`Unknown pattern: ${userChoice}`);
}
```

### 3. Apply CSS custom properties to a component

`getThemeVariables` returns an object of CSS variable names → values that you can set on a DOM element or inject into a `<style>` block.

```js
import { getThemeVariables } from "@hasm/color-patterns";

const vars = getThemeVariables("ocean");
// {
//   "--theme-primary":        "#0a4f73",
//   "--theme-secondary":      "#...",
//   "--theme-surface":        "#...",
//   "--theme-text":           "#d8f3ff",
//   "--theme-muted":          "rgba(...)",
//   "--theme-border":         "rgba(...)",
//   "--theme-soft":           "rgba(...)",
//   "--theme-textbackground": "#0c1f2a",
//   "--theme-input-bg":       "rgba(...)",
//   "--theme-input-text":     "#d8f3ff",
//   "--theme-success":        "#...",
//   "--theme-danger":         "#..."
// }

const root = document.documentElement;
Object.entries(vars).forEach(([name, value]) => {
  root.style.setProperty(name, value);
});
```

If the supplied id is unknown it automatically falls back to `"classic"` (or a custom `fallbackId`):

```js
const vars = getThemeVariables("unknown-id", "midnight");
```

### 4. Generate CSS for a markdown renderer

`getMarkdownThemeVariables` returns only the three variables consumed by the markdown renderer:

```js
import { getMarkdownThemeVariables } from "@hasm/color-patterns";

const vars = getMarkdownThemeVariables("forest");
// {
//   "--main-color":           "#1e5b2b",
//   "--text-color":           "#dff7e4",
//   "--textbackground-color": "#102518"
// }
```

### 5. Generate a full theme CSS stylesheet

`buildThemeClassCss` emits CSS that scopes each pattern to a class on a root element.

```js
import { buildThemeClassCss } from "@hasm/color-patterns";

const css = buildThemeClassCss(".MarkdownViewer");
// Produces:
// :root { --main-color: ...; --text-color: ...; --textbackground-color: ...; }
// .MarkdownViewer.theme-classic { --main-color: #0a1561; ... }
// .MarkdownViewer.theme-sunrise { --main-color: #8a2d0a; ... }
// ... (one block per pattern)

const styleEl = document.createElement("style");
styleEl.textContent = css;
document.head.appendChild(styleEl);
```

Switch themes at runtime by toggling the class on the root element:

```js
rootEl.className = rootEl.className.replace(/\btheme-\S+/, "");
rootEl.classList.add(`theme-${selectedPatternId}`);
```

### 6. Access raw color values from a pattern

```js
import { getPatternById } from "@hasm/color-patterns";

const pattern = getPatternById("royal");
console.log(pattern.id);                   // "royal"
console.log(pattern.label);               // "Royal"
console.log(pattern.colors.mainColor);    // "#1e3a8a"
console.log(pattern.colors.textColor);    // "#dbeafe"
console.log(pattern.colors.successColor); // mixed hex
console.log(pattern.colors.dangerColor);  // mixed hex
```

---

## Color Object Shape

Every `pattern.colors` object contains:

| Property | Description |
|---|---|
| `mainColor` | Primary brand / accent color |
| `textColor` | Main readable text color |
| `textBackgroundColor` | Background behind text content |
| `secondaryColor` | Blended secondary accent (22 % toward textColor) |
| `surfaceColor` | Card / surface background (defaults to textBackgroundColor) |
| `mutedColor` | Subdued text — textColor at 74 % opacity |
| `borderColor` | Subtle borders — textColor at 28 % opacity |
| `softColor` | Semi-transparent overlay — textBackgroundColor at 86 % opacity |
| `inputBgColor` | Input field background — textBackgroundColor at 74 % opacity |
| `inputTextColor` | Input field text (defaults to textColor) |
| `successColor` | Success state — mainColor blended 58 % toward `#22c55e` |
| `dangerColor` | Danger/error state — mainColor blended 62 % toward `#ef4444` |

---

## Suggested local flow before submodule wiring

1. Create remote repo for this folder.
2. Commit and push this repository.
3. Add as submodule in hasm.
4. Add as submodule in hasm_markdown.
5. In both apps, install local package from the submodule path.
