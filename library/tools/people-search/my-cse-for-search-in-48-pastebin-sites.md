---
id: my-cse-for-search-in-48-pastebin-sites
name: My CSE for search in 48 pastebin sites
description: Use when you have a `name`, `username`, `email` or other selector and want to find it in leaked/pasted data — a Google Custom Search Engine spanning ~48 pastebin sites, returning paste hits with contact/leak data.
url: https://cipher387.github.io/pastebinsearchengines/
category: people-search
path:
- people-search
bestFor: Sweeping dozens of pastebin/paste sites at once for a selector, to surface leaked credentials, dumps and mentions.
selectorsIn:
- name
- username
- email
selectorsOut:
- email
- phone
- document-id
status: live
pricing: free
costNote: Free — a hosted Google Custom Search Engine (CSE) over ~48 paste sites. No account; results are ordinary Google search results scoped to those sites.
opsec: passive
opsecNote: Passive to the target — you query Google's index, not the paste hosts directly, so the subject isn't alerted. Use a sock browser. Do NOT log into or download from any leak site; only read the indexed results.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Built by cipher387 / cyb-detective, a well-known OSINT tooling author. It is a curated Google CSE, so result quality is Google's; coverage is only what Google has indexed on those paste sites.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- pastebin search engines
- cipher387 pastebin CSE
- cyb-detective pastebin search
tags:
- Universal Contact Search and Leaks Search
- pastebin
- leaks
source: cyb-detective
lastVerified: '2026-07-14'
enrichment: full
---

# My CSE for search in 48 pastebin sites

> A hosted Google Custom Search Engine that searches ~48 pastebin-style sites at once — a fast way to find a selector inside pasted dumps, leaks and mentions.

## When to use
You have a selector — a `username`, `email`, real `name`, phone, handle, or a leak-specific string — and want to know if it appears in pasted data across the many pastebin clones where dumps and doxes get posted. Searching each site individually is impractical; this CSE queries them together via Google. Strong for surfacing leaked credentials, associated emails/phones, and where a subject's data has been exposed.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cipher387.github.io/pastebinsearchengines/ in a sock browser.
2. Enter the selector — quote exact strings (`"john.doe@example.com"`), and try variations (username, email, name, phone).
3. It runs a Google CSE scoped to the paste sites; review the returned paste URLs and snippets.
4. Read the output: paste hits that may contain associated `email`, `phone`, credentials, or identifiers (`document-id`). Open results cautiously (read-only).
5. Pivot: a leaked email/phone feeds breach-check and account-existence tools; co-located data in a dump maps `associate`s and other identities.

## Inputs → Outputs
- **In:** `name`, `username`, `email` (or phone/handle/leak string)
- **Out:** `email`, `phone`, `document-id` (identifiers found in pastes), plus context
- **Empty/negative result looks like:** no paste hits — meaning the selector isn't in Google's index of those sites (pastes are often removed or unindexed), NOT proof the data was never leaked.

## Gotchas & OpSec
- Coverage is limited to what Google has indexed on those sites; many pastes are deleted or never indexed, so a null result is weak evidence.
- Handle leaked data lawfully and ethically; do not authenticate to or re-host leak content — just read the indexed result.
- OpSec: passive; use a sock browser and avoid interacting with the leak sites directly.

## Overlaps ("do both")
- Pairs with dedicated breach-lookup services — this catches ad-hoc pastes and dumps that structured breach databases miss, and vice versa. Run both for coverage.

## Trust & verifiability
`trust: community` — a curated CSE by a respected OSINT author (cipher387/cyb-detective). The search mechanism (Google) is reliable; treat any leaked value as a lead to verify, since paste data is unvetted and can be fabricated or stale.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | my-cse-for-search-in-48-pastebin-sites |
| category | people-search |
| selectorsIn → selectorsOut | name, username, email → email, phone, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
