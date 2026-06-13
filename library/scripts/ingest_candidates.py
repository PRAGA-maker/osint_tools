"""Ingest harvested tool candidates (staging JSON) into the tools tree.

Harvest agents write JSON arrays of candidate tool objects to
library/ledger/harvest/<sourceId>.json. This script dedups them against the
existing library (and each other) and writes new tool skills. Existing tools
matched by URL/domain are recorded as overlaps (for relatedTools), not duplicated.

Candidate object (all optional except name+url):
  name, url, description, category, path, bestFor, pricing, opsec,
  selectorsIn[], selectorsOut[], bestInteractionPattern, trust, trustNote,
  missingPersonsRelevance, coverage[], humanInLoop, humanInLoopReason[],
  aliases[], tags[], api, localInstall, registration, notes

Usage:
    python library/scripts/ingest_candidates.py [--dry-run]
"""
import glob
import json
import os
import re
import sys

import _common as C

HARVEST_DIR = os.path.join(C.LEDGER_DIR, "harvest")
VALID_CATS = None  # loaded from taxonomy header below
TAXONOMY_CATS = {
    "people-search", "username", "email", "phone", "social-networks",
    "image-video-face", "geolocation",
    "public-records", "transportation", "communities-forums", "messaging",
    "dating-classifieds", "archives-cache", "documents-metadata",
    "translation-language", "maps-geospatial-data", "dark-web",
    "financial-crypto", "domains-ip-infrastructure", "ai-analysis-automation",
    "opsec-investigator-tooling", "evidence-capture", "training-ctf",
    "search-engines",
}
ALLOWED = {
    "pricing": {"free", "freemium"},
    "opsec": {"passive", "active", "unknown"},
    "trust": {"trusted", "community", "personal", "unverified", "untrustworthy"},
    "missingPersonsRelevance": {"high", "medium", "low"},
    "bestInteractionPattern": {"cli", "chrome-mcp", "web-manual", "api", "python-lib",
                               "desktop-app", "docker", "mobile-app", "browser-extension"},
}


def norm_url(u):
    u = (u or "").strip()
    u = re.sub(r"#.*$", "", u)
    u = re.sub(r"/+$", "", u)
    return u.lower()


def existing_index():
    """Return (urls set, dom_slug set, ids set) from current tools tree."""
    urls, domslug, ids = set(), set(), set()
    for _p, fm, _b in C.iter_skills(C.TOOLS_DIR):
        ids.add(fm.get("id", ""))
        u = fm.get("url", "")
        urls.add(norm_url(u))
        domslug.add((C.registered_domain(u), C.slugify(fm.get("name", ""))))
    return urls, domslug, ids


def pick(d, key, allowed, default):
    v = (d.get(key) or "").strip().lower() if isinstance(d.get(key), str) else d.get(key)
    return v if v in allowed else default


def main():
    dry = "--dry-run" in sys.argv
    files = sorted(glob.glob(os.path.join(HARVEST_DIR, "*.json")))
    if not files:
        print(f"no staging files in {HARVEST_DIR}")
        return
    urls, domslug, ids = existing_index()
    seen_new = set()
    stats = {"new": 0, "dup_existing": 0, "dup_batch": 0, "bad": 0, "by_source": {}}
    overlaps = []

    for fp in files:
        source_id = os.path.basename(fp)[:-5]
        stats["by_source"].setdefault(source_id, 0)
        try:
            cands = json.load(open(fp, encoding="utf-8"))
        except Exception as e:
            print(f"  skip {fp}: {e}")
            continue
        if isinstance(cands, dict):
            cands = cands.get("candidates", [])
        for c in cands:
            name = C.oneline(c.get("name", ""), 120)
            url = (c.get("url") or "").strip()
            if not name or not re.match(r"^(https?://|javascript:)", url):
                stats["bad"] += 1
                continue
            nu = norm_url(url)
            cat = c.get("category") if c.get("category") in TAXONOMY_CATS else None
            dslug = (C.registered_domain(url), C.slugify(name))
            if nu in urls or dslug in domslug:
                stats["dup_existing"] += 1
                overlaps.append({"name": name, "url": url, "source": source_id})
                continue
            if nu in seen_new:
                stats["dup_batch"] += 1
                continue
            seen_new.add(nu)

            base = C.slugify(name)
            fid = base
            i = 2
            while fid in ids:
                fid = f"{base}-{i}"
                i += 1
            ids.add(fid)
            category = cat or "ai-analysis-automation"
            path = c.get("path") if isinstance(c.get("path"), list) and c["path"] else [category]
            has_rich = bool(c.get("selectorsIn") and c.get("bestInteractionPattern") and c.get("description"))
            fm = {
                "id": fid,
                "name": name,
                "description": C.oneline(c.get("description") or c.get("bestFor") or f"OSINT tool: {name}."),
                "url": url,
                "category": category,
                "path": path,
                "bestFor": C.oneline(c.get("bestFor", "")),
                "selectorsIn": c.get("selectorsIn") or [],
                "selectorsOut": c.get("selectorsOut") or [],
                "status": "unknown",
                "pricing": pick(c, "pricing", ALLOWED["pricing"], "free"),
                "opsec": pick(c, "opsec", ALLOWED["opsec"], "unknown"),
                "opsecNote": C.oneline(c.get("opsecNote", "")),
                "humanInLoop": bool(c.get("humanInLoop")),
                "humanInLoopReason": c.get("humanInLoopReason") or [],
                "bestInteractionPattern": pick(c, "bestInteractionPattern", ALLOWED["bestInteractionPattern"], "web-manual"),
                "trust": pick(c, "trust", ALLOWED["trust"], "unverified"),
                "trustNote": C.oneline(c.get("trustNote", "")),
                "missingPersonsRelevance": pick(c, "missingPersonsRelevance", ALLOWED["missingPersonsRelevance"], "medium"),
                "coverage": c.get("coverage") or [],
                "auth": "none",
                "api": bool(c.get("api")),
                "localInstall": bool(c.get("localInstall")),
                "registration": bool(c.get("registration")),
                "aliases": c.get("aliases") or [],
                "tags": c.get("tags") or [],
                "source": source_id,
                "lastVerified": "",
                "enrichment": "full" if has_rich else "stub",
            }
            body = (
                f"# {name}\n\n> {fm['description']}\n\n"
                f"- **URL:** {url}\n- **Best for:** {fm['bestFor'] or '—'}\n"
                f"- **Source:** harvested from `{source_id}`\n\n"
                f"{C.oneline(c.get('notes',''), 600)}\n\n"
                f"_Enrichment: {fm['enrichment']}. If stub, complete per `schema/templates/tool.template.md`._\n"
            )
            stats["new"] += 1
            stats["by_source"][source_id] += 1
            if not dry:
                C.write_skill(os.path.join(C.TOOLS_DIR, *path, fid + ".md"), fm, body)

    if not dry:
        with open(os.path.join(C.LEDGER_DIR, "overlaps-found.json"), "w", encoding="utf-8") as f:
            json.dump(overlaps, f, indent=2)
    print(f"NEW={stats['new']} dup_existing={stats['dup_existing']} dup_batch={stats['dup_batch']} bad={stats['bad']}")
    print("by source:", json.dumps(stats["by_source"]))


if __name__ == "__main__":
    main()
