---
id: urlscan-io
name: urlscan.io
description: Use when you have a `domain`/URL or `ip-address` and want its scan history — returns screenshots, contacted domains/IPs, and page resources for pivoting.
url: https://urlscan.io/search/#*
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- discovery
bestFor: Looking up past scans of a URL/domain to see what it looked like, which IPs and domains it contacted, and what it hosted — without visiting it yourself.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
- image
status: live
pricing: freemium
costNote: Free to search the public scan database and submit public scans; private/unlisted scans and higher API volume need a paid commercial plan.
opsec: passive
opsecNote: Searching existing scans is fully passive — the target site never sees you. If you SUBMIT a new scan, urlscan fetches the URL from its own infrastructure (not yours), but a public scan is visible to everyone; mark scans unlisted/private (paid) if the URL itself is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Widely used, reputable web-scanning service relied on by the security/OSINT community; results are reproducible artifacts (screenshots, HAR, DOM) rather than opinions.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- urlscan
- urlscan.io search
tags:
- Domain/IP/Links
- Domain/IP investigation
- url-scanning
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# urlscan.io

> "A sandbox for the web" — search a huge archive of URL scans to see a page's screenshot, the IPs/domains it talked to, and its resources, all without touching the target.

## When to use
You have a suspicious or relevant `domain`/URL (a phishing link, a subject's site, a shortener destination) or an `ip-address`, and you want to know what it hosted and what infrastructure it connected to — historically and safely. urlscan lets you view someone else's prior scan (screenshot + network trace) instead of loading the page from your own machine.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://urlscan.io/search/ and query by `domain:`, `page.url:`, `ip:`, `hash:`, or ASN — e.g. `domain:example.com` or `ip:1.2.3.4`.
2. Open a result to see the screenshot, the list of contacted domains/IPs, HTTP transactions, and page metadata.
3. Pivot on any artifact: a shared favicon hash, a common IP, or a redirect chain links related malicious/related sites.
4. If no scan exists and it is safe/appropriate, submit the URL for a fresh scan — choose **unlisted/private** (paid) if the URL is sensitive, since public scans are world-visible.
5. Feed discovered IPs/domains into WHOIS, passive DNS and certificate tools.

## Inputs → Outputs
- **In:** `domain`/URL or `ip-address`
- **Out:** screenshot (`image`), contacted `domain`s and `ip-address`es, page resources, redirect chain
- **Empty/negative result looks like:** "no results" — the URL/domain has never been scanned publicly; this is not evidence the site is clean, only that no one scanned it. Submit a scan to generate data.

## Gotchas & OpSec
- **Public scans are visible to everyone** — never submit a sensitive/private URL as a public scan; use unlisted/private (paid) or don't submit.
- Search is passive; submitting is active-but-indirect (urlscan's infra fetches it, not yours).
- Historical scans may be stale — the site may have changed since.

## Overlaps ("do both")
- Pairs with passive-DNS, WHOIS and certificate-transparency tools: urlscan shows the live behaviour and screenshot, those add ownership and DNS history to the same `domain`/`ip-address`.

## Trust & verifiability
`trust: trusted` — a well-established scanning service; each result is a concrete captured artifact you can inspect, not a claim to take on faith.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | urlscan-io |
