---
id: wayback-keywords-search
name: Wayback Keyword Search
description: Use when you have a `domain` and a `name`/keyword and want to find it in the site's history — downloads a domain's Wayback snapshots for a period and full-text searches them offline.
url: https://github.com/lorenzoromani1983/wayback-keyword-search
category: archives-cache
path:
- archives-cache
bestFor: Full-text searching a domain's archived (Wayback) pages for a keyword over a chosen date range.
selectorsIn:
- domain
- name
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free and open-source script; runs locally, no account.
opsec: passive
opsecNote: It pulls pages from the Internet Archive, not the target's live server, so the site owner isn't alerted. Run it from a research machine/VPN if you want the archive requests off your own IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A small open-source community script over the Internet Archive's public snapshots; the archived data is authoritative, the tooling is a convenience wrapper.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- wayback-machine
- wayback-archive
aliases:
- wayback-keyword-search
- Wayback Keyword Search
tags:
- Archives
- Tools for working with web archives
- wayback
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# Wayback Keyword Search

> A CLI tool that grabs a domain's archived pages from the Wayback Machine for a given month/day and lets you keyword-search them at once — finding text that has since been edited or deleted from the live site.

## When to use
You have a `domain` (a subject's site, a forum, an organisation) and a `name`, handle, phone, or phrase you want to find in its *past*, not its present. Live search only sees the current site; this tool downloads the domain's historical snapshots for a chosen period and full-text searches them, surfacing a mention that was later removed — a deleted staff bio, an old contact detail, a scrubbed post.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo (github.com/lorenzoromani1983/wayback-keyword-search) and install its Python dependencies.
2. Run it against the target `domain` for the month/day range you want; it fetches that period's Wayback snapshots.
3. Provide your keyword/`name`; it searches the downloaded pages and reports which archived URLs contain it.
4. Pivot: a matching archived page (`document-id`) may hold a deleted email, name, or detail — open that snapshot on the Wayback Machine and extract the lead.

## Inputs → Outputs
- **In:** a `domain` plus a `name`/keyword and a date range
- **Out:** the archived page URLs (`document-id`) from that period that contain the keyword
- **Empty/negative result looks like:** no matching snapshots — the term never appeared in the archived pages for that range, or the Archive didn't capture them; widen the date range or check the domain's Wayback coverage.

## Gotchas & OpSec
- Human-in-the-loop: none, but it's a script — you need Python and the ability to run CLI tools.
- Coverage depends entirely on what the Internet Archive captured; sparse crawls mean gaps, so absence isn't proof the text never existed.
- Large date ranges download many pages and hit Archive rate limits; narrow the period for speed.

## Overlaps ("do both")
- Pairs with `[[wayback-machine]]` and `[[wayback-archive]]` — the Wayback site lets you eyeball individual snapshots, while this tool bulk-searches many of them for a keyword; use the tool to locate the snapshot, then the site to read/cite it.

## Trust & verifiability
`trust: community` — an open-source convenience script; the underlying archived pages are authoritative Internet Archive captures, so verify any hit against the snapshot on web.archive.org.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wayback-keywords-search |
| category | archives-cache |
| selectorsIn → selectorsOut | domain, name → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
