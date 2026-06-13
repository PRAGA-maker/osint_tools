---
id: amazon-registry-search
name: Amazon Registry Search
description: Use when you have a name (plus optional city/state and event date) and want to find a person's public Amazon wedding or baby registry to confirm partner, location, and timeline.
url: https://www.amazon.com/registries
category: people-search
path:
- people-search
- registries
bestFor: Finding a public Amazon (US) wedding or baby registry by name to surface partner, approximate location, and event/due date.
input: Registrant name (optionally city/state and event date)
output: Registry owner + partner names, city/state, event or estimated birth date, wish-list contents
selectorsIn:
- name
selectorsOut:
- name
- associate
- geolocation
- dob
status: live
pricing: free
costNote: Searching and viewing public registries is free; an Amazon account is only needed to purchase, not to view.
opsec: passive
opsecNote: You query Amazon's catalogue, not the target. Searching while logged into your own account links the lookup to you — use a logged-out or sock-puppet session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Amazon US registry search. Data is self-published by the registrant — authentic but only as accurate as entered.
missingPersonsRelevance: medium
coverage: [us]
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- amazon-co-uk-4
aliases: []
tags: []
source: arf-seed
lastVerified: '2026-06-13'
enrichment: full
---

# Amazon Registry Search

> Amazon US's public registry finder — turns a name into a couple/family, an approximate location, and a date anchor (wedding or baby due date).

## When to use
You have a `name` and want to confirm a relationship, hometown, or timeline. Public Amazon wedding and baby registries list both partners' names, a city/state, and an event or estimated birth date — useful `associate`, `geolocation`, and `dob`-adjacent pivots when profiling a person in a missing-persons case.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the URL. Pick the registry type (Wedding, Baby, Birthday, Custom Gift List).
2. In "Find a Registry," enter the registrant's name. For wedding, advanced search accepts name + city/state + event date; for baby, name + city/state + estimated birth month/year.
3. Read results: each hit shows the owner (and partner) name, location, and date. Open a registry for the wish list (interests, baby items implying a due date, children's sizes/ages).
4. Pivot: partner name → people-search / `[[ancestry-com]]`; city/state → a US phone directory or `[[advanced-background-checks]]`.

## Inputs → Outputs
- **In:** `name` (+ optional city/state, date)
- **Out:** `name`/`associate` (partner), `geolocation` (city/state), `dob` (baby due date as a soft date anchor)
- **Empty/negative result looks like:** "No registries found" — registry is private/shared, never made public, or the name differs. Wedding registries appear ~15 min after creation; baby registries 1–6 hours. Absence is not proof of no registry.

## Gotchas & OpSec
- Only **public** registries are searchable; private/shared ones never appear.
- No CAPTCHA or login to search — but run it logged out or from a sock account so the query isn't tied to your real Amazon identity.
- Baby-registry detail (due dates, children's ages) is sensitive; corroborate before relying on it.

## Overlaps ("do both")
- Pairs with `[[amazon-co-uk-4]]` (UK `.co.uk` wedding registry) for cross-region coverage of the same person.

## Trust & verifiability
`trust: trusted` — first-party Amazon US source. Platform is authentic; content is self-reported, so verify names/dates against a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | amazon-registry-search |
| category | people-search |
| selectorsIn → selectorsOut | name → name, associate, geolocation, dob |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
