import {
  COLOR_PATTERN_OPTIONS,
  DEFAULT_COLOR_PATTERN,
  buildThemeClassCss,
  isValidColorPattern
} from "../src/index.js";

if (!isValidColorPattern(DEFAULT_COLOR_PATTERN)) {
  throw new Error("Default pattern is not valid");
}

if (!isValidColorPattern("classic-light")) {
  throw new Error("Expected classic-light pattern to be registered");
}

const css = buildThemeClassCss(".Main");
if (!css.includes(".Main.theme-classic")) {
  throw new Error("Expected classic class in generated CSS");
}

console.log("hasm_markdown usage check ok", COLOR_PATTERN_OPTIONS.length);
