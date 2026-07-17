---
id: webarchive-loc-gov
name: Library of Congress Web Archives
description: Use when you have a `domain`/URL or topic and want curated, preserved historical web captures — returns archived pages and `metadata-exif`/dated snapshots.
url: https://webarchive.loc.gov/
category: archives-cache
path:
- archives-cache
bestFor: Finding preserved historical versions of websites the Library of Congress has curated into thematic web archives (elections, events, government, culture).
selectorsIn:
- domain
selectorsOut:
- domain
- metadata-exif
status: live
pricing: free
costNote: Free public archive from the U.S. Library of Congress; no account.
opsec: passive
opsecNote: Reading archived captures is passive — you view stored copies at the LoC, never the live target site, so nothing reaches the original operator.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: U.S. Library of Congress — an authoritative national institution; captures are faithful, timestamped preservation copies.
missingPersonsRelevance: medium
coverage:
- us
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- library-of-congress-ask-a-librarian
- library-of-congress-united-states
- newspaper-navigator
- usa-telephone-directory-collection
aliases:
- LoC Web Archives
- webarchive.loc.gov
tags:
- Archives
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Library of Congress Web Archives

> The Library of Congress's curated web-archiving program — thematic, preserved captures of websites around elections, events, government, and culture, complementing the Internet Archive.

## When to use
You have a `domain`/URL or a topic (a campaign, an event, a government body, a community) and want a historical, authoritative capture of how a website looked at a point in time — especially for U.S. political, governmental, and cultural sites the LoC has deliberately preserved. Useful when a page is gone or altered and you need a trustworthy, citable snapshot, or when the Internet Archive's coverage is thin for a curated collection.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://webarchive.loc.gov/ and browse the collections or use the search.
2. Search a site name, URL, or topic; open the archived collection/item.
3. Open a capture to view the preserved page and its capture date; note dates to establish a timeline.
4. Compare captures over time to see how content changed.
5. Pivot: names/claims/links in an archived page feed people- and domain-search; the capture date anchors a timeline and is citable evidence.

## Inputs → Outputs
- **In:** `domain`/URL or topic
- **Out:** archived page captures with `metadata-exif`/capture dates; preserved links to other `domain`s.
- **Empty/negative result looks like:** no capture — the site/topic isn't in an LoC collection (its scope is curated, not comprehensive); fall back to the Internet Archive's Wayback Machine for broad coverage.

## Gotchas & OpSec
- Coverage is curated and selective (heavily U.S. government/politics/culture) — not a general crawl; the Internet Archive is broader.
- Some captures have access conditions or are viewable only on-site for rights reasons — check the item notes.
- OpSec: passive; you view stored copies, never the live site.

## Overlaps ("do both")
- Pairs with the Internet Archive Wayback Machine and `[[newspaper-navigator]]` — the LoC offers authoritative curated captures; Wayback offers breadth; run both so a missing page in one is caught by the other.

## Trust & verifiability
`trust: trusted` — a national library's preservation program; captures are faithful, timestamped, and citable as primary archival evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | webarchive-loc-gov |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → domain, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
