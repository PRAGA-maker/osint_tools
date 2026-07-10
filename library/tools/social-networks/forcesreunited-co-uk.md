---
id: forcesreunited-co-uk
name: forcesreunited.co.uk
description: Use when you have a UK military subject's `name`, unit, or service era and want to place them via a veterans' network — returns a member `social-profile` tied to a regiment/unit and service dates.
url: http://www.forcesreunited.co.uk/
category: social-networks
path:
- social-networks
bestFor: Locating and corroborating UK armed-forces veterans via a military reunion/community network (by unit, regiment, and service period).
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- name
- associate
status: degraded
pricing: freemium
costNote: Free to search/see members; contacting members and full features have historically required a paid/premium membership. Uptime and activity have declined over the years — verify it's live before relying on it.
opsec: passive
opsecNote: Searching is passive, but the site is community-oriented and encourages contact. Browse logged-out where possible; if you register, use a sock-puppet identity and do not message the subject.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A UK forces reunion community; profiles are self-registered, so service claims are user-supplied and unverified — treat as leads, not proof of service.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- classmates
- stayfriends-de
aliases:
- Forces Reunited
- forcesreunited.co.uk
tags:
- uksocialmedia
- UK Social Media Sites
- military
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# forcesreunited.co.uk

> A UK armed-forces reunion network — find and corroborate a veteran through the regiment/unit and years they served, an angle that can place a military subject when civilian platforms don't.

## When to use
Your subject has a UK military background and you know (or can infer) a regiment, unit, ship, or service period. Forces Reunited organises members by service history, so it can locate a veteran, corroborate a claimed posting, and surface former comrades (`associate`) — useful for older subjects and for verifying military claims in a background check.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.forcesreunited.co.uk/ and search by `name`, or browse by service/regiment/unit and era.
2. Read the free member preview: service history claimed, unit, dates, and any profile detail.
3. Note that contacting members / full profiles is behind a paid membership; the free tier is for confirmation/leads.
4. Do not message the subject; use it to place and corroborate.
5. Pivot: unit + era feed military-history and genealogy research; former comrades are `associate` leads; cross-check service claims against official/other sources.

## Inputs → Outputs
- **In:** `name` (+ unit/regiment/era), or a unit to browse
- **Out:** member `social-profile` tied to service history, `name`, former-comrade `associate`s
- **Empty/negative result looks like:** no member found — many veterans never registered (and activity has waned); absence is weak evidence, especially for younger service leavers.

## Gotchas & OpSec
- Status **degraded**: uptime and activity have declined; confirm the site is functioning before relying on it.
- Human-in-the-loop: contact/full detail is **paywalled**; the free tier only confirms presence/claims.
- Service history is self-registered and unverified — corroborate before treating a posting as fact.
- UK-focused; irrelevant for non-UK forces.
- OpSec: passive to search; never use your real identity if you register.

## Overlaps ("do both")
- Same "find-via-shared-institution" technique as `[[classmates]]` (schools) and `[[stayfriends-de]]` (DACH schools) — here the institution is a military unit; corroborate service via official records.

## Trust & verifiability
`trust: community` — a genuine veterans' community, but with self-registered, unverified service claims and declining activity. Treat a hit as a locating/corroboration lead, not proof of service.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | forcesreunited-co-uk |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, name, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
