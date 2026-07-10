---
id: peekyou-people-search
name: PeekYou People Search
description: Use when you have a `name` or `username` and want a free aggregation of someone's social profiles, photos and contact leads — returns `social-profile`, `address`, `phone`, `associate`.
url: https://peekyou.com/
category: people-search
path:
- people-search
bestFor: Free people-search that stitches together social profiles, usernames, photos and work history from across the web.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- address
- phone
- associate
status: live
pricing: free
costNote: Free to search 300M+ profiles by name or username; some contact detail links out to paid data-broker partners, which you can ignore.
opsec: passive
opsecNote: Passive — PeekYou aggregates public web content; the subject is not notified. Its own servers log your queries. It only surfaces public content and is not a consumer reporting agency (FCRA), so it must not be used for employment/tenant/credit decisions.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A long-running people aggregator; results are compiled from scattered public sources and are often conflated across same-name individuals — treat as leads, not confirmations.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- PeekYou
- peekyou.com
tags:
- toddington
- curated-directory
- people-search
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# PeekYou People Search

> A free people-search aggregator: give it a name or username and it pulls together the social profiles, photos, usernames and work history scattered across the web into one identity view.

## When to use
You have a `name` or a `username` and want a fast, free first sweep that links a person to their social footprint — profiles, reused handles, photos, and rough location/work leads. Especially handy for turning a real name into a set of `social-profile`s (and vice versa) early in a trace, before you commit to paid tools.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://peekyou.com/ and search by `name` (add a city/state to narrow) or by `username`.
2. Open the best-matching profile card: linked social accounts, usernames, photos, approximate location, and work history.
3. Treat contact fields (address/phone) that route to paid partners as leads, not confirmations; ignore the upsell unless you separately verify.
4. Confirm each linked social account is really your subject before relying on it.
5. Pivot: reused usernames feed `[[sherlock]]`/`[[namechk]]`; photos feed reverse-image/face tools; a confirmed name feeds `[[familytree]]`/`[[beenverified-2]]`.

## Inputs → Outputs
- **In:** `name` (+ optional city/state) or `username`
- **Out:** `social-profile` links, reused `username`s, photos, `address`/`phone` leads, `associate`/work history
- **Empty/negative result looks like:** thin card or wrong-person matches — the subject has little public footprint, or the name is too common. Same-name conflation is frequent; verify before trusting.

## Gotchas & OpSec
- Human-in-the-loop: none, but you must manually confirm each linked profile (aggregators conflate people).
- OpSec: **passive** — subject not notified; PeekYou logs your queries.
- Not FCRA-compliant — do not use for employment/tenancy/credit screening; contact fields often push to paid brokers.

## Overlaps ("do both")
- Pairs with `[[sherlock]]`/`[[namechk]]` (username spread) and `[[familytree]]`/`[[beenverified-2]]` (US records) — PeekYou links name↔social footprint; the others confirm identity and add records.

## Trust & verifiability
`trust: unverified` — a convenient free aggregator, not an authority. Every linked profile and contact detail is a lead to confirm against a primary source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | peekyou-people-search |
| category | people-search |
| selectorsIn → selectorsOut | name, username → social-profile, address, phone, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
