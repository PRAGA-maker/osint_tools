---
id: google-search-results-scraper
name: Google Search Results Scraper
description: Use when you have a Google query (e.g. a `name` or dork) and want its results as a spreadsheet — returns titles, links, snippets and `email`s pulled from the snippets.
url: https://chromewebstore.google.com/detail/google-search-results-scr/cmdkhofenchpdlkbpkheddfgfdmmobcc
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Bulk-capturing a Google SERP into Excel — site, title, link, snippet, and any emails in the snippets — for offline triage.
selectorsIn:
- name
selectorsOut:
- email
- domain
status: live
pricing: free
costNote: Free Chrome extension; no account or payment. Requires a Chromium-based browser.
opsec: active
opsecNote: The extension automates paging through Google results in YOUR browser, which can look like scraping and trip Google's bot detection (CAPTCHAs, temporary blocks) on the IP/account you're signed into. Run it from a sock-puppet browser profile behind a VPN, not your personal Google session, and pace large collections.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: browser-extension
trust: unverified
trustNote: A third-party Chrome extension (Brain Gain Recruiting, LLC) with a modest user base; it reads the Google result pages you view. Functionally simple but unvetted — audit permissions before installing.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Google SERP scraper
tags:
- toddington
- curated-directory
- add-ons-apps-extensions
- serp
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# Google Search Results Scraper

> A Chrome extension that harvests a Google results page into an Excel table — handy for turning a name search or Google dork into a structured, deduped list you can work offline.

## When to use
You've built a good Google query — a subject's `name`, a `"quoted phrase"`, or a dork (`site:`, `intext:`, `filetype:`) — and it returns many results you want to capture and triage rather than click one by one. This extension collects each result's site, title, link, and snippet across all pages, removes duplicates, and pulls any `email` addresses out of the snippets, exporting to Excel. Good for footprinting and building a lead list from search.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the extension into a **sock-puppet** Chromium profile (not your personal Google session) and use a VPN.
2. Run your Google query as normal (craft dorks to sharpen it).
3. Trigger the extension; it pages through the results and collects site/title/link/snippet, extracting emails from snippets.
4. Solve any Google CAPTCHA that appears (heavy paging triggers bot checks) — see OpSec.
5. Export to Excel and triage: pivot emails into email-OSINT, domains into infrastructure lookups, and promising links into deeper review.

## Inputs → Outputs
- **In:** a Google query (`name`, phrase, or dork)
- **Out:** structured SERP rows (title, `domain`/link, snippet) + `email`s harvested from snippets
- **Empty/negative result looks like:** no rows captured — either the query returned nothing, or Google served a CAPTCHA/block mid-run and the extension stopped (retry slower, from a fresh IP).

## Gotchas & OpSec
- **Active / bot-like:** automated paging can trigger Google CAPTCHAs or temporary IP/account blocks. Use a disposable profile + VPN and pace it.
- It only sees what Google shows (image/video results excluded); snippet emails may be truncated or false matches — verify.
- A third-party extension with page-read access — review its permissions and keep it isolated to the investigation profile.

## Overlaps ("do both")
- Pairs with Google-dorking references and email/domain OSINT tools — this captures the SERP; those enrich the emails and domains it extracts.

## Trust & verifiability
`trust: unverified` — a functional but unvetted third-party extension; the output is just a structured copy of Google's own results, so reliability rests on your query, and every extracted email/lead should be confirmed independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-search-results-scraper |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | name → email, domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | yes (captcha) |
