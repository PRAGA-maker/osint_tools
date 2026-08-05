---
id: abilogic
name: AbiLogic
description: Use when you have an `employer-org` or business `name` and want a directory listing for it — returns the business's `domain` and `address`.
url: https://www.abilogic.com/
category: search-engines
path:
- search-engines
bestFor: Looking up a small business or website in a human-curated web directory to recover its site and contact details.
selectorsIn:
- employer-org
- name
selectorsOut:
- domain
- address
status: live
pricing: free
costNote: Free to browse and search listings; submitting a site is free (with a paid express-review upsell you can ignore for research).
opsec: passive
opsecNote: Browsing/searching a public directory leaks nothing to the listed business or person; requests go only to abilogic.com. Standard browser hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A general-purpose, submission-based business web directory; listings are self-submitted and lightly moderated, so treat entries as leads rather than authority.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- jayde-b2b-business-search
- 1websdirectory
- open-directory-finder
aliases:
- AbiLogic Business Web Directory
- abilogic.com
tags:
- toddington
- curated-directory
- web-directories
source: toddington-resources
lastVerified: '2026-08-05'
enrichment: full
---

# AbiLogic

> An old-school, human-submitted web directory — a niche place to turn a small-business `name` into its website and stated location when it isn't ranking well in mainstream search.

## When to use
You have an `employer-org` or small-business `name` (or a niche website) and mainstream search is noisy or unhelpful. Submission-based directories like AbiLogic sometimes carry a listing — with the site's own URL, category, and a self-described location — for small businesses that have thin footprints elsewhere. Useful as a supplementary lead when tying a person to a business or recovering a defunct site's old address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.abilogic.com/.
2. Use the directory search box for the business/website `name`, or drill down through the category tree (Business, Health & Beauty, Shopping, Regional/geographic branches, etc.).
3. Open a matching listing to read its title, described category, linked `domain`, and any stated location/`address`.
4. Treat the `domain` as the pivot: run it through WHOIS/DNS and site-content review to corroborate the business and find contact/owner details.

## Inputs → Outputs
- **In:** `employer-org` / business `name`
- **Out:** `domain` (the listed website), `address` / stated location
- **Empty/negative result looks like:** no listing matches the search, or matches are unrelated spam submissions. Most businesses are simply not in this directory — absence here means nothing about the business existing.

## Gotchas & OpSec
- Listings are self-submitted and can be stale, promotional, or SEO spam; verify the linked site is real and current.
- Coverage is thin and skewed toward businesses that chose to submit for backlinks, so it is a supplement, not a primary corporate source.
- OpSec: passive; nobody is notified when you view a listing.

## Overlaps ("do both")
- Pairs with `[[jayde-b2b-business-search]]` and `[[1websdirectory]]` — different directories index different submitters, so run the business name through several. Use `[[open-directory-finder]]` to locate yet more topical/regional directories to repeat the search in.

## Trust & verifiability
`trust: unverified` — it is a submission-driven directory with no authoritative vetting; every listing must be confirmed against the actual website and independent records before you rely on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | abilogic |
| category | search-engines |
| selectorsIn → selectorsOut | employer-org, name → domain, address |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
