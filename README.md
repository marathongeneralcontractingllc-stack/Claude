# Marathon GC – Claude Skills

Claude skills for **Marathon General Contracting LLC** (Fall River, MA), plus Anthropic's open-source skills from [anthropics/skills](https://github.com/anthropics/skills) (Apache-2.0, vendored in `vendor/anthropic-skills`, commit in `UPSTREAM_COMMIT`).

## Marathon skills (`marathon-skills/`)

| Skill | What it does |
| --- | --- |
| `marathon-brand-guidelines` | Crimson/charcoal colors, Oswald + Inter, M tile, hazard stripe, required footer |
| `marathon-theme` | "Marathon Jobsite" theme spec for decks, docs, sheets and web pages |
| `marathon-internal-comms` | Monday brief (3P), customer job updates, storm-day messages, sub/crew messages, newsletter |
| `marathon-job-documents` | Good/better/best quotes, c.142A contract checklist, change orders, snow agreement, job cost sheet |

`marathon-gc-agent` and `marathon-bid-estimator` hold private business details, so they are **not** in this public repo. They are already synced to Claude from the claude.ai account.

## Install

**Claude Desktop / claude.ai:** Settings → Capabilities → Skills → *Upload skill*, and upload each zip from `dist/` (one skill per zip). The Anthropic docx/xlsx/pptx/pdf skills are already built into Claude; the `anthropic-*.zip` files are only needed for the API or other agents.

**Claude Code (desktop app or terminal):**
```
/plugin marketplace add marathongeneralcontractingllc-stack/claude
/plugin install marathon-gc@marathon-skills
/plugin install document-skills@marathon-skills
```
Or copy folders manually: `cp -r marathon-skills/* ~/.claude/skills/`.

## Updating upstream
```
git clone --depth 1 https://github.com/anthropics/skills.git /tmp/as && rsync -a --delete /tmp/as/skills/ vendor/anthropic-skills/skills/
```
