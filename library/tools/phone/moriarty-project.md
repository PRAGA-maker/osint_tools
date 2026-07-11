---
id: moriarty-project
name: Moriarty-Project
description: Use when you have a `phone` number and want to aggregate owner, spam-risk, related links, and possible social platforms in one CLI run — returns name and social-profile leads.
url: https://github.com/AzizKpln/Moriarty-Project
category: phone
path:
- phone
bestFor: Running a single local CLI pass over a phone number to pull carrier/owner hints, spam risk, related links, and candidate social platforms.
selectorsIn:
- phone
selectorsOut:
- name
- social-profile
status: degraded
pricing: free
costNote: Free and open source (GitHub). Some enrichment modules depend on third-party services/keys that may have changed since the last release (v4.1.2).
opsec: passive
opsecNote: Runs locally and queries public phone-intel sources; it does NOT call or message the target, so the owner is not notified. However, some modules hit third-party APIs from your IP — run it from a VPN/sock-puppet host, and note that querying certain sources over their free tier may be rate-limited or logged.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source project (~2k stars) by AzizKpln; community-maintained with 100+ commits, but relies on scraping/third-party endpoints that can silently break, so validate results.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- phoneinfoga
- truecaller-search-engine
aliases:
- Moriarty
- Moriarty Project
tags:
- phone
- cli
- phone-osint
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# Moriarty-Project

> An open-source local CLI that fans a single phone number out across public phone-intel sources — owner hints, spam risk, related links, and candidate social platforms — in one run.

## When to use
You have a `phone` number and want a fast, self-hosted first pass that aggregates several lookups at once rather than querying sites one by one. Good as an opening move in phone OSINT: it surfaces owner/spam signals and points you at social platforms and links to chase manually. Because it is local, it is convenient for batch or scripted enrichment where a browser tool would be slow.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo: `git clone https://github.com/AzizKpln/Moriarty-Project`.
2. Install dependencies: `cd Moriarty-Project && bash install.sh`.
3. Run it: `bash run.sh` (desktop Linux; the author notes it is **not** supported on Termux / Kali NetHunter mobile).
4. Enter the target number in full international format when prompted.
5. Read the aggregated output: owner/`name` hints, spam-risk rating, related links, and candidate `social-profile` platforms.
6. Pivot: treat platform hits as leads to confirm manually — the tool flags where an account *might* exist, not that it belongs to the owner.

## Inputs → Outputs
- **In:** `phone` (international format)
- **Out:** owner `name` hints, spam-risk context, related links, candidate `social-profile` platforms
- **Empty/negative result looks like:** modules return "not found" or error out (a broken upstream source) — absence here is weak evidence; cross-check with a second phone tool before concluding.

## Gotchas & OpSec
- Scraper rot: modules that depend on third-party sites break silently when those sites change. A null result may be a dead module, not a real negative — verify against [[phoneinfoga]] or [[truecaller-search-engine]].
- Social-platform hits do **not** confirm ownership; the author explicitly states the social features don't prove the account belongs to the number's owner.
- OpSec: passive — no contact is made with the target. Run from a VPN/sock-puppet host since some modules query APIs from your IP.

## Overlaps ("do both")
- Pairs with [[phoneinfoga]] (stronger carrier/format/footprint analysis and active maintenance) and [[truecaller-search-engine]] (crowd-sourced caller-ID) — run both and reconcile, since each hits different sources.

## Trust & verifiability
`trust: community` — widely used open-source project, but it wraps third-party scrapers whose accuracy and uptime vary. Treat every hit as a lead to confirm at the source, not as verified fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | moriarty-project |
| category | phone |
| selectorsIn → selectorsOut | phone → name, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
