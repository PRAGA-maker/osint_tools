---
id: vefsafn-is
name: Vefsafn.is (Icelandic Web Archive)
description: Use when you have an Icelandic `domain` or URL and want historical snapshots of it — returns archived captures of .is / Iceland-related web pages from 1996 to now.
url: https://vefsafn.is/
category: archives-cache
path:
- archives-cache
bestFor: Recovering deleted or changed Icelandic web pages (.is domains and Iceland-related sites) that the global Wayback Machine may have missed.
selectorsIn:
- domain
selectorsOut:
- domain
- social-profile
status: live
pricing: free
costNote: Free public archive by the National and University Library of Iceland; open URL search, no account.
opsec: passive
opsecNote: You query the library's Wayback-style archive, not the live site, so the page owner sees nothing. The library may log your lookups; standard archive privacy applies. Some captures are access-restricted (paywalled or owner-closed) and simply won't display.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the National and University Library of Iceland (Landsbókasafn) as a legal-deposit web archive; an authoritative institutional source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Íslenska vefsafnið
- Icelandic Web Archive
- wayback.vefsafn.is
tags:
- Archives
- web-archive
- iceland
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Vefsafn.is (Icelandic Web Archive)

> Iceland's national web archive — a Wayback-style time machine for .is domains and Iceland-related sites, collected several times a year since 1996.

## When to use
Your subject or lead touches Iceland — an `.is` website, an Icelandic company, forum, news article, or profile that has since changed or vanished. The global Internet Archive has patchy Icelandic coverage; Vefsafn crawls the entire `.is` domain space several times a year (plus frequent captures of news/dynamic content), so it often holds snapshots nothing else does.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://vefsafn.is/ (the Wayback interface is at `wayback.vefsafn.is`).
2. Enter the target URL/`domain` into the URL search box.
3. Read the output: a calendar/list of capture dates; click a date to view the page as archived then.
4. Pivot: extract names, emails, phone numbers, and links from the archived page and feed them onward; compare captures over time to see what was added/removed.

## Inputs → Outputs
- **In:** an Icelandic or Iceland-related URL / `domain`
- **Out:** dated archived snapshots of that page (recovered content, links, `social-profile`s)
- **Empty/negative result looks like:** "no captures" for a URL means it was never crawled (non-.is, or added/removed between crawls) — try the global Wayback Machine and Archive.today as fallbacks.

## Gotchas & OpSec
- Scope is Iceland: `.is` domains and pages that are in Icelandic or clearly about Iceland — do not expect coverage of arbitrary foreign sites.
- Some snapshots are access-restricted (owner-closed or paywalled) and won't render even though a capture exists.
- Human-in-the-loop: none.
- OpSec: passive — you touch the archive, not the live target.

## Overlaps ("do both")
- Do both with the global Wayback Machine and Archive.today — Vefsafn's national crawl and their broader crawls capture different snapshots; check all three for a complete history of an Icelandic page.

## Trust & verifiability
`trust: trusted` — a national-library legal-deposit archive; captures are authoritative primary records, citable by their snapshot URL and timestamp.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vefsafn-is |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → domain, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
