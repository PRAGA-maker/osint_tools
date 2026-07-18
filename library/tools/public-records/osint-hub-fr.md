---
id: osint-hub-fr
name: OSINT-HUB-FR
description: Use when investigating a France-linked subject and you need French-focused tools, sources and methods — a curated directory pointing to other resources.
url: https://github.com/Anadema/OSINT-HUB-FR
category: public-records
path:
- public-records
bestFor: A curated French/international OSINT resource hub — tools, methodologies and guides, especially for France-focused investigations.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (GitHub); no account needed.
opsec: passive
opsecNote: A static reference repository — reading it touches no target and reveals nothing. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-maintained French OSINT hub (Anadema); a directory of methods and links, not a data source — vet each linked resource independently.
missingPersonsRelevance: medium
coverage:
- fr
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- osint-kit-buddhsen-tripathi
aliases:
- OSINT-HUB-FR
- Anadema/OSINT-HUB-FR
tags:
- meta-resource
- france
- tool-directory
source: gh-topic-osint-resources
lastVerified: '2026-07-18'
enrichment: full
---

# OSINT-HUB-FR

> A curated, actively maintained hub of French and international OSINT resources — the place to find France-specific tools, sources, and methodology when a case has a French dimension.

## When to use
Your subject or case touches France (French names, registries, telecoms, social platforms, or documents) and you want resources tuned to that context rather than generic global lists. OSINT-HUB-FR gathers tools, step-by-step methods, training, challenge platforms, and community links (bilingual FR/EN) aimed at students and investigators. It is a **directory/methodology hub** — it points you to resources; the actual data comes from whatever tool you then use.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the GitHub repo (github.com/Anadema/OSINT-HUB-FR) and browse the categorised sections.
2. Find the France-relevant tools/sources or the methodology/guide for your task.
3. Follow to the specific resource and cross-check it against this library's authored skills where they overlap.
4. Note the community links (e.g. OSINTFR Discord) for region-specific help.
5. Pivot: it routes you to French registries, telecom, and social tools — the selectors/outputs come from those, not from the hub.

## Inputs → Outputs
- **In:** (none — a browsable directory, not a query tool)
- **Out:** pointers to France-focused (and international) OSINT tools, methods, and communities
- **Empty/negative result looks like:** the niche you need isn't covered or a link has rotted — fall back to this library's index and broader awesome-lists.

## Gotchas & OpSec
- A **directory/guide**, not a tool — it produces no intelligence itself; verify each linked resource independently and mind French/EU legal (GDPR) constraints it flags.
- Curation reflects its maintainers' choices; not exhaustive.
- OpSec: passive reading; nothing disclosed.

## Overlaps ("do both")
- Complements `[[osint-kit-buddhsen-tripathi]]` and this library — use OSINT-HUB-FR for the France-specific angle and methodology, then the authored skills here for operational detail (opsec, selectors, trust).

## Trust & verifiability
`trust: community` — a community-curated hub; trust flows from the primary resources it links to, so evaluate each destination on its own before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-hub-fr |
| category | public-records |
| selectorsIn → selectorsOut | (none) → (directory of resources) |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
