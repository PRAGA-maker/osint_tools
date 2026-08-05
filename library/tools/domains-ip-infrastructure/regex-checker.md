---
id: regex-checker
name: Regex Checker
description: Use when you are viewing a `domain`/webpage and want to auto-highlight and extract selectors from it — returns `email`, `phone`, and `address` matches found on the page.
url: https://chrome.google.com/webstore/detail/regex-checker/gkcnkoebkkppbapcjifgokmpcflfhbde
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: One-click extraction of emails, phone numbers, dates, prices, and addresses from the page you are currently viewing.
selectorsIn:
- domain
selectorsOut:
- email
- phone
- address
status: live
pricing: free
costNote: Free Chrome extension; no account, key, or in-app purchase. Runs locally in your browser.
opsec: passive
opsecNote: The extension parses the already-loaded page in your own browser — it generates no new request to the target and sends nothing to a server. Vet the extension's permissions on install (it needs to read page content); use a dedicated research browser profile to keep it off your personal browsing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: unverified
trustNote: Third-party Chrome Web Store extension by an independent developer; it runs client-side and does not call home, but it is not from a vetted vendor — review its store listing/permissions before trusting it on sensitive pages.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Regex Checker Chrome extension
- Regex Scanner
tags:
- Domain/IP/Links
- Searchers, scrapers, extractors, parsers
- browser-extension
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# Regex Checker

> A Chrome extension that regex-scans the page you're on and highlights every email, phone, date, price, and address — turning a wall of text into a list of pivotable selectors.

## When to use
You are reading a page — a profile, a company "contact" page, a forum thread, a leaked document rendered in the browser, a directory listing — and want to pull out contact selectors without hand-scanning. Click once and the extension highlights all `email`, `phone`, and `address` (plus dates/prices) matches on the current `domain`/page, so you can harvest them in bulk and feed them into email/phone/address enrichment.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Regex Checker" from the Chrome Web Store (or a Chromium/Brave equivalent) into a research browser profile.
2. Navigate to the page you want to scan.
3. Click the extension icon (or run its scan action) — matches are highlighted in-page; use built-in patterns for emails/phones/addresses or supply your own regex for a custom selector.
4. Copy the highlighted values out.
5. Pivot: extracted `email` → email-existence/breach tools; `phone` → carrier/owner lookups; `address` → property/geolocation records.

## Inputs → Outputs
- **In:** the current `domain`/webpage (whatever is loaded in the tab)
- **Out:** highlighted `email`, `phone`, `address` (and date/price) matches on that page
- **Empty/negative result looks like:** nothing highlighted — either the page truly contains no matches, values are rendered as images/obfuscated, or the content loads dynamically after the scan (rescan after the page settles).

## Gotchas & OpSec
- Interaction is via the extension itself (browser-extension), so there is no separate login or CAPTCHA.
- False positives: regex catches string-shaped matches (version numbers can look like phone numbers; @-handles like emails) — eyeball before acting.
- OpSec: passive and local — it reads a page you already loaded and issues no new request, so the target sees nothing beyond your original page visit. Still, grant page-read permission only in a research profile.

## Overlaps ("do both")
- Pairs with server-side scrapers/parsers: those crawl a site you don't want to visit directly, while this instantly extracts from a page you are already looking at.

## Trust & verifiability
`trust: unverified` — an independent Chrome Web Store extension; it operates client-side and does not exfiltrate data, but it is unvetted third-party code, so review its permissions and keep it isolated to a research browser.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | regex-checker |
