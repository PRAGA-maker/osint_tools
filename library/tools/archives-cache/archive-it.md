---
id: archive-it
name: Archive-It
description: Use when you have a `domain`/URL or an organization `name` and want curated web archives of it — returns archived captures of pages/sites collected by libraries and institutions.
url: https://archive-it.org/explore?show=Collections
category: archives-cache
path:
- archives-cache
bestFor: Finding institutionally-curated web archive collections and captures of a site, group, or event.
selectorsIn:
- domain
- name
selectorsOut:
- domain
status: live
pricing: free
costNote: Browsing and searching public collections is free (an Internet Archive service). Creating/curating your own collections is a paid subscription for institutions — not needed to read archives.
opsec: passive
opsecNote: You read stored archive captures, not the live target site, so nothing reaches the subject's server and there's no alert. Content is a historical snapshot — a page may have changed or been removed since capture, which is exactly why it's useful, but date-stamp anything you cite.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Internet Archive; collections are curated by libraries, universities, and government/NGO partners.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- archive-it-org
- wayback-archive-it-org
aliases:
- archive-it.org
tags:
- web-archive
- curated-collections
- toddington
- curated-directory
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# Archive-It

> The Internet Archive's curated web-archiving service — thematic collections of captured sites built by libraries and institutions, searchable when a page you need is gone from the live web.

## When to use
You have a `domain`/URL that's changed or vanished, or an organization/event `name`, and want an archived version. Unlike a blind Wayback lookup, Archive-It's captures are grouped into curated collections (by universities, governments, NGOs) — useful for recovering a deleted profile, a defunct org's site, or event-related pages that a curator deliberately preserved. Good for pulling down content a subject has since scrubbed.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://archive-it.org/explore?show=Collections.
2. Search by keyword, organization `name`, or paste/search a `domain`/URL to find collections and captures containing it.
3. Open a collection, then a specific capture, to read the archived page as it appeared on the capture date (`selectorsOut`).
4. Pivot: recovered content (old contact details, names, links) feeds the rest of your workflow; note the capture date for provenance.

## Inputs → Outputs
- **In:** `domain`/URL or `name` (organization/topic)
- **Out:** archived page captures and the collections containing them (recovered `domain`/URL content)
- **Empty/negative result looks like:** no matching collection or capture — the URL may not have been curated here; fall back to the general Wayback Machine, which crawls far more broadly.

## Gotchas & OpSec
- Human-in-the-loop: none for reading.
- OpSec: passive — you read stored snapshots, never the live site.
- Coverage is curated, not comprehensive: Archive-It only holds what partner institutions chose to archive, so absence here isn't proof a page was never archived.

## Overlaps ("do both")
- Pairs with the general [[wayback-archive-it-org]] / Wayback Machine and [[archive-it-org]] — Archive-It holds deep, curated collections while the Wayback Machine has broad, shallow coverage; check both when recovering deleted content.

## Trust & verifiability
`trust: trusted` — run by the Internet Archive with institutional curators, so captures are authentic archival snapshots. The archived *content* is only as reliable as the original page was, but the archiving itself is authoritative and date-stamped.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | archive-it |
| category | archives-cache |
| selectorsIn → selectorsOut | domain, name → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
