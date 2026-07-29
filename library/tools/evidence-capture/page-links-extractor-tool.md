---
id: page-links-extractor-tool
name: Page Links Extractor Tool
description: Use when you have a `domain`/URL and want every hyperlink on that page pulled out — returns a list of internal and external links (further domains, social profiles).
url: https://shadowcrypt.net/tools/pagelinks
category: evidence-capture
path:
- evidence-capture
bestFor: Quickly harvesting all outbound and internal links from a single web page to map where it points.
selectorsIn:
- domain
selectorsOut:
- domain
- social-profile
status: live
pricing: free
costNote: Free browser tool on ShadowCrypt; no account required.
opsec: passive
opsecNote: ShadowCrypt fetches the page server-side, so the request to the target originates from ShadowCrypt's infrastructure, not your IP — mildly protective. But you are trusting a third party with the URL you are investigating; avoid submitting sensitive internal URLs. No alert reaches the page owner.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: ShadowCrypt is an independent free web-tools suite (WHOIS, subdomain finder, IP geolocation, DNS). Functional and live; a small community project rather than an established vendor, so verify anything critical.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- cloudflare-resolver-tool
- geoip-tracker-tool
- nmap-checker-tool
- phone-number-lookup-tool
- shadowcrypt-tools
aliases:
- ShadowCrypt Page Links Extractor
tags:
- link-extraction
- web-recon
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Page Links Extractor Tool

> A one-field web utility that fetches a page and returns every hyperlink on it — a fast way to see what a site links out to and reference internally.

## When to use
You have a subject's website, profile page, or landing `domain` and want to enumerate everywhere it points: linked social profiles, partner/related domains, downloadable documents, and internal structure. Handy as a first pass before deeper crawling, to spot the low-hanging external identities and infrastructure connected to a page.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://shadowcrypt.net/tools/pagelinks.
2. Paste the target page URL and run the extraction.
3. Read the returned link list — typically split into internal (same-domain) and external links.
4. Triage: external links to `social-profile` platforms (LinkedIn, Twitter/X, Instagram) and to other `domain`s are the pivot-worthy hits; internal links reveal site structure to crawl further.
5. Pivot: extracted social links feed profile-enumeration tools; extracted domains feed WHOIS/DNS via `[[shadowcrypt-tools]]` (`[[cloudflare-resolver-tool]]`, `[[geoip-tracker-tool]]`).

## Inputs → Outputs
- **In:** `domain` / page URL
- **Out:** list of hyperlinks → linked `domain`s and `social-profile` URLs
- **Empty/negative result looks like:** an empty or tiny list — the page is JavaScript-rendered (links load client-side and the server-side fetch misses them) or is a single-page app; use a browser-based capture instead.

## Gotchas & OpSec
- Server-side fetch means JS-injected links are often missed — a sparse result does not mean the page is bare. For dynamic pages, capture links from a real browser session.
- You hand the target URL to a third-party service; fine for public pages, not for sensitive internal links.
- Single-page-at-a-time; not a crawler. For whole-site link maps, pair with a dedicated crawler.

## Overlaps ("do both")
- Part of the `[[shadowcrypt-tools]]` suite — do both: extract links here, then run the discovered domains through `[[cloudflare-resolver-tool]]` and `[[geoip-tracker-tool]]` for infrastructure attribution.

## Trust & verifiability
`trust: community` — a functional independent web tool. Output is directly verifiable (the links are real and clickable), but treat the service itself as best-effort; cross-check dynamic pages by hand.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | page-links-extractor-tool |
