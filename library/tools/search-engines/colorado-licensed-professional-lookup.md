---
id: colorado-licensed-professional-lookup
name: Colorado Licensed Professional Lookup
description: Use when you have a `name` and think the subject holds a Colorado professional license — returns license status, profession/`employer-org`, and city `geolocation`.
url: https://www.colorado.gov/dora/licensing/Lookup/LicenseLookup.aspx
category: search-engines
path:
- search-engines
bestFor: Verifying a Colorado occupational/professional license and the licensee's profession and location.
selectorsIn:
- name
selectorsOut:
- employer-org
- geolocation
- name
status: live
pricing: free
costNote: Free official Colorado DORA license-lookup; no account required.
opsec: passive
opsecNote: Passive — you query the state licensing database; the licensee is not notified. Records are public. Standard state-site logging applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Colorado Department of Regulatory Agencies (DORA); authoritative for Colorado professional-license status.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Colorado DORA license lookup
tags:
- toddington
- curated-directory
- specialty-search
- professional-license
- colorado
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Colorado Licensed Professional Lookup

> Colorado's official DORA license search — confirm a person holds a state professional license and learn their profession, status, and city.

## When to use
You have a `name` and reason to think the subject works in a licensed profession in Colorado (nursing, medicine, real estate, cosmetology, engineering, contracting, mental health, etc.). Verifying a license confirms occupation, ties the person to Colorado (`geolocation` via the city on the license), reveals their profession (`employer-org`/field context), and shows disciplinary status — all useful for confirming identity and current activity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Colorado DORA license-lookup page.
2. Search by licensee `name` (optionally filter by profession/license type).
3. Review the record: license type/profession, license number, status (active/expired/disciplined), issue/expiration dates, and the city/`geolocation`.
4. Pivot: the profession points to likely employers and directories; the city narrows further searches; disciplinary actions can lead to public board records.

## Inputs → Outputs
- **In:** `name` (optionally profession/license type).
- **Out:** license status, profession/field (`employer-org` context), license city (`geolocation`), and confirmed `name`.
- **Empty/negative result looks like:** no matching license — the person holds no Colorado license under that name (or it's in another state / a different name), not proof of anything else.

## Gotchas & OpSec
- Colorado only: other states have their own boards/lookups.
- Name variants: try middle names/initials and maiden names; common names return multiple licensees — use profession/city to disambiguate.
- Scope: covers DORA-regulated professions, not every occupation.
- OpSec: passive; public records, no notification.

## Overlaps ("do both")
- Pairs with other state license lookups and employer/LinkedIn searches — the license confirms occupation and location, those flesh out the current employer.

## Trust & verifiability
`trust: trusted` — the official Colorado DORA system; authoritative for Colorado professional-license status.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | colorado-licensed-professional-lookup |
| category | search-engines |
| selectorsIn → selectorsOut | name → employer-org, geolocation, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
