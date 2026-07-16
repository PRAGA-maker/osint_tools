---
id: facebook-ad-s-link
name: Facebook Ad's Link (Meta Ad Library)
description: Use when you have a Facebook Page `social-profile` (or its page-ID) and want to pull every ad it has run — returns the advertiser's other pages, funding entity, and reach data.
url: https://www.facebook.com/ads/library/
category: social-networks
path:
- social-networks
bestFor: Reading the full ad history of a Facebook/Instagram Page, including who paid for political/issue ads.
selectorsIn:
- social-profile
- employer-org
- name
selectorsOut:
- social-profile
- employer-org
- geolocation
status: live
pricing: free
costNote: Free, public Meta transparency tool; no account needed to browse, though logging in shows more.
opsec: passive
opsecNote: You are browsing Meta's public transparency database, not contacting the target. Requests hit Facebook, so use a sock-puppet/logged-out browser if you do not want the query tied to your own account; nothing is disclosed to the advertiser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Meta as its legally-mandated ad-transparency archive; the ad and funder data is first-party and authoritative.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
aliases:
- Meta Ad Library
- Facebook Ad Library
tags:
- facebook
- Facebook General Links
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
---

# Facebook Ad's Link (Meta Ad Library)

> Meta's public ad-transparency archive: every active and past ad from a Facebook/Instagram Page, plus who funded the political ones.

## When to use
You have a Facebook Page tied to a subject, a business, or a campaign and want to see what it advertises, when it started, and — for political/issue ads — the paying entity, budget band, and audience geography. Useful for tying an individual to a business they run, confirming a Page is active, and finding sibling Pages the same advertiser operates.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.facebook.com/ads/library/.
2. Pick a country and ad category. For **all ads** from a specific Page, search the Page name or paste its numeric page-ID into a `view_all_page_id=` URL. For **political & issue** ads, choose that category to unlock the funder/spend/reach panels.
3. Read the results: each ad card shows creative, launch date, platforms, and (for political ads) "Paid for by", spend range, impressions, and audience geography/age/gender.
4. Note the advertiser's other Pages listed under "See ad details" — a common pivot to related entities.
5. Pivot: a funder name → company registry; another Page → back into profile OSINT.

## Inputs → Outputs
- **In:** `social-profile` (Page name/URL or page-ID), or an `employer-org`/`name` to search by
- **Out:** `social-profile` (sibling Pages, advertiser identity), `employer-org` (funding entity), `geolocation` (audience reach regions for political ads)
- **Empty/negative result looks like:** "0 results" — the Page has never advertised, or has no ads in the selected country/category. That is common; absence of ads is not absence of a Page.

## Gotchas & OpSec
- Full spend/funder/reach data appears only for **political & issue** ads; commercial ads show creative and dates only.
- Coverage and the political-ad category vary by country; pick the right `country=` value.
- There is an official Ad Library API for bulk political-ad pulls (requires ID verification), but the web UI needs no login.
- OpSec: passive — you query Meta, never the advertiser.

## Overlaps ("do both")
- Pairs with general Facebook profile/graph search tools — those find the person, this exposes what their Page pays to promote and who bankrolls it.

## Trust & verifiability
`trust: trusted` — this is Meta's own mandated transparency archive; ad content, funder disclosures, and spend bands are first-party.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facebook-ad-s-link |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile, employer-org, name → social-profile, employer-org, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
