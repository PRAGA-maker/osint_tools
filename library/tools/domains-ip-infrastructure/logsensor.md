---
id: logsensor
name: LogSensor
description: Use when you have a `domain`/host list and want to find its login panels — returns discovered login-page URLs (with an optional, authorised-only SQLi form check).
url: https://github.com/Mr-Robert0/Logsensor
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Enumerating login/admin panels across one or many hosts from the command line.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source (GPL-3.0) Python tool on GitHub; only the runtime dependencies (BeautifulSoup4, requests, termcolor, tabulate) are needed.
opsec: active
opsecNote: This connects directly to the target hosts to fetch pages and forms, so the target's server logs your requests. The optional `--sqli` mode actively probes login forms for SQL injection — that is intrusive testing and must only be run against systems you are explicitly authorised to test. For panel discovery alone, route through a proxy and use the login-detection mode without SQLi.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Community-maintained GitHub project (Mr-Robert0), ~500+ stars, GPL-3.0; audit the code before running as with any offensive tool.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Logsensor
tags:
- Domain/IP/Links
- Dorks/Pentest/Vulnerabilities
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# LogSensor

> A Python CLI that hunts for login/admin panels across a host or a whole list of hosts — with an optional, authorised-only SQL-injection probe of the forms it finds.

## When to use
You have a `domain` (or a file of subdomains/hosts) and want to locate its login and admin panels — a common step when mapping a target's attack surface or finding the authenticated entry points of a site suite. Its multiprocessed scan makes it practical over large host lists. The SQLi mode is a pentest capability, not general OSINT — use it only under authorisation.

## How to use it (`bestInteractionPattern`: cli)
1. `git clone https://github.com/Mr-Robert0/Logsensor` and `pip install -r requirements.txt`, then run the install script.
2. Login-panel discovery over a list: `python3 logsensor.py -f subdomains-list` (tune threads, default 30).
3. Single host: `python logsensor.py -u www.example.com/login`.
4. (Authorised only) form SQLi check: `python logsensor.py -u www.example.com/login --sqli`, optionally `--proxy http://127.0.0.1:8080`.
5. Pivot: discovered panels feed further recon of the same `domain`; found technologies feed a fingerprinter like [[w3techs]].

## Inputs → Outputs
- **In:** `domain` or a file of hosts/subdomains
- **Out:** discovered login-panel URLs (and, in SQLi mode, forms flagged as potentially injectable) — all tied to the input `domain`
- **Empty/negative result looks like:** no panels found — either the host exposes none on the paths checked, blocks the scanner, or hides them behind non-standard routes; absence is not proof there is no login.

## Gotchas & OpSec
- **Active and intrusive.** Requests hit the target directly and are logged; the `--sqli` mode performs vulnerability testing that is illegal without permission. Only test systems you own or are authorised to assess.
- Run behind a proxy/sock-puppet infrastructure; expect WAFs/rate-limits to block or poison results.
- Audit the source before running any offensive third-party tool.

## Overlaps ("do both")
- Complements infrastructure fingerprinters like [[w3techs]] — LogSensor finds the login surface, a fingerprinter tells you the stack behind it; together they scope a `domain`'s footprint.

## Trust & verifiability
`trust: community` — open-source and inspectable, but unofficial and offensive; the results (panels found, injectability flags) must be verified by hand and used only within an authorised engagement.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | logsensor |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
