"""Seed stub tool skills from the forked OSINT-Framework arf.json.

Breadth seed: every free/freemium leaf becomes a stub tool .md with frontmatter
mapped from existing arf metadata. Paid-only tools are skipped (logged, not dropped
silently). Stubs are later upgraded to full skills by enrichment passes.

Usage:
    python library/scripts/seed_from_arf.py [--dry-run]
"""
import json
import os
import sys

import _common as C

ARF = os.path.join(C.ROOT, "public", "arf.json")

# arf top-level category name -> canonical taxonomy category id (best-effort).
CAT_MAP = {
    "Username": "username",
    "Email Address": "email",
    "Domain Name": "domains-ip-infrastructure",
    "Cloud Infrastructure": "domains-ip-infrastructure",
    "IP & MAC Address": "domains-ip-infrastructure",
    "Images / Videos / Docs": "image-video-face",
    "Social Networks": "social-networks",
    "Instant Messaging": "messaging",
    "People Search Engines": "people-search",
    "Dating": "dating-classifieds",
    "Telephone Numbers": "phone",
    "Public Records": "public-records",
    "Compliance & Risk Intelligence": "public-records",
    "Business Records": "public-records",
    "Transportation": "transportation",
    "Geolocation Tools / Maps": "geolocation",
    "Search Engines": "search-engines",
    "Online Communities": "communities-forums",
    "Archives": "archives-cache",
    "Language Translation": "translation-language",
    "Mobile OSINT": "documents-metadata",
    "Dark Web": "dark-web",
    "Disinformation & Media Verification": "image-video-face",
    "Blockchain & Cryptocurrency": "financial-crypto",
    "Classifieds": "dating-classifieds",
    "Encoding / Decoding": "ai-analysis-automation",
    "Tools": "ai-analysis-automation",
    "AI Tools": "ai-analysis-automation",
    "Malicious File Analysis": "documents-metadata",
    "Cyber Threat Intelligence": "domains-ip-infrastructure",
    "OpSec": "opsec-investigator-tooling",
    "Documentation / Evidence Capture": "evidence-capture",
    "Training": "training-ctf",
}

MP_HIGH = {"Username", "Images / Videos / Docs", "Social Networks",
           "People Search Engines", "Telephone Numbers", "Geolocation Tools / Maps",
           "Email Address", "Instant Messaging", "Dating", "Classifieds"}
MP_MEDIUM = {"Public Records", "Transportation", "Archives", "Language Translation",
             "Online Communities", "Search Engines", "Mobile OSINT", "Dark Web",
             "Business Records", "Disinformation & Media Verification",
             "Documentation / Evidence Capture", "OpSec", "Blockchain & Cryptocurrency"}


ALLOWED_STATUS = {"live", "degraded", "down", "deprecated", "unknown"}
STATUS_SYN = {"defunct": "down", "dead": "down", "offline": "down",
              "ok": "live", "online": "live", "active": "live", "": "unknown"}


def norm_status(s):
    s = (s or "unknown").strip().lower()
    s = STATUS_SYN.get(s, s)
    return s if s in ALLOWED_STATUS else "unknown"


def norm_opsec(s):
    s = (s or "unknown").strip().lower()
    return s if s in {"passive", "active", "unknown"} else "unknown"


def mp_for(top):
    if top in MP_HIGH:
        return "high"
    if top in MP_MEDIUM:
        return "medium"
    return "low"


def category_for(top):
    return CAT_MAP.get(top, C.slugify(top))


def marker_clean(name):
    flags = {
        "localInstall": "(T)" in name,
        "googleDork": "(D)" in name,
        "registration": "(R)" in name,
        "editUrl": "(M)" in name,
    }
    import re
    clean = re.sub(r"\s*\([TDRM]\)", "", name).strip()
    return clean, flags


used_ids = set()
used_paths = set()
skipped_paid = []
stats = {"made": 0, "skipped_paid": 0, "no_url": 0}


def unique_id(slug):
    cand = slug
    i = 2
    while cand in used_ids:
        cand = f"{slug}-{i}"
        i += 1
    used_ids.add(cand)
    return cand


def build_stub(node, top, path_ids, dry):
    name = node.get("name", "")
    url = node.get("url", "")
    if not url:
        stats["no_url"] += 1
        return
    clean, flags = marker_clean(name)
    pricing = (node.get("pricing") or "").lower()
    if pricing == "paid":
        skipped_paid.append({"name": clean, "url": url, "path": "/".join(path_ids)})
        stats["skipped_paid"] += 1
        return
    if pricing not in ("free", "freemium"):
        pricing = "free"  # arf is free-focused; assume free when unset

    folder = os.path.join(C.TOOLS_DIR, *path_ids)
    base_slug = C.slugify(clean)
    fid = unique_id(base_slug)
    fpath = os.path.join(folder, fid + ".md")

    desc = C.oneline(node.get("bestFor") or node.get("description") or f"OSINT tool: {clean}.")
    fm = {
        "id": fid,
        "name": clean,
        "description": desc,
        "url": url,
        "category": category_for(top),
        "path": path_ids,
        "bestFor": C.oneline(node.get("bestFor", "")),
        "input": C.oneline(node.get("input", "")),
        "output": C.oneline(node.get("output", "")),
        "selectorsIn": [],
        "selectorsOut": [],
        "status": norm_status(node.get("status")),
        "pricing": pricing,
        "opsec": norm_opsec(node.get("opsec")),
        "opsecNote": C.oneline(node.get("opsecNote", "")),
        "humanInLoop": bool(node.get("registration")) or "(R)" in name,
        "humanInLoopReason": (["account-login"] if (node.get("registration") or "(R)" in name) else []),
        "bestInteractionPattern": ("cli" if flags["localInstall"] else "web-manual"),
        "trust": "unverified",
        "trustNote": "",
        "missingPersonsRelevance": mp_for(top),
        "coverage": [],
        "auth": ("account" if (node.get("registration") or "(R)" in name) else "none"),
        "api": bool(node.get("api")),
        "localInstall": flags["localInstall"] or bool(node.get("localInstall")),
        "registration": flags["registration"] or bool(node.get("registration")),
        "invitationOnly": bool(node.get("invitationOnly")),
        "deprecated": bool(node.get("deprecated")),
        "relatedTools": [],
        "aliases": [],
        "tags": [],
        "source": "arf-seed",
        "lastVerified": "",
        "enrichment": "stub",
    }
    body = (
        f"# {clean}\n\n"
        f"> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.\n"
        f"> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.\n\n"
        f"- **URL:** {url}\n"
        f"- **Best for:** {fm['bestFor'] or '—'}\n"
        f"- **Input → Output:** {fm['input'] or '?'} → {fm['output'] or '?'}\n"
        f"- **OpSec:** {fm['opsec']}. {fm['opsecNote']}\n\n"
        f"_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and "
        f"`bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.\n"
    )
    stats["made"] += 1
    if not dry:
        C.write_skill(fpath, fm, body)


def walk(node, top, path_ids, dry):
    children = node.get("children")
    if children is None:
        return
    for ch in children:
        if ch.get("children") is not None:
            sub = C.slugify(ch.get("name", ""))
            walk(ch, top, path_ids + [sub], dry)
        else:
            build_stub(ch, top, path_ids, dry)


def main():
    dry = "--dry-run" in sys.argv
    with open(ARF, encoding="utf-8") as f:
        data = json.load(f)
    for top_node in data.get("children", []):
        top = top_node.get("name", "")
        walk(top_node, top, [category_for(top)], dry)

    os.makedirs(C.LEDGER_DIR, exist_ok=True)
    if not dry:
        with open(os.path.join(C.LEDGER_DIR, "skipped-paid.json"), "w", encoding="utf-8") as f:
            json.dump(skipped_paid, f, indent=2)
    print(f"made={stats['made']} skipped_paid={stats['skipped_paid']} no_url={stats['no_url']} "
          f"unique_ids={len(used_ids)} {'(dry-run)' if dry else ''}")


if __name__ == "__main__":
    main()
