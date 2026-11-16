---
name: capability-mapping
description: Invoke after rfp-requirements-extraction to map each requirement (or each claim in a seller bid) to the product capability and underlying module that meets it, with a documentation citation and a fit classification.
---

## Purpose
Show, requirement by requirement, what the product version under assessment actually covers, which capability and module covers it, and where the gaps are, with evidence for every claim.

## Uses
- Agent capabilities: code interpreter, file/document storage search
- Knowledge: the official `<PRODUCT>` `<VERSION>` documentation, the `<PRODUCT>` `<VERSION>` reference files in agent Knowledge, and the Claims Register

## Capability taxonomy (map every row to one or more)
Define your own taxonomy in this section. Suggested shape:
`<Capability 1> · <Capability 2> · … · Platform (install, security, user and licence administration, AI/automation interfaces) · Not <PRODUCT>`.
For each capability, record the underlying module or product only if a `<VERSION>` source names it. Confirm each mapping against the documentation before relying on it.

## Instructions
1. Load the requirements register from `02 - Requirements`.
2. For each row, search the `<VERSION>` sources using 2–3 keyword variants. Read only the passages that match.
3. Classify each row as one of: **Meets** (a `<VERSION>` source explicitly describes it), **Partially Meets** (state what is missing), **Gap** (not supported, or only on the roadmap), **Needs Evidence** (plausible but no citation found), or **Needs Clarification** (the requirement itself is ambiguous).
4. Record the delivery route: Out of the box / Configuration / Integration / Custom work / Partner / Not possible. Configuration and custom work add delivery risk, so note it.
5. Add the citation (document, page or URL, and a quote of 25 words or fewer), and a confidence rating of High, Medium or Low.
6. For seller bids, mark any claim that goes beyond the cited capability as an **Over-commitment**.
7. Roll up the results: coverage by capability, a list of failed Mandatory requirements, and weighted coverage if the RFP gives weights.
8. Pass every row classified as Gap, Partially Meets or Needs Evidence to `capability-gap-capture`.

## Output
Save `<Client> - Capability Map - YYYY-MM-DD.xlsx` to `03 - Analysis` with these columns:
`Req ID | Capability | Product | Classification | Delivery route | Evidence | Confidence | Over-commitment? | Action`
In chat, report: mandatory pass/fail, a coverage heatmap by capability as a table, and the top 5 gaps.

## Rules
- No citation means the row cannot be Meets. General model knowledge is never evidence.
- Use only `<VERSION>` sources. If a search returns a page for any other version, discard it.
- Only use capability names that appear in your defined taxonomy and in the `<VERSION>` documentation.
- Never state what platform or infrastructure the product is built on unless a `<VERSION>` source says so.
