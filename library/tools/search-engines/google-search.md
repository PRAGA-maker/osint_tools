---
id: google-search
name: Google Search
description: Use when you have almost any selector (name, username, email, phone, domain, address) and want the broadest first-pass web coverage — returns links to social-profiles, records, mentions, images.
url: https://www.google.com
category: search-engines
path:
- search-engines
bestFor: The default first move on any selector, and precision dorking with advanced operators to surface indexed pages others miss.
selectorsIn:
- name
- username
- email
- phone
- domain
- address
selectorsOut:
- social-profile
- address
- phone
- employer-org
- associate
- image
status: live
pricing: free
costNote: Free; no account required for web search.
opsec: passive
opsecNote: Searching does not touch the subject's infrastructure — it is passive toward the target. Google logs your queries and IP, so run sensitive dorking from a sock-puppet browser/VPN, and never log in with an attributable account while investigating.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The results index is Google's; the ranking is authoritative as an index but the linked pages are third-party — verify each source, and note Google personalizes and geo-localizes results.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- google.com
- Google dorking
tags:
- general-search
- dorking
- search-operators
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# Google Search

> The universal starting point: cast the widest net on any selector, then tighten with advanced operators to dork out precisely the pages you want.

## When to use
Almost always, first. You have any selector — a `name`, `username`, `email`, `phone`, `domain`, or `address` — and you want a broad sweep of what the indexed web knows before reaching for specialist tools. Google's real OSINT power is *dorking*: operators that turn a vague search into a surgical one (exact phrases, site restriction, file types, title/URL matches).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.google.com in a clean/sock-puppet session (logged out).
2. Start broad: put the selector in `"double quotes"` for an exact-match (a full name, a username, a phone number in several formats).
3. Tighten with operators:
   - `"John Q Public" site:linkedin.com` — restrict to one site.
   - `"jdoe" -site:pinterest.com` — exclude noise.
   - `intext:"john.doe@example.com"` / `intitle:` / `inurl:"username"` — match where the term appears.
   - `filetype:pdf "Full Name"` — surface documents (résumés, rosters, leaked lists).
   - `site:example.com "target"` — enumerate a domain's indexed pages.
4. Read results: profile links (`social-profile`), leaked docs, mentions tying the subject to an `employer-org`/`associate`, cached addresses/phones. Switch to the **Images** tab for `image` results.
5. Pivot each promising hit into the appropriate specialist tool.

## Inputs → Outputs
- **In:** `name`, `username`, `email`, `phone`, `domain`, `address`
- **Out:** links to `social-profile`, `address`, `phone`, `employer-org`, `associate`, `image`
- **Empty/negative result looks like:** "did not match any documents" or only irrelevant hits — reformulate (quote it, vary phone/name formats, add a disambiguating term) before concluding nothing is indexed; absence from Google is not absence from the web.

## Gotchas & OpSec
- Human-in-the-loop: heavy or automated dorking can trigger a CAPTCHA — solve it manually or slow down; do not scrape without accounting for this.
- OpSec: **passive** toward the target, but Google records your queries. Stay logged out of any attributable account; use a VPN/sock-puppet for sensitive work.
- Results are **personalized and geo-localized** — what you see may differ from what someone else sees; use an incognito/clean session for reproducibility, and try Google country domains or `gl=` for other regions.
- Google's index is not everything — cross-check with a second engine (Bing/Yandex/DuckDuckGo) since each indexes differently.

## Overlaps ("do both")
- Pairs with alternative search engines (Bing, Yandex, DuckDuckGo) — each indexes and ranks differently, and Yandex in particular surfaces content Google buries; never rely on one engine alone.

## Trust & verifiability
`trust: trusted` — the index itself is Google's and authoritative, but every *linked page* is third-party; treat hits as leads and verify each source directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-search |
