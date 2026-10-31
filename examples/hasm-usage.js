import { COLOR_PATTERNS, getThemeVariables } from "../src/index.js";
import { createLogger } from "../hasm_logger/src/react/logger.js";

const logger = createLogger("hasm-color-patterns");
const firstPattern = COLOR_PATTERNS[0];
const themeVariables = getThemeVariables(firstPattern.id);

if (!themeVariables["--theme-primary"]) {
  throw new Error("Missing --theme-primary variable");
}

logger.info("hasm usage check ok", firstPattern.id, Object.keys(themeVariables).length);
