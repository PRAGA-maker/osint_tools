---
id: netcraft
name: Netcraft
description: Use when you have a domain or ip-address and want its hosting history, technology stack, and network attribution — returns ip-address, domain, and hosting/registrar history for infrastructure attribution.
url: https://netcraft.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Site reports with hosting history, tech stack, and network details to attribute and track a domain over time.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: The public Site Report tool is free; Netcraft's takedown/anti-phishing and API products are commercial. No account needed for the basic report.
opsec: passive
opsecNote: Netcraft answers from its own long-running survey data, so the target site is not directly contacted by your query — passive attribution research.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Netcraft has run internet-infrastructure surveys since the 1990s; its hosting-history data is a recognized, long-standing reference.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- netcraft-site-report
aliases:
- Netcraft Site Report
tags:
- site-report
- dns
- hosting-history
source: gh-topic-footprinting
lastVerified: '2026-07-23'
enrichment: full
---

# Netcraft

> The classic internet-infrastructure survey: a Site Report giving a domain's hosting history, network owner, and technology stack going back years.

## When to use
You have a `domain` (or `ip-address`) tied to a subject — a personal site, a scam page, a business — and want to attribute and track it: which hosts/ASNs it has lived on, when it moved, what tech it runs, and its registrar/nameserver footprint. Hosting history is especially useful for linking sites that shared infrastructure. It's infrastructure attribution, not people-search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://sitereport.netcraft.com (or netcraft.com → Site Report) and enter the `domain`.
2. Read the report: network `ip-address`, hosting company/ASN, registrar, nameservers, first-seen date, and a **hosting history** timeline.
3. Note the tech stack (server, framework, tracking IDs) — shared trackers/hosts can link a subject's other sites.
4. Cross-reference a shared IP/host with other domains to cluster related infrastructure.
5. Pivot: an ASN/host → [[ipvoid]] or ARIN/RIR WHOIS; a first-seen date → archive tooling.

## Inputs → Outputs
- **In:** a `domain` (or `ip-address`).
- **Out:** `ip-address`, hosting company/ASN, registrar, nameservers, tech stack, and a dated hosting-history timeline.
- **Empty/negative result looks like:** "We could not find a site report" for a domain Netcraft's survey has never crawled, or a sparse report for a very new/low-traffic site — absence of history, not proof the domain is fake.

## Gotchas & OpSec
- Data comes from Netcraft's periodic survey, so a brand-new domain or a rarely-visited site may have thin or missing history.
- Hosting behind a CDN (Cloudflare, etc.) masks the true origin IP — the report shows the CDN, not the backend.
- Free report is rate-limited; heavy/automated use pushes you toward their paid API.

## Overlaps ("do both")
- Pairs with [[ipvoid]] and RIR WHOIS (e.g. [[whois-arin]]): Netcraft gives the historical hosting timeline, those give current reputation and registrant ownership.

## Trust & verifiability
`trust: trusted` — decades-old infrastructure-survey provider; the hosting-history data is widely cited, and current DNS/IP facts are independently re-checkable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | netcraft |
