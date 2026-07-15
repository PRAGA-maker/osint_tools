---
id: funeralnet
name: FuneralNet Obituaries
description: Use when you have a `name` and want to confirm a death and surface funeral/obituary details — date, hometown and surviving family — across US funeral-home sites; returns dob/death date, address, and associate (relatives).
url: http://www.funeralnet.com/obits.html
category: public-records
path:
- public-records
bestFor: Confirming a death and pulling obituary details (dates, hometown, next-of-kin) from funeral-home-hosted memorial pages.
selectorsIn:
- name
selectorsOut:
- dob
- address
- associate
- name
status: degraded
pricing: free
costNote: Free to read obituaries. FuneralNet (which invented online obituaries in 1997) was acquired by Frazer Consultants in 2017; obituary content now lives on Frazer-powered funeral-home sites and the `obit.funeralnet.com` client pages, so the legacy `obits.html` search may be flaky.
opsec: passive
opsecNote: Reading a public obituary is entirely passive and never touches a living subject. Note that obituaries expose relatives' names — handle that PII responsibly, especially in active missing-persons work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-established death-care web provider (founded 1996, now under Frazer Consultants) serving thousands of US/CA/AU funeral homes. Obituary text is authored by funeral homes/families — authoritative for the death event, but family details are as given.
missingPersonsRelevance: high
coverage:
- us
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- the-ancestor-hunt
- legacy-com
aliases:
- funeralnet.com
- FuneralNet obituaries
tags:
- toddington
- curated-directory
- specialty-search
- obituaries
source: toddington-resources
lastVerified: '2026-07-15'
enrichment: full
---

# FuneralNet Obituaries

> The original online-obituary provider, now folded into Frazer Consultants — a route into funeral-home-hosted memorial pages that confirm a death and name the surviving family.

## When to use
You have a `name` and need to establish whether the person has died, and if so, pull the obituary details: death date, age/`dob`, hometown (`address`), and — crucially for genealogy and missing-persons cases — the list of surviving and predeceased relatives (`associate`s). Reach for it when resolving whether a lead is deceased, or when an obituary is the fastest way to map a family tree.

## How to use it (`bestInteractionPattern`: web-manual)
1. Try http://www.funeralnet.com/obits.html; if that legacy search is unresponsive (it's been through the Frazer migration), search the name on Google with `site:obit.funeralnet.com` or `funeralnet obituary "<name>"`.
2. Open the funeral-home memorial page for the match.
3. Read the obituary for death date, age, hometown, and named relatives.
4. Cross-check the name/date against a second obituary source to avoid same-name confusion.
5. Pivot: relatives' names feed people-search and `[[the-ancestor-hunt]]`; a hometown feeds local records.

## Inputs → Outputs
- **In:** `name` (age/locality help disambiguate)
- **Out:** `dob`/death date, `address` (hometown/service location), `associate` (surviving & predeceased family), `name` confirmation
- **Empty/negative result looks like:** no memorial page found — could mean the person is alive, or simply that their funeral home doesn't use FuneralNet/Frazer; absence is NOT proof of life. Check Legacy.com and other obituary aggregators too.

## Gotchas & OpSec
- **Migration state:** post-2017 the content is spread across Frazer-powered sites, so a name search via Google often works better than the old on-site form.
- Same-name collisions are common in obituaries — always corroborate with a second detail (age, town, relatives).
- OpSec: passive; but obituaries reveal living relatives' names — treat that PII carefully.

## Overlaps ("do both")
- Pairs with `[[the-ancestor-hunt]]` (broader obituary/newspaper directories) and Legacy.com — coverage differs by funeral home, so run more than one.
- Feed confirmed relatives into people-aggregators to reach current contacts of the family.

## Trust & verifiability
`trust: community` — an established death-care provider; the death event is authoritative, but family/biographical details are family-authored, so verify anything you'll act on.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | funeralnet |
| category | public-records |
| selectorsIn → selectorsOut | name → dob, address, associate, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
