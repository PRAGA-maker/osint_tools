---
id: google-chrome-webpage-regexp-search
name: Google Chrome webpage Regexp search
description: Use when you have a rendered web page and want to extract patterned data — returns every regex match (emails, phones, IPs, IDs) highlighted on the page.
url: https://chromewebstore.google.com/detail/chrome-regex-search/bpelaihoicobbkgmhcbikncnpacdbknn
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Searching the current web page with a regular expression to pull out emails, phones, IPs or other patterned strings.
selectorsIn: []
selectorsOut:
- email
- phone
- ip-address
- crypto-wallet
status: live
pricing: free
costNote: Free, open-source Chrome extension; no account.
opsec: passive
opsecNote: The extension runs locally in your browser against pages you already have open — it sends nothing anywhere. It does not fetch the page for you, so use it behind whatever browsing OpSec (sock-puppet/VPN) you already apply to the visit itself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Popular open-source Chrome extension (source on GitHub) that adds Ctrl+F-style search with full regular-expression support; it only reads the DOM of the current tab.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- chrome regex search
- regexp page search
tags:
- Domain/IP/Links
- browser-extension
- regex
- data-extraction
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Google Chrome webpage Regexp search

> Ctrl+F on steroids: a Chrome extension that searches the current page with a regular expression and highlights every match — perfect for scraping emails, phones, IPs or IDs out of a long page.

## When to use
You're on a page dense with text — a data dump, a forum thread, a directory, a paste, source view — and want to pull every instance of a pattern rather than eyeball it. Chrome's built-in find only does literal strings; this extension lets you run a regex (email, phone, `ip-address`, crypto address, ID formats) and see and count all matches at once, which turns a wall of text into an extracted selector list.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Chrome Regex Search" from the Chrome Web Store (link above; source on GitHub).
2. Navigate to the page you want to mine (apply your usual browsing OpSec first).
3. Open the extension (its shortcut or toolbar button) and type a regular expression, e.g.
   - emails: `[\w.+-]+@[\w-]+\.[\w.-]+`
   - IPv4: `\b\d{1,3}(\.\d{1,3}){3}\b`
   - BTC-ish: `\b(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}\b`
4. Every match is highlighted and counted; step through them and copy out the values.
5. Pivot: extracted `email`/`phone`/`ip-address`/`crypto-wallet` values feed the corresponding lookup tools.

## Inputs → Outputs
- **In:** a regular expression run against the current page (no selector in)
- **Out:** highlighted matches — `email`, `phone`, `ip-address`, `crypto-wallet`, or any patterned string on the page
- **Empty/negative result looks like:** zero highlights — either the pattern is wrong or the data isn't in the rendered DOM (it may be in an iframe, image, or loaded after search); adjust the regex or view source.

## Gotchas & OpSec
- Searches only the *rendered* current tab — content in images, PDFs, iframes, or not-yet-loaded elements won't match.
- It doesn't fetch pages; your visit to the page is what carries OpSec risk, so browse accordingly.
- Local-only: nothing leaves the browser, a good privacy property.

## Overlaps ("do both")
- Complements a full scraper/`curl` + grep workflow — the extension is instant for a page you're already viewing, while scripted extraction scales across many pages; use the extension for spot extraction, scripts for bulk.

## Trust & verifiability
`trust: community` — an open-source, widely-installed browser extension that only reads the current tab's DOM; low risk, and you can read its source, but as a community tool it carries no formal guarantee.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-chrome-webpage-regexp-search |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut |  → email, phone, ip-address, crypto-wallet |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
