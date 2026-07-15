---
id: google-com-2
name: Google site search — stayfriends.de
description: Use when you have a `name` (and a German school/town) and want to find someone's StayFriends classmates profile without an account — returns `social-profile` links via Google's index.
url: https://www.google.com/search?q=site%3Astayfriends.de
category: social-networks
path:
- social-networks
bestFor: Finding StayFriends (German-speaking classmates/reunion network) profiles by name/school using a Google `site:stayfriends.de` dork.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free — it is a Google web search; no StayFriends account needed to read the indexed snippets.
opsec: passive
opsecNote: You search Google, not StayFriends, so the platform is not notified by the query. Google logs your searches — use a logged-out/sock-puppet session. StayFriends is heavily login-walled, so clicking through will hit a registration prompt; read the Google snippet/cache first.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Google's own web search with a `site:` operator — authoritative engine; results limited only by what Google has indexed from a largely login-walled site.
missingPersonsRelevance: high
coverage:
- de
auth: none
api: false
localInstall: false
registration: false
aliases:
- site:stayfriends.de
- Google StayFriends dork
tags:
- esocialmedia
- European Social Media Sites
- stayfriends
- google-dork
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Google site search — stayfriends.de

> A Google `site:stayfriends.de` dork for finding StayFriends profiles — the German-speaking equivalent of Classmates.com — by name and school without registering.

## When to use
Your subject has a German, Austrian, or Swiss background and you want to place them to a **school, class year, or hometown**. StayFriends is a long-established DACH classmates/reunion network where members list the schools they attended and years — valuable for confirming a person's origin, age band, and early social circle. Because its pages are login-walled, `site:stayfriends.de` via Google is the practical way to surface indexed public fragments (name + school + year) without creating an account.

## How to use it (`bestInteractionPattern`: web-manual)
1. In a logged-out / sock-puppet browser, run: `site:stayfriends.de "Full Name"` (add a school name or town to disambiguate).
2. Read the result titles/snippets — these expose name, school, and often a class year.
3. Prefer the Google snippet or cached copy; the live page will demand registration.
4. Pivot: a confirmed school + year narrows age/DOB and hometown, seeding people-search and other reunion-network lookups.

## Inputs → Outputs
- **In:** `name` (plus optional German school/town)
- **Out:** `social-profile` (StayFriends URL), `name`, school affiliation and class year from the snippet
- **Empty/negative result looks like:** no results or only same-name strangers — Google hasn't indexed a matching profile (common, given the login wall), not proof the person isn't on StayFriends.

## Gotchas & OpSec
- Heavy login wall: expect most detail to require a (sock-puppet) account; lean on snippets/cache.
- German-language name variants and umlauts matter — try both spellings.
- OpSec: the Google search is passive; registering on StayFriends is not — avoid attributable sign-ups.

## Overlaps ("do both")
- Sibling to the `[[google-com-55]]` / `[[google-com-63]]` professional-network dorks — same technique for a reunion network. Pair with other classmates/reunion sites when building an origin/age picture.

## Trust & verifiability
`trust: trusted` — Google search itself; the operator only filters to one host. Confirm each hit is the right individual (same-name collisions) before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-com-2 |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
