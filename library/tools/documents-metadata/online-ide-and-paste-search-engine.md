---
id: online-ide-and-paste-search-engine
name: Online IDE and Paste Search Engine
description: Use when you have a `username`, `email`, or `domain` and want to find it leaked in public paste/code sites — returns `document-id` (paste URLs) and exposed `password`/secrets.
url: https://redhuntlabs.com/online-ide-search
category: documents-metadata
path:
- documents-metadata
bestFor: Searching 40+ paste sites, online IDEs, and code-sharing platforms for a keyword, handle, or leaked secret.
selectorsIn:
- username
- email
- domain
selectorsOut:
- document-id
- password
- email
status: live
pricing: freemium
costNote: Free web search tool by RedHunt Labs; no login for basic searches. It's a lead-in to their paid NVADR attack-surface platform, but the search box itself is free.
opsec: passive
opsecNote: You query RedHunt Labs' index, not the paste sites directly, so the target isn't touched. RedHunt sees your search terms — avoid pasting a live secret you don't want logged by a third party; search a fragment instead.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Run by RedHunt Labs, an established attack-surface-management vendor; index freshness and coverage aren't independently audited.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- RedHunt Labs Code Leak Search
- paste search engine
tags:
- paste-sites
- code-leak
- credentials
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Online IDE and Paste Search Engine

> A free RedHunt Labs search box that scans 40+ paste sites, online IDEs (Pastebin, GitHub Gist, JSFiddle, CodePen, Ideone, Replit…) and code-sharing platforms for your keyword — built to surface leaked code and secrets.

## When to use
You have a `username`, `email`, `domain`, or a distinctive string tied to your subject and you want to know whether it shows up in a public paste or code snippet — leaked credentials, a config dump, source with hard-coded contacts, or a handle someone pasted. Pastebins are where breaches and doxxes get dropped, so this is a quick way to check exposure. Missing-person relevance is low but non-zero: a subject's reused handle or email in an old paste can reveal accounts, an alternate email, or a `password` they reuse elsewhere.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://redhuntlabs.com/online-ide-search.
2. Enter the search term — a `username`, `email`, `domain`, API-key fragment, or any unique string.
3. Submit; it returns matching snippets/pastes across the indexed platforms with links (`document-id`).
4. Open each hit to read the full paste — look for adjacent secrets, emails, or other handles in the same dump.
5. Pivot: a leaked `email`/`password` feeds credential-reuse and breach-lookup tools; a co-occurring handle feeds username search.

## Inputs → Outputs
- **In:** `username`, `email`, or `domain` (or any keyword)
- **Out:** `document-id` (paste/snippet URLs), and whatever the paste exposes — `password`/secrets, `email`, other usernames
- **Empty/negative result looks like:** no matches returned — the term isn't in RedHunt's index (which covers public pastes only, not deleted or private ones), so absence is not proof of no leak.

## Gotchas & OpSec
- You're searching a third-party index, so it's passive toward the target — but RedHunt logs your queries; don't paste a full live credential you care about.
- Coverage is "what RedHunt has indexed" — many pastes are short-lived or removed, so this is a snapshot, not exhaustive.
- Treat any found credential as evidence to corroborate, not to use — using it would be intrusive and likely illegal.

## Overlaps ("do both")
- Complements breach-lookup tools: this finds free-text pastes, breach databases find structured dumps — run both for the same `email`/`username`.

## Trust & verifiability
`trust: community` — a vendor-run free tool; every hit links to the actual paste so you can verify the content yourself, but the completeness and freshness of the index are not independently guaranteed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | online-ide-and-paste-search-engine |
| category | documents-metadata |
| selectorsIn → selectorsOut | username, email, domain → document-id, password, email |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
