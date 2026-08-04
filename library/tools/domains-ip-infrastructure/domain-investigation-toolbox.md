---
id: domain-investigation-toolbox
name: Domain Investigation Toolbox
description: Use when you have a `domain` and want a single launchpad to 40+ WHOIS, subdomain, hosting-history and tech-profiling lookups — returns links out to registration data, related domains and contact info.
url: http://cipher387.github.io/domain_investigation_toolbox/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Pivoting one domain into 40+ investigation tools from a single page without hunting for each URL.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
- email
status: live
pricing: freemium
costNote: The launchpad page is free; a few of the destination tools it links (e.g. DomainTools) have paid tiers, most are free.
opsec: passive
opsecNote: The toolbox page itself is a static list of links and runs nothing. OpSec depends on the destination you click — WHOIS/DNS lookups are passive, but each linked service sees the domain you submit. Assume the domain is disclosed to whichever tool you open.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Curated by OSINT researcher cipher387 (Cyber Detective); a hand-maintained link hub, so individual destinations may go stale.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- domain investigation toolbox cipher387
tags:
- domain
- launchpad
- link-hub
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Domain Investigation Toolbox

> A one-page launchpad by cipher387: type a domain once and jump into 40+ WHOIS, subdomain, hosting-history and tech-profiling services.

## When to use
You have a `domain` (a subject's website, a scam site, an employer domain) and want to run the standard battery of domain checks — registration and WHOIS history, hosting/IP history, subdomains, technologies, headers, traffic and contact-info lookups — without remembering or bookmarking each individual tool's URL.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://cipher387.github.io/domain_investigation_toolbox/.
2. Enter the target `domain` in the page's input box.
3. Click through the categorised buttons (WHOIS, hosting history, subdomains, tech stack, contacts, etc.) — each opens the destination tool pre-filled with your domain.
4. Collect the outputs from each service: registrant/email, historical IPs, subdomains, and related infrastructure.
5. Pivot: a registrant `email` feeds email-OSINT; historical `ip-address` and subdomains feed infrastructure clustering.

## Inputs → Outputs
- **In:** `domain`.
- **Out:** links to registration/WHOIS data, historical `ip-address` records, subdomains and additional `domain`s, and any exposed registrant `email`.
- **Empty/negative result looks like:** a destination tool showing "no records" or a redacted-by-privacy WHOIS — normal for privacy-protected domains; move to hosting/cert-based pivots instead.

## Gotchas & OpSec
- It's a link hub, not an aggregator: it does no analysis itself and produces no combined report — you read each destination separately.
- Some linked destinations (marked `$`) require paid accounts; skip or substitute a free equivalent.
- Links rot over time; if a button 404s, the underlying service may have moved or closed.

## Overlaps ("do both")
- Complements automated domain enrichers like `[[recon-ng]]` and `[[hostintel-keithjjones-github]]` — the toolbox is fast manual triage, those give scripted, storable output for larger domain/IP sets.

## Trust & verifiability
`trust: community` — a single researcher's curated list; trustworthy as a menu, but the authority of any result rests entirely on the destination service you land on, not the toolbox.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | domain-investigation-toolbox |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address, email |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
