---
id: getdewey-co
name: Getdewey.co
description: Use when you are collecting `social-profile` links and posts across many platforms during an investigation and want them aggregated, tagged and searchable in one place — returns an organised, exportable evidence library (it is a bookmark manager, not a lookup).
url: https://getdewey.co/
category: social-networks
path:
- social-networks
bestFor: Aggregating and organising saved social-media bookmarks/posts/profile links collected during an investigation into one searchable, exportable library.
selectorsIn:
- social-profile
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Freemium — a free tier plus paid plans that add bulk AI auto-tagging and higher limits. An account is required to use it at all.
opsec: passive
opsecNote: Dewey only stores links/bookmarks you already gathered; it runs no query against any target, so it is passive. Caution: it offers publicly shareable collections and exports — never make a case collection public, and treat anything you upload as sitting on a third-party server.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial bookmark-aggregation SaaS, not an OSINT data source. It organises what you feed it and produces no independent intelligence; "trust" here is only that it is a legitimate, functioning product.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- Dewey
- getdewey
tags:
- bookmark-manager
- case-management
- social-media
source: osint4all
lastVerified: '2026-07-15'
enrichment: full
---

# Getdewey.co

> A cross-platform bookmark manager repurposed as a case-organisation aid — where you park and tag every social link you collect, not a place that finds them for you.

## When to use
You are running a social-media-heavy investigation and are piling up saved posts and profile links from X, Instagram, TikTok, Reddit, LinkedIn, Threads, Bluesky, Substack, etc. Dewey consolidates those saved items into one dashboard you can tag, foldering, note, and full-text search — useful for keeping a timeline of "where I saw this" straight. It is a **workflow/organisation tool**, never a lookup: it surfaces nothing new about a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create an account at https://getdewey.co/ and connect/import your saved bookmarks from the platforms you use.
2. Let it pull in your saved posts/links; add tags, folders, and notes to mark relevance to the case.
3. Use full-text search and filters to retrieve items later; the paid tier can bulk-auto-tag large imports.
4. Export the organised set (CSV / PDF / Google Sheets with media) for the case file.
5. Pivot: Dewey is the holding pen — the actual discovery still comes from search/lookup tools; Dewey just keeps their outputs findable.

## Inputs → Outputs
- **In:** `social-profile` links / saved posts you already collected
- **Out:** an organised, tagged, searchable, exportable `social-profile` library
- **Empty/negative result looks like:** N/A — it stores what you give it. "Empty" just means you haven't imported anything; it will never return a lead you didn't already have.

## Gotchas & OpSec
- This is **not** an investigative search tool — do not expect it to find accounts; it only organises links you supply.
- Sharing/collaboration features can make a collection public — keep case data private and export rather than share.
- OpSec: **passive** (no target query), but your bookmark library lives on Dewey's servers; keep sensitive material out or self-host an alternative if policy requires.

## Overlaps ("do both")
- Sits downstream of every discovery tool in this library: use reverse-lookup / username / social-search tools to *find* profiles, then Dewey (or any case-management/notebook tool) to *retain and organise* them.

## Trust & verifiability
`trust: unverified` — a legitimate commercial bookmark SaaS with no role as a data source. There is no data-quality question because it originates no data; the only consideration is that your collected evidence is stored on a third party.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | getdewey-co |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → social-profile |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
