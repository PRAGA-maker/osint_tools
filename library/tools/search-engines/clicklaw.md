---
id: clicklaw
name: Clicklaw
description: Use when you need plain-language British Columbia / Canadian legal context and want to understand a process or your rights — returns curated legal explainers, not personal records.
url: https://wiki.clicklaw.bc.ca
category: search-engines
path:
- search-engines
bestFor: Understanding a BC or Canadian legal process (family, employment, criminal, seniors, Indigenous law) in plain language before pursuing records.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, publicly funded legal-information wiki; no account or payment.
opsec: passive
opsecNote: Passive — reading static public wiki pages. No query touches any subject and there is nothing to leak; standard clean-browser hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Courthouse Libraries BC with the Law Foundation of BC, Law Society of BC, and the BC Ministry of Attorney General; authored by 50+ legal professionals and non-profits.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- cso
- search-for-open-information-documents
- search-the-open-information-catalogue
- security-licence-status-verification
aliases:
- Clicklaw Wikibooks
- wiki.clicklaw.bc.ca
tags:
- toddington
- curated-directory
- legal-information
- canada
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Clicklaw

> A free, plain-language legal-information wiki for British Columbia and Canada — a reference for understanding process and rights, not a people- or records-search engine.

## When to use
You need to understand the *legal framework* around a case in BC or Canada — how family, employment, criminal, seniors', or Indigenous-law matters work — so you can figure out which records exist, which authority holds them, and what rights govern access. Reach for it as background before hitting an actual records source (courts, licence registries), not to look up a specific person. Its OSINT value is orientation and terminology, not selectors.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://wiki.clicklaw.bc.ca.
2. Browse or search the Wikibooks (e.g. "Legal Information for Indigenous People", family-law guides, employment/criminal manuals).
3. Read the plain-language explainer to identify the governing statute, the responsible body, and the correct process.
4. Pivot: use that context to target the right records tool — e.g. BC's court-record search `[[cso]]` or an open-information catalogue for the actual filings.

## Inputs → Outputs
- **In:** a legal question or topic (no personal selector)
- **Out:** curated legal explainers, procedural guides, and pointers to the right authority
- **Empty/negative result looks like:** a topic outside BC/Canadian law, or a request for a specific person's record — Clicklaw holds neither; it only explains process.

## Gotchas & OpSec
- **Not a records database.** It will never return a name, address, or case file — it explains how the system works.
- BC-centric; only some content (e.g. the Indigenous-law national edition) generalizes across Canada.
- Fully passive: nothing you read is logged against a subject.

## Overlaps ("do both")
- Pairs with `[[cso]]` and `[[search-the-open-information-catalogue]]` — Clicklaw tells you *which* record and authority to target, and those tools retrieve the actual document.

## Trust & verifiability
`trust: trusted` — a Courthouse Libraries BC project backed by the Law Foundation of BC, the Law Society of BC, and the provincial Ministry of Attorney General, authored by named legal professionals; content is authoritative for its jurisdiction.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | clicklaw |
| category | search-engines |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
