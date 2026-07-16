---
id: app-fanpagekarma-com
name: Fanpage Karma Facebook Catalogue
description: Use when you have a `name` or `username` and want to find and compare public Facebook (and other social) pages/profiles by keyword — returns social-profile and name.
url: https://app.fanpagekarma.com/facebook-catalogue
category: social-networks
path:
- social-networks
bestFor: Keyword-searching a directory of public Facebook pages to locate a person's or brand's page.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: freemium
costNote: The Facebook catalogue/page-search is free to browse; deeper analytics (engagement, posting-time analysis, historical metrics) require a Fanpage Karma account and paid plan.
opsec: passive
opsecNote: Searches a directory/analytics index of public pages — it does not visit the page as you or notify its admin. Only your IP touches Fanpage Karma. Good for locating a page without leaving a footprint on Facebook itself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Fanpage Karma is an established commercial social-analytics company; its public catalogue is a legitimate page-discovery index, though coverage skews to public Pages rather than personal profiles.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- FanpageKarma
- Fanpage Karma Catalogue
- app.fanpagekarma.com
tags:
- facebook
- Facebook General Links
- page-search
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- fanpage-karma
---

# Fanpage Karma Facebook Catalogue

> A searchable directory of public Facebook Pages (and other social channels) from a social-analytics vendor — useful for finding a page by keyword without touching Facebook directly.

## When to use
You have a `name`, brand, or `username` and want to locate the associated public Facebook Page (or compare several similar pages) without searching from your own Facebook account. It is best for organisations, businesses, and public figures who run Pages; it is a discovery/triage step that surfaces the page URL and headline stats, which you then open and enrich.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://app.fanpagekarma.com/facebook-catalogue.
2. Enter the `name`/keyword/`username` and search the catalogue.
3. Review the returned pages: page name, handle, category, follower counts, and a link to the page.
4. Open the real Facebook page from the result to verify it is your subject; note the vanity URL/ID.
5. Pivot: the confirmed page/handle feeds Facebook-specific investigation; follower/engagement stats hint at activity level; the vanity URL yields the numeric page ID for other tools.

## Inputs → Outputs
- **In:** `name` / keyword / `username`
- **Out:** `social-profile` (Facebook Page link + handle), page `name`, headline metrics
- **Empty/negative result looks like:** no catalogue matches — the subject may have only a personal profile (not a Page), or a page too small/new to be indexed; not proof they have no Facebook presence.

## Gotchas & OpSec
- Catalogue coverage favours public **Pages**, not personal profiles — a private individual may simply not appear.
- Deeper analytics are paywalled behind a Fanpage Karma account; the free layer is discovery only.
- Passive: this does not register a visit on Facebook or alert the page owner.

## Overlaps ("do both")
- Pairs with `[[stalkface]]` and direct Facebook search — Fanpage Karma finds the page cleanly off-platform; those tools then work the page/profile itself once you have the handle/ID.

## Trust & verifiability
`trust: community` — a reputable commercial analytics provider. The page-discovery results are reliable pointers to real Facebook Pages; always open the actual page to confirm identity before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | app-fanpagekarma-com |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
