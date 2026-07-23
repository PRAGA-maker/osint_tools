---
id: whois-domain-search-tool
name: Whois Domain Search Tool
description: Use when you have a `domain` (or a bare name) and want to check WHOIS/registration across many TLDs at once — returns registrant/domain records and availability.
url: https://whois.marcaria.com/en
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Checking a name's WHOIS record and registration status across many domain zones in one query.
selectorsIn:
- domain
- name
selectorsOut:
- domain
- name
- email
status: live
pricing: freemium
costNote: WHOIS lookup and multi-TLD availability search are free; Marcaria is a domain registrar that monetises by selling registrations. No account needed to look up records.
opsec: passive
opsecNote: You query Marcaria's WHOIS front-end, not the target — the subject's infrastructure sees nothing. Note that registrar lookup pages sometimes place speculative registration orders; only use the read-only WHOIS/availability view and don't trigger a purchase flow. Use a VPN to keep your own query private from Marcaria.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Front-end of a commercial registrar (Marcaria). WHOIS output mirrors registry data but is increasingly redacted by GDPR/privacy proxies; the multi-TLD view is convenient but the registrar's primary goal is selling you a domain.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Marcaria WHOIS
- whois.marcaria.com
tags:
- Domain/IP/Links
- Domain/IP investigation
- whois
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Whois Domain Search Tool

> Marcaria's WHOIS + multi-TLD search — look up a domain's registration record, or check one name across many domain zones at once.

## When to use
You have a `domain` and want its WHOIS record (registrar, creation/expiry dates, registrant contact where not redacted), or you have a bare brand/name and want to see which TLD variants (`.com`, `.net`, `.co`, ccTLDs…) are registered versus available. The multi-zone view is useful for spotting *other* domains a subject may have registered under the same string.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://whois.marcaria.com/en .
2. For a WHOIS record: enter the full `domain` and read the registration record — registrar, dates, nameservers, and any exposed registrant `name`/`email`/org.
3. For zone coverage: enter just the label (the part before the dot) to see which TLDs are taken vs available — taken variants are pivot leads to check individually.
4. Stay in the read-only lookup; do not proceed into the registrar's buy/order flow.
5. Pivot: an exposed registrant `email`/`name` feeds email- and name-OSINT; other registered TLD variants feed fresh WHOIS lookups and content review.

## Inputs → Outputs
- **In:** `domain`, or a bare label/`name` for multi-TLD availability
- **Out:** WHOIS `domain` record (dates, registrar, nameservers), any exposed registrant `name`/`email`, and taken-vs-available status across TLDs
- **Empty/negative result looks like:** a record with registrant fields showing "Redacted for Privacy" / a privacy-proxy — the domain exists but the owner is hidden; that is normal post-GDPR, not a failed lookup.

## Gotchas & OpSec
- Most registrant contact data is now redacted behind privacy services; expect the personal fields to be empty on many domains.
- It's a registrar's site — avoid the purchase funnel; a speculative order can tip your hand and cost money.
- OpSec: **passive** — nothing touches the target; only Marcaria sees your query.

## Overlaps ("do both")
- Complements historical-WHOIS and reverse-WHOIS services (which can surface pre-redaction registrant data and other domains sharing a registrant). Use this for the current record and multi-TLD sweep, those for history and reverse pivots.

## Trust & verifiability
`trust: community` — a commercial registrar's WHOIS front-end. The record data mirrors registry sources and is reliable for dates/registrar/nameservers; treat exposed contact fields with normal WHOIS skepticism and ignore the sales prompts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whois-domain-search-tool |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, name → domain, name, email |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
