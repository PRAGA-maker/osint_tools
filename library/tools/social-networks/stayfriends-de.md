---
id: stayfriends-de
name: stayfriends.de
description: Use when you have a German-speaking subject's `name` and a school and want to place them via a class-reunion network — returns a `social-profile` tied to a school, year, and hometown.
url: https://www.stayfriends.de/
category: social-networks
path:
- social-networks
bestFor: Locating people in Germany/Austria/Switzerland via their school and graduation year on a class-reunion network.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- name
status: live
pricing: freemium
costNote: Free to search and see that a member exists (name, school, year, thumbnail); contacting members or viewing full profiles/photos requires a paid membership.
opsec: passive
opsecNote: Searching is passive, but StayFriends notifies members when their profile is viewed by a logged-in user and encourages contact. Browse logged-out where possible, and use a sock-puppet account (never your real one) if you must register — do not message the subject.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Established DACH-region class-reunion site (StayFriends/Classmates family); profiles are self-registered, so data is user-supplied and its accuracy/currency varies.
missingPersonsRelevance: high
coverage:
- de
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- classmates
- classmates-canada-alumni-lookup
aliases:
- StayFriends
- stayfriends.de
tags:
- esocialmedia
- European Social Media Sites
- classmates
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# stayfriends.de

> The German-speaking world's class-reunion network (StayFriends) — find a person through the school and year they attended, a useful angle when other social platforms come up empty.

## When to use
Your subject is in Germany, Austria, or Switzerland and you know (or can guess) a school they attended. StayFriends organises people by school and graduation year, so it can locate someone via their education history and hometown even when they have little other online presence — valuable for older subjects and for building a picture of a person's origins and cohort (`associate` links to former classmates).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.stayfriends.de and search by `name`, or browse by school → year.
2. Read the free preview: whether a member exists, their listed school/year, hometown, and a thumbnail — enough to confirm presence and cohort.
3. Note that full profiles, photos, and contact are behind a paid membership; the free tier is for confirmation/leads.
4. Do not message the subject; use it to place and corroborate, not to make contact.
5. Pivot: school + year + hometown feed name-based people-search and genealogy; former classmates are `associate` leads.

## Inputs → Outputs
- **In:** `name` (+ school/region), or a school/year to browse
- **Out:** `social-profile` tied to a school/year/hometown, member `name`
- **Empty/negative result looks like:** no member found — the person may not have registered (many haven't); absence is weak evidence, especially for younger people who use mainstream socials instead.

## Gotchas & OpSec
- Human-in-the-loop: contact and full detail are **paywalled**; the free tier only confirms existence and cohort.
- Data is self-registered and can be old or sparse; verify before treating school/year as fact.
- OpSec: passive to search, but logged-in profile views can notify members — browse logged-out and never use your real identity.
- Coverage is DACH-specific; useless outside German-speaking Europe.

## Overlaps ("do both")
- Direct analogue of `[[classmates]]` (US) and `[[classmates-canada-alumni-lookup]]` (Canada) — use the region-appropriate reunion site; the technique (find-via-school) is the same.

## Trust & verifiability
`trust: community` — an established reunion network, but with self-registered, user-supplied data. Treat a hit as a strong locating lead to corroborate, not as verified current information.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | stayfriends-de |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
