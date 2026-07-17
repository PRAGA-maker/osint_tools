---
id: deleteme-digital-footprint-analyzer
name: DELETEME (digital footprint analyzer)
description: Use when you have a `username` and want to enumerate matching accounts across many sites — returns social-profile hits plus GDPR deletion templates.
url: https://github.com/surfruit/deleteme
category: username
path:
- username
bestFor: Sherlock-style username enumeration across many platforms from the CLI, with an added privacy/GDPR-removal angle.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free open-source Python tool; no account or API key required.
opsec: active
opsecNote: The tool requests each candidate profile URL to test existence, so requests hit the target platforms directly (not the subject). Run from a research host/VPN; profiles you request may log the visit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: A small single-author project (~1 star) inspired by Sherlock; functional but far less mature and less maintained than Sherlock/Maigret — prefer those for coverage.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- deleteme
- surfruit/deleteme
tags:
- username-enumeration
- sherlock-like
- privacy
source: gh-topic-footprinting
lastVerified: '2026-07-17'
enrichment: full
---

# DELETEME (digital footprint analyzer)

> A local, Sherlock-inspired username enumerator that scans many sites for a handle and also generates GDPR account-deletion templates.

## When to use
You have a `username` and want to enumerate where it exists across platforms, entirely locally. DELETEME checks the handle against a customizable site list and exports audit reports (PDF/CSV/TXT). Its distinguishing feature is the privacy angle — it auto-generates GDPR Article 17 removal templates — but for pure investigative coverage the mature tools (Sherlock, Maigret) are the better first choice.

## How to use it (`bestInteractionPattern`: cli)
1. Clone and install:
   ```
   git clone https://github.com/surfruit/deleteme
   python -m pip install aiohttp fpdf2 colorama
   ```
2. Run a scan: `python -m deleteme.engine <username>`.
3. Review the reports (PDF/CSV/TXT); CSV is formatted for Google Sheets tracking.
4. Update/extend the site list in `deleteme/sites.py` (or run `sync.py` to pull community-added sites) for better coverage.
5. Pivot: open each confirmed `social-profile` to harvest names, photos and links; cross-run the same handle through `[[sherlock]]`/Maigret to catch sites this list misses.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` hits across the configured site list, exported as PDF/CSV/TXT (plus GDPR deletion templates)
- **Empty/negative result looks like:** no confirmed profiles — but with a small/stale site list this understates presence; treat absence as "not found on these sites," not proof of no accounts.

## Gotchas & OpSec
- **Active:** it fetches candidate profile URLs directly; run behind a VPN/research host.
- Small, lightly-maintained project — the built-in site list is narrower than Sherlock/Maigret, so recall is lower. Expect false negatives.
- Username matches aren't identity proof; the same handle can belong to different people.

## Overlaps ("do both")
- Pairs with `[[sherlock]]` and Maigret — run those for breadth; DELETEME adds the GDPR-removal templates if the privacy angle matters.

## Trust & verifiability
`trust: unverified` — a tiny single-author Sherlock clone; it works but is far less proven, so verify every hit on the live profile and prefer mature enumerators for coverage.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | deleteme-digital-footprint-analyzer |
| category | username |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
