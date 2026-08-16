const BASE_PATTERN_DEFINITIONS = [
  { id: "classic", label: "Classic", markdownLabel: "Classic Blue", mainColor: "#0a1561", textColor: "#d4d4d4", textBackgroundColor: "#1e1e1e" },
  { id: "sunrise", label: "Sunrise", markdownLabel: "Sunrise Orange", mainColor: "#8a2d0a", textColor: "#ffe9dc", textBackgroundColor: "#2a140e" },
  { id: "forest", label: "Forest", markdownLabel: "Forest Green", mainColor: "#1e5b2b", textColor: "#dff7e4", textBackgroundColor: "#102518" },
  { id: "dawn", label: "Dawn", markdownLabel: "Dawn", mainColor: "#7b341e", textColor: "#fff1e8", textBackgroundColor: "#2f1610" },
  { id: "copper", label: "Copper", markdownLabel: "Copper", mainColor: "#7c2d12", textColor: "#ffedd5", textBackgroundColor: "#2b1a13" },
  { id: "pine", label: "Pine", markdownLabel: "Pine", mainColor: "#14532d", textColor: "#dcfce7", textBackgroundColor: "#0e2418" },
  { id: "ocean", label: "Ocean", markdownLabel: "Ocean Cyan", mainColor: "#0a4f73", textColor: "#d8f3ff", textBackgroundColor: "#0c1f2a" },
  { id: "arctic", label: "Arctic", markdownLabel: "Arctic", mainColor: "#155e75", textColor: "#ecfeff", textBackgroundColor: "#10222a" },
  { id: "slate", label: "Slate", markdownLabel: "Slate Gray", mainColor: "#334155", textColor: "#e2e8f0", textBackgroundColor: "#111827" },
  { id: "charcoal", label: "Charcoal", markdownLabel: "Charcoal", mainColor: "#374151", textColor: "#f3f4f6", textBackgroundColor: "#111315" },
  { id: "coffee", label: "Coffee", markdownLabel: "Coffee Brown", mainColor: "#5a3b2e", textColor: "#f5e8dc", textBackgroundColor: "#2a1a14" },
  { id: "sand", label: "Sand", markdownLabel: "Sand", mainColor: "#92400e", textColor: "#fef3c7", textBackgroundColor: "#2e1c12" },
  { id: "emerald", label: "Emerald", markdownLabel: "Emerald Teal", mainColor: "#0f766e", textColor: "#d1fae5", textBackgroundColor: "#062b28" },
  { id: "teal-night", label: "Teal Night", markdownLabel: "Teal Night", mainColor: "#0f766e", textColor: "#ccfbf1", textBackgroundColor: "#05201f" },
  { id: "midnight", label: "Midnight", markdownLabel: "Midnight Navy", mainColor: "#1e293b", textColor: "#cbd5e1", textBackgroundColor: "#020617" },
  { id: "royal", label: "Royal", markdownLabel: "Royal", mainColor: "#1e3a8a", textColor: "#dbeafe", textBackgroundColor: "#0b1536" },
  { id: "high-contrast", label: "High Contrast", markdownLabel: "High Contrast", mainColor: "#000000", textColor: "#ffffff", textBackgroundColor: "#1a1a1a", overrides: { secondaryColor: "#3b3b3b", borderColor: "rgba(255, 255, 255, 0.58)", mutedColor: "rgba(255, 255, 255, 0.88)", softColor: "rgba(26, 26, 26, 0.94)", inputBgColor: "rgba(26, 26, 26, 0.94)" } },
  { id: "classic-light", label: "Classic Light", markdownLabel: "Classic Light", mainColor: "#0a1561", textColor: "#0f172a", textBackgroundColor: "#f8fafc", overrides: { secondaryColor: "#1f2a44", borderColor: "rgba(15, 23, 42, 0.22)", mutedColor: "rgba(15, 23, 42, 0.72)", softColor: "rgba(248, 250, 252, 0.9)", inputBgColor: "rgba(255, 255, 255, 0.86)" } },
  { id: "sunrise-light", label: "Sunrise Light", markdownLabel: "Sunrise Light", mainColor: "#8a2d0a", textColor: "#3a1c11", textBackgroundColor: "#fff7ed", overrides: { secondaryColor: "#5b2a13", borderColor: "rgba(58, 28, 17, 0.18)", mutedColor: "rgba(58, 28, 17, 0.7)", softColor: "rgba(255, 247, 237, 0.92)", inputBgColor: "rgba(255, 255, 255, 0.84)" } },
  { id: "forest-light", label: "Forest Light", markdownLabel: "Forest Light", mainColor: "#1e5b2b", textColor: "#12311f", textBackgroundColor: "#f0fdf4", overrides: { secondaryColor: "#204d30", borderColor: "rgba(18, 49, 31, 0.18)", mutedColor: "rgba(18, 49, 31, 0.72)", softColor: "rgba(240, 253, 244, 0.92)", inputBgColor: "rgba(255, 255, 255, 0.84)" } },
  { id: "ocean-light", label: "Ocean Light", markdownLabel: "Ocean Light", mainColor: "#0a4f73", textColor: "#082f49", textBackgroundColor: "#f0f9ff", overrides: { secondaryColor: "#0c5774", borderColor: "rgba(8, 47, 73, 0.2)", mutedColor: "rgba(8, 47, 73, 0.72)", softColor: "rgba(240, 249, 255, 0.92)", inputBgColor: "rgba(255, 255, 255, 0.84)" } },
  { id: "slate-light", label: "Slate Light", markdownLabel: "Slate Light", mainColor: "#334155", textColor: "#0f172a", textBackgroundColor: "#f8fafc", overrides: { secondaryColor: "#475569", borderColor: "rgba(15, 23, 42, 0.2)", mutedColor: "rgba(15, 23, 42, 0.72)", softColor: "rgba(248, 250, 252, 0.92)", inputBgColor: "rgba(255, 255, 255, 0.86)" } },
  { id: "royal-light", label: "Royal Light", markdownLabel: "Royal Light", mainColor: "#1e3a8a", textColor: "#111827", textBackgroundColor: "#eff6ff", overrides: { secondaryColor: "#1f3f84", borderColor: "rgba(17, 24, 39, 0.2)", mutedColor: "rgba(17, 24, 39, 0.72)", softColor: "rgba(239, 246, 255, 0.94)", inputBgColor: "rgba(255, 255, 255, 0.86)" } },
  { id: "high-contrast-light", label: "High Contrast Light", markdownLabel: "High Contrast Light", mainColor: "#111827", textColor: "#111827", textBackgroundColor: "#ffffff", overrides: { secondaryColor: "#374151", borderColor: "rgba(17, 24, 39, 0.36)", mutedColor: "rgba(17, 24, 39, 0.76)", softColor: "rgba(255, 255, 255, 0.9)", inputBgColor: "rgba(243, 244, 246, 0.96)" } }
];

export { BASE_PATTERN_DEFINITIONS };
