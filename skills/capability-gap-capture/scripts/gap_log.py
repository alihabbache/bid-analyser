#!/usr/bin/env python3
"""Find likely duplicates between new gaps and the existing Capability Gap Log.

stdin JSON:
{"existing": [{"gap_id": "G001", "need": "..."}],
 "new": [{"req_id": "R12", "need": "..."}],
 "threshold": 0.45}
stdout: each new gap with its best existing match and similarity score, and
whether to merge (score >= threshold) or create a new Gap ID.
"""
import json, re, sys

STOP = set("a an the to of and or for in on with as by i we need so that be is are can must shall should able support provide system solution user users".split())


def tokens(text):
    words = re.findall(r"[a-z0-9]+", (text or "").lower())
    return {w for w in words if w not in STOP and len(w) > 2}


def jaccard(a, b):
    return len(a & b) / len(a | b) if a and b else 0.0


data = json.loads(sys.stdin.read() or "{}")
existing = data.get("existing", [])
threshold = float(data.get("threshold", 0.45))
next_num = 1 + max([int(re.sub(r"\D", "", e["gap_id"]) or 0) for e in existing] or [0])

out = []
for item in data.get("new", []):
    t = tokens(item.get("need"))
    best = max(((jaccard(t, tokens(e.get("need"))), e["gap_id"]) for e in existing), default=(0.0, None))
    if best[1] and best[0] >= threshold:
        out.append({**item, "action": "merge", "gap_id": best[1], "similarity": round(best[0], 2)})
    else:
        out.append({**item, "action": "new", "gap_id": f"G{next_num:03d}",
                    "closest": best[1], "similarity": round(best[0], 2)})
        next_num += 1

print(json.dumps(out, indent=2))
print("\nNote: similarity is a hint only. Confirm every merge before writing it to the log.", file=sys.stderr)
