---
id: robottester
name: robotstester
description: Use when you have a `domain` and want to pull every path listed in its robots.txt and see which are actually reachable — returns a tested list of disallowed/hidden URLs.
url: https://github.com/p0dalirius/robotstester
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Enumerating and access-testing the paths a site's robots.txt tries to hide from crawlers.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Open source under GPL-3.0; free Python CLI.
opsec: active
opsecNote: The tool fetches robots.txt and then requests each listed path directly from the target server, so every test appears in the site's access logs. Route through a proxy/VPN and only probe hosts you are authorised to test.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A small, auditable open-source script by researcher p0dalirius; does one narrow job and does it transparently.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- robotstester
- p0dalirius robotstester
tags:
- Domain/IP/Links
- Dorks/Pentest/Vulnerabilities
- robots-txt
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# robotstester

> A focused CLI that reads a site's robots.txt, extracts every path it tells crawlers to avoid, and then checks which of those "hidden" paths are actually reachable.

## When to use
You are mapping a `domain` and want the low-hanging fruit that a robots.txt often leaks: admin panels, staging areas, upload directories, and other paths the owner asked crawlers not to index. robotstester turns that Disallow list into a tested inventory of what actually responds, so you know which hinted paths are real and open.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `https://github.com/p0dalirius/robotstester` and install (Python).
2. Point it at a robots.txt (or a file of many): `robotstester -u https://target.com/robots.txt` (flags for threads, proxy, cookies, insecure SSL, redirects, JSON output).
3. Read the output: each Disallow/Allow path with an access-test result (reachable vs blocked). Use JSON output to pipe into other tooling.
4. Pivot: reachable "hidden" paths feed manual review and directory enumeration; a login/admin path feeds infrastructure and org OSINT.

## Inputs → Outputs
- **In:** a `domain`'s robots.txt URL (or a list of them)
- **Out:** the enumerated paths with per-path access results
- **Empty/negative result looks like:** robots.txt absent, empty, or all listed paths returning 403/404 — many sites have a trivial robots.txt, so a blank result is common and not a failure.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **active** — you request each path directly from the target, landing in its logs. Use a proxy/VPN, throttle threads, and only test authorised hosts.
- It only knows paths robots.txt names; it does not discover paths the file omits — pair with real directory brute-forcing for coverage.

## Overlaps ("do both")
- Pairs with the Wayback Machine and content-discovery tools — robots.txt reveals what the owner wanted hidden, archives reveal what once existed; together they reconstruct a site's non-obvious surface.

## Trust & verifiability
`trust: community` — a small, open-source, single-purpose script you can read end to end. Its results are direct HTTP responses from the target, so they are self-verifying (re-request to confirm).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | robottester |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
