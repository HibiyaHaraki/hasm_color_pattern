const BASE_PATTERN_DEFINITIONS = [
  { id: "classic", label: "Classic", markdownLabel: "Classic Blue", mainColor: "#3157c8", textColor: "#f8fafc", textBackgroundColor: "#111827" },
  { id: "sunrise", label: "Sunrise", markdownLabel: "Sunrise Orange", mainColor: "#c2410c", textColor: "#fff7ed", textBackgroundColor: "#1c100d" },
  { id: "forest", label: "Forest", markdownLabel: "Forest Green", mainColor: "#276749", textColor: "#f0fdf4", textBackgroundColor: "#0d1b13" },
  { id: "dawn", label: "Dawn", markdownLabel: "Dawn", mainColor: "#b45309", textColor: "#fff7ed", textBackgroundColor: "#21130d" },
  { id: "copper", label: "Copper", markdownLabel: "Copper", mainColor: "#c2410c", textColor: "#fff7ed", textBackgroundColor: "#1f120d" },
  { id: "pine", label: "Pine", markdownLabel: "Pine", mainColor: "#166534", textColor: "#f0fdf4", textBackgroundColor: "#0b1710" },
  { id: "ocean", label: "Ocean", markdownLabel: "Ocean Cyan", mainColor: "#0369a1", textColor: "#f0f9ff", textBackgroundColor: "#0b1720" },
  { id: "arctic", label: "Arctic", markdownLabel: "Arctic", mainColor: "#0e7490", textColor: "#ecfeff", textBackgroundColor: "#0c1b22" },
  { id: "slate", label: "Slate", markdownLabel: "Slate Gray", mainColor: "#475569", textColor: "#f1f5f9", textBackgroundColor: "#111827" },
  { id: "charcoal", label: "Charcoal", markdownLabel: "Charcoal", mainColor: "#4b5563", textColor: "#f9fafb", textBackgroundColor: "#101214" },
  { id: "coffee", label: "Coffee", markdownLabel: "Coffee Brown", mainColor: "#6f4e37", textColor: "#fff7ed", textBackgroundColor: "#1b1511" },
  { id: "sand", label: "Sand", markdownLabel: "Sand", mainColor: "#92400e", textColor: "#fffbeb", textBackgroundColor: "#21180e" },
  { id: "emerald", label: "Emerald", markdownLabel: "Emerald Teal", mainColor: "#0f766e", textColor: "#ecfdf5", textBackgroundColor: "#071d1b" },
  { id: "teal-night", label: "Teal Night", markdownLabel: "Teal Night", mainColor: "#115e59", textColor: "#ccfbf1", textBackgroundColor: "#071c1a" },
  { id: "midnight", label: "Midnight", markdownLabel: "Midnight Navy", mainColor: "#334155", textColor: "#e2e8f0", textBackgroundColor: "#080d18" },
  { id: "royal", label: "Royal", markdownLabel: "Royal", mainColor: "#4338ca", textColor: "#eef2ff", textBackgroundColor: "#0e1027" },
  { id: "high-contrast", label: "High Contrast", markdownLabel: "High Contrast", mainColor: "#000000", textColor: "#ffffff", textBackgroundColor: "#1a1a1a", overrides: { secondaryColor: "#3b3b3b", borderColor: "rgba(255, 255, 255, 0.58)", mutedColor: "rgba(255, 255, 255, 0.88)", softColor: "rgba(26, 26, 26, 0.94)", inputBgColor: "rgba(26, 26, 26, 0.94)" } },
  { id: "classic-light", label: "Classic Light", markdownLabel: "Classic Light", mainColor: "#3157c8", textColor: "#0f172a", textBackgroundColor: "#f8fafc", overrides: { secondaryColor: "#1f2a44", borderColor: "rgba(15, 23, 42, 0.22)", mutedColor: "rgba(15, 23, 42, 0.72)", softColor: "rgba(248, 250, 252, 0.9)", inputBgColor: "rgba(255, 255, 255, 0.86)" } },
  { id: "sunrise-light", label: "Sunrise Light", markdownLabel: "Sunrise Light", mainColor: "#c2410c", textColor: "#3a1c11", textBackgroundColor: "#fff7ed", overrides: { secondaryColor: "#5b2a13", borderColor: "rgba(58, 28, 17, 0.18)", mutedColor: "rgba(58, 28, 17, 0.7)", softColor: "rgba(255, 247, 237, 0.92)", inputBgColor: "rgba(255, 255, 255, 0.84)" } },
  { id: "forest-light", label: "Forest Light", markdownLabel: "Forest Light", mainColor: "#276749", textColor: "#12311f", textBackgroundColor: "#f0fdf4", overrides: { secondaryColor: "#204d30", borderColor: "rgba(18, 49, 31, 0.18)", mutedColor: "rgba(18, 49, 31, 0.72)", softColor: "rgba(240, 253, 244, 0.92)", inputBgColor: "rgba(255, 255, 255, 0.84)" } },
  { id: "ocean-light", label: "Ocean Light", markdownLabel: "Ocean Light", mainColor: "#0369a1", textColor: "#082f49", textBackgroundColor: "#f0f9ff", overrides: { secondaryColor: "#0c5774", borderColor: "rgba(8, 47, 73, 0.2)", mutedColor: "rgba(8, 47, 73, 0.72)", softColor: "rgba(240, 249, 255, 0.92)", inputBgColor: "rgba(255, 255, 255, 0.84)" } },
  { id: "slate-light", label: "Slate Light", markdownLabel: "Slate Light", mainColor: "#475569", textColor: "#0f172a", textBackgroundColor: "#f8fafc", overrides: { secondaryColor: "#475569", borderColor: "rgba(15, 23, 42, 0.2)", mutedColor: "rgba(15, 23, 42, 0.72)", softColor: "rgba(248, 250, 252, 0.92)", inputBgColor: "rgba(255, 255, 255, 0.86)" } },
  { id: "royal-light", label: "Royal Light", markdownLabel: "Royal Light", mainColor: "#4338ca", textColor: "#111827", textBackgroundColor: "#eef2ff", overrides: { secondaryColor: "#1f3f84", borderColor: "rgba(17, 24, 39, 0.2)", mutedColor: "rgba(17, 24, 39, 0.72)", softColor: "rgba(239, 246, 255, 0.94)", inputBgColor: "rgba(255, 255, 255, 0.86)" } },
  { id: "high-contrast-light", label: "High Contrast Light", markdownLabel: "High Contrast Light", mainColor: "#111827", textColor: "#111827", textBackgroundColor: "#ffffff", overrides: { secondaryColor: "#374151", borderColor: "rgba(17, 24, 39, 0.36)", mutedColor: "rgba(17, 24, 39, 0.76)", softColor: "rgba(255, 255, 255, 0.9)", inputBgColor: "rgba(243, 244, 246, 0.96)" } }
];

export { BASE_PATTERN_DEFINITIONS };
