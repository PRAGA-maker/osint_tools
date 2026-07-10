---
id: the-courts-of-british-columbia-home
name: Courts of British Columbia
description: Use when you have a `name` involved in a BC (Canada) court matter and want published judgments, daily hearing lists and case references — returns name, document-id and associate/party links.
url: https://www.bccourts.ca/index.aspx
category: public-records
path:
- public-records
bestFor: Finding British Columbia court judgments, daily hearing/court lists and case file references naming a party.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- associate
status: live
pricing: freemium
costNote: Judgments (Court of Appeal, Supreme Court) and daily hearing/court lists are free to search and read on bccourts.ca. Full case-file search by party name is done via the separate Court Services Online (CSO) portal, which charges a per-search fee (a few dollars).
opsec: passive
opsecNote: Searching public judgments and court lists is passive and touches nothing the subject controls. If you use CSO party search you register/pay, so that activity is logged by the court service — use a research account for CSO.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official website of the Courts of British Columbia (Court of Appeal, Supreme Court, Provincial Court); judgments and lists are authoritative primary court records.
missingPersonsRelevance: high
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- BC Courts
- bccourts.ca
- Courts of British Columbia
tags:
- court
- inmate
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Courts of British Columbia

> The official BC courts portal — free access to published judgments and daily hearing lists (with deeper case-file search via Court Services Online) for placing a person in a British Columbia legal proceeding.

## When to use
You have a `name` you believe is a party, accused, litigant or witness in a British Columbia matter, and you want the court paper trail: a published judgment (which often narrates facts, dates, addresses and other parties), an upcoming hearing on a daily court list, or a case-file reference number. Judgments are especially rich for corroborating identity, timelines and associates; hearing lists tell you someone is due in court on a given day and where.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.bccourts.ca/ and use **Quick Search** for Court of Appeal and Supreme Court judgments; enter the subject's `name`.
2. Check **Daily Hearing Lists / Court Lists** (posted each morning, ~6:00–6:30 am PST) for scheduled criminal/civil matters by name and location.
3. For a full case-file search by party, follow the link to **Court Services Online (CSO)** and use "Search Civil/Criminal by Party Name" (this step is paid, per-search).
4. Read judgments for named parties (`associate`), case numbers (`document-id`), dates and facts.
5. Pivot: co-parties become new `name` leads; a case number feeds CSO file details; a hearing location anchors a place/time.

## Inputs → Outputs
- **In:** `name` (party/accused/litigant)
- **Out:** `name` (confirmed party), `document-id` (case/file/citation number), `associate` (co-parties, counsel)
- **Empty/negative result looks like:** no judgment or list entry matching the name — meaning no *published* decision or scheduled hearing under that name; most matters (especially resolved or lower-court ones) never appear in the free judgment database.

## Gotchas & OpSec
- Free judgments cover mainly the higher courts (Appeal, Supreme); comprehensive by-name file search lives behind the paid CSO portal.
- Publication bans and privacy rules mean some parties (youth, protected persons) are anonymised — absence is not proof.
- OpSec: passive for judgments/lists; CSO search ties activity to your paid account.

## Overlaps ("do both")
- Pairs with CanLII (free Canadian case-law) and CSO — run CanLII for full-text judgment search across Canada, bccourts.ca for BC lists/recent judgments, and CSO for the actual case file.

## Trust & verifiability
`trust: trusted` — first-party official court records; judgments and lists are authoritative primary sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-courts-of-british-columbia-home |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
