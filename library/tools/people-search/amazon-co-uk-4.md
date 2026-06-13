---
id: amazon-co-uk-4
name: amazon.co.uk
description: Use when you have a name (and rough city/region) and want to find a person's public Amazon UK wedding registry to learn partner name, location, and event date.
url: https://www.amazon.co.uk/gp/registry/search.html?ie=UTF8&type=wedding
category: people-search
path:
- people-search
bestFor: Finding a public Amazon UK wedding registry by registrant name to surface partner, approximate location, and event date.
selectorsIn:
- name
selectorsOut:
- name
- associate
- geolocation
status: live
pricing: free
costNote: Searching and viewing public registries is free; an Amazon account is only needed to purchase items, not to view.
opsec: passive
opsecNote: You are querying Amazon's catalogue, not contacting the target. Browsing while logged into your own Amazon account ties the lookup to your identity — use a clean/sock account or logged-out session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Amazon UK registry search. Data is self-published by the registrant, so it is authentic but only as accurate as what they entered.
missingPersonsRelevance: medium
coverage: [uk]
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- peoplesearch
- People Search Sites
source: uk-osint
lastVerified: '2026-06-13'
enrichment: full
---

# amazon.co.uk (Wedding Registry Search)

> Amazon UK's public wedding-registry finder — turns a name into a couple, an approximate location, and an event date.

## When to use
You have a `name` and want to confirm a relationship or a place/date anchor. Couples create public Amazon wedding registries that list both partners' names, a city/region, and the wedding date — a useful `associate` and `geolocation` pivot when building a person profile for a missing-persons case (e.g. confirming a partner, a hometown, or a timeline).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the URL (or from amazon.co.uk: account menu → "Find a Registry/Gift List" → Wedding).
2. Enter the registrant's first and last name. Optionally narrow with the partner's name; there is no city filter on the UK wedding search, so a full name works best.
3. Read the result list: each hit shows the couple's names and the event date. Open a registry to see the location/shipping region hints and the wish-list contents (interests, sizes, children's items).
4. Pivot: feed the partner name into `[[ancestry-genealogy-family-trees-and-family-history-records]]` or general people-search; feed the location into a UK directory like `[[britishphonebook-com]]`.

## Inputs → Outputs
- **In:** `name`
- **Out:** `name` (partner), `associate`, `geolocation` (rough)
- **Empty/negative result looks like:** "No registries found" — means the registry is private, was never made public, or the name differs. Private/shared registries are not searchable; absence is not proof the person has no registry.

## Gotchas & OpSec
- Only **public** registries appear; many are private. Newly created registries take ~15 minutes to become searchable.
- No CAPTCHA or login to search, but do it from a logged-out or sock-puppet session so the query isn't tied to your real Amazon identity.
- Wish-list contents can leak sensitive lifestyle detail (pregnancy, children's ages) — treat as investigative context, corroborate before acting.

## Overlaps ("do both")
- Pairs with `[[amazon-registry-search]]` (the US `.com` equivalent) for cross-region coverage of the same person.

## Trust & verifiability
`trust: trusted` — first-party Amazon UK source. The platform is authentic; the *content* is self-reported by the registrant, so verify names/dates against a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | amazon-co-uk-4 |
| category | people-search |
| selectorsIn → selectorsOut | name → name, associate, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
