import { COLOR_PATTERNS, getThemeVariables } from "../src/index.js";

const firstPattern = COLOR_PATTERNS[0];
const themeVariables = getThemeVariables(firstPattern.id);

if (!themeVariables["--theme-primary"]) {
  throw new Error("Missing --theme-primary variable");
}

console.log("hasm usage check ok", firstPattern.id, Object.keys(themeVariables).length);
