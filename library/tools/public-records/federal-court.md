---
id: federal-court
name: Federal Court (Canada) Decisions
description: Use when you have a `name` and want to find Federal Court of Canada judgments and orders naming that party — returns case decisions, docket/citation IDs, and the legal context a person appears in.
url: https://decisions.fct-cf.gc.ca/fc-cf/en/d/s/index.do
category: public-records
path:
- public-records
bestFor: Searching Federal Court of Canada judgments for a person's name (immigration, judicial review, IP, federal matters).
selectorsIn:
- name
selectorsOut:
- name
- document-id
- associate
status: live
pricing: free
costNote: Free official government decisions database; no account or payment.
opsec: passive
opsecNote: Passive — you search a public court-decisions repository, not the subject. Parties are not notified of searches. Standard government-site logging applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official decisions portal of the Federal Court of Canada — authoritative primary-source case law, not a third-party aggregator.
missingPersonsRelevance: high
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- Federal Court of Canada decisions
- decisions.fct-cf.gc.ca
tags:
- court
- case-law
- canada
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Federal Court (Canada) Decisions

> The Federal Court of Canada's official judgment database — search by name to find federal court decisions (immigration, judicial review, IP, admiralty, federal boards) a person is named in.

## When to use
You have a `name` with a Canadian nexus and want to know whether they appear in Federal Court of Canada proceedings. The Federal Court hears immigration/refugee appeals, judicial reviews of federal decisions, IP, and admiralty — so this is especially valuable for immigration histories and for surfacing the legal context (and co-parties/counsel as `associate`s) around a subject. It complements provincial/criminal court sources, which this does not cover.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://decisions.fct-cf.gc.ca/fc-cf/en/d/s/index.do.
2. Enter the subject's `name` (full-text search; use quotes and try name variants/spellings).
3. Browse the result list of decisions; open a judgment to read the facts and parties.
4. Extract the neutral citation/docket (`document-id`), the parties, and named counsel/co-parties (`associate`s).
5. Pivot: an immigration decision can reveal nationality, arrival timeline, and locations; co-parties/counsel are further leads. Cross-check with CanLII for the same and related matters.

## Inputs → Outputs
- **In:** `name`
- **Out:** decision text, neutral citation/docket `document-id`, party names, sometimes locations/dates within the judgment, co-parties/counsel (`associate`)
- **Empty/negative result looks like:** no decisions match — meaning the person isn't named in a *reported Federal Court* judgment. That's narrow: it excludes provincial courts, criminal matters, and unreported/settled cases. Absence here is not "no legal history."

## Gotchas & OpSec
- Scope is the Federal Court only — not provincial superior/criminal courts, not tribunals' own sites. Use CanLII and provincial portals for broader coverage.
- Immigration/refugee matters are sometimes anonymised (initials only) for privacy — a subject may appear as "X.Y." and be unfindable by full name.
- Common names produce unrelated hits; confirm via case facts (dates, locations) before attributing.
- Passive and free; no login/captcha.

## Overlaps ("do both")
- Pairs with `[[parallelsearch-case-law]]` and general case-law search — this is the authoritative Federal Court source; aggregators widen coverage across courts.
- For incarceration status (a different question) use inmate locators like `[[state-and-county-jail-inmate-locators]]` (US) or the relevant Canadian corrections source.

## Trust & verifiability
`trust: trusted` — it is the Federal Court of Canada's own primary-source publication of its decisions, authoritative for what those judgments say. The only caveat is scope (Federal Court only) and privacy anonymisation in some case types.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | federal-court |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
