---
id: cacador
name: Cacador
description: Use when you have a report, threat feed, or blob of text and want to extract and deduplicate indicators (IPs, domains, emails, hashes, URLs) — returns ip-address, domain and email leads.
url: https://github.com/sroberts/cacador
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- ioc-tools
bestFor: Fast local extraction and deduplication of IOCs (IPs, domains, URLs, emails, hashes) from unstructured text.
selectorsIn:
- domain
selectorsOut:
- ip-address
- domain
- email
status: live
pricing: free
costNote: Free, open-source (Go) CLI by Scott Roberts. Download a binary or build from source; no account.
opsec: passive
opsecNote: Fully passive and offline — it parses text you already have and makes no network calls, so it's safe to run against sensitive reports or dumps in an air-gapped environment. Extraction only; it does not query or contact any indicator.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Mature open-source IOC-extraction tool from a well-known DFIR author (Scott Roberts); regex-based, so review output for false positives.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- jager
aliases:
- Cacador
- cacador ioc extractor
tags:
- ioc-extraction
- dfir
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# Cacador

> A tiny, fast Go CLI that reads any text and spits out a clean, deduplicated list of indicators — IPs, domains, URLs, emails, and file hashes — ready for the next tool.

## When to use
You have unstructured text with indicators buried in it — a threat-intel report, a pasted email, an incident write-up, a scraped page, or a log — and you want the IOCs pulled out and deduplicated in one pass rather than by hand. It's the offline first step that turns prose into a structured indicator list you can then enrich, block, or pivot on. Passive and local, so it's safe for sensitive material.

## How to use it (`bestInteractionPattern`: cli)
1. Grab a Cacador binary (or `go install`) from https://github.com/sroberts/cacador.
2. Pipe or feed text: `cat report.txt | cacador` (outputs structured JSON/CSV of found IOCs).
3. Read the deduplicated results grouped by type: `ip-address`es, `domain`s, URLs, `email`s, and hashes (MD5/SHA1/SHA256).
4. Save the output for downstream enrichment.
5. Pivot: extracted `ip-address` → `[[team-cymru-ip-to-asn]]`/geolocation; `domain` → WHOIS/DNS; hashes → VirusTotal; `email` → email OSINT.

## Inputs → Outputs
- **In:** any text/report/feed (piped or file) — often collected from a `domain`/source
- **Out:** deduplicated `ip-address`es, `domain`s, URLs, `email`s, and file hashes
- **Empty/negative result looks like:** empty groups — the text genuinely contains no indicators of that type, or they're defanged/obfuscated (e.g. `hxxp`, `[.]`) beyond the parser; refang the text and re-run.

## Gotchas & OpSec
- Regex extraction → some false positives and misses (especially defanged IOCs) — review before acting.
- It extracts, it doesn't validate or enrich — a pulled domain/IP still needs verification.
- OpSec: fully offline/passive; ideal for confidential reports.

## Overlaps ("do both")
- Same job family as `[[jager]]`, iocextract, and `[[grep-for-osint]]` — Cacador is the quick Go binary; use the others when you need Python integration or richer defang handling.

## Trust & verifiability
`trust: community` — established open-source tool from a respected DFIR author; deterministic regex extraction, so results are reproducible and easy to audit.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cacador |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → ip-address, domain, email |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
