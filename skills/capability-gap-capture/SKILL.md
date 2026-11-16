---
name: capability-gap-capture
description: Invoke after the analysis skills, or whenever the user says "log a gap", "capture a gap", "feature request", "idea" or "the product can't do X". Collects gaps from capability mapping, integration fit, competitive analysis and the user, asks the user to confirm them, then writes them to the cross-bid Capability Gap Log and a roadmap-tool import file.
---

## Purpose
Turn the gaps found in each bid into product evidence. Over time the log shows which missing capabilities keep costing deals and how much they matter. It is the input for roadmap decisions, not a commitment to build anything.

## Uses
- Agent capabilities: code interpreter, file/document storage search
- Knowledge: the `<PRODUCT>` `<VERSION>` documentation and reference files, and the Claims Register
- Log: `00 - Capability Gap Log.xlsx`. Keep one log across all bids, in the user's bids parent folder rather than inside any single client's folder. If you can't find the log, ask the user for it. Otherwise, create a new log for them to download.

## Gap sources (record the source on every gap)
| Source | What to collect |
|---|---|
| `capability-mapping` | Rows classified as Gap, Partially Meets or Needs Evidence, including roadmap promises |
| `ecosystem-integration-fit` | Integrations classified as Partner/Custom or Not supported/Unknown, and any hop marked Unverified |
| `competitive-defensibility` | "Where competitors are stronger" items, plus missing capabilities that competitor-shaped requirements reveal |
| User (manual) | Anything the user asks to log, during a bid or on its own |

Skip Needs Clarification rows until the clarification is resolved.

## Instructions
1. **Collect** candidate gaps from every source that ran. For a manual gap, ask only for what is missing: the need, who needs it, and the related bid or customer context (optional).
2. **Confirm it's a gap.** Search the `<VERSION>` sources once more using different keywords. If you find a citation, it isn't a gap: tell the user and update the relevant analysis instead. Rows classified as Needs Evidence, and gaps supported only by web sources, are logged as **Unconfirmed**.
3. **Write the need, not the solution:** "As a <persona>, I need <outcome> so that <reason>". Keep the customer's or user's original wording in its own column.
4. **Classify the gap:**
   - Gap type: Missing capability / Partial capability / Integration / Competitive / Non-functional / Compliance & certification / Platform & deployment / AI / Usability.
   - Nearest capability: one entry from your capability taxonomy, or New area.
   - Impact: **Blocker** (fails a Mandatory requirement), **Score loss** (points at stake if known), **Competitive** (a competitor offers it), or **Nice to have**.
   - Workaround available today, with evidence, or "None".
5. **Deduplicate.** Run `scripts/gap_log.py` against the existing log. Mark each candidate **New**, or **Merge into G0xx** (which adds demand to that gap).
6. **Review gate. Do not write anything to the log yet.** Show the user a numbered table: `# | Need statement | Type | Impact | Source | Status | New or Merge into G0xx`. Ask them to reply with one of:
   - `approve all`
   - `approve 1,3,5` (log only those)
   - `edit 2: <change>` (then show the table again)
   - `reject 4: <reason>`
   - `merge 6 into G012` (overrides the suggested match)

   Wait for their reply. If they don't answer, save the table as `<Bid> - Proposed Gaps - YYYY-MM-DD.xlsx` and stop.
7. **Write** only the approved rows, including who approved each one and the date.
8. **Do not prioritise.** Do not assign a priority or a release. Show the demand evidence only (number of bids, blockers, points at stake, competitors that offer it). The product owner decides priority.

## Output
1. Update `00 - Capability Gap Log.xlsx` with these columns:
   `Gap ID | Need statement | Original wording (≤40 words) | Gap type | Nearest capability | Source skill | Status (Confirmed/Unconfirmed) | Bids affected | Blocker count | Points at stake | Competitor coverage | Workaround | Evidence searched | Approved by | First seen | Last seen | Roadmap idea ref`
2. Export `Capability Gaps - Roadmap import - YYYY-MM-DD.csv` with these columns: `Name, Description, Category, Votes`. Include approved rows only, and no client names. Adapt the column set to your roadmap or idea-management tool.
3. In chat, report: how many gaps were approved, merged or rejected; the top 5 gaps by blocker count; and any workaround the response team could use now.

## Rules
- Never write that a gap "will be delivered" or give a roadmap date.
- Client names may appear only in the internal log's bid references, never in the roadmap-tool export.
- One need per row. Split compound requirements.
- Never write to the log without the user's approval from step 6.
