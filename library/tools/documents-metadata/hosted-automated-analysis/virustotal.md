---
id: virustotal
name: VirusTotal
description: Use when you have a file hash, `domain`, `ip-address`, or URL and want reputation/malware context — returns detection verdicts, related infrastructure, and pivot data.
url: https://www.virustotal.com/gui/
category: documents-metadata
path:
- documents-metadata
- hosted-automated-analysis
bestFor: Reputation and relationship lookups on files, hashes, domains, IPs, and URLs — a central pivot point for infrastructure OSINT.
selectorsIn:
- domain
- ip-address
- document-id
selectorsOut:
- domain
- ip-address
- metadata-exif
status: live
pricing: freemium
costNote: Free tier with a registered account (public API, ~4 requests/min, 500/day). Enterprise/VT Intelligence with advanced search, retrohunt, and relationships is paid.
opsec: active
opsecNote: Submitting a FILE uploads it to VirusTotal and shares it with the security community and paying customers — never upload sensitive/private documents you don't want disclosed. Looking up an existing hash/domain/IP/URL is passive (no upload) and safe. Uploading a URL causes VT to fetch it, which can touch the target site.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Google (Chronicle); the de-facto standard multi-engine reputation service. Aggregates 70+ AV engines and vast passive-DNS/relationship data. Verdicts are indicative, not definitive.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- urlscan-io
- shodan
- hybrid-analysis
aliases:
- VT
- virustotal.com
tags:
- malware-analysis
- reputation
- passive-dns
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# VirusTotal

> The standard multi-engine reputation and relationship service — look up a file hash, `domain`, `ip-address`, or URL and get detection verdicts plus a rich web of related infrastructure to pivot on.

## When to use
You have a suspicious `domain`, `ip-address`, URL, or a file hash (`document-id`) tied to your subject's infrastructure and want reputation context and connections. VirusTotal's real OSINT value is the **Relations** tab: passive DNS, hosted files, subdomains, resolutions, and communicating files that let you pivot from one indicator to a whole cluster of related infrastructure.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign in at https://www.virustotal.com/gui/ (free account raises limits).
2. Search a hash, `domain`, `ip-address`, or URL (or paste a URL to have VT scan it).
3. Read the **Detection** tab for AV verdicts, then the **Details** and **Relations** tabs for the pivot gold: passive-DNS history, subdomains, resolutions, referrer/downloaded files.
4. For files: only upload when you accept it becomes public; prefer hash lookup when you just need reputation.
5. Pivot: related `domain`s/`ip-address`es feed `[[shodan]]` and `[[urlscan-io]]`; file `metadata-exif`/relationships feed malware-focused follow-up.

## Inputs → Outputs
- **In:** file hash (`document-id`), `domain`, `ip-address`, URL
- **Out:** detection verdicts, `domain`/`ip-address` relations (passive DNS, subdomains), file `metadata-exif` and links
- **Empty/negative result looks like:** "no matches" / "0/70 detections" — the indicator is unknown or clean to VT, not proof of safety; combine with other sources.

## Gotchas & OpSec
- **Uploading a file discloses it.** Treat every file upload as public. Use hash lookup for private material.
- Free tier is rate-limited (account required); heavy pivoting needs the paid VT Intelligence.
- A clean verdict ≠ benign; a detection ≠ confirmed malicious. Verdicts are leads to corroborate.

## Overlaps ("do both")
- Pairs with `[[urlscan-io]]` (renders and screenshots URLs, shows page-level connections) and `[[shodan]]` (service/banner view of an IP). Do all three on a domain/IP to combine reputation, page behaviour, and exposed services.

## Trust & verifiability
`trust: trusted` — Google-operated, industry-standard, transparent multi-engine aggregation. Highly reliable as a pivot hub; treat individual AV verdicts as advisory and cross-check.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | virustotal |
