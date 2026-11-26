# Claude: Marathon GC workspace

Claude Code setup for Marathon General Contracting LLC: shared rules, slash commands for the bid and sub workflow, a bid-pricing tool and safety guardrails.

- **`CLAUDE.md`**: rules Claude follows in this repo. It points to *Marathon Brain* in Notion for private facts.
- **`.claude/commands/`**: `/brain-check`, `/log-activity`, `/bid-price`, `/sub-quote-request`, `/gc-email-draft`, `/jetpost-update`
- **`.claude/agents/bid-reviewer.md`**: checks margin, sub quotes, scope gaps and escalations before Nick sees a bid.
- **`.claude/hooks/marathon_guard.py`**: blocks destructive commands, and blocks commits that contain private-looking data.
- **`.claude/settings.json`**: email, texts, calls, payroll and ad writes ask first. Token files can't be read.
- **`tools/bid_price.py`**: the bid calculator. Rates are passed in at run time and never stored in this public repo.
- **`docs/claude-code-picks.md`**: picks from [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) worth installing.

## Use it

```bash
git clone https://github.com/marathongeneralcontractingllc-stack/claude.git
cd claude
claude            # then try: /brain-check pricing the next bid
```

Run the tests: `python3 -m pytest tests -q`

**This repository is public.** Keep EINs, addresses, phone numbers, customers, prices and markup out of it.
