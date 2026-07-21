---
id: brightcloud
name: BrightCloud
description: Use when you have a `domain` or `ip-address` and want its web-content category, reputation score, WHOIS summary and (for IPs) geolocation and co-hosted domains — returns `domain`/`ip-address` reputation and infrastructure context.
url: https://brightcloud.com/tools/url-ip-lookup.php
category: search-engines
path:
- search-engines
bestFor: Reputation, content-category and infrastructure lookup for a domain or IP — including co-hosted (virtually hosted) domains on an IP.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
- geolocation
status: live
pricing: free
costNote: Free single lookups (you accept OpenText's terms on use); bulk/API "Web Classification" and "IP Reputation" feeds are paid enterprise products.
opsec: passive
opsecNote: Passive toward the subject — you query OpenText's threat-intel index about the domain/IP, not the target's server, so no connection reaches the subject's infrastructure. OpenText logs your lookups.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by OpenText (formerly Webroot BrightCloud), a major commercial threat-intelligence provider; classifications are authoritative for reputation/category, though the free tool is a summarized view of the paid feed.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- webroot-brightcloud-url-ip-lookup
aliases:
- Webroot BrightCloud
- OpenText BrightCloud URL/IP lookup
tags:
- speciality-search-engines
source: awesome-osint
lastVerified: '2026-07-21'
enrichment: full
---

# BrightCloud

> A threat-intelligence lookup (now OpenText, formerly Webroot BrightCloud) that classifies a domain or IP — category, reputation, WHOIS, and the other domains sharing an IP.

## When to use
You have a `domain` or `ip-address` from an investigation — a site a subject runs, a server in a network trail, an IP from a header/log — and want to characterize it: what content category it falls in, whether it has a bad reputation, basic WHOIS, and (for an IP) its geolocation and the **other domains virtually hosted on it** (a strong pivot for linking a subject's infrastructure).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the lookup (https://brightcloud.com/tools/url-ip-lookup.php — it now redirects to OpenText's threat-intel support host).
2. Enter the `domain` or `ip-address` and accept the terms prompt.
3. For a URL: read category, reputation score + influences, and basic WHOIS.
4. For an IP: read threat status/analysis, geolocation, and the list of virtually-hosted domains on that IP.
5. Pivot: co-hosted domains link a subject's other sites; a reputation/category flag guides whether infrastructure is malicious/parked; WHOIS/geolocation feed further infra OSINT.

## Inputs → Outputs
- **In:** `domain` or `ip-address`
- **Out:** content category + reputation, WHOIS summary, IP `geolocation`, co-hosted `domain`s
- **Empty/negative result looks like:** "uncategorized" / no reputation data — the target is too new or low-traffic to be classified, not proof it's clean; corroborate with other passive-DNS/reputation tools.

## Gotchas & OpSec
- The free tool is a **summarized** view of OpenText's paid feed — depth is limited vs. the enterprise API.
- Co-hosted-domain data reflects shared hosting; on big shared IPs it can be noisy (many unrelated sites).
- OpSec: passive toward the subject; OpenText logs your queries.

## Overlaps ("do both")
- Pairs with passive-DNS and other IP-reputation tools — reputation vendors disagree, and co-hosted-domain lists differ, so cross-check an IP across two providers before drawing links.

## Trust & verifiability
`trust: trusted` — a major commercial threat-intel provider (OpenText/Webroot); classifications are authoritative, but treat the free summary as a lead and verify infrastructure links with a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | brightcloud |
| category | search-engines |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
