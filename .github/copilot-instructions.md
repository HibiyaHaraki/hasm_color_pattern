# Copilot instructions for hasm_color_patterns

## Color contrast rule
Each pattern defines `mainColor`, `textColor`, and `textBackgroundColor`. `textBackgroundColor` is meant to be a
dark/neutral surface behind text, not a variant of `mainColor`. Never set `textBackgroundColor` (or any
background paired with `textColor`) to `mainColor` or a close tint/shade of it — this produces low-contrast,
hard-to-read text (e.g. main-colored text on a main-colored background).

When adding or editing patterns:
- Keep `textColor` and its paired background at a high contrast ratio (aim for WCAG AA, ~4.5:1 for normal text).
- `textBackgroundColor` should stay close to the existing dark/neutral tones already used in `src/patterns.js`
  (near-black or near-white), not a saturated hue derived from `mainColor`.
- `mainColor` is for large surfaces/accents (buttons, headers), not for text-on-background combinations.
