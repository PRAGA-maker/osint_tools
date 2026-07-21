---
id: ivpaste
name: ivpaste
description: Use when you have a `name`, `email`, or `username` and want to check whether it appears in a public paste (dump, leak, dox) — returns `email`, `password`, and `document-id` fragments.
url: https://ivpaste.com
category: communities-forums
path:
- communities-forums
bestFor: Searching (via site-scoped web search) a pastebin for a subject's identifiers appearing in leaked or dumped text.
selectorsIn:
- name
- email
- username
selectorsOut:
- email
- password
status: live
pricing: free
costNote: Free public pastebin; no account needed to create or view pastes.
opsec: passive
opsecNote: Reading public pastes is passive. Treat any credentials/PII you find as sensitive evidence — never test found passwords or reuse leaked data; that would be active and likely illegal.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A minor public pastebin; pastes are anonymous and unverified, and content can be fabricated, so corroborate anything found before relying on it.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- ivpaste.com
tags:
- pastebins
- leaks
- paste-search
source: awesome-osint
lastVerified: '2026-07-21'
enrichment: full
---

# ivpaste

> A small public pastebin — one of the many paste sites where credential dumps, leaked lists, and doxes get posted; check it when hunting a subject's identifiers in leaked text.

## When to use
You have a `name`, `email`, `username`, phone, or other identifier and want to know whether it appears in a public paste — a breach dump, a combolist, a leaked contact list, or a dox. Pastebins are a common home for such content, and a hit can surface an associated `password`, other accounts, or personal details. Because pastebins rarely have good on-site search, you drive this mostly through a search engine scoped to the site.

## How to use it (`bestInteractionPattern`: web-manual)
1. In a search engine, query `site:ivpaste.com "<identifier>"` (email, username, name, phone) — this is more reliable than the site's own search.
2. Open any matching paste in a sock-puppet browser and read the surrounding context (what list/dump it's part of, other entries).
3. Extract associated identifiers — linked `email`s, `username`s, `password` fragments, or `document-id`s — noting they are unverified.
4. Do **not** test or reuse any credential you find.
5. Pivot: run recovered emails/usernames through account-existence and breach-check tools; corroborate any personal detail independently.

## Inputs → Outputs
- **In:** `name`, `email`, `username`, or other identifier
- **Out:** matching paste(s) containing the identifier, plus associated `email`/`password`/`document-id` fragments
- **Empty/negative result looks like:** no `site:ivpaste.com` hits — the identifier isn't in a paste here (there are many other paste sites); weak negative evidence.

## Gotchas & OpSec
- **Unverified & possibly fabricated:** anyone can post anything; a paste is a lead, never proof. Corroborate.
- **Handle credentials ethically/legally:** never test found passwords or act on leaked data beyond noting its existence.
- On-site search is weak — use `site:` queries in an external search engine.

## Overlaps ("do both")
- Pairs with breach-lookup tools and other paste-search engines — pastebin content is scattered across many sites, so run the same identifier across several and against HaveIBeenPwned-style checks.

## Trust & verifiability
`trust: unverified` — an anonymous public pastebin; content is unauthenticated and may be fake or stale, so treat every finding as a lead to verify elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ivpaste |
| category | communities-forums |
| selectorsIn → selectorsOut | name, email, username → email, password |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
