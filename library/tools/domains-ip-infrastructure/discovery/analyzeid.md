---
id: analyzeid
name: AnalyzeID
description: Use when you have a `domain` and want other sites the same person runs — pivots on shared Google Analytics/AdSense/Amazon/tracking IDs and emails to return related `domain`s.
url: https://analyzeid.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- discovery
bestFor: Finding other websites owned by the same operator via shared tracking/analytics IDs and contact details.
selectorsIn:
- domain
selectorsOut:
- domain
- email
status: live
pricing: freemium
costNote: Free lookups are available (with a paid tier for more/volume); a username-checker is also offered. No account needed for basic queries.
opsec: passive
opsecNote: AnalyzeID queries its own crawl/index of a domain's tracking IDs — it does not fetch pages from the target on your behalf at query time, so the subject is not alerted. Standard sock-puppet browser hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party service inferring ownership from shared identifiers; the signal is real but circumstantial, and its index coverage/freshness is not independently audited.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- username-checker
aliases:
- Analyze ID
- AnalyzeID
tags:
- domain-recon
- tracking-id-pivot
- attribution
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# AnalyzeID

> Reverse-lookup a domain by the tracking IDs it embeds — Google Analytics/AdSense, Amazon affiliate, shared emails — to surface the operator's *other* websites.

## When to use
You have a `domain` tied to a subject and want the rest of their web footprint. Site owners reuse the same Google Analytics/AdSense codes, Amazon affiliate tags, and contact emails across every site they run; AnalyzeID indexes those identifiers and returns the sibling domains sharing them. It is a stronger ownership signal than reverse-IP alone (which lumps in unrelated shared-hosting neighbors).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://analyzeid.com/.
2. Enter the target `domain`/URL.
3. Read the results: related domains grouped by the shared identifier that links them (analytics ID, AdSense ID, affiliate tag, email, IP, etc.).
4. Weight the links: a shared **Analytics/AdSense** ID is a strong same-owner signal; a shared IP alone is weak (could be shared hosting).
5. Pivot: each related `domain` feeds WHOIS, `[[whois-search]]`, and content review; a surfaced `email` feeds email-OSINT.

## Inputs → Outputs
- **In:** a `domain`
- **Out:** related `domain`s (with the shared tracking ID/`email` that connects them)
- **Empty/negative result looks like:** no related domains — the site either uses no reused trackers, hides them, or AnalyzeID has not indexed them; absence is not proof the operator runs nothing else.

## Gotchas & OpSec
- Human-in-the-loop: none for a basic lookup; the paid tier lifts volume limits.
- OpSec: passive — you query AnalyzeID's index, not the target's server.
- Shared-identifier links vary in strength: analytics/AdSense IDs are compelling; shared IP/CDN links are often false positives from common hosting. Confirm before asserting common ownership.
- Index coverage depends on when/whether AnalyzeID crawled the site; a fresh or obscure domain may be missing.

## Overlaps ("do both")
- Pairs with reverse-WHOIS and certificate pivoting (`[[certgraph]]`): AnalyzeID links by *tracking IDs*, certgraph by *TLS certs*, reverse-WHOIS by *registrant* — each catches relationships the others miss, so run several and intersect the results.

## Trust & verifiability
`trust: community` — the underlying signal (shared, publicly embedded tracking codes) is genuine and independently checkable by viewing a site's source, but AnalyzeID's coverage is unaudited; verify a claimed link by confirming the shared ID appears in both sites' HTML.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | analyzeid |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, email |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
