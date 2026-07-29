---
id: awesome-privacy
name: awesome-privacy
description: Use when you need a privacy-respecting alternative to a mainstream tool/service for your own investigative opsec — returns a curated directory of vetted alternatives.
url: https://github.com/Lissy93/awesome-privacy/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Choosing privacy-respecting software/services to harden your own investigator opsec.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free/open-source curated list (GitHub + awesome-privacy.xyz); the listed tools have their own pricing.
opsec: passive
opsecNote: Passive — it's a reference directory; you consult it, you don't query any subject. Its value is defensive: picking browsers, VPNs, DNS, email and search tools that reduce your own footprint during investigations.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-known community-maintained "awesome" list by Alicia Sykes (Lissy93); entries are opinionated recommendations, not audits.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- personal-security-checklist
aliases:
- awesome-privacy.xyz
- Lissy93 awesome-privacy
tags:
- related-awesome-lists
- privacy
- opsec
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# awesome-privacy

> A large curated directory of privacy-respecting software and services — a go-to reference for hardening your own operational security.

## When to use
You want to run investigations without leaking your identity/footprint and need a vetted alternative to a data-harvesting mainstream product: a private browser, search engine, VPN, DNS resolver, email provider, note app, or messaging tool. awesome-privacy organises hundreds of such alternatives by category with descriptions and caveats. It is an opsec/reference resource, not a data source — it produces no OSINT selectors.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the repo (github.com/Lissy93/awesome-privacy) or the web version at awesome-privacy.xyz.
2. Browse to the relevant section (Essentials, Communication, Networking, Security Tools, etc.).
3. Read each entry's description, "notable mentions," and any security warning.
4. Pick an alternative and configure it as part of your sock-puppet/opsec setup.
5. Pivot: use the chosen tools (private browser/VPN/search) when running the rest of the library's active-collection tools.

## Inputs → Outputs
- **In:** a category/need ("private search engine", "VPN") — no OSINT selector
- **Out:** vetted alternative tools with descriptions and caveats
- **Empty/negative result looks like:** a category with only heavily-caveated options — read the warnings; "recommended here" is an opinion, not a guarantee.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: this is the opsec resource — its purpose is to improve yours. Still vet each tool yourself; the list is curated opinion, not an audit.
- Recommendations change; check the entry's freshness and the tool's current status before adopting.

## Overlaps ("do both")
- Complements `[[personal-security-checklist]]` (also by Lissy93) — the checklist tells you what habits to adopt, awesome-privacy tells you which tools to adopt them with.

## Trust & verifiability
`trust: community` — a reputable, widely-used community list, but entries are curated recommendations; independently verify a tool's security claims before relying on it for sensitive work.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | awesome-privacy |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
