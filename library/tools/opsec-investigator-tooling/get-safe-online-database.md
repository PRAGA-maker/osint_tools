---
id: get-safe-online-database
name: Get Safe Online
description: Use as a reference when you need to understand or explain a scam/fraud typology (romance, investment, phishing) — a public advice library, not a lookup tool.
url: https://www.getsafeonline.org
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Reference library on online scams, fraud types, and safety guidance for briefing victims/families.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free public-education resource; no account, no paid tier.
opsec: passive
opsecNote: Reading advice articles is entirely passive — no query about any target, nothing logged beyond a normal site visit. This is background/reference material, not an investigative data source, so it neither exposes you nor returns subject data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: UK-based public-awareness initiative backed by government and industry partners; authoritative for safety guidance, but it holds advice, not searchable records.
missingPersonsRelevance: low
coverage:
- uk
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- getsafeonline.org
- Get Safe Online
tags:
- fraud-awareness
- reference
- toddington
- curated-directory
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# Get Safe Online

> A public online-safety advice library — reference material for recognizing and explaining scam and fraud typologies, not a searchable OSINT database.

## When to use
Not a selector-transform tool. Reach for it as *reference* when an investigation touches online fraud and you need to understand or explain a scam pattern — romance scams, investment/crypto fraud, phishing, sextortion, account takeover. Useful for briefing a victim or a missing person's family on how a scam likely worked, or for recognizing the hallmarks of a fraud in the evidence you're reviewing.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.getsafeonline.org.
2. Browse or search the guidance sections (safeguarding topics, scam types, protection how-tos).
3. Read the relevant article to understand the typology, common red flags, and recommended protective/reporting steps.
4. Use it to frame your analysis or advise a subject/family; route actual fraud reports to the appropriate national body (e.g. Action Fraud in the UK).

## Inputs → Outputs
- **In:** none (a topic/query into an advice library — no OSINT selector)
- **Out:** educational guidance on scams, fraud, and online safety (no subject data)
- **Empty/negative result looks like:** a topic not covered — it's a curated advice site, not exhaustive; consult law-enforcement or specialist fraud resources for anything it lacks.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive reference reading; nothing about a target is queried.
- It provides advice, not data — don't expect lookups, records, or search of any person/entity here.

## Overlaps ("do both")
- Complements official fraud-reporting portals and threat/scam databases — Get Safe Online explains the typology, while reporting bodies and scam-tracker tools handle the actual case data.

## Trust & verifiability
`trust: trusted` — an established UK public-awareness initiative with government and industry backing, authoritative for safety guidance. Just remember its role is educational reference, not an investigative source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | get-safe-online-database |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
