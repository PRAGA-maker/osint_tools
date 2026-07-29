---
id: archive-it-org
name: Archive-it.org
description: Use when you have a `domain`/URL or an organisation `name` and want to find curated, thematically-archived web snapshots of it — returns historical `social-profile`/page captures from institutional collections.
url: https://archive-it.org/
category: search-engines
path:
- search-engines
bestFor: Searching thousands of curated web-archive collections built by libraries, archives, and NGOs.
selectorsIn:
- domain
- name
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Browsing and full-text searching the public collections is free; building/hosting your own archive collection is a paid institutional subscription.
opsec: passive
opsecNote: You query the Internet Archive's Archive-It portal, not the target's live site, so the subject sees nothing. It logs your searches like any web service — browse behind a VPN for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Internet Archive; collections are curated by named libraries, universities, and archives, making captures well-provenanced.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- archive-it
- wayback-archive-it-org
aliases:
- Archive-It
tags:
- web-archive
- wayback
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Archive-it.org

> The Internet Archive's curated-collections service — searchable thematic web archives built by libraries and NGOs, where you can find historical snapshots the general Wayback Machine may not surface as cleanly.

## When to use
You want historical captures of a site, organisation, campaign, or event — especially one likely covered by an institutional collection (government sites, NGO campaigns, news, disasters, elections). Archive-It's full-text search across curated collections often finds pages, and prior versions of them, that a subject has since taken down.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://archive-it.org and use the "Explore" / collection search.
2. Search by `domain`/URL, organisation `name`, keyword, or topic; you can also browse by collecting institution.
3. Open a matching collection and drill into archived seeds; select a capture date to view the preserved page.
4. Note the collecting organisation and capture timestamp for provenance in your evidence log.
5. Pivot: recovered old pages may expose former staff, contact details, or `social-profile` links now deleted — feed those into people/email lookups; cross-check with the general Wayback Machine.

## Inputs → Outputs
- **In:** `domain`/URL or organisation `name`/topic
- **Out:** archived page snapshots (historical `social-profile`/contact/content), with capture dates and collecting institution
- **Empty/negative result looks like:** no collection covers your target — that is common for private individuals/sites; fall back to the general Wayback Machine, which has far broader (if less curated) coverage.

## Gotchas & OpSec
- Coverage is collection-driven, so it skews toward institutions, events, and public-interest sites — not random personal pages.
- Freemium: searching is free; the paid tier is only for institutions that build archives.
- OpSec: **passive**; you never touch the target's live infrastructure.

## Overlaps ("do both")
- Pairs with `[[wayback-archive-it-org]]` and the broader Wayback Machine — do both, since curated Archive-It collections and the general crawl capture different things.

## Trust & verifiability
`trust: trusted` — Internet Archive infrastructure with named institutional curators; captures carry timestamps and provenance you can cite.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | archive-it-org |
| category | search-engines |
| selectorsIn → selectorsOut | domain, name → social-profile |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
