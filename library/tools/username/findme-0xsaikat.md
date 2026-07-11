---
id: findme-0xsaikat
name: findme (0xSaikat)
description: Use when you have a `username` and want to enumerate matching accounts across the web — returns social-profile links on 400+ platforms for a digital-footprint sweep.
url: https://github.com/0xSaikat/findme
category: username
path:
- username
bestFor: Fast username-to-profile enumeration across hundreds of sites from the command line.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free and open-source (MIT). Install via `pip install findme-osint` or from the GitHub source; no account or API key.
opsec: passive
opsecNote: The tool checks target profiles by requesting each platform directly from your machine — that reveals your IP to hundreds of sites and does not contact the subject. Run behind a VPN/proxy and a sock-puppet environment; some sites may rate-limit or log the sweep.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: cli
trust: community
trustNote: Community username enumerator (~300 GitHub stars); actively maintained (v1.0.7, Dec 2025). Verify hits manually — enumerators produce false positives.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- findme-osint
- 0xSaikat findme
tags:
- username-enumeration
- cli
source: gh-topic-osint-resources
lastVerified: '2026-07-11'
enrichment: full
---

# findme (0xSaikat)

> A Sherlock-style CLI: give it one username and it checks 400+ platforms for an account, fast, for a first-pass footprint map.

## When to use
You have a `username` (a handle from an email, a chat, another profile) and want to know everywhere else that same handle exists. This is the standard opening move in username-pivoting: sweep hundreds of sites at once, then hand-verify the hits to build the subject's cross-platform footprint.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install findme-osint` (or clone `https://github.com/0xSaikat/findme` and `pip install -r requirements.txt`).
2. Run `findme` (PyPI) or `python3 findme.py` (source).
3. Enter the target `username` when prompted; it queries the 400+ supported platforms (dev, social, gaming, creative, professional, media).
4. Read the output: reported hits are candidate `social-profile` URLs.
5. **Verify each hit manually** — open the profile and confirm it's the same person (photo, bio, linked accounts), not just the same string.
6. Pivot: confirmed profiles feed name/image/email extraction and `associate` mapping.

## Inputs → Outputs
- **In:** `username`
- **Out:** candidate `social-profile` links across 400+ sites
- **Empty/negative result looks like:** few or no hits. Enumerators rely on each site's account-exists signal, which breaks silently when a platform changes — a "not found" can be a stale check, not a real absence. Conversely, common handles yield many *unrelated* people's accounts.

## Gotchas & OpSec
- False positives/negatives are inherent: verify every hit; treat the list as leads, not conclusions.
- Human-in-the-loop: manual verification of each candidate is required.
- OpSec: **passive** toward the subject, but your machine directly contacts hundreds of platforms — use a VPN/proxy and a clean environment; expect some rate-limiting.

## Overlaps ("do both")
- Pairs with `[[sherlock]]`, `[[whatsmyname-web]]`, and `[[maigret]]` — each covers a different (and shifting) site list, so running two enumerators catches accounts a single one misses. Reconcile and de-dupe the combined hits.

## Trust & verifiability
`trust: community` — an actively maintained open-source project (v1.0.7, Dec 2025), but community tooling with no guarantee of accuracy; the check logic can silently rot, so confirm each hit against the live site.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | findme-0xsaikat |
| category | username |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (manual-review) |
