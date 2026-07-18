---
id: ohio-mhas
name: Ohio Dept. of Mental Health & Addiction Services (OhioMHAS)
description: Use when an Ohio subject may be in behavioral-health treatment and you want licensed-provider/facility references — returns employer-org and address leads.
url: http://mha.ohio.gov/
category: public-records
path:
- public-records
bestFor: Official Ohio behavioral-health agency site — provider/facility references and regulatory info, not a person search.
selectorsIn:
- name
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free Ohio state government site; no account needed.
opsec: passive
opsecNote: Browsing a public government resource site reveals nothing about any subject. Note that individual patient/treatment records are confidential and NOT available here — this is agency/provider information only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Ohio state agency (OhioMHAS); authoritative for licensed providers and regulations, but not a database of individuals.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- ohio
aliases:
- OhioMHAS
- mha.ohio.gov
tags:
- behavioral-health
- ohio
- government
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Ohio Dept. of Mental Health & Addiction Services (OhioMHAS)

> The Ohio state behavioral-health agency's site — a reference for licensed treatment providers and facilities, with only indirect investigative use and no personal records.

## When to use
This is a narrow, context-only resource. Reach for it when an Ohio missing-person or welfare case might intersect the behavioral-health system — e.g. building a list of licensed treatment `employer-org`s/facilities in a county where a vulnerable subject could be, or understanding provider regulation. It does **not** hold patient records (those are confidential) and cannot search for a person; treat any facility as a lead to contact through proper legal channels, not a place to look someone up online.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://mha.ohio.gov/ and use its provider/facility locator and resource directories.
2. Identify licensed providers/facilities and crisis services in the relevant Ohio area.
3. Note facility names and `address`es as leads to pursue through lawful, human channels.
4. Pivot: a facility → contact via appropriate legal/welfare process; regulatory info → understanding what records might exist elsewhere.

## Inputs → Outputs
- **In:** `name` (only as a locality/context anchor — not a person lookup)
- **Out:** `employer-org` (licensed providers/facilities), `address` (facility locations), crisis-resource info
- **Empty/negative result looks like:** no facilities/resources for the area, or a page with only general policy content — meaning nothing actionable here for your location.

## Gotchas & OpSec
- **No personal/patient data** — treatment records are confidential; this is provider and policy information only.
- Not a search engine for people; its value is limited to facility/provider context.
- OpSec: passive; but any follow-up involving a facility must go through lawful welfare/legal channels.

## Overlaps ("do both")
- Pairs with local welfare/missing-person procedures and county service directories — this identifies the licensed providers; the actual person-locating happens through law-enforcement and welfare channels, not open records.

## Trust & verifiability
`trust: trusted` — an authoritative state agency; reliable for provider/regulatory facts, but it offers no individual data to verify in the first place.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ohio-mhas |
| category | public-records |
| selectorsIn → selectorsOut | name → employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
