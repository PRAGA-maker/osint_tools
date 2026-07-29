---
id: webpalm
name: WEBPALM
description: Use when you have a `domain` and want to map its full page tree and regex-scrape content from it — returns discovered URLs/paths and extracted strings for further pivoting.
url: https://github.com/XORbit01/webpalm
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Crawling a target website into a structured tree and pulling out emails/links/comments via custom regex.
selectorsIn:
- domain
selectorsOut:
- domain
- email
status: live
pricing: free
costNote: Free and open-source (Go); no account or key.
opsec: active
opsecNote: WebPALM actively crawls the target site — every page it visits hits the subject's server and appears in their logs (your IP, user-agent, request timing). Use a VPN/sock-puppet egress and throttle worker count if you don't want to be conspicuous.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: Single-maintainer open-source project (formerly Malwarize/webpalm, now XORbit01/webpalm); popular but community-maintained, no formal audit.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- webpalm
- Malwarize/webpalm
tags:
- Domain/IP/Links
- Website analyze
- web-crawler
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# WEBPALM

> A Go command-line crawler that turns a website into a page tree and lets you regex-extract anything (emails, comments, links) from every page it touches.

## When to use
You have a `domain` (a subject's personal site, blog, or small business page) and want to enumerate its structure and harvest artefacts — contact emails, hidden paths, embedded links to other profiles, HTML comments — rather than reading it page by page. Best when the site is small enough to crawl politely and you specifically want machine-extracted output to feed the next pivot.

## How to use it (`bestInteractionPattern`: cli)
1. Install (Go required): `go install github.com/XORbit01/webpalm/v2@latest` (or clone and `go build -o webpalm`).
2. Map the site to depth 2: `webpalm -u https://example.com -l2 -o results.json`.
3. Extract with a custom regex, e.g. emails: `webpalm -u https://example.com -l2 --regexes emails="[\w.]+@[\w.]+" -o out.json`.
4. Throttle with workers for larger sites: `-w 20` (fewer workers = quieter, slower).
5. Pivot: feed extracted `email` addresses into email-OSINT tools and any newly-found `domain`/subdomain links into infrastructure lookups.

## Inputs → Outputs
- **In:** `domain` (target URL) + crawl depth + optional regex patterns
- **Out:** JSON/XML/TXT tree of discovered pages (`domain`/paths) and regex-matched strings (e.g. `email`)
- **Empty/negative result looks like:** a tree with only the root node and no regex hits — the site is a single page, blocks crawlers, or your depth/regex was too narrow.

## Gotchas & OpSec
- **Active** — this is direct contact with the subject's server; it is logged. Do not run it from an attributable IP against a sensitive target.
- Respect scope: crawling depth grows fast; a high `-l` on a large site is noisy and slow.
- It follows links as written; JS-rendered sites may expose little to a static crawler.

## Overlaps ("do both")
- Complements passive WHOIS/reverse-IP tools: those tell you *who hosts* the domain without touching it, WebPALM tells you *what is on the pages* but at the cost of active contact — do the passive lookups first, crawl only if needed.

## Trust & verifiability
`trust: unverified` — open-source and inspectable, but a single-maintainer community tool; the code moved orgs (Malwarize → XORbit01), so verify you are installing from the current repo before running.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | webpalm |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, email |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
