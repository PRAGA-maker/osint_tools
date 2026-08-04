---
id: security-list
name: Security_list (zbetcheckin)
description: Use when you need to find a tool or resource for a security/OSINT task — returns a large curated GitHub directory of security and OSINT tools, blogs, and datasets.
url: https://github.com/zbetcheckin/Security_list
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: A broad, curated index of information-security and OSINT resources to find the right tool/reference for a task.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, open GitHub repository; no account needed.
opsec: passive
opsecNote: Reading a resource list is passive — you query no target. OpSec depends entirely on which linked tool you then choose and how you use it; assess each tool separately.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing, popular community "awesome"-style list (zbetcheckin); curation is opinionated and links can rot, so treat it as a discovery index, not an endorsement of each entry.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Security_list
- zbetcheckin security list
tags:
- related-awesome-lists
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# Security_list (zbetcheckin)

> A big, curated GitHub index of security and OSINT resources — the place to browse when you know the *kind* of tool you need but not its name.

## When to use
This is a discovery reference, not a lookup. Reach for it when you have a task ("I need a subdomain tool", "a malware sandbox", "a breach dataset", "an OSINT blog to learn from") and want a vetted starting shortlist rather than a blind web search. It aggregates tools, learning resources, blogs and datasets across many security/OSINT sub-areas.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/zbetcheckin/Security_list.
2. Use the README's section headings (or the browser's find) to jump to the relevant category.
3. Pick candidate tools/resources from the curated links.
4. Evaluate each candidate on its own page — is it live, free, maintained, appropriate?
5. Pivot: take the chosen tool into your workflow; for OSINT-specific automation, cross-reference [[apis-for-osint]].

## Inputs → Outputs
- **In:** none (you bring a task/need, not a subject selector)
- **Out:** curated links to tools, resources, blogs and datasets — pointers, not data about a person
- **Empty/negative result looks like:** no entry for a niche need, or a linked resource that has since moved/died — lists lag reality, so verify each link is current.

## Gotchas & OpSec
- **A pointer, not a source:** it returns no investigative data; every real capability lives in the linked tool, which you must vet yourself.
- Curated lists rot — expect some dead links and dated entries; check the tool's own repo/site for current status.

## Overlaps ("do both")
- Sits alongside other curated indexes and toolkits — for OSINT APIs specifically, [[apis-for-osint]] is more focused; use this one for broader security tooling.

## Trust & verifiability
`trust: community` — a reputable, widely referenced community list, but it endorses breadth over vetting; confirm any specific tool's provenance and maintenance before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | security-list |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
