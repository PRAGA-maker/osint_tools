---
id: find-plus
name: find+ (Regex Find-in-Page)
description: Use when you have a page full of text and want to pull every `email`, `domain`, `phone` or ID matching a pattern — a regex find-in-page Chrome extension that extracts and copies all matches.
url: https://chromewebstore.google.com/detail/find-regex-find-in-page/fddffkdncgkkdjobemgbpojjeffmmofb
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Regex-extracting all emails/domains/phones/IDs from the current web page.
selectorsIn: []
selectorsOut:
- email
- domain
- phone
status: live
pricing: free
costNote: Free Chrome extension (v2.2.3, Feb 2026); developer states no data collection.
opsec: passive
opsecNote: Runs entirely locally in your browser against the page already loaded in your tab — it sends nothing anywhere. Whatever page you run it on has of course seen your visit; the extension itself adds no new exposure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: A popular (~10k users, 4.2★) third-party developer extension; open in behavior and no-data-collection per the listing, but not audited here.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- find plus
- find+ regex
tags:
- Domain/IP/Links
- Searchers, scrapers, extractors, parsers
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# find+ (Regex Find-in-Page)

> A Chrome extension that upgrades Ctrl+F to full regular expressions — search the current page by pattern, then copy every match at once.

## When to use
You're on a page dense with contact data or identifiers — a dump, a directory, a scraped profile, a WHOIS or breach page — and want to harvest every `email`, `domain`, `phone` number or ID in one pass instead of eyeballing. Point a regex at it and copy all matches to your clipboard for pivoting.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install find+ from the Chrome Web Store (link above).
2. Open the target page (static HTML works best; it struggles with dynamic apps like Google Sheets).
3. Launch find+ and enter a regex — e.g. emails `[\w.+-]+@[\w-]+\.[\w.-]+`, or a phone/ID pattern.
4. Review the highlighted matches; use "copy matches" to grab them all, or find-and-replace to reshape them.
5. Pivot: feed the extracted `email`s/`domain`s/`phone`s into the relevant email/domain/phone OSINT tools; save reusable regexes for next time.

## Inputs → Outputs
- **In:** a regular expression run against the current page (no external selector query)
- **Out:** all matching strings — commonly `email`, `domain`, `phone`, document/IDs — copyable in bulk
- **Empty/negative result looks like:** zero matches — either the pattern is wrong, or the data is rendered dynamically/off-DOM (large or JS-driven pages); simplify the regex or use a scraper.

## Gotchas & OpSec
- Human-in-the-loop: none, though writing a correct regex is on you; it's aimed at technical users.
- OpSec: **passive** — it operates purely on the page already in your tab and transmits nothing; safe for sensitive pages.
- Doesn't handle dynamic/very large pages well; for those, use a dedicated scraper/parser instead.

## Overlaps ("do both")
- Complements server-side scrapers/extractors — find+ is the instant, in-browser option for one page; a scraper is better for many pages or dynamic content.

## Trust & verifiability
`trust: community` — a widely-used third-party extension that declares no data collection and runs locally; the extracted values are only as good as the page you run it on.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | find-plus |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut |  → email, domain, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
