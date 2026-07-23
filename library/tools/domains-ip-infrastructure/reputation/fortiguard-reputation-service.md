---
id: fortiguard-reputation-service
name: FortiGuard Web Filter / IP Reputation Lookup
description: Use when you have an `ip-address` or `domain` and want Fortinet's categorization and reputation for it — returns the content category and any malicious/reputation flag.
url: https://fortiguard.com/iprep
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- reputation
bestFor: Checking how Fortinet categorizes and rates a URL/IP (content category, malicious reputation).
selectorsIn:
- ip-address
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free public lookup from Fortinet (FortiGuard Labs); no account required for single lookups.
opsec: passive
opsecNote: Passive — you query FortiGuard's threat-intel database, not the target host, so the subject site/IP is not contacted and receives no notification. Reflects Fortinet's classification, which is one vendor's view.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Fortinet/FortiGuard Labs data — a major commercial threat-intelligence vendor; authoritative for how Fortinet products will treat the target.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- fortiguard-labs
aliases:
- FortiGuard
- FortiGuard Web Filter Lookup
- iprep
tags:
- reputation
- threat-intel
- web-filter
- ip
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# FortiGuard Web Filter / IP Reputation Lookup

> Fortinet's public lookup for how FortiGuard Labs categorizes and rates a URL or IP — content category plus any malicious/reputation flag.

## When to use
You have a `domain`/URL or `ip-address` and want to know how a major security vendor classifies it: what content category it's filed under (e.g. malware, phishing, business, personal blog) and whether it carries a bad reputation. Useful for triaging a suspicious link found in an investigation, or for understanding whether a subject's infrastructure is flagged.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://fortiguard.com/iprep (or the Web Filter lookup) and enter the `ip-address` or `domain`/URL.
2. Submit and read the assigned category and reputation.
3. If you believe the category is wrong, FortiGuard offers a re-categorization request form (optional).
4. Cross-check against other reputation engines before drawing conclusions from a single vendor's rating.
5. Pivot: a "malicious"/"phishing" category flags the host for deeper (authorized) infrastructure investigation.

## Inputs → Outputs
- **In:** `ip-address` or `domain`/URL
- **Out:** Fortinet content category and reputation/threat classification for the target
- **Empty/negative result looks like:** "not rated"/uncategorized or a benign category — means Fortinet has no adverse classification, not that the host is definitively clean.

## Gotchas & OpSec
- Reflects **one vendor's** view; categories can be stale or disputed — corroborate with other reputation sources.
- "Uncategorized" is common for new/low-traffic domains and isn't a safety guarantee.
- Passive lookup only; it doesn't scan the target itself.

## Overlaps ("do both")
- Pairs with VirusTotal, URLhaus, and other reputation engines — take the consensus across several vendors rather than trusting a single classification.

## Trust & verifiability
`trust: trusted` — first-party FortiGuard Labs data; authoritative for Fortinet's own classification, though it's still one vendor's opinion and worth cross-checking.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fortiguard-reputation-service |
