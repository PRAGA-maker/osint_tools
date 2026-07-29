---
id: urlvoid
name: URLVoid
description: Use when you have a `domain`/URL and want its reputation across 30+ blocklists plus basic hosting info — returns domain, ip-address and reputation leads.
url: http://www.urlvoid.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Checking a website/domain's reputation against many blocklist and threat-reputation engines at once.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free website-reputation checker (by NoVirusThanks). No account needed for basic scans; an API is available on paid plans.
opsec: passive
opsecNote: Passive against the target — URLVoid queries reputation services and its own data, so you do not connect to the suspect site directly. Your query is logged by URLVoid, a third party; don't submit anything you must keep confidential.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running reputation aggregator (NoVirusThanks); it summarizes third-party blocklists, so treat a clean result as "not flagged", not "proven safe".
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- url-void
aliases:
- urlvoid.com
tags:
- domain-and-ip-research
- reputation
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# URLVoid

> A one-shot website-reputation checker — paste a domain and see how 30+ blocklists and reputation engines rate it, plus basic hosting and registration facts.

## When to use
You have a `domain` or URL from a lead (a link in a message, a site tied to a subject, a suspected phishing/scam page) and want a fast reputation read before engaging with it: is it flagged as malicious/phishing by security engines, when was it registered, and where is it hosted. Useful for triaging whether a domain is hostile and for pulling quick registration/hosting context passively.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.urlvoid.com.
2. Enter the `domain` (host only, not a full path) and scan.
3. Read the report: blocklist detections (which engines flag it), the IP/hosting/server location, and domain creation date.
4. Note any detections and the hosting details.
5. Pivot: the resolved `ip-address`/host → infrastructure mapping; registration date → newness as a phishing signal; detections → cross-check on VirusTotal / urlscan.io.

## Inputs → Outputs
- **In:** a `domain`/URL
- **Out:** reputation/blocklist detection summary, `ip-address` and hosting/server location, domain age (`domain` metadata)
- **Empty/negative result looks like:** "0/30 detections" and sparse data — the domain is unflagged and possibly new/obscure; a clean score is absence of a flag, not proof of safety.

## Gotchas & OpSec
- Aggregates other services' verdicts — coverage and freshness vary; confirm on VirusTotal/urlscan for anything you'll act on.
- Domain-only input; strip the path/scheme.
- OpSec: passive — you don't touch the suspect site; URLVoid does the lookups.

## Overlaps ("do both")
- Pairs with VirusTotal, urlscan.io and `[[url-void]]` — different engines flag different threats; run more than one for confidence.

## Trust & verifiability
`trust: community` — reputable aggregator, but it's summarizing third-party blocklists; treat results as reputation signal, not ground truth.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | urlvoid |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
