---
id: email-assumptions
name: Email Assumptions
description: Use when you have an email address and want to run it through dozens of OSINT services from one dashboard — returns links into breach, social, and search-engine results for that address.
url: https://inteltechniques.com/osint/email.html
category: email
path:
- email
bestFor: A consolidated IntelTechniques dashboard that pivots one email address across many search and breach services at once.
selectorsIn:
- email
selectorsOut:
- social-profile
- name
- username
- metadata
status: live
pricing: free
costNote: The web search tool page is free; Bazzell's books/courses are paid but not required to use it.
opsec: passive
opsecNote: The page builds and opens queries into third-party services; each engine you click runs a live search that the downstream service can log, so work behind a sock puppet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Maintained by Michael Bazzell (IntelTechniques), a respected OSINT author; it is a query launcher, so reliability depends on the third-party engines and some buttons break when those services change.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- IntelTechniques Email Tool
tags:
- email
source: metaosint
lastVerified: ''
enrichment: full
---

# Email Assumptions

> The IntelTechniques email search tool: one dashboard that fans an email address out across many breach, social, and search services.

## When to use
You have an `email` for a missing person, tipster, or associate and want a thorough, repeatable sweep across dozens of services without copy-pasting into each. Strong as a structured first-pass that covers breach lookups, social presence, and search engines in one place.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://inteltechniques.com/osint/email.html.
2. Enter the email address in the master field at the top.
3. Click individual service buttons (or "Submit All" where offered); each opens that service's pre-filled query in a new tab.
4. Work through the tabs, recording hits — breach databases, social platforms, Gravatar, search engines.
5. Pivot: take any `username`, `name`, or `social-profile` found to the matching specialist tool.

## Inputs → Outputs
- **In:** `email`
- **Out:** links surfacing `social-profile`, `name`, `username`, and breach/registration `metadata`
- **Empty/negative result looks like:** every linked service returns nothing — typical for fresh or disposable addresses; also note some buttons may 404 when an upstream service changes its URL scheme.

## Gotchas & OpSec
- Human-in-the-loop: none on the launcher; downstream services may show captchas/paywalls.
- OpSec: passive locally, but each click is a live query against a third party — use a clean/sock-puppet browser.
- It is a launcher, not a database; buttons rot as upstream services change, so a dead button is not a negative result.

## Overlaps ("do both")
- Pairs with `[[email-finder]]` (osint.sh) and `[[e-mail-search-tool]]` — overlapping launchers; run more than one because each curates a different service set.

## Trust & verifiability
`trust: community` — authored by a well-known OSINT practitioner; treat each downstream service on its own merits and expect occasional broken links.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | email-assumptions |
| category | email |
| selectorsIn → selectorsOut | email → social-profile, name, username, metadata |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
