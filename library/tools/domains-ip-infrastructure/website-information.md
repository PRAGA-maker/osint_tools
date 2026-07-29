---
id: website-information
name: Website Information
description: Use when you have a `domain`, `ip-address`, or `email` and want a bundled panel of website-research lookups — returns WHOIS, DNS, `geolocation`, headers, and tech profile.
url: https://one-plus.github.io/WebsiteInformation
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: A single free page linking many website/network lookups (WHOIS, DNS, IP geolocation, headers, tech stack) for quick domain triage.
selectorsIn:
- domain
- ip-address
- email
selectorsOut:
- ip-address
- geolocation
- domain
status: live
pricing: free
costNote: Free static toolkit hosted on GitHub Pages; it links out to third-party services (CentralOps, Robtex, etc.) that are themselves free for interactive use.
opsec: passive
opsecNote: The page is a set of links; each lookup runs on a third-party service, so the target isn't touched directly by you. As with any WHOIS/DNS tool, you're querying public records — the exception is any email-verification link, which may probe a mail server. Prefer the passive lookups.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-built link hub (GitHub Pages) that aggregates established third-party tools; trust each destination on its own merits.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- central-ops
- osint-toolkit
- bookmarks
- document-search
- google-and-bing
- instagram-reddit-and-snapchat
- twitter-monitoring
- youtube-periscope-twitch-and-dailymotion
aliases:
- WebsiteInformation toolkit
tags:
- domain-research
- whois
- toolkit
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Website Information

> A free GitHub-Pages hub that gathers website- and network-research lookups in one place — WHOIS, DNS, IP geolocation, headers/source, and technology profiling — routing you to the right third-party tool.

## When to use
You have a `domain`, `ip-address`, or `email` tied to a lead (a subject's site, a suspicious link, a message header) and want a quick, consolidated triage before deciding where to dig. It's a dashboard of links rather than a single engine, so reach for it when you want the common domain/IP lookups side by side without remembering each tool's URL. Infrastructure-oriented, so direct missing-person value is low, but registrant details and hosting `geolocation` can corroborate ownership or origin.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://one-plus.github.io/WebsiteInformation.
2. Pick the lookup you need: WHOIS (domain / IP / reverse), DNS report, IP geolocation, HTTP headers/source, technology profile, or TLD info.
3. Enter the `domain`, `ip-address`, or `email` in the relevant tool (some hand off to CentralOps, Robtex, etc.).
4. Read the results — registrant and dates from WHOIS, hosting country/city from geolocation, stack from the tech profile.
5. Pivot: a registrant `name`/`address` feeds people-search; a hosting `ip-address` feeds reverse-IP and subdomain enumeration.

## Inputs → Outputs
- **In:** `domain`, `ip-address`, or `email`
- **Out:** `domain` (WHOIS, DNS), `ip-address` (hosting, reverse), `geolocation` (hosting country/city), plus headers and detected technologies
- **Empty/negative result looks like:** privacy-redacted WHOIS or a dead third-party link — try the equivalent tool directly (e.g. `[[central-ops]]`) rather than assuming no data exists.

## Gotchas & OpSec
- It's a link hub: some destinations may rot or rate-limit; the underlying tool is the real source of truth.
- Hosting `geolocation` is the server's location, not the person's — don't confuse infrastructure with the subject's whereabouts.
- Passive for the WHOIS/DNS/geo lookups; be cautious with any email-verification link, which can touch a mail server.

## Overlaps ("do both")
- Overlaps `[[central-ops]]` (which several of its lookups call) and `[[osint-toolkit]]`; use this to discover the right lookup, then the dedicated tool for depth.

## Trust & verifiability
`trust: community` — a hobby aggregator of reputable third-party services; the data quality is that of whichever destination you land on, all of which surface verifiable public records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | website-information |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address, email → ip-address, geolocation, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
