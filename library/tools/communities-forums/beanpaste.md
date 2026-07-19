---
id: beanpaste
name: BeanPaste
description: Use when you have a `username`/`email`/`domain` term and want to check a pastebin for dumped text referencing it — returns pastes that may contain credentials or contact data.
url: https://beanpaste.fun/
category: communities-forums
path:
- communities-forums
bestFor: A small public pastebin to search/monitor for dumped text (credential lists, contact data, leaks) mentioning a selector.
selectorsIn:
- username
- email
- domain
selectorsOut:
- email
- password
- document-id
status: live
pricing: free
costNote: Free to read and create pastes; no account required. Pastes can be set with an expiry.
opsec: passive
opsecNote: Reading public pastes is passive. Never enter live credentials you find, and don't create a paste with case data. Prefer a search-engine site: query so you don't tip off anyone monitoring a paste. Handle any breach data lawfully.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A tiny, community-run pastebin ("a tiny way to share text"); low volume and no index guarantees, so treat it as one minor source among many rather than authoritative.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- beanpaste.fun
tags:
- pastebins
- leaks
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# BeanPaste

> A small public pastebin — worth a quick check (and periodic re-check) for leaked credentials, contact lists, or dumped text that mentions your selector, alongside the bigger paste sites.

## When to use
You're hunting for exposed data — a `username`, `email`, `domain`, or company name that might appear in a dumped credential list or leaked text. Pastebins are common dumping grounds, so include this one in a sweep of paste sites when checking whether a selector has surfaced in a leak.

## How to use it (`bestInteractionPattern`: web-manual)
1. Visit https://beanpaste.fun/.
2. It's primarily a create/share pastebin with limited on-site search, so use a search engine: `site:beanpaste.fun "<email-or-username-or-domain>"`.
3. Open any matching paste and scan for credentials, contact details, or document references.
4. Never reuse/enter a live credential you find; record the finding and its context.
5. Pivot: leaked `email`/`password` pairs → breach-analysis and account-existence checks; document references → further record searches.

## Inputs → Outputs
- **In:** `username`, `email`, or `domain` search term
- **Out:** pastes possibly containing `email`s, `password`s/credentials, and `document-id` references
- **Empty/negative result looks like:** no indexed pastes match — nothing is dumped *here* under that term. It's a low-volume site; absence says nothing about the broader paste ecosystem, so check the big aggregators too.

## Gotchas & OpSec
- Small and low-volume — a miss here is not meaningful; sweep the major pastebins and breach services as well.
- On-site search is weak; rely on `site:` engine queries.
- Legal/ethical: handle breach/credential data responsibly; never authenticate with found credentials.

## Overlaps ("do both")
- Pairs with `[[cutapaste]]`, larger paste-aggregators, and breach-search tools — a single small pastebin covers little, so cross-check several and the big HIBP-style services for the same selector.

## Trust & verifiability
`trust: unverified` — a tiny community pastebin; any hit is only as trustworthy as the paste's anonymous content, so corroborate before acting on anything found here.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | beanpaste |
| category | communities-forums |
| selectorsIn → selectorsOut | username, email, domain → email, password, document-id |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
