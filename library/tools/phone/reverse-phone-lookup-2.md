---
id: reverse-phone-lookup-2
name: IDCrawl Reverse Phone Lookup
description: Use when you have a US `phone` number and want the linked person and their online footprint — returns name, likely social profiles and address leads.
url: https://www.idcrawl.com/phone
category: phone
path:
- phone
bestFor: Reversing a US phone number to a name and associated social-media profiles via IDCrawl's people/aggregation index.
selectorsIn:
- phone
selectorsOut:
- name
- social-profile
- address
status: live
pricing: freemium
costNote: IDCrawl's basic name/preview results are free; some detailed reports/contact data are gated or handed off to paid partner sources.
opsec: passive
opsecNote: You query IDCrawl's aggregated index, not the subject, so no alert is sent. IDCrawl links usernames/profiles across sites; treat the associations as leads and use a sock-puppet session for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: IDCrawl is a well-known people/username aggregator; useful for pivoting a number to social profiles, but its cross-site links are heuristic and can be wrong, so verify each match.
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
- telegram-finder
aliases:
- IDCrawl phone
- idcrawl.com/phone
tags:
- reverse-phone
- people-aggregator
- us
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# IDCrawl Reverse Phone Lookup

> IDCrawl's reverse-phone entry — put in a US number and it surfaces the likely owner's name plus the social-media profiles and public records IDCrawl associates with it.

## When to use
You have a US `phone` number and want to move from digits to a person and their online footprint. IDCrawl is particularly good at tying identifiers to social-media accounts, so a reverse-phone hit can jump you straight to Facebook/Instagram/LinkedIn profiles and a name — a strong pivot when the number is your only starting selector.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.idcrawl.com/phone and enter the full US `phone` number.
2. Read the results: associated name(s), linked social profiles, and location/address hints.
3. Treat each linked profile as a candidate — confirm it's your subject via corroborating detail, not the aggregator's say-so.
4. For deeper contact/records data, follow the gated report or cross-check a dedicated broker.
5. Pivot: a resolved `name` feeds `[[411-us]]`/`[[searchbug]]`; check the number on messaging apps via `[[telegram-finder]]`.

## Inputs → Outputs
- **In:** `phone` (US)
- **Out:** `name`, likely `social-profile` links, and `address`/location leads
- **Empty/negative result looks like:** no owner/profiles found — common for mobiles not tied to public records or for VoIP/burner numbers (classify those separately); absence isn't proof.

## Gotchas & OpSec
- Cross-site profile links are **heuristic** — IDCrawl can attach the wrong account; verify every match on the actual platform.
- US-centric; weaker for non-US numbers. Burner/VoIP numbers often return nothing.
- OpSec: passive toward the target; use a clean session.

## Overlaps ("do both")
- Pairs with `[[searchbug]]` and `[[411-us]]` for contact/records depth, and with `[[telegram-finder]]` to test the same number against messaging apps. Different sources, different hits.

## Trust & verifiability
`trust: community` — a capable aggregator for social-profile pivots, but its associations are inferred; confirm identity independently before relying on any link.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reverse-phone-lookup-2 |
| category | phone |
| selectorsIn → selectorsOut | phone → name, social-profile, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
