---
id: google-com-77
name: Google Advanced Search
description: Use when you have a name, username or phrase and want precise, operator-controlled web results — returns web pages, social profiles and document mentions with less noise.
url: https://www.google.com/advanced_search
category: search-engines
path:
- search-engines
bestFor: Running tightly-scoped Google queries (exact phrase, site, filetype, date, exclusions) without memorising operator syntax.
selectorsIn:
- name
- username
selectorsOut:
- name
- social-profile
status: live
pricing: free
costNote: Free; no account required for search (some heavy/automated querying may trigger a CAPTCHA).
opsec: passive
opsecNote: Queries go to Google, not to the target, so the subject is not alerted. Google logs your IP and search history; use a sock-puppet/VPN for sensitive names, and remember that clicking a result fetches that result's host, which can log you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Google's own first-party advanced-search form; it is a query builder over the standard index, so results are as authoritative as any Google search.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Google advanced search
- google.com advanced_search
- Google dorking form
tags:
- searchengines
- Search Engines
- google
- dorking
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Google Advanced Search

> Google's own advanced-search form — a point-and-click front end for exact-phrase, site, filetype, date and exclusion operators, so you can pin down a person without fighting query syntax.

## When to use
You have a `name`, `username` or distinctive phrase and plain Google is drowning you in noise. The advanced form (and the operators it teaches) lets you demand an **exact phrase**, restrict to a **site** (`site:linkedin.com`), a **filetype** (`filetype:pdf`), a **language/region**, or a **date range**, and to **exclude** noise terms. This precision is the backbone of nearly every OSINT web sweep — it turns "10,000 John Smiths" into the handful that match your subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.google.com/advanced_search in a sock-puppet browser.
2. Fill the fields: "this exact word or phrase" for a `name`/`username`; "site or domain" to target a platform; language/region/last-update to localise; the minus/"none of these words" box to strip noise.
3. Run it, then iterate the generated query directly in the address bar (`"John Smith" site:facebook.com -recruiter`).
4. Combine operators: quotes + `site:` + `filetype:` is the classic person-finding stack.
5. Pivot: a discovered `social-profile` feeds the matching platform tool; a document hit feeds `[[exif-data-viewer]]`/metadata analysis.

## Inputs → Outputs
- **In:** `name`, `username`, or an exact phrase (address, phone, bio line)
- **Out:** `name` mentions and `social-profile` links, plus documents and pages, ranked and de-noised by your operators
- **Empty/negative result looks like:** zero or only-irrelevant hits. Loosen (drop the exact phrase), rotate operators, and try `[[usearchfrom-com]]` to search as another country before concluding there is no footprint.

## Gotchas & OpSec
- Personalisation and geolocation shape results — use a clean/sock-puppet session and `[[usearchfrom-com]]` to see a subject's local results.
- Heavy or automated querying trips a CAPTCHA; slow down or solve it.
- Google's index is not the whole web — pair with Yandex/Bing and specialised engines for coverage the majors miss.

## Overlaps ("do both")
- Pairs with `[[usearchfrom-com]]` (localise the same query) and `[[monstercrawler-com]]` (a different index's long tail).
- Feeds `[[github-io-2]]` (FilePhish) for the filetype-dork half of document hunting.

## Trust & verifiability
`trust: trusted` — this is Google's first-party search; the tool is authoritative as a *search*, but every hit is only a pointer — verify the underlying page/source before treating a match as your subject.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-com-77 |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → name, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
