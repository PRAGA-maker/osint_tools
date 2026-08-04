---
id: investigator-recon-tool
name: Investigator Recon Tool
description: Use when you have a `domain` and want a fast one-page recon dashboard — returns related `domain`s, subdomains and open-source footprint via pre-built Google-dork and lookup links.
url: https://abhijithb200.github.io/investigator/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Kicking off domain recon with a menu of ready-made Google dorks and OSINT lookups.
selectorsIn:
- domain
selectorsOut:
- domain
- email
status: live
pricing: free
costNote: Free, open-source, hosted on GitHub Pages; no account or API key.
opsec: passive
opsecNote: The page itself just generates links and queries; it is client-side and does not phone home. But clicking through the generated Google dorks and third-party lookups is done from your own browser — those services (Google, Shodan, etc.) see your IP. Use a sock-puppet/VPN session if the target might monitor.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source project by security researcher Abhijith B (abhijithb200); a convenience launcher for public dorks, not a data source itself.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Investigator by abhijithb200
- investigator dork tool
tags:
- Domain/IP/Links
- Dorks/Pentest/Vulnerabilities
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Investigator Recon Tool

> A web-based recon launcher that takes one domain and hands you a menu of pre-filled Google dorks and OSINT lookups to run against it.

## When to use
You have a target `domain` and want to sweep its public footprint quickly — exposed subdomains, login/admin pages, indexed documents, leaked emails, third-party mentions — without hand-typing each `site:` dork. It's an orchestration front-end, not a scanner: it builds the queries; the answers come from Google and the linked services.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://abhijithb200.github.io/investigator/ on a desktop screen (it warns on small viewports).
2. Enter the target `domain` in the input field.
3. Pick a category (e.g. subdomains, files/documents, exposed pages, social/email) — the tool generates the corresponding Google dork or lookup link.
4. Click through to run each query; read the search results for subdomains, indexed PDFs/spreadsheets, exposed panels or `email` addresses tied to the domain.
5. Pivot: feed discovered subdomains into DNS/passive-DNS tooling, and any surfaced emails into email-OSINT lookups.

## Inputs → Outputs
- **In:** `domain`
- **Out:** related `domain`s / subdomains, indexed documents, occasionally `email` addresses (via the dorks it launches)
- **Empty/negative result looks like:** the generated Google searches return no results — meaning nothing is indexed for that dork, not that the asset doesn't exist. Try alternate dork categories before concluding.

## Gotchas & OpSec
- Human-in-the-loop: none in the tool itself; Google may throw a CAPTCHA if you fire many dorks rapidly.
- OpSec: **passive** — the page is static client-side JS, but every dork you click runs from your browser against Google/third parties, exposing your IP to them (not to the target's server unless a dork links to the target directly). Use a clean session for sensitive work.
- It's a link builder: coverage and quality depend entirely on what Google has indexed and on the underlying services, not on the tool.

## Overlaps ("do both")
- Complements dedicated subdomain and passive-DNS tools — this gives you the fast manual dork sweep; automated enumerators find hosts Google never indexed.

## Trust & verifiability
`trust: community` — an open-source convenience launcher by an individual researcher; it holds no data of its own, so trust the underlying Google/third-party results, not the tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | investigator-recon-tool |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, email |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
