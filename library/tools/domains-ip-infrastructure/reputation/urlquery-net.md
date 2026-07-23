---
id: urlquery-net
name: UrlQuery.net
description: Use when you have a suspicious `domain`/URL and want a safe hosted analysis of it — screenshots, hosting IP, redirects, and malware/phishing verdicts — returns `ip-address` and threat findings.
url: https://urlquery.net/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- reputation
bestFor: Safely analysing a URL for malware/phishing and capturing its hosting IP, redirects, and content without visiting it yourself.
input: URL or webpage
output: Threat report, detected threats, malicious behavior, anomalies, security assessment
selectorsIn:
- domain
selectorsOut:
- ip-address
- domain
status: live
pricing: free
costNote: Free to submit and view reports; no account required for basic use.
opsec: active
opsecNote: The SERVICE visits the target URL from its own infrastructure, so your IP/browser never touches the target — that's the point. But the target's server sees urlquery's scanner and the report is often PUBLIC, so submitting a private/unindexed URL can tip off the owner and expose the link to others. Don't submit sensitive URLs you don't want disclosed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running URL-analysis service; reputable in the malware-analysis community, results are automated heuristics to interpret, not absolute verdicts.
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
- urlquery
aliases:
- urlquery
tags:
- url-analysis
- malware
- phishing
- reputation
source: arf-seed
lastVerified: '2026-07-23'
---

# UrlQuery.net

> A hosted URL sandbox: submit a link and its servers visit and analyse it for you — returning a screenshot, the hosting IP and redirect chain, and malware/phishing indicators — so you never load a hostile page yourself.

## When to use
You have a suspicious `domain`/URL — from a phishing message, a scam profile, a shortened link in a subject's activity — and want to know what it does and where it lives without exposing your own machine. UrlQuery captures the page safely and surfaces the hosting `ip-address`, redirects to other `domain`s, embedded resources, and threat scores.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://urlquery.net/ and submit the URL (or search existing reports for it).
2. Wait for the automated analysis.
3. Read the report: screenshot, final and intermediate `domain`s (redirects), hosting `ip-address` and geo, detected scripts/behaviour, and UQ/IDS/TDS threat metrics.
4. Pivot: the hosting IP feeds reverse-IP and WHOIS; redirect domains feed further infrastructure mapping; the screenshot confirms what a victim sees.

## Inputs → Outputs
- **In:** `domain`/URL
- **Out:** `ip-address` (hosting), redirect `domain`s, screenshot, malware/phishing indicators
- **Empty/negative result looks like:** a clean report (no threats) or a page that failed to load / is offline — "clean" means no automated flags, not a guarantee of safety.

## Gotchas & OpSec
- Reports are often public and searchable: submitting a private/unshared URL can leak it and alert the operator — treat submission as disclosure.
- OpSec: **active** toward the target (urlquery's scanner visits it), but it shields *you* — that separation is the benefit; still don't submit sensitive links.
- Automated verdicts have false positives/negatives; interpret, don't blindly trust.

## Overlaps ("do both")
- Pairs with urlscan.io, VirusTotal, and redirect tracers — different sandboxes render and flag pages differently, so cross-check a borderline URL.

## Trust & verifiability
`trust: community` — a well-regarded analysis service; verify a decisive finding (e.g. an origin IP) against a second sandbox before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | urlquery-net |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → ip-address, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
