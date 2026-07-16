---
id: peekyou
name: PeekYou
description: Use when you have a `name` or `username` and want their web/social footprint — returns aggregated social profiles, usernames and public web presence tied to that person.
url: https://www.peekyou.com/
category: people-search
path:
- people-search
- general-people-search
bestFor: Aggregating a person's social profiles and web presence from a name or username.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- username
- name
status: live
pricing: freemium
costNote: Free to search and see aggregated profiles/links; deeper contact/background reports route to paid partner brokers.
opsec: passive
opsecNote: PeekYou aggregates public web/social data — the subject is not contacted and nothing is posted. You disclose the searched name/handle to PeekYou; use a sock-puppet browser. Some "full report" links hand off to commercial data brokers.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A long-running US-focused people aggregator that links names to social profiles; convenient, but a third-party scraper whose matches (and any broker upsell data) need verification.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
aliases:
- PeekYou
- peekyou.com
tags:
- people-search
- social-aggregator
- web-footprint
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- peek-you-user-name
- peekyou-people-search
---

# PeekYou

> A name-to-profiles aggregator: turn a name or handle into a bundle of linked social accounts and web presence, US-focused.

## When to use
You have a `name` (ideally with a city) or a `username` and want to quickly assemble the person's social and web footprint — which platforms they're on, linked usernames, and public mentions. Good as an early consolidation step that connects a real name to online accounts you can then work individually.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.peekyou.com/ in a sock-puppet browser.
2. Search by `name` (add location to disambiguate) or by `username`.
3. Read the aggregated result: linked `social-profile`s, associated `username`s, age/location hints, and web mentions.
4. Verify each linked profile actually belongs to your subject — aggregators over-link for common names.
5. Pivot: confirmed handles feed `[[user-searcher]]`/`[[instant-username]]`; a real name + location feeds `[[thats-them]]`/`[[radaris-people-and-business-search-north-america]]`; avoid the paid broker upsells unless needed.

## Inputs → Outputs
- **In:** `name` (+ optional location) or `username`
- **Out:** aggregated `social-profile`s, `username`s, `name`/age/location hints, web mentions
- **Empty/negative result looks like:** few/no linked profiles — a low-footprint or non-US person, or a common name diluting results. Absence is not proof of no presence; try adding location or a known handle.

## Gotchas & OpSec
- **Over-linking risk:** for common names, PeekYou may bundle several different people. Confirm each profile belongs to your subject before relying on it.
- US-centric; coverage thins internationally.
- OpSec: **passive**; "full report" buttons hand off to paid brokers — stick to the free aggregation for triage, using a sock puppet.

## Overlaps ("do both")
- Pairs with `[[webmii]]` (another name aggregator) and username tools (`[[user-searcher]]`, `[[instant-username]]`) — aggregators differ in what they link, so cross-check, then verify each surfaced profile directly.

## Trust & verifiability
`trust: unverified` — a third-party aggregator with no match verification; treat every linked profile as a candidate to confirm by opening it and corroborating identity across accounts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | peekyou |
| category | people-search |
| selectorsIn → selectorsOut | name, username → social-profile, username, name |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
