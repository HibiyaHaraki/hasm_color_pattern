# hasm_color_patterns

Shared color pattern definitions for both hasm and hasm_markdown.

## Purpose

This repository is a single source of truth for selectable color patterns.

- hasm can use full theme token objects
- hasm_markdown can use lightweight pattern options and CSS variables

## What is included

- `COLOR_PATTERNS`: full palette objects with derived colors
- `COLOR_PATTERN_OPTIONS`: ID and labels for selection lists
- `DEFAULT_COLOR_PATTERN`
- `isValidColorPattern(patternId)`
- `getPatternById(patternId, fallbackId)`
- `getThemeVariables(patternId)`: CSS variable map for hasm
- `getMarkdownThemeVariables(patternId)`: CSS variable map for hasm_markdown
- `buildThemeClassCss(rootSelector)`: generates `.theme-<id>` class CSS text

## Example usage in hasm

```js
import { COLOR_PATTERNS, getThemeVariables } from "@hasm/color-patterns";

const themeStyle = getThemeVariables(activePatternId);
```

## Example usage in hasm_markdown

```js
import {
  COLOR_PATTERN_OPTIONS,
  DEFAULT_COLOR_PATTERN,
  isValidColorPattern,
} from "@hasm/color-patterns";
```

```js
import { buildThemeClassCss } from "@hasm/color-patterns";

const css = buildThemeClassCss(".Main");
```

## Suggested local flow before submodule wiring

1. Create remote repo for this folder.
2. Commit and push this repository.
3. Add as submodule in hasm.
4. Add as submodule in hasm_markdown.
5. In both apps, install local package from the submodule path.

## Install from submodule path (example)

```bash
npm install ../hasm_color_patterns
```

If submodule location differs, adjust the relative path.
