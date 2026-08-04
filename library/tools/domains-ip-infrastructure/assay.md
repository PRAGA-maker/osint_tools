---
id: assay
name: ASSAY
description: Use when you have a `domain`/URL and want a one-stop inspection — returns subdomains, WHOIS, GeoIP, DNS, headers, archives, cookies and phishing/malware reputation.
url: https://d09r.github.io/assay-url-inspection-tools/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: A single browser-extension dashboard bundling WHOIS, DNS, subdomains, GeoIP, headers, archives and reputation for any URL.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
- geolocation
status: live
pricing: free
costNote: Free browser extension (Chrome/Edge/Firefox); donation-supported via the author's Patreon. No account.
opsec: passive
opsecNote: Most checks (WHOIS, DNS, archives, reputation feeds) are passive lookups against third parties. The "live web requests" / page-source features fetch the target itself — that portion is active, so use a sock-puppet profile when inspecting a hostile site.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: unverified
trustNote: Maintained by a single independent developer (#d09r); convenient aggregator, but each result comes from an underlying third-party service whose accuracy it inherits.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Assay URL Inspection
- d09r Assay
tags:
- Domain/IP/Links
- Searchers, scrapers, extractors, parsers
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# ASSAY

> A browser-extension "swiss army knife" for URLs — WHOIS, DNS, subdomains, GeoIP, headers, archives, cookies and reputation, all from one panel.

## When to use
You have a `domain` or URL (a suspicious link, a target's site, a phishing lure) and want a fast all-in-one profile without opening a dozen separate services. Good as a first-pass triage that then tells you which specialised tool to drill into.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the ASSAY extension from https://d09r.github.io/assay-url-inspection-tools/ (Chrome/Edge/Firefox).
2. On the target page (or by entering a URL), open the panel and pick a module: WHOIS, subdomains/connected domains, GeoIP, DNS, headers, archives, cookies, reputation.
3. Read the aggregated results; note the `ip-address`, hosting `geolocation`, and any subdomains for pivoting.
4. Follow up in a dedicated tool (passive DNS, full WHOIS history) for anything load-bearing.

## Inputs → Outputs
- **In:** `domain` / URL
- **Out:** subdomains/connected `domain`s, `ip-address`, hosting `geolocation`, WHOIS, DNS, headers, archives, reputation verdicts
- **Empty/negative result looks like:** a module returns nothing (no subdomains found, no archive) — a gap in the underlying feed, not proof of absence; confirm with a second source.

## Gotchas & OpSec
- Human-in-the-loop: none, but it is a browser extension you must install and trust.
- OpSec: mostly passive; the live-request/page-source features touch the target directly — sandbox those against hostile sites.
- It aggregates third-party services — results are only as good/current as those upstreams.

## Overlaps ("do both")
- A convenience front-end over many tools: use ASSAY to triage quickly, then `[[haklistgen]]`-style recon or dedicated passive-DNS/WHOIS-history tools for depth.

## Trust & verifiability
`trust: unverified` — a handy single-dev aggregator; treat its output as pointers and verify critical findings against the primary services it wraps.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | assay |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address, geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
