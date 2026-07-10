---
id: the-knot
name: The Knot
description: Use when you have a couple's `name`(s) and want to find their wedding registry and wedding website — returns wedding location, date, partner name, and a registry/gift page.
url: https://www.theknot.com/registry/couplesearch
category: people-search
path:
- people-search
- registries
bestFor: Finding a couple's wedding registry/website by name to surface a partner, date, and location.
selectorsIn:
- name
selectorsOut:
- name
- associate
- address
status: live
pricing: free
costNote: Free public couple/registry search; no account needed to look one up.
opsec: passive
opsecNote: Passive — you search a public wedding-registry index, not the couple directly. They are not notified. No login required, so nothing ties the query to you beyond normal site logging.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: The Knot is a major, legitimate wedding-planning platform; registry/couple listings are self-published by the couple, so details are as accurate (and as current) as what they entered.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- The Knot couple search
- theknot.com registry
tags:
- registry
- wedding
- people-search
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# The Knot

> A public search over one of the largest US wedding platforms — enter a name and find the couple's registry and wedding website, which often expose a partner, a date, and a location.

## When to use
You have one person's `name` and suspect a marriage/engagement, and you want to confirm a partner (`associate`), a wedding date, or a city (`address`). Wedding registries and wedding websites are a rich, under-used source: couples self-publish their names, event location, and sometimes a shipping city — exactly the relational and geographic links useful when building out a subject's family and timeline.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.theknot.com/registry/couplesearch.
2. Enter one partner's first + last `name`, and (if prompted) the wedding month/year to disambiguate.
3. Read the hit list: each result names both partners and links to the registry and, often, the couple's wedding website.
4. Open the wedding website — these frequently include the ceremony city/venue, date, a "how we met" bio, and a wedding-party list (more `associate`s).
5. Pivot: partner names feed people-search; the venue/city is a location lead; the wedding party gives friends/family to enumerate. Cross-check on `[[myfamilyannouncements-co-uk]]`-style announcement sources.

## Inputs → Outputs
- **In:** `name` (one partner; optional month/year)
- **Out:** partner `name` (`associate`), wedding date, city/venue (`address`), registry/website links
- **Empty/negative result looks like:** no matching couple — meaning no Knot registry under that name (they may have used a different platform like Zola, or none). Absence isn't proof of no marriage.

## Gotchas & OpSec
- All data is self-published by the couple; names can be nicknames and details can be stale or aspirational.
- Common names collide — use the wedding month/year and cross-confirm the partner before trusting a match.
- Registries are sometimes set private or removed after the event; a missing listing may mean "taken down," not "never existed."
- Fully passive and free — no login or captcha, nothing reaches the couple.

## Overlaps ("do both")
- Pairs with obituary/announcement sources like `[[myfamilyannouncements-co-uk]]` and `[[canadian-obituaries]]` — weddings and deaths both map family relationships from a different angle.
- Feed discovered partner/family names into general people-search (`[[searchpeoplefree]]`).

## Trust & verifiability
`trust: community` — The Knot is a legitimate mainstream platform, but every field is user-entered by the couple. Treat listings as strong relational leads to corroborate (via the wedding site, a second registry, or public records), not as verified facts on their own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-knot |
| category | people-search |
| selectorsIn → selectorsOut | name → name, associate, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
