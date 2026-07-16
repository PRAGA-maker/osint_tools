---
id: intelligence-x-person-tools
name: Intelligence X Person Tools
description: Use when you have a `name`, `email`, `phone`, or `username` and want a launchpad of prebuilt search links into many people-search services at once — returns social-profile, address and name leads.
url: https://intelx.io/tools?tab=person
category: people-search
path:
- people-search
bestFor: A one-page dashboard that generates ready-made queries into dozens of third-party people/identity databases.
selectorsIn:
- name
- email
- phone
- username
selectorsOut:
- social-profile
- address
- name
- phone
status: live
pricing: free
costNote: The Intelligence X tools dashboard (URL generator) is free and needs no IntelX account. Some of the third-party services it links to have their own paywalls/logins.
opsec: passive
opsecNote: The dashboard itself only builds links — it does not query anyone until you click through. Once you do, you are interacting with third-party brokers (Spokeo, Radaris, ThatsThem, etc.), which may log your IP; some require you to be logged in. Use sock-puppet accounts and a VPN for the onward services.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Maintained by Intelligence X, a reputable data-search firm; it is a curated link launcher, so quality of results comes from the third-party services, not IntelX itself.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- IntelX Person Tools
- Intelligence X Tools person tab
- intelx.io tools person
tags:
- people-search
- link-launcher
- intelligence-x
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- facebook-graph-searcher-intelligencex
- intelligence-x
- intelligence-x-2
- intelligence-x-telegram-search
- intelligencex
- intelligencex-linkedin-search
- intelx-io
- tools
---

# Intelligence X Person Tools

> A free dashboard from Intelligence X that turns one identifier into prebuilt search links across dozens of people-search and identity services.

## When to use
You have a `name`, `email`, `phone`, or `username` and want to blitz it across many people-search engines quickly without hand-building each query. The "person" tab groups tools by input type (full-name lookups into Spokeo/ThatsThem/FamilyTreeNow/ZabaSearch/Radaris/TruthFinder, plus email, phone, and username lookups), so you paste once and open the relevant services in turn. It is a launchpad, not a data source — the results come from wherever you click through to.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://intelx.io/tools?tab=person.
2. Find the section matching your input (Full Name, Email, Phone, Username) and enter the value.
3. Click a generated link to open that third-party service's search for your value. Some require you to be logged in to that service to work.
4. Review each service's results and harvest addresses, phones, relatives, and profiles.
5. Pivot: cross-reference results across several linked services — agreement across brokers raises confidence; a single-source claim stays a lead.

## Inputs → Outputs
- **In:** `name`, `email`, `phone`, or `username`
- **Out:** launches into services returning `social-profile`, `address`, `phone`, `name`, relatives
- **Empty/negative result looks like:** the dashboard always builds the links; "empty" means the downstream service returned nothing — try several of the linked services before concluding.

## Gotchas & OpSec
- The dashboard is only a URL builder — data quality and freshness belong entirely to the third-party services it opens.
- Human-in-the-loop: some linked services need you logged in; use sock-puppet accounts, and a VPN, since those brokers log your IP.
- Many linked services are US-centric; coverage varies by service and region.

## Overlaps ("do both")
- Pairs with `[[idcrawl]]` and `[[cyberbackgroundchecks]]` — this launcher fans you out to many brokers at once, while those give focused aggregate results; use the launcher for breadth, the aggregators for depth, and cross-check.

## Trust & verifiability
`trust: community` — curated by Intelligence X (reputable), but it is a link launcher: verify results at the destination services, and treat single-broker data as a lead until corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | intelligence-x-person-tools |
| category | people-search |
| selectorsIn → selectorsOut | name, email, phone, username → social-profile, address, name, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
