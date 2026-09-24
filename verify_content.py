#!/usr/bin/env python3
from pathlib import Path
import json,hashlib,sys
root=Path(__file__).resolve().parent
lock=json.loads((root/"CONTENT_INTEGRITY.json").read_text(encoding="utf-8"))
if (root/"app/src/main/assets/pages_manifest.json").exists():
    manifest=root/"app/src/main/assets/pages_manifest.json"; pages=root/"app/src/main/assets/Pages"
else:
    manifest=root/"Resources/pages_manifest.json"; pages=root/"Resources/Pages"
def sha(p):
    h=hashlib.sha256(); h.update(p.read_bytes()); return h.hexdigest()
obj=json.loads(manifest.read_text(encoding="utf-8"))
current=[(c["id"],c["title"],c["pages"],c["pageNumbers"]) for c in obj["chapters"]]
expected=[(c["id"],c["title"],c["pages"],c["pageNumbers"]) for c in lock["chapters"]]
errors=[]
if current!=expected: errors.append("chapter manifest changed")
for name,digest in lock["pageSha256"].items():
    p=pages/name
    if not p.exists(): errors.append(f"missing page: {name}")
    elif sha(p)!=digest: errors.append(f"page changed: {name}")
if errors:
    print("CONTENT INTEGRITY FAILED")
    for e in errors: print("-",e)
    sys.exit(1)
print(f"CONTENT INTEGRITY OK: {len(expected)} exact chapter titles, {len(lock['pageSha256'])} approved pages")
