---
id: e-mail-search-tool
name: E-mail search tool
description: Use when you have an email address and want a one-stop launcher that runs it through multiple search engines and OSINT services — returns links into those services' results.
url: https://www.aware-online.com/osint-tools/e-mail-search-tool/
category: email
path:
- email
bestFor: A guided launcher page that fans an email address out across several search engines and lookup services.
selectorsIn:
- email
selectorsOut:
- social-profile
- name
- username
status: live
pricing: free
costNote: Free tool page from Aware Online (a Dutch OSINT training company); training/courses are paid but this page is open.
opsec: passive
opsecNote: The page builds pre-filled queries you click into third-party engines; do searches behind a sock puppet / clean browser since the downstream services (and Aware Online) may log activity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Aware Online is a recognized OSINT training provider; the tool is a curated query launcher, so its value depends on the third-party engines it points at, not on Aware Online itself.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- email-search
source: osint4all
lastVerified: ''
enrichment: full
---

# E-mail search tool

> A free Aware Online launcher page that takes one email address and fires it through several search engines and people/social services.

## When to use
You have an `email` for a missing person or associate and want a fast, broad first pass: see whether the address surfaces on social platforms, in indexed pages, or in people-search services. Good as an opening sweep before targeted breach/verifier tooling.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.aware-online.com/osint-tools/e-mail-search-tool/.
2. Type the email address into the input field.
3. Click each engine/service button it offers; each opens a pre-filled query in a new tab.
4. Read each result set for matches — a profile, a name, a reused username.
5. Pivot: take any recovered `username` to username-search tooling and any `name` to people-search.

## Inputs → Outputs
- **In:** `email`
- **Out:** links that may reveal `social-profile`, `name`, `username` (depending on the downstream engine)
- **Empty/negative result looks like:** every launched engine returns nothing for the address — common for fresh, alias, or disposable mailboxes.

## Gotchas & OpSec
- Human-in-the-loop: none on the launcher itself; some downstream services may show captchas or paywalls.
- OpSec: passive but you are querying live third-party engines — use a clean/sock-puppet browser; some downstream people-search sites notify or log.
- It is a pointer page, not a data source: it finds nothing on its own, only what the linked engines return.

## Overlaps ("do both")
- Pairs with `[[email-finder]]` and `[[email-checker-searches-email-via-social-networks]]`, which directly probe social-network presence rather than just launching generic search queries.

## Trust & verifiability
`trust: community` — maintained by a reputable OSINT training company; treat each downstream service's reliability on its own merits.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | e-mail-search-tool |
| category | email |
| selectorsIn → selectorsOut | email → social-profile, name, username |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
