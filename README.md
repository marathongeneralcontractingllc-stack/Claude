# Marathon GC — MCP Toolkit

The official [Model Context Protocol reference servers](https://github.com/modelcontextprotocol/servers),
installed, tuned and pre-configured for **Marathon General Contracting LLC** (Fall River, MA).

## Quick start

```bash
scripts/setup-mcp.sh        # clone (pinned), build, install everything
python3 scripts/test-mcp.py # start every server and call one tool on each
```

Open this folder in Claude Code and the servers in `.mcp.json` load automatically.
For Claude Desktop: `python3 scripts/claude-desktop-config.py` and paste the output into
`claude_desktop_config.json`.

Requires Node 18+, npm, git and [uv](https://docs.astral.sh/uv/).

## What's installed

| Server | What Marathon uses it for |
| --- | --- |
| `marathon-files` (filesystem) | Read/write job files in `marathon/` only: leads, estimates, contracts, snow-ice routes, marketing, sub paperwork (COIs, W-9s, lien waivers). |
| `marathon-memory` (memory) | Persistent knowledge graph, pre-seeded with Marathon's business facts, service area, 2026–27 Snow & Ice pricing, and compliance rules. Add customers, jobs and subs as you go. |
| `sequential-thinking` | Step-by-step reasoning for estimates, job scoping, scheduling around snow, margin checks. |
| `fetch` | Read web pages as clean Markdown: supplier prices, permit pages, competitor sites, city code. |
| `git` | Version history for this repo (every estimate/contract change is tracked). |
| `time` | Eastern time (America/New_York) for storm timing, 6-hour clearing windows, follow-up deadlines. |

`everything` is also built but not enabled — it is a protocol test server, not a business tool.

## Performance tuning applied

- **Built locally, no `npx`/`uvx` cold starts** — every server starts in ~0.2–2 s from prebuilt `dist/` and `.venv/`.
- **Pinned commit** (`c799c85`, Nov 18 2026) so updates never break you unannounced. Override with `MCP_SERVERS_REF=<sha>`.
- **Readability.js pre-installed** for the fetch server: better page extraction and no npm install at first use.
- **Fetch timeout 45 s** for slow supplier/municipal sites; private-IP guard left on.
- **Filesystem scoped** to `marathon/` only; **git scoped** to this repo only.
- **Thought logging off** for sequential-thinking (less stderr noise).
- **Timezone fixed** to America/New_York.

## Layout

```
marathon/
  leads/  estimates/  contracts/  snow-ice/  marketing/  subcontractors/
  memory/marathon-memory.jsonl   # knowledge graph
```

## Updating

```bash
MCP_SERVERS_REF=<new-commit> scripts/setup-mcp.sh && python3 scripts/test-mcp.py
```
