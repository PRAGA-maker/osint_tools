---
id: the-time-machine
name: TheTimeMachine
description: Use when you have a `domain` and want historical intel from the Wayback Machine — CLI that harvests archived subdomains, URLs, parameters and sensitive endpoints for recon.
url: https://github.com/anmolksachan/TheTimeMachine
category: archives-cache
path:
- archives-cache
bestFor: Mining the Wayback Machine at scale for a domain's historical subdomains, URLs, parameters, and exposed/sensitive endpoints (recon).
selectorsIn:
- domain
selectorsOut:
- domain
- document-id
status: live
pricing: free
costNote: Free, open-source Python CLI; no cost beyond running it yourself.
opsec: passive
opsecNote: It pulls from the Wayback Machine / archive APIs, not the live target, so recon is passive — the target's server isn't touched. If you then visit any discovered endpoint directly, that request hits the target; do that from a sock-puppet IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A community-published OSINT/recon script (by anmolksachan); it automates public Wayback data, so results are as reliable as the archive itself — verify sensitive findings before acting.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- TheTimeMachine
- anmolksachan TheTimeMachine
tags:
- Archives
- Tools for working with web archives
- recon
- wayback
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# TheTimeMachine

> A CLI that squeezes the Wayback Machine for a `domain`'s history — archived subdomains, URLs, parameters, and endpoints that a site has since removed but the archive still remembers.

## When to use
You're mapping a `domain`'s attack/OSINT surface and want what it *used* to expose: old subdomains, forgotten pages, URL parameters, and sensitive endpoints (config/JSON/API paths) captured by the Wayback Machine before they were taken down. Great for uncovering infrastructure and content that no longer appears on the live site but persists in the archive.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo: `git clone https://github.com/anmolksachan/TheTimeMachine` and install Python requirements.
2. Run it against the target `domain` (per the repo's usage), e.g. to fetch archived URLs/subdomains.
3. It harvests waybackurls, extracts subdomains, and greps for interesting patterns (e.g. `/api/`, JSON/config endpoints, parameters).
4. Review the output for historical subdomains and any exposed/sensitive paths.
5. Confirm live status of anything interesting by checking it directly (from a sock-puppet IP) or via a current archive snapshot.
6. Pivot: discovered subdomains feed DNS/infra mapping; archived endpoints/parameters feed deeper investigation.

## Inputs → Outputs
- **In:** `domain`
- **Out:** archived subdomains, URLs/parameters, and sensitive-endpoint (`document-id`-style) references from the Wayback Machine
- **Empty/negative result looks like:** the domain has few/no archived captures — a young, low-traffic, or archive-excluded site yields little. Absence in the archive isn't proof the paths never existed.

## Gotchas & OpSec
- Data is *historical* — archived endpoints may be dead now; verify before relying on them.
- Depends on Wayback coverage; sparse for obscure domains.
- Passive against the target during harvesting; only direct visits to discovered paths touch the target's server.

## Overlaps ("do both")
- Pairs with waybackurls/gau and live subdomain-enumeration tools — this focuses on Wayback history, while active enumeration finds what's currently live; together they compare past vs present surface.

## Trust & verifiability
`trust: community` — an open-source recon script over authoritative Wayback data; the archive itself is verifiable, so cross-check any sensitive endpoint against the live site or a fresh snapshot before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-time-machine |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → domain, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
