---
id: pastesite-net
name: PasteSite.Net
description: Use when you have a `username`, `email` or keyword and want to check a pastebin for dumped text — browse/search public pastes that may contain leaked selectors.
url: https://pastesite.net/
category: communities-forums
path:
- communities-forums
bestFor: Scanning a public pastebin for pasted text (credentials, contact lists, dumps) that mentions a subject's selector.
selectorsIn:
- username
- email
- name
selectorsOut:
- email
- username
- password
- document-id
status: live
pricing: free
costNote: Free to read and post; an account is only needed to manage your own pastes, not to read public ones.
opsec: passive
opsecNote: Reading public pastes is passive and does not notify anyone. Do NOT paste your target's data into it (that publishes it). Treat any credentials you find as sensitive and do not test/reuse them; access unknown pastes in a sandboxed browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A newer general-purpose pastebin with ad-revenue monetisation. Content is anonymous, user-posted and unverified; pastes can be edited or removed, so treat findings as leads and snapshot them.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- pastesite
- pastesite.net
tags:
- pastebins
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# PasteSite.Net

> A general-purpose public pastebin — one more surface to check when hunting for dumped text (leaked credentials, contact lists, doxes) that references your subject.

## When to use
You have a `username`, `email`, `name` or other keyword and want to see whether it appears in pasted text on this pastebin. Pastebins are a classic home for breach dumps, combolists and doxes, so scanning them can surface a subject's leaked `email`/`password` pairs, aliases, or associate lists. Because a single pastebin only holds a slice of the paste ecosystem, treat this as one of several to sweep, not the whole picture.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://pastesite.net/ and use its search/recent-pastes listing for your keyword.
2. If on-site search is weak, pivot to a search engine dork such as `site:pastesite.net "target@example.com"`.
3. Open matching pastes in a sandboxed browser and read the content for selectors (emails, passwords, handles, phone numbers).
4. Snapshot anything relevant immediately — pastes can be edited or deleted, and there is no guarantee of persistence.
5. Pivot: leaked `email`/`password` pairs feed breach-check and account-existence tools; aliases feed username sweeps.

## Inputs → Outputs
- **In:** `username` / `email` / `name` (search keyword)
- **Out:** `email`, `username`, `password`, and the paste itself (`document-id`) plus any other selectors in the dumped text
- **Empty/negative result looks like:** no pastes match — the data may live on a different pastebin, may have been removed, or may never have been posted here. Absence is not proof the subject is un-leaked.

## Gotchas & OpSec
- Human-in-the-loop: none for reading public pastes.
- OpSec: **passive** for reading. Never paste target data here; never test found credentials — that is intrusive and may be illegal.
- Content is anonymous and unverified, laden with ads, and can be spam or bait; corroborate any selector before acting on it.

## Overlaps ("do both")
- Pairs with breach-search and other pastebin/leak tools, since each pastebin and index covers different dumps — sweep several.

## Trust & verifiability
`trust: community` — a real but lightly-moderated, monetised pastebin; useful as a lead source, but every finding is unverified user-posted text that must be confirmed elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pastesite-net |
| category | communities-forums |
| selectorsIn → selectorsOut | username, email, name → email, username, password, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
