---
name: marathon-job-documents
description: Builds Marathon GC's paperwork as branded Word/PDF/Excel files: good/better/best quotes, home-improvement contracts (M.G.L. c.142A items), change orders, snow & ice service agreements, sub agreements packets, lien-waiver requests and job cost sheets. Use when Nick needs a quote, contract, change order, agreement, invoice-ready cost sheet or any job document for Marathon General Contracting.
license: Built on anthropics/skills docx, pdf and xlsx (Apache-2.0)
---

# Marathon Job Documents

Use the `docx` skill for Word, `pdf` for PDF and `xlsx` for cost sheets, styled with `marathon-brand-guidelines`. Load `marathon-gc-agent` for prices, margin and legal rules. Templates are in `templates/`.

## Always

- Header: M tile + MARATHON wordmark (logo file or labeled placeholder). Footer: brand footer with MA HIC #218125.
- Fill only facts Nick or the Leads sheet gives. Never invent prices, quantities, dates or customer details; leave `[ ]` blanks.
- Drafts only. Nick reviews and signs. Never send.
- Margin check every priced document: gross margin = (price − cost) / price, checked against the current floor in Marathon Brain (Notion). Show the check to Nick, not on the customer copy.
- Minimum job $500.

## Document types

| Doc | Template | Must include |
| --- | --- | --- |
| Good/Better/Best quote | `templates/quote-gbb.md` | 3 options, scope per option, exclusions, price hold date, next start date, valid 30 days |
| Home-improvement contract | `templates/hic-contract-checklist.md` | every c.142A §2 item (checklist), 3-day cancel notice, deposit ≤ 1/3 or special-order cost |
| Change order | `templates/change-order.md` | CO #, description, $ change, schedule impact, new contract total, both signatures before work |
| Snow & ice agreement | `templates/snow-agreement.md` | season dates, plan price, trigger, response times, 60 in cap, add-ons, payment schedule |
| Job cost sheet (xlsx) | `templates/job-cost-sheet.md` | cost lines, markup, margin, deposit, payments, sub paperwork status |

The c.142A checklist is a drafting aid, not legal advice; tell Nick to have his attorney approve the master contract once, then reuse it.
