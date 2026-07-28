---
id: ndorker
name: nDorker
description: Use when you have a `domain` and want an automated dorking sweep — returns Google/GitHub/Shodan/vendor dork results exposing exposed assets and info.
url: https://github.com/nerrorsec/nDorker
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Automating Google, GitHub, Shodan, and vendor dorking against a target domain.
selectorsIn:
- domain
selectorsOut:
- domain
- email
status: live
pricing: free
costNote: Free and open source (Python CLI); some engines may need free API keys (e.g. Shodan).
opsec: active
opsecNote: The dorks run against live search engines and services (Google, GitHub, Shodan). You are not touching the target's own servers, but the queries are logged by those platforms and can be rate-limited/blocked — run from a puppet environment and mind API-key attribution.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: An open-source community tool (nerrorsec, ~200+ stars); auditable, but a small project — treat it as a convenience automator over well-known dork techniques.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- nDorker
- Google-Dorker
- nerrorsec/nDorker
tags:
- Domain/IP/Links
- Dorks/Pentest/Vulnerabilities
- dorking
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# nDorker

> A Python CLI that automates dorking against a `domain` — fires Google, GitHub, Shodan, and vendor dorks to surface exposed files, credentials, subdomains, and services.

## When to use
You have a `domain` and want to quickly enumerate what's publicly exposed about it via search-engine dorks — leaked documents, config files, API keys in code, indexed subdomains, exposed hosts — without hand-crafting each dork. nDorker batches the common dork categories into one run.

## How to use it (`bestInteractionPattern`: cli)
1. Clone https://github.com/nerrorsec/nDorker and install its Python dependencies.
2. Add any API keys the engines need (e.g. Shodan).
3. Run: `python3 nDorker.py -d example.com`.
4. Work through the results per category — Google, GitHub, Shodan, vendor (Codepad/Codepen/etc.) dorks.
5. Pivot: exposed subdomains feed passive-DNS mapping; leaked `email`s feed email-OSINT; exposed hosts feed [[checkip]]/Shodan review.

## Inputs → Outputs
- **In:** `domain`
- **Out:** dork hits — exposed `domain`s/subdomains, indexed files, leaked `email`s/credentials, exposed services
- **Empty/negative result looks like:** few or no hits — either a well-secured target or (often) search engines rate-limiting/blocking automated dork queries; re-run slowly or dork manually.

## Gotchas & OpSec
- Automated dorking gets rate-limited or CAPTCHA'd fast — Google especially blocks scripted queries; expect partial results.
- Queries are logged by the engines and tied to your IP/API keys — use a puppet environment.
- It automates known techniques, not magic — manual, targeted dorks often beat it for a specific goal.
- Only as current as the search engines' indexes.

## Overlaps ("do both")
- Pairs with subdomain-enumeration and Shodan/passive-DNS tools — nDorker casts a wide dork net, while those go deep on the assets it surfaces.

## Trust & verifiability
`trust: community` — open-source and auditable, but a small automator whose output is entirely the search engines' index data; verify each hit directly before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ndorker |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, email |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
