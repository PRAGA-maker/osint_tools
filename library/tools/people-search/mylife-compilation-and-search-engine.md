---
id: mylife-compilation-and-search-engine
name: MyLife
description: Use when you have a US `name` and want an aggregated profile with address, phone, age and relatives — returns contact and background leads, but treat its "reputation" data skeptically.
url: https://www.mylife.com/
category: people-search
path:
- people-search
bestFor: US aggregated people-search — surfacing addresses, phones, age, relatives and a profile summary from public-records compilation.
selectorsIn:
- name
selectorsOut:
- address
- phone
- associate
- social-profile
status: live
pricing: freemium
costNote: Free search shows a teaser profile (name, age, city, relatives, a "reputation score"); full contact/background reports require a paid subscription.
opsec: passive
opsecNote: Queries hit MyLife's aggregated data, not the subject — but note MyLife also notifies people that someone searched them and markets "reputation" repair, so a subject monitoring their own MyLife page could infer interest. Use a sock-puppet context; don't create an account tied to you.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: MyLife has a poor consumer reputation (FTC settlement over deceptive practices); its "reputation scores" are marketing, not fact. The underlying public-records contact data can be useful, but verify everything.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- searchbug
- 411-us
- nuwber
aliases:
- mylife.com
tags:
- toddington
- curated-directory
- people-search
- us
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# MyLife

> A US people-search/"reputation" aggregator — it will surface a person's addresses, phones, age and relatives, but its headline "reputation scores" are marketing gimmicks; mine it for contact leads, not judgments.

## When to use
You have a US `name` and want another aggregator's take on their contact and background details — address history, phone numbers, age, and relatives — to cross-check against other brokers. Treat MyLife as one more data point: useful for leads, unreliable for its editorializing. Its main OSINT value is the public-records compilation buried under the reputation-score marketing.

## How to use it (`bestInteractionPattern`: web-manual)
1. Search a `name` (add a state/city) at https://www.mylife.com/.
2. Read the free teaser: age, city, relatives, past addresses, and a "reputation score" (ignore the score).
3. Use relatives/age to disambiguate common names.
4. If you need the full report, it's paywalled — but often other brokers give the same data more cheaply.
5. Pivot: relative `associate` names and past `address`es feed `[[searchbug]]`, `[[411-us]]`, `[[nuwber]]`; verify any contact detail against those before relying on it.

## Inputs → Outputs
- **In:** `name` (US)
- **Out:** `address` history, `phone`, `associate`/relatives, and sometimes linked `social-profile`s
- **Empty/negative result looks like:** no or distant matches — person is young/opted-out/non-US; absence isn't conclusive. Beware confidently-wrong "profiles" stitched from mismatched records.

## Gotchas & OpSec
- **Reputation scores are marketing** (MyLife settled with the FTC over deceptive practices) — never treat them as findings.
- Data can conflate different people; verify addresses/relationships elsewhere.
- Human-in-the-loop: full data **paywalled**; and MyLife's "someone searched you" nudges mean a self-monitoring subject could notice interest — use a sock puppet.

## Overlaps ("do both")
- Run alongside `[[searchbug]]`, `[[411-us]]` and `[[nuwber]]` — use MyLife only to cross-check contact leads, and trust the corroborated fields, not MyLife's narrative.

## Trust & verifiability
`trust: unverified` — reputationally poor and prone to stitched/incorrect profiles; extract raw contact leads and confirm every one against a more reliable source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mylife-compilation-and-search-engine |
| category | people-search |
| selectorsIn → selectorsOut | name → address, phone, associate, social-profile |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
</content>
