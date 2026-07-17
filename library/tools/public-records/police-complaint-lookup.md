---
id: police-complaint-lookup
name: Police Complaint Lookup (CUAPB)
description: Use when you have a Minnesota officer's `name` or badge number and want their complaint history — returns documented complaints, involved officers, and outcomes.
url: http://complaints.cuapb.org/
category: public-records
path:
- public-records
bestFor: Searching formal complaints filed against Minnesota law-enforcement officers by name, badge, department, or case number.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
- associate
status: live
pricing: free
costNote: Free public database maintained by a nonprofit (Communities United Against Police Brutality). No account or payment.
opsec: passive
opsecNote: Read-only search of a published public-records database; the officer is not notified. CUAPB may log site traffic (your IP). Subjects here are public officials acting in their official capacity, but treat the data factually and note its documented incompleteness.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Compiled by an advocacy nonprofit from public records and requests; useful and sourced, but self-described as incomplete, so treat as a lead index rather than a definitive registry.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- judyrecords
- courtlistener
aliases:
- CUAPB complaints database
- Communities United Against Police Brutality
tags:
- police
- public-records
- minnesota
- accountability
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# Police Complaint Lookup (CUAPB)

> A nonprofit-maintained, searchable archive of formal complaints against Minnesota police officers — by name, badge, department, or case number — surfacing misconduct history the state makes hard to find.

## When to use
Your subject is a Minnesota law-enforcement officer (or you're vetting one named in another record) and you want their documented complaint history. The database lets you confirm an officer exists at a given department, see how many complaints they've drawn, and — for sustained/disciplined cases — the nature of the complaint and any discipline. It's a niche but authoritative-for-its-scope accountability source when researching a specific officer.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://complaints.cuapb.org/ and choose a search: officer name/badge (with a department picker covering 400+ MN agencies), case number, or alphabetical last-name browse.
2. Enter the officer `name` (or badge) and select the department to disambiguate.
3. Read results by outcome: **unsustained** entries show only that a complaint existed, the officer(s) involved, and status; **sustained/disciplined** entries add the complaint's nature and any discipline.
4. Note co-involved officers as `associate` links and the department as `employer-org`.
5. Pivot: cross-reference names against court records (`[[courtlistener]]`, `[[judyrecords]]`) for related civil suits.

## Inputs → Outputs
- **In:** `name` (officer) or badge number (+ department)
- **Out:** `name`/badge confirmation, `employer-org` (department), `associate` (co-involved officers), complaint status/outcome
- **Empty/negative result looks like:** no matching officer/complaint — the officer is outside Minnesota, no formal complaint was filed, or (per the site's own caveat) the complaint never entered the tracked system. Absence is explicitly not proof of a clean record.

## Gotchas & OpSec
- Minnesota only, and the maintainers state it is incomplete — it omits many formal and most informal complaints, so treat a null result cautiously.
- Unsustained complaints reveal little detail by design; don't over-read a bare "complaint existed" entry.
- OpSec: **passive** — searching a published database; subjects are public officials, but keep your use factual.

## Overlaps ("do both")
- Pairs with `[[courtlistener]]` and `[[judyrecords]]` — court dockets capture civil-rights suits and outcomes the complaint database won't, so run an officer's name through both for a fuller picture.

## Trust & verifiability
`trust: community` — a diligent nonprofit compilation from public records; reliable within its documented limits, but confirm any specific finding against the underlying case/record before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | police-complaint-lookup |
| category | public-records |
| selectorsIn → selectorsOut | name → name, employer-org, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
