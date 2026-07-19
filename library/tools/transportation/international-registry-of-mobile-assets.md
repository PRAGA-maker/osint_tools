---
id: international-registry-of-mobile-assets
name: International Registry of Mobile Assets
description: Use when you have an aircraft identifier or owner/creditor `employer-org` and want registered financial interests in aircraft — returns registered parties and interests via free guest search.
url: https://www.internationalregistry.aero/ir-web
category: transportation
path:
- transportation
bestFor: Searching the Cape Town Convention registry of international financial interests in aircraft/engines to link an aircraft to its financing parties and owners.
selectorsIn:
- employer-org
- vin
selectorsOut:
- employer-org
- document-id
status: live
pricing: freemium
costNote: Guest searches (and tutorials/help) are free; only registering or consenting to an interest requires an approved, paying account. For OSINT, the free guest search is what you need.
opsec: passive
opsecNote: A registry search is passive — you query the registry, not any target, and owners are not notified. Guest access requires no personal registration. Note the interface historically relied on Java/digital certificates for registered users, but guest search does not.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official Cape Town Convention International Registry (operated under Aviareto/ICAO auspices); its records of registered aircraft financial interests are authoritative legal records.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- International Registry
- Cape Town Convention registry
- internationalregistry.aero
tags:
- toddington
- curated-directory
- aviation
- specialty-search
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# International Registry of Mobile Assets

> The official Cape Town Convention registry of financial interests in aircraft and aircraft engines — a free guest search that links an aircraft to the banks, lessors, and organisations holding interests in it.

## When to use
You are investigating an aircraft, or a person/`employer-org` connected to aviation assets, and want to know who holds registered financial interests (security, lease, ownership) in a specific aircraft or engine. This can reveal financing banks, leasing companies, and owning entities behind an aircraft — useful for mapping the corporate/financial web around an aviation asset.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.internationalregistry.aero/ir-web and use guest access (no account needed to search).
2. Search by aircraft object (manufacturer, model, serial number) or by registered party name (`employer-org`).
3. Review the returned registered interests: the parties, interest types, and registration `document-id`s.
4. Use the video tutorials/help if the interface (built for legal professionals) is unfamiliar.
5. Pivot: identified financing/owning organisations feed corporate-registry and company OSINT; serial numbers feed aviation databases and tail-number lookups.

## Inputs → Outputs
- **In:** aircraft object identifier (manufacturer serial, akin to a `vin`) or party `employer-org`
- **Out:** registered `employer-org` parties (creditors/owners/lessors), interest types, registration `document-id`s
- **Empty/negative result looks like:** no registered interest for the object — many aircraft (especially unfinanced or older/pre-registry) won't appear. It is a *financial-interest* registry, not an aircraft ownership/registration authority, and returns no personal `name`/`address`.

## Gotchas & OpSec
- Scope is financial interests under the Cape Town Convention, not general aircraft registration (use national civil-aviation registries for tail-number → owner).
- The interface is built for legal/finance professionals; use the tutorials.
- OpSec: fully passive guest search.

## Overlaps ("do both")
- Pairs with national aircraft registries and tail-number trackers — those give registration/ownership and live flights, while this adds the financing/security-interest layer.

## Trust & verifiability
`trust: trusted` — an authoritative official registry of legal interests; entries are formal registrations, so treat results as reliable records while remembering coverage is limited to registered interests.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | international-registry-of-mobile-assets |
| category | transportation |
| selectorsIn → selectorsOut | employer-org, vin → employer-org, document-id |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
