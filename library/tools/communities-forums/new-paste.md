---
id: new-paste
name: New Paste
description: Use when you have a `username`, `email`, or leaked keyword and want to check a public pastebin for dumped text — returns paste content that may contain `email`, `password`, `username`.
url: https://paste1.com/
category: communities-forums
path:
- communities-forums
bestFor: Sweeping a general-purpose pastebin (with burn-after-read pastes) for dumped credentials, doxes, or contact fragments.
selectorsIn:
- username
- email
selectorsOut:
- email
- password
- username
status: live
pricing: free
costNote: Free to create and read pastes; no account required.
opsec: passive
opsecNote: Reading existing pastes is passive. Never post the subject's data here — public pastes become searchable and attributable. Note the "burn after read" option means some leads self-destruct on first view.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A general-purpose pastebin at paste1.com; content is user-submitted and unvetted, so hits are raw leads, not facts.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- paste1.com
- paste1
tags:
- pastebins
source: awesome-osint
lastVerified: '2026-07-20'
enrichment: full
---

# New Paste

> A general-purpose pastebin (paste1.com) with expiry and burn-after-read — another bin to sweep when hunting a subject's data in dumped text.

## When to use
You have a `username`, `email`, or distinctive keyword and you're sweeping pastebins for leaked/dumped material — credential lists, doxes, contact fragments. paste1.com is a standard pastebin with title/language, expiration controls, and a "burn after read" option. Include it in a *breadth* pass across many bins; its OSINT value comes from whatever gets indexed, since it has no strong native search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://paste1.com/ in a clean/sock-puppet browser.
2. There is no reliable native full-text search of others' pastes — rely on search-engine indexing.
3. Dork it: `site:paste1.com "<selector>"` to surface indexed public pastes.
4. Read matches for `email`, `password`, `username`, name/phone fragments.
5. Pivot: feed recovered credentials/handles into breach-check and username-enumeration tools; corroborate before trusting.

## Inputs → Outputs
- **In:** `username`, `email`, or keyword (via `site:` dork)
- **Out:** raw paste text possibly containing `email`, `password`, `username`, other fragments
- **Empty/negative result looks like:** no indexed match — absence proves nothing; the same data may live on other bins, and burn-after-read pastes leave no trace.

## Gotchas & OpSec
- Burn-after-read and short expiry mean some pastes vanish before indexing — coverage is inherently leaky.
- Unvetted user content; any hit is a lead to corroborate.
- OpSec: reading is passive; **never** post the subject's data here.

## Overlaps ("do both")
- Pairs with `[[paste-monster]]`, `[[textbin]]`, and broad paste-search tools — run the same selector across many bins, since each holds only a slice.

## Trust & verifiability
`trust: community` — unvetted user submissions on a third-party bin; corroborate identity and recency before acting on any hit.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | new-paste |
| category | communities-forums |
| selectorsIn → selectorsOut | username, email → email, password, username |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
