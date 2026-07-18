---
id: vivastreet-classified-ads-united-kingdom
name: Vivastreet Classified Ads (United Kingdom)
description: Use when you have a `phone`, `name`, or region and want to find a subject's UK classified ads (jobs, personals, services, vehicles for sale) — returns `phone`, `geolocation`, `social-profile`.
url: http://www.vivastreet.co.uk
category: dating-classifieds
path:
- dating-classifieds
bestFor: Searching UK local classified ads to surface a subject's postings, contact number, and rough location.
selectorsIn:
- phone
- name
- geolocation
selectorsOut:
- phone
- geolocation
- social-profile
status: live
pricing: free
costNote: Free to browse and search; posting is free in most categories though some charge a fee.
opsec: passive
opsecNote: Browsing and searching ads is passive. Replying to an ad or using its contact form is active and attributable — use a sock-puppet identity and never send your real number.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial UK classifieds marketplace, not an OSINT tool; ad content is user-submitted and unvetted.
missingPersonsRelevance: medium
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- Vivastreet UK
tags:
- classifieds
- toddington
- curated-directory
- specialty-search
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Vivastreet Classified Ads (United Kingdom)

> A large UK local-classifieds marketplace — search it to surface a subject's ads (services, personals, vehicles, jobs) and the phone number and area behind them.

## When to use
You have a `phone` number, a `name`, or a target region and want to find whether the subject posts classified ads in the UK. Vivastreet spans jobs, personals/dating, services (including trades and adult services), property, and vehicle sales, organized by region — so an ad can reveal a working phone number, a rough location, a trade or side business, or a personals persona. Useful when a subject advertises services or is active on personals but is quiet on mainstream social media.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.vivastreet.co.uk.
2. Choose the relevant category and UK region, then search a keyword, `name`, or trade; also run site-scoped engine queries: `site:vivastreet.co.uk "phone"` or `site:vivastreet.co.uk "name"` (a phone number in an ad is often indexed).
3. Open matching ads: note the posting area, the contact number, the poster's alias, and any linked images.
4. Read the output: the ad's region is a `geolocation` lead, the contact number is `phone`, and the alias/handle is a `social-profile` pivot.
5. Pivot: reverse-search the ad's `phone` and reuse images in reverse-image tools; reuse the alias on username tools.

## Inputs → Outputs
- **In:** `phone`, `name`, or `geolocation` (region/keyword)
- **Out:** `phone` (contact number in ads), `geolocation` (posting area), `social-profile` (poster alias/handle)
- **Empty/negative result looks like:** no ads for the search terms — the subject may not advertise here, or old ads have expired (listings are removed after a period); not evidence of anything.

## Gotchas & OpSec
- Human-in-the-loop: none for search/browse; posting or replying may require a free account and, in some categories, a fee.
- OpSec: passive to browse; replying to an ad is active and reveals you — use a sock puppet and a burner number.
- Adult-services categories carry legal/ethical sensitivity; stay within the scope of your investigation.

## Overlaps ("do both")
- Pairs with reverse-phone and reverse-image tools — pull a number/photo from an ad here, then run it there to link the ad to a named identity.

## Trust & verifiability
`trust: unverified` — a commercial classifieds site with user-submitted, unvetted content; treat any name/number/photo in an ad as a lead to corroborate, not a confirmed fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vivastreet-classified-ads-united-kingdom |
| category | dating-classifieds |
| selectorsIn → selectorsOut | phone, name, geolocation → phone, geolocation, social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
