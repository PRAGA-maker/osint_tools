---
id: cornell-legal-information-institute-united-states
name: Cornell Legal Information Institute (United States)
description: Use when you have a `name`, statute cite, or legal topic and want authoritative free US law and court opinions — returns document-id, name.
url: http://www.law.cornell.edu
category: public-records
path:
- public-records
bestFor: Reading the actual text of US federal/state law and Supreme Court opinions for free, and finding the parties/citations in reported cases.
selectorsIn:
- name
selectorsOut:
- document-id
- name
status: live
pricing: free
costNote: Free public-service resource operated by Cornell Law School; no account or payment. Funded by donations/sponsorship.
opsec: passive
opsecNote: Passive reading of published law and public court opinions — nothing here contacts or notifies any subject. No login, no trail beyond normal web browsing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by Cornell Law School since the early web; a long-standing, authoritative free mirror of US primary law and the Wex legal encyclopedia.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- lexcraft-cornell-university-legal-wiki-canada
aliases:
- Cornell LII
- Legal Information Institute
- law.cornell.edu
- Wex
tags:
- toddington
- legal
- public-records
source: toddington-resources
lastVerified: '2026-07-16'
enrichment: full
---

# Cornell Legal Information Institute (United States)

> Cornell Law School's free primary-law library: the authoritative text of US statutes, regulations, and Supreme Court opinions, plus the Wex encyclopedia.

## When to use
You need the *actual law* behind an investigation — the exact wording of a federal statute or regulation, a Supreme Court or appellate opinion, or a plain-language explainer — for free and without a Westlaw/Lexis subscription. In a person-centric case it is a supporting resource: read the statute a subject is charged under, pull a reported opinion that names them as a party (surfacing a `name` and the citation `document-id`), or understand the legal framework governing a records request. It is context/primary-source, not a people-finder.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.law.cornell.edu and use the search box, or browse the collections: U.S. Code, CFR, U.S. Constitution, Supreme Court opinions, the federal Rules, state law by topic, and the UCC.
2. To read a specific provision, navigate the U.S. Code / CFR tree; to understand a term, open its **Wex** article.
3. For case law, search a party name or citation; reported opinions list the parties, court, date, and full text.
4. Pivot: a citation (`document-id`) feeds deeper case-law tools (CourtListener/PACER); a statute cite frames what public records exist; a named party feeds people/court-records search.

## Inputs → Outputs
- **In:** a legal `name` (party), statute/case citation, or legal topic
- **Out:** `document-id` (statute/regulation/case citations and full text) and, in opinions, party `name`s
- **Empty/negative result looks like:** no results for a party name — LII is not a comprehensive docket search; most trial-level filings and unreported cases won't appear (use CourtListener/PACER for those).

## Gotchas & OpSec
- Human-in-the-loop: none; free public site.
- OpSec: **passive** — reading published law.
- LII's strength is *primary law and famous opinions*, not exhaustive case coverage. It won't surface routine local filings or return anyone's address — treat it as legal context, not a person database.

## Overlaps ("do both")
- Do both with a docket/case-law search engine (CourtListener/PACER) — LII gives you the authoritative statute or landmark opinion text; the docket tools give you the filings and parties LII doesn't index.

## Trust & verifiability
`trust: trusted` — a decades-old Cornell Law School public service mirroring official primary law; text is authoritative and citeable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cornell-legal-information-institute-united-states |
| category | public-records |
| selectorsIn → selectorsOut | name → document-id, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
