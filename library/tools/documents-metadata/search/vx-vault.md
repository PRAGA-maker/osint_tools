---
id: vx-vault
name: VX Vault
description: Use when you have a malware `domain`/URL or file hash and want to check a live malware-URL tracker — returns recent malicious URLs, hosting IPs and sample hashes.
url: https://vxvault.net/ViriList.php
category: documents-metadata
path:
- documents-metadata
- search
bestFor: Checking a live feed of recently-seen malware distribution URLs, their IPs and sample hashes.
selectorsIn:
- domain
- ip-address
- document-id
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free public tracker, no account. A plain list view and per-entry detail pages; refreshed roughly every 12 hours.
opsec: passive
opsecNote: You browse VX Vault's own catalogue of already-collected malware URLs — you are not visiting the malicious sites themselves. Do NOT open the listed URLs in a real browser; they point to live malware. Analyse hashes/URLs in a sandbox.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running community malware-URL tracker, ingested by mainstream blocklists (FireHOL, IntelMQ). Reliable as a feed of observed malicious URLs; it's a tracker, not an analysis verdict service.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- VXVault
- vxvault.net
tags:
- malware
- threat-intel
- ioc
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# VX Vault

> A live, free malware-URL tracker — a rolling list of recently-observed malware distribution URLs with their hosting IPs and sample hashes, feeding mainstream blocklists.

## When to use
You have a suspicious `domain`/URL, a hosting `ip-address`, or a file hash (`document-id`) and want to check it against a continually-updated record of known malware-distribution URLs. Also useful for pulling fresh IOCs — recent malicious URLs and the IPs behind them — for infrastructure clustering.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://vxvault.net/ViriList.php for the current list of recently-tracked malware URLs (refreshed ~every 12 hours).
2. Scan or search for your `domain`/`ip-address`/hash; open an entry for detail — the malicious URL, resolved IP, and associated sample hash(es).
3. Treat a match as "seen distributing malware", and record the URL/IP/hash as IOCs.
4. **Never open a listed URL** in a normal browser — analyse the hash/URL in a sandbox (any.run, VT) instead.
5. Pivot: the hosting `ip-address` feeds reverse-IP/infrastructure mapping; the hash feeds VirusTotal and sample repositories.

## Inputs → Outputs
- **In:** malware `domain`/URL, hosting `ip-address`, or file hash (`document-id`)
- **Out:** matching malicious `domain`/URL, hosting `ip-address`, sample hash(es)
- **Empty/negative result looks like:** no match in the list — the URL/IP isn't in VX Vault's recent tracking, NOT proof it's benign. Cross-check other malware feeds.

## Gotchas & OpSec
- It's a *tracker* of observed malicious URLs, not an on-demand scanner; absence means "not tracked", not "clean".
- The list is a rolling window; older entries age out — pull data when you need it and timestamp it.
- OpSec: **passive** on VX Vault's own pages, but the listed links are live malware — sandbox everything, never click through with a real identity.

## Overlaps ("do both")
- Complements other malware/IOC feeds (URLhaus, MalwareBazaar) and phishing feeds like `[[https-openphish-com-feed-txt]]` — each tracks different slices; combine for coverage.

## Trust & verifiability
`trust: community` — an established community tracker consumed by major blocklists. A listing is credible evidence a URL served malware; corroborate current status and analyse samples in a sandbox before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vx-vault |
| category | documents-metadata |
| selectorsIn → selectorsOut | domain, ip-address, document-id → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
