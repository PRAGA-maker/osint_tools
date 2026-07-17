---
id: plain-view-project
name: Plain View Project
description: Use when you have the `name` of a current or former police officer in one of the covered US departments and want their public Facebook posts flagged for bias/violence — returns `social-profile` posts tied to the officer.
url: https://www.plainviewproject.org/data
category: public-records
path:
- public-records
bestFor: Finding archived public Facebook posts by named police officers in the departments the project covered.
selectorsIn:
- name
selectorsOut:
- social-profile
- employer-org
status: live
pricing: free
costNote: Free research database published by the Plain View Project; no account or payment.
opsec: passive
opsecNote: You browse a published research dataset, not the officer's live account, so there is no footprint on the subject. The posts were already public when collected; reading the archive is passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A documented research project (launched 2019) that recorded public Facebook posts by officers and matched them to rosters; methodology is published, though it is a point-in-time snapshot of specific departments only.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- boston-police-internal-affairs-cases-2010-2020
aliases:
- Plain View Project
- plainviewproject.org
tags:
- police-accountability
- social-media-archive
- public-records
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# Plain View Project

> A searchable archive of public Facebook posts by US police officers, matched to named officers in specific departments and flagged for bias, violence, or misconduct.

## When to use
Your subject is (or was) a police officer in one of the departments the Plain View Project covered — including Philadelphia, Dallas, Phoenix, St. Louis, and several others. Searching their `name` can surface archived public Facebook posts the project attributed to them, with the officer's department (`employer-org`) and the collected post content. This is a concrete accountability/attribution source: it links a named officer to their own public statements and to a specific department roster.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.plainviewproject.org/data and select a covered department or search by officer `name`.
2. Review the matched records: officer name, department, and the archived post text/screenshots.
3. Confirm the identity match — the project matched public accounts to rosters, but common names warrant care; corroborate with the department roster or the officer's own profile.
4. Capture the archived post (screenshot + record the project's reference) since it is a preserved snapshot.
5. Pivot: the confirmed `employer-org` feeds public-records/payroll checks; the officer's Facebook account feeds live social-media OSINT.

## Inputs → Outputs
- **In:** `name` (an officer in a covered department)
- **Out:** `social-profile` (archived Facebook posts) and `employer-org` (department)
- **Empty/negative result looks like:** no record — the officer isn't in a covered department, had no flagged public posts, or joined after the collection window; absence here is not proof of clean conduct, only that the project didn't capture them.

## Gotchas & OpSec
- Fixed scope and date: only specific departments, collected around 2017–2019 — it is a historical snapshot, not a live monitor.
- Attribution care: matches of public accounts to officers can err on common names; verify before publishing an identification.
- Sensitivity: this is accountability data about named individuals — handle per your legal/ethical rules.
- OpSec: passive; you read the archive, never the officer's live account.

## Overlaps ("do both")
- Pairs with police-accountability records like `[[boston-police-internal-affairs-cases-2010-2020]]` — combine an officer's own public posts with formal misconduct/IA records for a fuller picture, and confirm current assignment via department payroll.

## Trust & verifiability
`trust: trusted` — a methodologically documented research project working from posts that were public at collection; reliable as a preserved record, but confirm the name-to-officer match and remember it is a bounded historical dataset.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | plain-view-project |
| category | public-records |
| selectorsIn → selectorsOut | name → social-profile, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
