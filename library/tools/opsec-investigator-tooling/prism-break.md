---
id: prism-break
name: PRISM Break
description: Use when you want anti-surveillance software alternatives (by platform) to harden your own investigative opsec — returns a curated directory of privacy tools.
url: https://prism-break.org/en/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Picking privacy/anti-surveillance software alternatives, organised by OS/platform.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, open-source directory (hosted on GitLab, community-maintained); listed tools have their own pricing.
opsec: passive
opsecNote: Passive — a reference directory; you consult it, you never query a subject. Its purpose is defensive: choosing tools that reduce your own footprint against mass-surveillance programs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running, actively-maintained community project (last updated Dec 2024) available in 28+ languages; recommendations are curated, not audits, and include a "no guarantee" disclaimer.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- prism-break.org
- PRISM-Break
tags:
- privacy
- opsec
- anti-surveillance
- directory
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# PRISM Break

> A curated, platform-organised directory of privacy and anti-surveillance software — a reference for hardening your own operational security.

## When to use
You want to opt out of mass-data-collection and pick privacy-respecting software for your investigator setup, organised by where you'll run it: Android/iOS, BSD/Linux/macOS/Windows, and network infrastructure (routers/servers). It's an opsec/reference resource, not a data source; it produces no OSINT selectors.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://prism-break.org/en/.
2. Navigate to your platform section (mobile OS, desktop OS, or network).
3. Read the recommended alternatives for each function (browser, messaging, email, DNS, etc.).
4. Choose and configure tools as part of your sock-puppet/opsec environment.
5. Pivot: use the selected privacy tools when running the library's active-collection tasks.

## Inputs → Outputs
- **In:** a platform/need — no OSINT selector
- **Out:** recommended privacy-respecting software alternatives
- **Empty/negative result looks like:** a category with only a few, heavily-caveated options — read the disclaimer; a listing is a suggestion, not a guarantee of protection.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: this is the opsec resource — its purpose is to improve yours. Still vet each tool independently; recommendations are curated opinion.
- The site itself disclaims that following it won't guarantee protection from surveillance — treat it as a starting point.

## Overlaps ("do both")
- Overlaps with `[[awesome-privacy]]` — both are privacy-tool directories; cross-reference them, as each organises and vets recommendations differently.

## Trust & verifiability
`trust: community` — a reputable, actively-maintained community list; entries are curated recommendations, so confirm a tool's current status and security claims before adopting it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | prism-break |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
