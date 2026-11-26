# Claude Code picks for Marathon GC

Hand-picked from [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) (about 260 resources, Nov 2026). That list is licensed CC BY-NC-ND 4.0, so it isn't copied here. This page is our own short list of links and notes. Browse the full list at the link above.

The **Built in** column notes where this repo already includes a small version of the idea, so there's nothing to install for that part.

## Install first (on Nick's PC)

| Tool | Why it helps Marathon | Built in |
| --- | --- | --- |
| [Official Plugin Directory](https://github.com/anthropics/claude-plugins-official) | Anthropic's vetted plugins. Install from inside Claude Code with `/plugin`. Start here before trying third-party tools. | — |
| [Anthropic Agent Skills](https://github.com/anthropics/skills) | Official skills for documents (docx, xlsx, pdf, pptx): bid forms, sub agreements and proposals. | — |
| [ccusage](https://github.com/ccusage/ccusage) | `npx ccusage` shows what Claude Code is costing, with no install. Keeps AI spend visible the same way Meta spend is. | — |
| [Claude Code Safety Net](https://github.com/kenryu42/claude-code-safety-net) | Catches destructive git and file commands before they run. | Yes: `.claude/hooks/marathon_guard.py` |
| [Agent Guard](https://github.com/JeongJaeSoon/agent-guard) | Real-time guardrails that stop secrets leaking into commits. This repo is public, so it matters here. | Yes: the guard hook blocks EIN-, phone- and address-like strings in commits |
| [ccstatusline](https://github.com/sirmalloc/ccstatusline) or [Claude HUD](https://github.com/jarrodwatts/claude-hud) | A richer status line covering context, usage and git. | Basic version: `.claude/statusline.sh` |

## Worth a look

| Tool | Use for Marathon |
| --- | --- |
| [anotifier](https://github.com/DevinoSolutions/anotifier-for-claude-codex-cursor) | Desktop and free phone push when a long Claude job (bid takeoff, sub search) finishes or needs approval. Useful when Nick is on a site walk. |
| [Claude CLI ↔ Telegram](https://github.com/Imolatte/claude-cli-telegram) / [WhatsApp Channel Plugin](https://github.com/Rich627/whatsapp-claude-plugin) | Drive Claude from the phone in the field. Keep approvals with Nick, and don't link the customer-facing number. |
| [VoiceMode](https://github.com/mbailey/voicemode) | Talk to Claude hands-free from the truck. |
| [Avoid AI Writing](https://github.com/conorbronsdon/avoid-ai-writing) | Cleans "AI-sounding" text out of GC emails, proposals and ads before Nick sends them. |
| [Claude Code Tips](https://github.com/ykdojo/claude-code-tips) / [Claude Code Best Practices](https://code.claude.com/docs/en/best-practices) | The fastest way to get good at Claude Code. |
| [Steering Claude Code: skills, hooks, rules, subagents](https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents) | How to decide what becomes a skill, a hook or a CLAUDE.md rule when the Marathon bots grow. |
| [Claude Code GitHub Action](https://github.com/anthropics/claude-code-action) | Mention @claude on this repo's issues to have it update tools, for example a new pricing rule. |
| [Rulesync](https://github.com/dyoshikawa/rulesync) | Keeps one rule set in sync across Claude, Cursor and Codex. Useful because ChatGPT and Grok also work for Marathon. |

## Skip for now

- Heavy multi-agent orchestrators and observability stacks (Grafana, OTel). The Notion Activity Log already covers this.
- Third-party memory servers. Marathon Brain in Notion is the shared memory, and a second memory store would split the truth.
- Anything that needs broad shell or "bypass permissions" mode on the Windows PC that runs the permit monitor.

**Security note:** read a third-party hook or plugin before installing it. Hooks run with your permissions. Prefer the official directory.
