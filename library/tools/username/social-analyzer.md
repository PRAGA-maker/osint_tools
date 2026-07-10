---
id: social-analyzer
name: Social Analyzer
description: Use when you have a `username` or `name` and want to find matching profiles across 1000+ sites with confidence scoring — returns rated `social-profile` matches with screenshots.
url: https://github.com/qeeqbox/social-analyzer
category: username
path:
- username
bestFor: Wide username/name enumeration across 1000+ sites with a 0-100 match-confidence rating and profile screenshots.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- image
- name
status: live
pricing: free
costNote: Free and open-source (qeeqbox); run locally via pip/npm/Docker. No account or key for the core username search.
opsec: passive
opsecNote: The tool requests public profile pages directly from your host, so those sites (and any CDN/analytics) see your IP hitting many URLs in a burst. Run behind a proxy/VPN (it supports proxy config) from a sock-puppet environment; it does not log into or notify the target profiles.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Well-known open-source OSINT project (thousands of GitHub stars); actively used, but results are heuristic and must be verified — a "maybe" is not a confirmed profile.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- whatsmyname-web
- sherlock-2
- blackbird-2
aliases:
- social-analyzer
- qeeqbox social-analyzer
tags:
- username-check
- profile-enumeration
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Social Analyzer

> An open-source profile-hunter that searches a `username`/`name` across 1000+ sites and scores each hit 0-100 (No / Maybe / Yes) to cut false positives — with screenshots and JSON export.

## When to use
You have a `username` (or a real `name`) and want the broadest possible sweep for matching accounts, with confidence ratings so you aren't drowned in false positives. Its string permutation/combination and multi-layer detection (including OCR) make it stronger than a plain "does this URL 200?" checker, which is valuable when a target uses handle variants.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install social-analyzer` (or run the Node.js version / `docker-compose` deployment).
2. Run a search: `python -m social-analyzer --username "target_handle" --metadata` (add `--top 100`, `--profiles detected`, `--output pretty`). A web UI is also available at `app.html` and it can be imported as a Python object/API.
3. Optionally set country/site-type filters, timeout, and a proxy for OpSec.
4. Read output: each candidate profile carries a rating (0-100), title, description, and optional screenshot; export to JSON.
5. Pivot: manually confirm "Yes"/high-rated hits, then feed confirmed `social-profile`s into per-platform enrichment tools.

## Inputs → Outputs
- **In:** `username` or `name` (with optional country/site filters)
- **Out:** rated `social-profile` matches, profile `image`/screenshots, and any `name`/bio metadata extracted
- **Empty/negative result looks like:** all candidates rated low ("No") — the handle likely isn't in use on covered sites, but very new or niche platforms may be missed.

## Gotchas & OpSec
- Ratings are heuristic: treat "Maybe" as a lead and always open "Yes" hits to confirm the profile is actually your subject, not a namesake.
- A burst of requests to 1000+ sites is noisy on the network; use the proxy option and pace runs to avoid IP blocks.
- Site list drifts as platforms change; a miss can be a broken detector rather than a real absence.
- OpSec: passive toward targets (no login/notify), but your host's IP touches many sites — mask it.

## Overlaps ("do both")
- Run alongside `[[whatsmyname-web]]`, `[[sherlock-2]]`, and `[[blackbird-2]]` — each covers a different, overlapping site set and uses different detection logic; union the results and reconcile.

## Trust & verifiability
`trust: community` — a mature, popular open-source tool, but its matches are algorithmic confidence scores, not verified identities. Confirm every actionable hit by eye before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | social-analyzer |
| category | username |
| selectorsIn → selectorsOut | username, name → social-profile, image, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
