---
id: web-data-exposure-scanner
name: Web Data Exposure Scanner
description: Use when you have a `domain`/URL and want to find sensitive data it exposes — crawls the site and returns `email`, `phone`, `document-id` and leaked file URLs.
url: https://github.com/eduardoit/web-data-exposure-scanner
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- vulnerabilities
- scanners
bestFor: Crawling a target website to surface exposed emails, phone numbers, ID-document numbers and sensitive files for an authorized exposure audit.
selectorsIn:
- domain
selectorsOut:
- email
- phone
- document-id
status: live
pricing: free
costNote: Free and open source (MIT). A Python 3.8+ CLI; no service fees.
opsec: active
opsecNote: This actively crawls the target site (recursive, multi-threaded), so it generates real traffic and log entries and can trip WAF/IDS alerts — only run against sites you are authorized to assess. It has optional Tor support to mask origin, but Tor plus aggressive crawling can itself look hostile; throttle depth/threads and get authorization first.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: A single-developer open-source project (eduardoit) with public source you can audit; useful but not a widely vetted tool, so review the code and validate findings before relying on them.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
aliases:
- WDES
- web-data-exposure-scanner
tags:
- recon
- scanner
- data-exposure
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# Web Data Exposure Scanner

> An open-source Python crawler that scans a website for inadvertently exposed sensitive data — emails, phone numbers, ID-document patterns and downloadable sensitive files.

## When to use
You have a `domain` (your own, a client's, or an authorized target) and want to know what personal or sensitive data it leaks publicly: harvestable `email`s, `phone` numbers, national-ID patterns (it ships recognizers for several Latin-American countries and Spain), and exposed files (`.pdf`, `.doc`, `.xls`, `.sql`, `.bak`, etc.). Strictly an authorized exposure-audit / attack-surface tool — the README stresses ethical, permissioned use.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo; ensure Python 3.8+ and install requirements.
2. Run `python scanner.py` (interactive mode) or pass CLI arguments (target URL, crawl depth, thread count, custom patterns).
3. Optionally enable Tor for origin masking — but keep crawl depth/threads modest to stay within authorized, non-disruptive bounds.
4. Let it recursively crawl and pattern-match the pages.
5. Read the JSON/TXT report: discovered emails, phones, ID numbers, and sensitive-file URLs; verify each hit manually (regex matches produce false positives).

## Inputs → Outputs
- **In:** a target `domain`/URL (+ depth/thread/pattern options)
- **Out:** `email`, `phone`, `document-id` (ID-number patterns), and exposed file URLs, as a JSON/TXT report
- **Empty/negative result looks like:** an empty findings report — the crawl reached pages but matched no patterns (good hygiene, or the data sits behind auth the crawler can't reach).

## Gotchas & OpSec
- **Active and noisy:** recursive multi-threaded crawling shows in the target's logs and can trigger WAF/rate-limit/IDS responses — authorization is mandatory; throttle.
- Pattern matching (especially ID-number regexes) yields false positives; confirm findings before reporting.
- Country-specific ID recognizers are region-scoped (mainly LatAm + Spain); coverage elsewhere is limited to email/phone/file detection.

## Overlaps ("do both")
- Pairs with search-engine dorking and other site-crawlers — this automates on-site pattern extraction; dorking finds exposure indexed off-site. Cross-check both for full coverage.

## Trust & verifiability
`trust: unverified` — a legitimate but single-maintainer open-source tool; the source is public and auditable, yet it lacks broad third-party vetting, so review the code and independently confirm each finding.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | web-data-exposure-scanner |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → email, phone, document-id |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
