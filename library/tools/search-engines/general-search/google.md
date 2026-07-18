---
id: google
name: Google
description: Use when you have almost any selector (`name`, `username`, `email`, `phone`, `domain`) and want the broadest web footprint — returns pages, `social-profile`, `domain` and document hits, sharpened with search operators (dorks).
url: https://www.google.com/
category: search-engines
path:
- search-engines
- general-search
bestFor: The default first-pass web search for any selector, made precise with operators (site:, intext:, filetype:, inurl:, "exact phrase").
selectorsIn:
- name
- username
- email
- phone
- domain
selectorsOut:
- social-profile
- domain
- document-id
status: live
pricing: free
costNote: Free to search. The paid Custom Search / Programmable Search JSON API is a separate product; manual searching needs no account.
opsec: passive
opsecNote: Searching is passive toward the target, but if you are signed into a Google account every query is tied to that identity and personalises/creates a history — search logged out, in a clean/sock-puppet profile, ideally via VPN. Clicking a result then contacts that site directly, which can expose your IP to the target's server; open sensitive results through an archive or sandbox.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The results index is Google's and authoritative as a pointer to live/cached pages; the linked pages themselves are third-party and must be judged individually.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- google-custom-search
- google-dork-cheatsheet
aliases:
- Google Search
- google.com
tags:
- search-engine
- google-dorks
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Google

> The universal starting point — and, with operators ("dorks"), a precision instrument for pulling a specific person, file or site out of the open web.

## When to use
Almost always, first. Whatever selector you hold — a `name`, `username`, `email`, `phone`, `domain`, or a distinctive phrase — Google is the widest net and the fastest way to find where a subject appears online. Its real power for OSINT is **operators**: quoting exact strings, scoping to a site, filtering by file type, or excluding noise turns a vague query into a targeted one. Use it to map a footprint before reaching for specialist tools, and to pivot between selectors as you discover them.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.google.com/ (logged out, in a clean/sock-puppet browser profile).
2. Start broad, then tighten with operators:
   - `"Firstname Lastname"` — exact-phrase to avoid split matches.
   - `"John Smith" (Denver OR Colorado)` — add a location to disambiguate.
   - `site:linkedin.com "John Smith"` / `site:facebook.com` — scope to one platform for `social-profile` hits.
   - `"username"` — hunt a handle across the web.
   - `"john@example.com"` or `"555-123-4567"` — quoted email/phone to find leaks and listings.
   - `filetype:pdf "John Smith"` / `inurl:` / `intitle:` — surface documents and specific URL/title patterns.
   - Add `-term` to exclude noise (e.g. `-jobs -pinterest`).
3. Also check the **Images**, **News**, and date-range (Tools) tabs.
4. Pivot: each hit yields new selectors (a handle, an employer, a domain) to feed back into Google or a specialist tool.

## Inputs → Outputs
- **In:** `name`, `username`, `email`, `phone`, `domain`, or any phrase
- **Out:** ranked web pages, `social-profile` links, personal `domain`s, `document-id` files (PDFs/docs), image and news hits
- **Empty/negative result looks like:** few or generic results — the person may have a small footprint, use a different name/handle, or be buried under a common-name namesake. Reformulate with operators before concluding absence; also try Bing/DuckDuckGo/Yandex, which index differently.

## Gotchas & OpSec
- Human-in-the-loop: none for searching; heavy automated querying triggers a CAPTCHA/rate limit.
- OpSec: **passive** to search, but **stay logged out** — a signed-in session ties queries to you and personalises results (hiding the neutral view). Clicking a result reveals your IP to that site; use an archive/sandbox for sensitive targets.
- Results are **personalised and localised**; a sock-puppet in the wrong country sees a skewed index. Use verbatim/quoted queries to reduce Google's "helpful" reinterpretation.
- **`cache:` is gone** — Google retired the cached-page operator/links in 2024; use the Wayback Machine or an archive tool for historical copies instead.
- Google doesn't index everything (paywalled, robots-blocked, deep-web, or platform-internal content); a blank isn't proof of absence.

## Overlaps ("do both")
- Pairs with `[[google-dork-cheatsheet]]` for a fuller operator reference, and with `[[google-custom-search]]` to save a scoped multi-site search you run repeatedly. Always cross-run the same query on other engines — each index has different blind spots.

## Trust & verifiability
`trust: trusted` — the index is authoritative as a pointer, but Google only tells you a page *exists and matches*; the credibility of each linked page is a separate judgement you must make.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, email, phone, domain → social-profile, domain, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
