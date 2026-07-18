---
id: justia-us-supreme-court-center-united-states
name: Justia US Supreme Court Center
description: Use when you have a `name` or `employer-org` and want to check US Supreme Court case law — returns full opinions where they appear as a party, counsel, or subject.
url: https://supreme.justia.com/
category: public-records
path:
- public-records
bestFor: Free full-text search and reading of US Supreme Court opinions to find where a person or organization appears as a party or is discussed.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
status: live
pricing: free
costNote: Free to search and read full opinions; no account. Justia is ad-supported with paid products elsewhere, but the Supreme Court Center is free.
opsec: passive
opsecNote: You search Justia's public case-law library, not a target — the lookup is invisible to anyone named in a case. No login; standard research-browser hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Justia is a long-established free legal-information provider; Supreme Court opinions are reproduced from the public record. It is a secondary host — for citation-critical work, confirm against the official U.S. Reports.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- justia-blawgsearch
aliases:
- Justia Supreme Court
- supreme.justia.com
tags:
- toddington
- curated-directory
- legal
- case-law
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Justia US Supreme Court Center

> A free, full-text library of US Supreme Court opinions (1791–present) — search by party name, topic, or citation and read the complete decisions.

## When to use
Your subject may have been party to, or named in, a US Supreme Court case — as a litigant, an organization, counsel, or because their conduct/case reached the Court. Searching a `name` or `employer-org` here surfaces the full opinion text, which can confirm involvement in landmark litigation, reveal an organization's legal history, or provide authoritative narrative facts about an event. It's a narrow but authoritative slice: SCOTUS only (for lower courts, use CourtListener/PACER/Justia's other centers).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://supreme.justia.com/ and use the search for a `name`, `employer-org`, topic, or citation.
2. Browse results — cases are listed by name and year; open one for the full opinion text.
3. Read the caption for parties and counsel, and the opinion body for the facts and holding.
4. Note the citation (e.g. "576 U.S. 644") to cross-reference elsewhere.
5. Pivot: parties/counsel `name`s → people/firm research; an `employer-org` party → its litigation history and corporate records; cited lower-court history → CourtListener/PACER for the fuller docket.

## Inputs → Outputs
- **In:** `name` / `employer-org` / topic / citation
- **Out:** full Supreme Court opinions naming parties, counsel, and `employer-org`s
- **Empty/negative result looks like:** no matching cases — the subject was never a party at the Supreme Court level (the vast majority of litigation never reaches SCOTUS); check lower-court databases instead.

## Gotchas & OpSec
- **SCOTUS only** — a tiny fraction of cases; absence here says nothing about lower-court or state-court involvement.
- Justia is a free secondary host; for citation-critical or evidentiary use, verify against the official U.S. Reports / court source.
- Common names produce unrelated matches — confirm identity via case facts and dates.
- Fully passive and anonymous.

## Overlaps ("do both")
- Complements CourtListener/RECAP, PACER, and state court portals for the far larger body of lower-court cases, and `[[justia-blawgsearch]]` for legal commentary — use this for the SCOTUS layer specifically.

## Trust & verifiability
`trust: trusted` — reproduces public-record Supreme Court opinions faithfully and is widely relied upon; for formal citation, confirm the text against the official U.S. Reports.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | justia-us-supreme-court-center-united-states |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → name, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
