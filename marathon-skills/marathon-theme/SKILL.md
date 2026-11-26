---
name: marathon-theme
description: A ready theme ("Marathon Jobsite") for slides, docs, reports and HTML artifacts in Marathon GC's colors and fonts. Use with pptx/docx/xlsx/web-artifacts skills when a Marathon piece needs a consistent look fast.
license: Adapted from anthropics/skills theme-factory (Apache-2.0)
---

# Marathon Jobsite Theme

Load `marathon-brand-guidelines` for the rules; this is the quick spec.

```json
{
  "name": "Marathon Jobsite",
  "colors": {
    "primary": "#A51C30",
    "background_dark": "#161414",
    "surface_dark": "#2A2626",
    "background_light": "#F4F1EE",
    "text_on_light": "#2A2626",
    "text_on_dark": "#F4F1EE",
    "positive": "#2E7D32",
    "warning": "#E0A100"
  },
  "fonts": { "heading": "Oswald", "body": "Inter", "fallback": "Arial" },
  "accents": ["hazard-stripe band", "crimson rule under headings", "M tile top-left"],
  "chart_series": ["#A51C30", "#2A2626", "#8C8580", "#D9A3AC"]
}
```

- Title slide: Black background, Oswald uppercase title in Stone, crimson keyword, stripe band at bottom.
- Content: Stone background, Charcoal text, one crimson accent per slide.
- Tables/sheets: Charcoal header row with Stone text, Stone banding, money right-aligned, totals bold.
- Status colors in job trackers: Booked = green, Estimate scheduled = amber, Lost = gray, New = crimson.
