---
id: majordomo-russia
name: Majordomo (Russia)
description: Use when you have a `.ru`/`.рф` `domain` and want registrar/WHOIS and availability data from a major Russian host — returns `domain` registration status and hosting leads.
url: https://www.majordomo.ru
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Checking .ru/.рф domain availability and registrar/hosting context on one of RuNet's oldest hosting providers.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: The WHOIS/availability check is free; registration and hosting are paid services you do not need for OSINT.
opsec: passive
opsecNote: A WHOIS/availability query hits Majordomo's lookup service, not the domain's owner. It is a Russian commercial site; use a sock-puppet browser and expect a Russian-language interface. Avoid registering or logging in.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-established (since 2000) Russian registrar/host; its WHOIS reflects registry data but the site is a commercial vendor, not the registry itself.
missingPersonsRelevance: low
coverage:
- ru
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- majordomo.ru
- Majordomo hosting
tags:
- toddington
- curated-directory
- whois-ip-lookups-website-analysis
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Majordomo (Russia)

> One of RuNet's oldest hosting providers and registrars, whose free WHOIS/availability tool is a convenient window into `.ru`/`.рф` domain status when investigating Russian infrastructure.

## When to use
You have a Russian `domain` (`.ru`, `.рф`, `.su`) and want a quick registrar-side WHOIS and availability read from a local provider — useful when Western WHOIS services are sparse or redacted for RuNet TLDs. It confirms whether a domain is registered, and provides hosting/registrar context to characterise the infrastructure behind a Russian-language site of interest.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.majordomo.ru in a sock-puppet browser (interface is Russian; a translate extension helps).
2. Find "Сервис WHOIS" / "Проверить занятость домена" (WHOIS / check domain availability) in the navigation.
3. Enter the domain. Read whether it is занят (taken/registered) or свободен (available), plus any registrar/registration detail exposed.
4. Pivot: cross-check with the authoritative registry WHOIS (`.ru` via TCI/RU-CENTER, `.рф` similarly) and resolve the domain to an `ip-address` via a DNS/passive-DNS tool.

## Inputs → Outputs
- **In:** `domain` (`.ru`/`.рф`/`.su`)
- **Out:** `domain` registration/availability status and registrar context; hosting-provider leads that can point toward an `ip-address`.
- **Empty/negative result looks like:** "свободен" (available) means no registration exists; a taken domain with redacted personal data (typical for `.ru`) shows only registrar/technical fields, not the registrant name.

## Gotchas & OpSec
- `.ru` WHOIS heavily redacts private registrant data by policy — expect registrar and dates, rarely a person.
- This is a vendor front end, not the registry; for authoritative records confirm against the official RuNet registry WHOIS.
- OpSec: passive query, but it's a Russian commercial site — use a clean browser/VPN and never register or log in with real details.

## Overlaps ("do both")
- Complements authoritative RuNet registry WHOIS and passive-DNS tools — use Majordomo for a fast availability read, then confirm registrant/technical data against the registry and resolve the hosting IP elsewhere.

## Trust & verifiability
`trust: community` — an established commercial registrar; its lookup surfaces registry-derived data but should be corroborated against the official registry for anything you'll rely on.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | majordomo-russia |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
