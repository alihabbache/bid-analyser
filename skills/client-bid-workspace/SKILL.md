---
name: client-bid-workspace
description: Invoke whenever a new client RFP, RFI, or supporting bid document is added, to derive a consistent client workspace name, classify the document, produce the required folder plan, and verify filing completeness.
---

## Purpose
Create a repeatable filing plan for each client bid and check that every RFP, RFI, analysis artifact, evidence item, response draft, and review output has a defined destination.

## Uses
- Agent capabilities: code interpreter, file/document storage search
- Agent knowledge sources: your product documentation

## Instructions
1. Identify the client name from the user's statement or the supplied document. If it cannot be determined confidently, ask for it before continuing.
2. Run `scripts/main.py` with the client name and any supplied filenames to produce the canonical workspace name, required subfolders, proposed file destinations, and completeness checklist.
3. Ask the user where their bids parent folder is, and use it as the filing target. If they don't give one, present the folder plan with the folder names only, so they can file the documents themselves.
4. Apply the generated structure consistently:
   - `01 - Intake` for original RFPs, RFIs, amendments, and customer attachments.
   - `02 - Requirements` for extracted requirements and compliance matrices.
   - `03 - Analysis` for fit assessments, risks, gaps, clarifications, and executive summaries.
   - `04 - Response` for response drafts and final submissions.
   - `05 - Evidence` for product documentation, references, and supporting proof.
   - `06 - Reviews` for review notes, approvals, and decision logs.
   - `99 - Archive` for superseded or withdrawn material.
5. Keep original source files unchanged. For generated artifacts, use `<Client> - <Artifact> - YYYY-MM-DD.<ext>` and place each in the proposed destination.
6. Check that every supplied or generated file has exactly one destination, required folders are present in the plan, and no client material is assigned outside the client workspace.
7. Report the workspace path, filing plan, missing items, duplicates, and any actions that still require a person or connected storage action. Do not claim that a folder or file was created unless the connected environment confirms it.

## Parameters
- Client name, when known.
- One or more RFP, RFI, amendment, supporting-document, or generated-artifact filenames.
- Optional bid identifier and submission date.

## Output
- Canonical client workspace name and full target path.
- Required subfolder checklist.
- File-to-folder assignment list.
- Missing, duplicate, ambiguous, or unfiled-item warnings.
