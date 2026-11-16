---
name: competitive-defensibility
description: Invoke when an RFP, seller bid or capability map mentions a competitor by name or uses competitor-shaped requirements; produces evidence-backed differentiators and flags inaccurate claims about your product or competitors.
---

## Purpose
Help the team argue its case against competitors using only claims it can defend. Flag inaccurate claims in either direction: your company overselling itself, or the RFP or a competitor misrepresenting your product.

## Uses
- Agent capabilities: file/document storage search, web search (for competitor facts only)
- Knowledge: the Claims Register, the Capability Map from `capability-mapping`

## Instructions
1. List competitor mentions from the requirements register. Also flag **competitor-shaped requirements**: wording or features that look lifted from one vendor's product (for example, a feature name or workflow term that only one vendor uses). Treat these as a signal of who is likely already favoured.
2. Draw differentiators **only** from Claims Register rows marked Verified that link to a requirement scoring Meets or Partially Meets in the Capability Map. Candidate areas to check: legacy or mainframe platform support, service virtualization, an integrated end-to-end value stream, hybrid and air-gapped deployment, AI capabilities.
3. Rows marked Unverified go in an internal "To confirm before use" list, never into response wording. Rows marked Rejected must be flagged wherever they appear.
4. For each competitor, record where they are likely stronger, citing a public source and the date you checked it. Never invent competitor weaknesses.
5. Write a **trap question** for each differentiator: a clarification or demo request that exposes the gap in the competitor's offering without naming them.
6. Check the bid or response draft for claims that are not in the register, comparisons with no evidence, and absolute words ("only", "unique", "first"). Flag each one.

## Output
Save `<Client> - Competitive Defensibility - YYYY-MM-DD.docx` to `03 - Analysis` with these sections: Competitors detected · Requirements that look written for a competitor · Defensible differentiators (with requirement links) · Where competitors are stronger · Claims to remove or soften · Trap questions · To confirm before use.

## Rules
- A differentiator must cite a Verified claim and a requirement it helps win. Otherwise drop it.
- Do not use any claim about a platform or infrastructure governance advantage unless the register marks it Verified.
- Keep everything about competitors factual and dated. No disparaging language.

## Hand-off
Pass each "where competitors are stronger" item to `capability-gap-capture` with gap type Competitive, together with the competitor, its public source and the date you checked it. Do the same for capabilities that a competitor-shaped requirement revealed the product lacks. Only pass items that point to a missing product capability. Do not pass items about pricing or the company itself.
