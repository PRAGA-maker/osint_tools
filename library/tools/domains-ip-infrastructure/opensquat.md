---
id: opensquat
name: openSquat
description: Use when you have a brand/keyword and want to catch look-alike phishing `domain`s registered against it — scans newly-registered-domain feeds and returns suspicious squatting `domain`s.
url: https://github.com/atenreiro/opensquat
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Detecting typosquatting/phishing domains impersonating a brand from newly-registered-domain feeds.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Community/core engine is free and open-source (GPLv3, atenreiro). VirusTotal confirmation needs a free VT API key; premium NRD feeds/API need an opensquat.com key.
opsec: passive
opsecNote: The core keyword scan reads public newly-registered-domain feeds and does not touch the suspect sites, so it's low-footprint. Enabling --vt/--dns queries VirusTotal/Quad9 about the candidates over your IP — expected, but attributable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source anti-phishing tool; keyword/Levenshtein matching is transparent, but candidate lists need human triage to separate real threats from coincidental names.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- atenreiro/opensquat
- OPENSQUAT
tags:
- Domain/IP/Links
- Domain/IP investigation
- phishing
- typosquatting
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- dns-twist
---

# openSquat

> Anti-phishing radar: give it your brand keywords and it flags freshly-registered look-alike domains before they're weaponised.

## When to use
You want to detect domains registered to impersonate a brand, org, or name — typosquats, homoglyphs, bitsquats, and phishing look-alikes. openSquat scans newly-registered-domain (NRD) feeds against your keyword list using Levenshtein distance and confusable-character checks, surfacing candidate `domain`s that mimic your target. Useful for protecting an organisation and for spotting infrastructure being stood up against a person or brand you're tracking.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install opensquat` (Python 3.10+) or clone the repo.
2. Put your brand/keywords in `keywords.txt` (one per line).
3. Run: `opensquat -k keywords.txt -o results.txt`.
4. Add confirmation flags: `--vt` (VirusTotal check, needs a VT API key), `--dns` (Quad9 malicious-DNS check), `--ct` (Certificate Transparency).
5. Triage results manually, then pivot: feed confirmed squats into WHOIS/hosting lookups and reputation checks; monitor them over time.

## Inputs → Outputs
- **In:** brand/keyword list (the `domain`/name you want protected)
- **Out:** candidate look-alike `domain`s from recent NRD feeds, optionally scored via VT/Quad9/CT
- **Empty/negative result looks like:** no candidates — no recently-registered domain matched your keywords in the scanned window; run regularly, since squats appear continuously.

## Gotchas & OpSec
- Matches include innocent coincidental domains — human triage is required; a hit is a lead, not a verdict.
- Coverage is limited to the NRD feed window; premium feeds widen it. Some checks (VT) need your own API key.
- OpSec: the core scan is passive (reads feeds), but VT/DNS confirmation queries third parties over your IP.

## Overlaps ("do both")
- Pairs with `[[dns-twist]]` — dnstwist permutes a single domain to find registered variants, while openSquat matches keywords against live NRD feeds; together they cover both "variants of my domain" and "new domains mentioning my brand".

## Trust & verifiability
`trust: community` — a well-known open-source anti-phishing tool with transparent matching logic; results are algorithmic candidates that must be confirmed (optionally via the built-in VT/DNS/CT checks).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | opensquat |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
