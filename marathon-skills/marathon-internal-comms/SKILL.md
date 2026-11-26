---
name: marathon-internal-comms
description: Writes Marathon GC's recurring business communications in fixed formats: Nick's Monday brief (3P), customer job-status updates, storm-day ops updates, sub/crew coordination messages, and the monthly customer newsletter. Use for any status report, update, newsletter or crew/sub message for Marathon General Contracting or Marathon Snow & Ice.
license: Adapted from anthropics/skills internal-comms (Apache-2.0)
---

# Marathon Internal & Customer Comms

For Marathon General Contracting LLC (owner Nicholas J. Brown, President). Load `marathon-gc-agent` for business facts, prices and rules. Marathon only.

1. Identify the type and load its file from `examples/`:
   - `examples/monday-brief.md` – Nick's weekly 3P (Progress / Plans / Problems) with the revenue numbers
   - `examples/job-status-update.md` – update to a construction customer
   - `examples/storm-day-update.md` – snow ops: before, during and after a storm
   - `examples/sub-crew-coordination.md` – scheduling, scope and paperwork messages to subs and crew
   - `examples/customer-newsletter.md` – monthly email/Facebook roundup
2. Pull facts from the Marathon Leads sheet, Bid Board, Gmail (Marathon account only) and calendar when connected; otherwise ask Nick.
3. Draft only. Never send to a customer, sub or the public without Nick's OK in the conversation.

Voice: plain, confident, local, short sentences. Sound like the guy who shows up on time. No corporate filler, no fake urgency, no emoji walls. Never post customer names or addresses publicly.
