---
id: kraken
name: Kraken
description: Use when you have a set of `domain`/`ip-address` hosts to test and want to organise screenshots, notes and progress across a team — returns a self-hosted web-testing tracker/report.
url: https://github.com/Sw4mpf0x/Kraken
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- discovery
bestFor: Self-hosted workflow app for enumerating/inventorying web interfaces and tracking testing notes.
selectorsIn:
- domain
- ip-address
selectorsOut: []
status: degraded
pricing: free
costNote: Free/open-source; self-hosted (Django/Apache/MySQL, Dockerised). Cost is only your own hosting.
opsec: active
opsecNote: Active — capturing screenshots means fetching each target web interface, so requests reach the subject's servers and appear in their logs. Run from a research/VPN egress and only against systems you are authorised to test.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: docker
trust: unverified
trustNote: Community single-author project (~104 stars) that is largely inactive; ships with a default admin credential you must change on deploy.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Sw4mpf0x/Kraken
tags:
- web-enumeration
- pentest-workflow
- self-hosted
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# Kraken

> A self-hosted Django web app for enumerating web interfaces across a set of hosts and organising the screenshots, notes and reports a team produces.

## When to use
You have a list of `domain`/`ip-address` hosts (from earlier recon) and want a shared place to screenshot each web interface, record who tested what, take notes, and generate a report at the end. It is a testing-workflow/inventory tool for authorised assessment work — not a data source that discovers people or infrastructure on its own; relevance to missing-persons work is minimal.

## How to use it (`bestInteractionPattern`: docker)
1. Deploy it self-hosted — the recommended path is Docker (create a volume, run the container); a legacy clone-and-setup install also exists (Django on port 8000).
2. Log in and **immediately change the default admin credentials** shipped in the docs.
3. Add your target hosts; Kraken captures web-interface screenshots and lets the team annotate and mark progress.
4. Track testing status across hosts, then generate a report from the Reports section.
5. Pivot: this consumes recon output (hosts/URLs) and produces documentation — the discovery itself comes from other tools.

## Inputs → Outputs
- **In:** `domain`/`ip-address` hosts (web interfaces to inventory)
- **Out:** organised screenshots, notes and reports (workflow artefacts, not OSINT selectors)
- **Empty/negative result looks like:** hosts with no reachable web interface produce blank captures — a status result, not a finding.

## Gotchas & OpSec
- Human-in-the-loop: self-hosting + login required (`account-login`); rotate the default admin password on first run.
- OpSec: **active** — screenshotting fetches each target site; only run against authorised scope from a controlled egress.
- Status **degraded**: the project is largely unmaintained (old "quick start"); expect to do your own hardening and dependency fixes.

## Overlaps ("do both")
- Pairs with discovery tools like `[[webosint]]`/`[[jsleak]]` — those find and probe hosts; Kraken is where you organise and document the web interfaces you then review.

## Trust & verifiability
`trust: unverified` — a single-author, inactive project with a default credential; audit the code before self-hosting and treat it as an internal workflow aid, not an authoritative source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kraken |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → — |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | docker |
| opsec | active |
| human-in-loop | yes (account-login) |
