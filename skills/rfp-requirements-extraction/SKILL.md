---
name: rfp-requirements-extraction
description: Invoke after client-bid-workspace, whenever an RFP, RFI, tender, amendment or seller bid needs its requirements, compliance mandates, NFRs and evaluation scoring extracted into a structured register. Extraction only — no fit judgement.
---

## Purpose
Turn procurement documents into one complete, traceable register of requirements that every later skill works from.

## Uses
- Agent capabilities: code interpreter, file/document storage search
- Input: documents in the client's `01 - Intake` folder

## Instructions
1. Read every intake document, including amendments. Where an amendment changes a requirement, the amendment wins. Record both IDs in that case.
2. Extract one row per requirement and split compound requirements. Keep the original ID and wording, and note the location (doc, section/page, or sheet!cell). Quote no more than 40 words.
3. Assign each row exactly one **type**: Functional, NFR-Performance, NFR-Availability/DR, NFR-Scalability, Security, Compliance/Regulatory, Integration, Deployment/Platform, Service/Support, Commercial, Contractual.
4. Assign the **obligation**: Mandatory (pass/fail), Scored, Desirable or Informational. Phrases like "must" or "shall" are only evidence of obligation. If the RFP defines its own terms, use those instead.
5. Extract the **evaluation model**: criteria, weights, pass/fail gates, scoring scale and any page or word limits. If no weights are stated, record "Not stated". Never estimate them.
6. Extract **compliance mandates** separately: standards, certifications, data residency, accessibility, regulatory frameworks. Record each with the exact standard and version named.
7. Record **competitor mentions**, **named products or integrations**, and **key dates** (questions deadline, submission, demo, award) for the skills that run next.
8. Run a completeness check: compare the number of rows with any requirement count or numbering in the RFP, and list numbering gaps, unreadable pages or sheets, and ambiguous items.

## Output
Save `<Client> - Requirements Register - YYYY-MM-DD.xlsx` to `02 - Requirements` with these columns:
`Req ID | Source location | Requirement (verbatim) | Type | Obligation | Weight/Points | Amended by | Notes`
Include separate tabs for the Evaluation Model, Compliance Mandates, Competitor & Product Mentions, and Key Dates.
In chat, report: total rows by type and obligation, mandatory pass/fail count, completeness warnings, and the 3 most ambiguous requirements.

## Rules
- Do not classify fit here. That is done by `capability-mapping`.
- Never paraphrase a Mandatory requirement in a way that changes what it obligates.
