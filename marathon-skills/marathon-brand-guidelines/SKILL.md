---
name: marathon-brand-guidelines
description: Applies Marathon General Contracting's brand (crimson/charcoal colors, Oswald + Inter type, hazard stripe, M-tile logo, "Built to go the distance.") to any document, deck, flyer, door hanger, social graphic, quote or web page. Use whenever something is made for or about Marathon GC or Marathon Snow & Ice.
license: Adapted from anthropics/skills brand-guidelines (Apache-2.0)
---

# Marathon GC Brand Styling

Marathon General Contracting LLC, Fall River, MA. Sub-brand: Marathon Snow & Ice. Marathon only: never mix in Howard Home Solutions names, logos, accounts or customers.

## Colors

| Token | Hex | Use |
| --- | --- | --- |
| Crimson | `#A51C30` | Primary accent, CTAs, the M tile, headline highlights |
| Charcoal | `#2A2626` | Body text on light, secondary dark panels |
| Black | `#161414` | Dark backgrounds, hazard-stripe partner |
| Stone | `#F4F1EE` | Light backgrounds, cards, text on dark |
| White | `#FFFFFF` | Text on crimson, logo "M" |

Rules: crimson is an accent, not a background for long text. Keep contrast at WCAG AA (Stone or White on Crimson/Black; Charcoal on Stone). No gradients, no extra brand colors.

## Typography

- Headlines: **Oswald**, bold, UPPERCASE, slight letter-spacing (fallback: Arial Narrow, Arial).
- Body: **Inter** regular/medium (fallback: Arial).
- python-pptx / docx: headings 24pt+ Oswald, body 11–14pt Inter. Google Fonts links are fine for HTML.

## Signature assets (repeat everywhere)

- **M tile**: crimson square, white "M" under a roof peak, beside the MARATHON wordmark. Use the logo-pack files; never redraw, recolor, stretch or add effects. If no file is available, leave a labeled placeholder rather than inventing a logo.
- **Hazard stripe**: 45° crimson/black stripes, used as a thin top or bottom band (CSS: `repeating-linear-gradient(45deg,#A51C30 0 14px,#161414 14px 28px)`).
- Tagline: **"Built to go the distance."**
- Lines: "One crew. One contract." / "Text SNOW to (857) 320-5186."

## Required footer on customer-facing pieces

`Marathon General Contracting LLC · MA HIC #218125 · Licensed & Insured · (857) 320-5186 · marathongeneralcontracting.com`

Never print the street address (home office). Never print a CSL number unless Nicholas provides it. Never claim years in business, job counts, ratings or awards that Nicholas has not given.

## Layout habits

- One idea, one offer, one call to action per piece.
- Benefit first, company second. Phone or link on every piece; add `?src=` tracking (`flyer`, `facebook`, `google`, `nextdoor`, `fbads`).
- Photos: real job photos only, no house numbers or addresses visible.

## Applying it

- PPTX: Black title slides with the stripe band, Stone content slides, crimson accents for shapes (cycle crimson → charcoal).
- DOCX/PDF: Stone or white page, crimson rule under the header, Oswald headings, the required footer.
- HTML: define the hex values above as CSS tokens; dark mode uses Black/Stone swapped.
