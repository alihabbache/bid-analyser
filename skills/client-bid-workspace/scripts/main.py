#!/usr/bin/env python3
"""Plan the client bid workspace: canonical name, subfolders, file assignments.
Input (stdin JSON): {"client": "...", "files": ["..."]}
"""
import json, re, sys
from collections import Counter
from datetime import date

SUBFOLDERS = [
    "01 - Intake", "02 - Requirements", "03 - Analysis",
    "04 - Response", "05 - Evidence", "06 - Reviews", "99 - Archive"
]

# Most specific first: an "RFP Response" is a response, not intake.
RULES = [
    (6, ('superseded', 'withdrawn', 'archive', '_old', ' old ')),
    (5, ('review', 'approval', 'decision log', 'sign-off', 'signoff')),
    (1, ('requirement', 'compliance', 'matrix', 'traceability')),
    (2, ('analysis', 'risk', 'gap', 'executive summary', 'clarification', 'battlecard', 'capability map')),
    (3, ('response', 'submission', 'proposal', 'answer')),
    (4, ('evidence', 'reference', 'product doc', 'datasheet', 'claims register')),
    (0, ('rfp', 'rfi', 'rfq', 'tender', 'amendment', 'addendum', 'itt', 'attachment', 'appendix')),
]


def clean(value):
    value = re.sub(r'[<>:"/\\|?*]+', '-', (value or '').strip())
    return re.sub(r'\s+', ' ', value).strip(' .-')


def classify(name):
    n = f" {name.lower()} "
    for idx, keys in RULES:
        if any(k in n for k in keys):
            return SUBFOLDERS[idx]
    return None  # unclassified -> must be resolved by a person


payload = json.loads(sys.stdin.read() or '{}')
client = clean(payload.get('client', ''))
files = payload.get('files', [])

warnings = []
if not client:
    warnings.append("Client name missing - ask before filing.")
    client = "UNKNOWN CLIENT"
if not files:
    warnings.append("No files supplied.")

assignments, unclassified = [], []
for f in files:
    folder = classify(f)
    if folder is None:
        unclassified.append(f)
    assignments.append({'file': f, 'folder': folder or 'UNCLASSIFIED - confirm with user'})

dupes = [f for f, c in Counter(x.lower() for x in files).items() if c > 1]
if unclassified:
    warnings.append(f"Unclassified: {unclassified}")
if dupes:
    warnings.append(f"Duplicates: {dupes}")

print(json.dumps({
    'workspace': client,
    'subfolders': SUBFOLDERS,
    'assignments': assignments,
    'generated_name_pattern': f"{client} - <Artifact> - {date.today().isoformat()}.<ext>",
    'warnings': warnings,
    'complete': bool(files) and not unclassified and not dupes and client != "UNKNOWN CLIENT",
}, indent=2))
