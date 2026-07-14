---
id: landregistryservices-com
name: landregistryservices.com
description: Use when you have a UK property `address` and want the registered owner's `name` and title details — returns name, address, and document-id (paid, independent agent).
url: https://www.landregistryservices.com/
category: public-records
path:
- public-records
bestFor: Ordering HM Land Registry title registers/plans for a UK property to identify the registered legal owner.
selectorsIn:
- address
selectorsOut:
- name
- address
- document-id
status: live
pricing: freemium
costNote: Independent search agent, not the official registry. Per-document fees apply (title registers/plans typically ~£20-£45 each). HM Land Registry's own service is cheaper (title summary free, register £3-£7) — use this only for the agent's convenience/bundling.
opsec: passive
opsecNote: You order a document about a property, not a query against the subject. The owner is not notified. Purchase leaves a payment trail with the agent; use appropriate payment hygiene if attribution matters.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Independent commercial reseller of HM Land Registry documents; not affiliated with the UK government. The underlying title data is official, but you pay a middleman markup.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- gov-uk-land-registry
- landregistry-uk-com
aliases:
- Land Registry Services
tags:
- propertysites
- Property Related Sites
- land-registry
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# landregistryservices.com

> An independent search agent that resells HM Land Registry title documents: turn a UK `address` into the registered owner's name and the property's title register.

## When to use
You have a UK property `address` — a subject's home, a property they're linked to, an inheritance lead — and you want the registered legal owner's `name` and title details. The title register names the current proprietor(s), often with an address for service that may differ from the property itself, plus the title number (`document-id`) and any charges/mortgages.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.landregistryservices.com/ and choose the title register (ownership) and/or title plan product.
2. Search for the property by `address` and select the matching title.
3. Pay the per-document fee and receive the official HM Land Registry title register/plan (usually by email, sometimes with a short processing delay).
4. Read the proprietorship register: registered owner name(s), an address for service, the title number, price paid (if post-2000), and any registered charges.
5. Pivot: the owner `name` + address-for-service feeds people-search; a corporate owner feeds a companies registry.

## Inputs → Outputs
- **In:** `address` (UK property)
- **Out:** `name` (registered proprietor), `address` (address for service, may differ from the property), `document-id` (title number), mortgage/charge details
- **Empty/negative result looks like:** no matching title, or a property registered to a company/overseas entity rather than a person — follow the entity instead.

## Gotchas & OpSec
- **Prefer the official route.** HM Land Registry's own service ([[gov-uk-land-registry]]) gives a free title summary and a £3-£7 register; this agent charges more for the same underlying document. Only use it for bundling/convenience.
- Not all land is registered (mostly pre-1990 unregistered titles exist), and very recent transfers may lag.
- Human-in-the-loop: payment required per document.
- OpSec: passive toward the subject; the payment trail sits with the agent.

## Overlaps ("do both")
- Pairs with [[gov-uk-land-registry]] — go to the official registry first for the free summary to confirm the title exists and get the title number, then decide whether to pay anyone for the full register.

## Trust & verifiability
`trust: community` — the documents delivered are genuine HM Land Registry records (authoritative), but the site is an unaffiliated commercial reseller, so verify pricing and consider the official source before paying.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | landregistryservices-com |
| category | public-records |
| selectorsIn → selectorsOut | address → name, address, document-id |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
