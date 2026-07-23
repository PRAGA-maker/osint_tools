---
id: metadefender
name: MetaDefender Cloud
description: Use when you have a file or hash (`document-id`) or a `domain`/`ip-address` and want multi-engine malware/reputation analysis — returns verdicts and extracted IOCs.
url: https://metadefender.opswat.com/
category: documents-metadata
path:
- documents-metadata
- hosted-automated-analysis
bestFor: Multi-engine file/URL/IP reputation and malware analysis with IOC extraction (hash lookups possible).
selectorsIn:
- document-id
- domain
- ip-address
selectorsOut:
- document-id
- domain
- ip-address
status: live
pricing: freemium
costNote: Free tier (web + limited API) for scanning and hash/URL/IP lookups; higher volume and advanced features are paid (OPSWAT commercial plans).
opsec: active
opsecNote: Submitting a file uploads it to OPSWAT's cloud (shared for analysis) — don't upload sensitive/evidential files; use the hash-lookup path instead, which reveals nothing new. Domain/IP/hash lookups query OPSWAT's database and never touch the target, so those are effectively passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party service from OPSWAT, an established security vendor. Multi-engine verdicts are credible but are engine opinions (false positives/negatives apply); reputation data quality varies by indicator.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- opswat-meta-defender
- jotti-s-malware-scanner
aliases:
- OPSWAT MetaDefender
- MetaDefender Cloud
tags:
- malware
- multi-av
- reputation
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# MetaDefender Cloud

> OPSWAT's multi-engine analysis platform — scan a file or (safer) look up its hash, a URL, IP, or domain against dozens of engines and get verdicts plus extracted indicators.

## When to use
You have a suspicious file, a hash (`document-id`), or a `domain`/`ip-address` and want a vendor-grade, multi-engine read: is it malicious, what do the engines call it, and what IOCs are associated. Prefer the **hash/URL/IP lookup** paths for anything sensitive so you never have to upload the file itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://metadefender.opswat.com/ .
2. Choose the input: paste a **hash** (best for sensitive files), a URL, an IP/domain — or upload a file only if it's safe to share.
3. Read the multi-engine verdict, threat classification, and any extracted IOCs / behavioural notes.
4. For a file you can't upload, compute its SHA-256 locally and use the hash lookup — same intel, no exposure.
5. Pivot: extracted `domain`/`ip-address` IOCs feed infrastructure clustering; the hash feeds VirusTotal / `[[jotti-s-malware-scanner]]` cross-checks.

## Inputs → Outputs
- **In:** file or hash (`document-id`), URL, `domain`, or `ip-address`
- **Out:** multi-engine malware verdicts, reputation, and extracted IOCs (`domain`/`ip-address`)
- **Empty/negative result looks like:** "no threats detected" / unknown indicator — the engines/database don't flag it, which is *inconclusive*, not clearance. Novel malware and fresh infrastructure read clean.

## Gotchas & OpSec
- **Uploading a file shares it** with OPSWAT's cloud; use hash lookups for confidential/evidential material.
- Free tier has rate/volume limits; heavy or API use pushes into paid plans.
- Verdicts are engine opinions and reputation is heuristic — corroborate across tools.

## Overlaps ("do both")
- Pairs with `[[jotti-s-malware-scanner]]` and VirusTotal — overlapping-but-different engine sets; cross-check (by hash) to catch what one misses.

## Trust & verifiability
`trust: trusted` — a reputable vendor service. Multi-engine consensus is a strong signal; treat any single verdict cautiously and prefer hash-based lookups to avoid exposing files.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | metadefender |
| category | documents-metadata |
| selectorsIn → selectorsOut | document-id, domain, ip-address → document-id, domain, ip-address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
