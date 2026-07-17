---
id: buffalo-police
name: Buffalo Police Accountability Database
description: Use when you have a Buffalo (NY) police officer `name` or badge and want accountability/misconduct records — returns officer identity and complaint/disciplinary details.
url: https://airtable.com/embed/shra4F3cAE7H2PV5m?backgroundColor=gray&viewControls=on
category: public-records
path:
- public-records
bestFor: Looking up Buffalo, NY police officers in a community-compiled accountability/misconduct Airtable.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
status: degraded
pricing: free
costNote: Free public Airtable embed; no account needed to view. Community-maintained, so availability depends on the volunteer host keeping the base public.
opsec: passive
opsecNote: You view a public Airtable; no query about your subject is transmitted to the officer or department. Standard Airtable/web logging only. Do not attempt to edit — it is read-only for the public.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Volunteer-compiled from public complaint/disciplinary records and news. Useful as a lead index; verify any specific record against the primary source (court, CCRB-equivalent, news).
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- san-francisco-copwatch-database
- simplescraper-osint-airtable
aliases:
- Buffalo Police copwatch
- Buffalo PD accountability
tags:
- police
- accountability
- us
- new-york
- airtable
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# Buffalo Police Accountability Database

> A community-maintained Airtable indexing Buffalo, NY police officers and accountability records — a starting index, not a system of record.

## When to use
You have the `name` (or badge) of a Buffalo, New York police officer and want to check whether they appear in a community-compiled accountability dataset — complaints, disciplinary actions, lawsuits, or news mentions. Use it to generate leads about an officer's history that you then confirm against primary sources. This is a narrow, jurisdiction-specific resource; it is not a general people-finder and has little direct missing-persons value beyond investigations that involve a specific officer.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Airtable embed at the URL above in a browser.
2. Use the table's search/filter to look up the officer's `name` or badge number.
3. Read the row: officer identity, rank/unit, and whatever accountability detail (complaint, discipline, incident, source link) the compilers recorded.
4. Treat every cell as a lead — follow the linked source (news article, court record) to confirm.
5. Pivot: a confirmed name/rank feeds court-record and news searches; the department affiliation (`employer-org`) anchors further public-records requests.

## Inputs → Outputs
- **In:** `name` (Buffalo PD officer, or badge)
- **Out:** `name`, `employer-org` (department/unit), plus recorded accountability details and source links
- **Empty/negative result looks like:** officer not listed — the dataset is not exhaustive, so absence means "not in this volunteer index," not "no record exists."

## Gotchas & OpSec
- Hosted on a public Airtable that a volunteer controls; it can go private or stale without notice (marked `status: degraded` for that reason). Verify it still loads.
- Buffalo, NY only. Do not confuse with similarly named departments elsewhere.
- OpSec: passive; nothing is sent to the officer or department.

## Overlaps ("do both")
- Pairs with `[[san-francisco-copwatch-database]]` as a sibling jurisdiction index, and with `[[simplescraper-osint-airtable]]` if you need to pull the whole base out of the Airtable embed for offline analysis.

## Trust & verifiability
`trust: community` — crowd-compiled from public complaint/disciplinary records and news. Good for surfacing leads; every specific claim must be corroborated against the cited primary source before use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | buffalo-police |
| category | public-records |
| selectorsIn → selectorsOut | name → name, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
