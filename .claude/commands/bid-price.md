---
description: Price a commercial trade bid with Marathon's markup rules (draft for Nick)
argument-hint: [bid name or Bids database row]
---
Price the bid: $ARGUMENTS

1. Run `/brain-check` for this bid. From Marathon Brain Section 4, get the current self-performed markup, the sub-quote markup, the margin floor and the in-house rate sheet. Also open the bid's row in the **Bids** database.
2. Build a CSV in the scratchpad (never in this repo, which is public) with the columns `trade,kind,cost,market_low`. `kind` is `self` or `sub`. Sub lines must use **firm written sub quotes** from the Sub Bench or Gmail. If a quote is missing, leave the line out and list it as a gap; never guess one.
3. Run: `python3 tools/bid_price.py <csv> --self-markup <x> --sub-markup <y> --margin-floor <z>`
4. For a prevailing-wage job, use the DLS schedule rates from that job's bid docs and say so.
5. Hand the result to the `bid-reviewer` agent.
6. Show Nick the table, the gaps, the flags and the reviewer's notes. Don't write "Our price" into the Bids database or send anything until Nick approves. Log it with `/log-activity` (Needs: Nick).
