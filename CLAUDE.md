# Marathon GC: Claude Code workspace

This repository sets up Claude Code for Marathon General Contracting LLC (Marathon GC), a general contractor in Fall River, MA, with a winter snow brand, Marathon Snow & Ice.

**This repo is public.** Never commit any of the following: EINs, the street address, phone numbers, customer or sub names, prices, markup percentages, rate sheets, policy numbers, tokens or passwords. Private facts live in Notion, in **Marathon Brain**.

## Before acting

1. Read Marathon Brain in Notion (search for "Marathon Brain"), and especially Sections 1 (lanes), 3 (facts), 4 (prices and markup) and 5 (rules). Run `/brain-check` to do this.
2. Read the last 48 hours of the **Activity Log** database so no work gets done twice.
3. If the task belongs to another AI's lane (Grok owns HighLevel, ChatGPT owns content and Nextdoor), don't do it. Log it with "Needs" set to that owner.

## After acting

Add one row to the Activity Log (`/log-activity`) that says what was done, in which system, and what needs Nick. For notes meant for people, also post to Jetpost, in Management's workspace.

## Hard rules (summary; Marathon Brain wins if they differ)

- Nick approves all money, contracts, prices, new offers and signatures.
- Nothing goes to customers or GCs without Nick's OK. The one exception: the Sub Bench lane may email subs, limited to quote requests (one request and one follow-up).
- Never pay, buy, cancel or change a subscription.
- Escalate to Nick: anything over $25,000, contract changes, injuries, damage claims, legal threats, bonds, and prevailing or federal wage rules.
- Never invent reviews, photos, stats, customers, prices, license numbers, bond numbers or policy numbers. If proof isn't issued yet, say it's "pending".
- Never mix Howard Home Solutions LLC with Marathon.
- No firm price before a site visit. Every quote is good / better / best.

## Tools in this repo

| Command | What it does |
| --- | --- |
| `/brain-check` | Reads Marathon Brain and the last 48 hours of the Activity Log, then reports the rules and open items that bear on the task |
| `/log-activity` | Writes one Activity Log row for the work just done |
| `/bid-price` | Prices a commercial trade bid with `tools/bid_price.py`, using the markup rules from Marathon Brain |
| `/sub-quote-request` | Drafts a quote request to a sub (sent only by the Sub Bench lane) |
| `/gc-email-draft` | Drafts an email to a GC estimator as a Gmail draft, never sent |
| `/jetpost-update` | Posts a short status note to Jetpost |
| Agent `bid-reviewer` | Checks a priced bid against the margin floor and the "never invent" rules before Nick sees it |

`tools/bid_price.py` holds no rates or percentages. Every number is passed in at run time from Marathon Brain.

Guardrails in `.claude/settings.json` and `.claude/hooks/marathon_guard.py`:
- Sending email or texts, placing calls, running payroll and writing to ad accounts all ask first.
- Destructive shell commands are blocked.
- A commit is blocked if it contains an EIN-, phone- or address-like string.

See `docs/claude-code-picks.md` for tools from the awesome-claude-code list worth installing on Nick's PC.
