---
id: usersearch-ai
name: usersearch.ai
description: Use when you have a username, email, phone, or photo and want to find matching social/dating profiles and accounts across many platforms — returns linked social profiles and usernames.
url: https://usersearch.ai/
category: email
path:
- email
bestFor: Reverse username/email/phone/image search across social, dating, and forum platforms.
selectorsIn:
- username
- email
- phone
- image
selectorsOut:
- social-profile
- username
- name
status: live
pricing: freemium
costNote: Some lookups preview free; full results, image search, and bulk use are paid/credit-based.
opsec: passive
opsecNote: Searches platforms' public/indexed data on usersearch.ai's side; the subject is not contacted. Use a sock-puppet account/session to avoid linking searches to you.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: usersearch.ai (related to the long-running usersearch.org username tool) is a known reverse-identifier search service; results vary by platform coverage and can include false matches.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: false
relatedTools:
- thatsthem
- venacus
aliases:
- usersearch
- usersearch.org
tags:
- email
- Email Related Sites
- username-search
- reverse-lookup
source: uk-osint
lastVerified: ''
enrichment: full
---

# usersearch.ai

> A reverse-identifier search engine: feed a username, email, phone, or photo and surface matching profiles across social, dating, and forum sites.

## When to use
You have a `username`, `email`, `phone`, or `image` of a subject and want to map their online presence — especially dating and niche platforms that general people-search tools miss. High value in missing-persons work for connecting a recovered handle/email to live accounts that may show recent activity or location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to `https://usersearch.ai/` (use a sock-puppet session).
2. Choose the search type (username / email / phone / image) and submit the selector.
3. Review the matched profiles; the preview is often partial, with full links/credits gated behind payment.
4. Pivot: open promising `social-profile`s directly; cross-check any recovered `name` in [[thatsthem]] and breach data in [[venacus]].

## Inputs → Outputs
- **In:** `username`, `email`, `phone`, `image`
- **Out:** `social-profile`, `username`, sometimes `name`
- **Empty/negative result looks like:** no matched accounts, or low-confidence matches — common for very common usernames (false positives) or privacy-locked subjects.

## Gotchas & OpSec
- Human-in-the-loop: full results and image search are credit/pay-gated.
- Common usernames produce false matches — corroborate by content, not just handle.
- OpSec: passive toward the subject; use a sock-puppet account so searches aren't tied to you.

## Overlaps ("do both")
- Pairs with [[thatsthem]] (contact data from an email/phone) and [[venacus]] (breach-sourced linkage) to triangulate the same identity.

## Trust & verifiability
`trust: community` — a recognized reverse-identifier search service; treat matches as leads and verify with profile content before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | usersearch-ai |
| category | email |
| selectorsIn → selectorsOut | username, email, phone, image → social-profile, username, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
