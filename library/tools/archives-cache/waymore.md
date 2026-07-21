---
id: waymore
name: WayMore
description: Use when you have a `domain` and want the fullest possible historical URL/content footprint — returns archived links and downloaded response bodies as `document-id`/`metadata-exif` leads.
url: https://github.com/xnl-h4ck3r/waymore
category: archives-cache
path:
- archives-cache
bestFor: Pulling every known archived URL for a domain (and optionally the archived page bodies) from many sources at once.
selectorsIn:
- domain
selectorsOut:
- domain
- document-id
status: live
pricing: free
costNote: Free, open-source (pip/Docker). Some sources (URLScan, VirusTotal, Intelligence X) work better or faster with a free API key you add to the config.
opsec: passive
opsecNote: Queries public archive indexes (Wayback, Common Crawl, AlienVault OTX, URLScan, VirusTotal, GhostArchive, Intelligence X), not the live target site, so it does not touch the subject's own infrastructure. The requests go to those third parties under your own IP/API keys — run from a research VPN if you don't want those providers to log your investigative interest. Downloading archived responses (mode R/B) can be high-volume; respect rate limits.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Widely used, actively maintained open-source tool by xnl-h4ck3r; results are only as authoritative as the underlying public archives it aggregates.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- xnlinkfinder
- archive-org-downloader
aliases:
- waymore.py
- xnl-h4ck3r waymore
tags:
- Archives
- Tools for working with web archives
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# WayMore

> An archive aggregator that sweeps Wayback, Common Crawl, URLScan, AlienVault OTX, VirusTotal, GhostArchive and Intelligence X for every URL a domain ever exposed — and can download the archived page bodies for deeper mining.

## When to use
You have a `domain` (a subject's personal site, a business, a suspect blog, a site linked from a forum handle) and want the widest possible historical map of what lived on it — deleted pages, old profile URLs, uploaded files, parameters — without hitting the live server. Use it early in domain/infrastructure work to build a URL corpus you then grep for names, emails, phone numbers, or document IDs.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install waymore` (or `pip install git+https://github.com/xnl-h4ck3r/waymore.git`, or run the bundled Docker image).
2. Pull just the URLs: `waymore -i example.com -mode U` → writes `waymore.txt`.
3. Pull URLs **and** download the archived response bodies: `waymore -i example.com -mode B` → saves per-response files plus an `index.txt` mapping each saved body to its source URL.
4. Narrow the sweep on large domains with filters: `-ft` (MIME types), `-fc` (HTTP status codes), `-l`/`-from`/`-to` (date range), `-ko`/`-ki` (keyword include/exclude).
5. Pivot: feed `waymore.txt` into a link/parameter extractor like `[[xnlinkfinder]]`, or grep the downloaded bodies for `name` / `email` / `phone` strings and document references.

## Inputs → Outputs
- **In:** `domain` (bare `example.com` or `example.com/path`; also accepts a file of domains or piped input)
- **Out:** a deduplicated list of archived URLs (`domain` leads), optionally the archived page bodies themselves (mineable for `document-id`, contact strings, `metadata-exif`)
- **Empty/negative result looks like:** an empty or near-empty `waymore.txt` — the domain has little/no archival footprint. That is a finding (new/obscure/never-crawled site), not a tool error; try alternate spellings, subdomains, or a longer date window.

## Gotchas & OpSec
- No login needed to run, but adding free API keys (URLScan, VirusTotal, Intelligence X) in the config unlocks more sources and higher limits.
- Mode B can download a lot of data and take a long time on big domains — scope with date and MIME filters first.
- Passive toward the target, but every source provider sees your queries; use a research IP if that matters.

## Overlaps ("do both")
- Pairs with `[[xnlinkfinder]]` — WayMore gathers the raw archived URLs/bodies, XnLinkFinder parses them into endpoints and parameters worth chasing.
- Pairs with `[[archive-org-downloader]]` — WayMore finds what a domain hosted; the downloader pulls full borrowable archive.org items when the lead is a scanned document rather than a web page.

## Trust & verifiability
`trust: community` — a well-regarded, actively maintained open-source project; treat every recovered URL as an archival claim to confirm against the original snapshot (each URL traces back to Wayback/URLScan/etc.).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | waymore |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → domain, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
