---
id: nebraska
name: Nebraska DCS Inmate Search
description: Use when you have a `name` and want to check whether a person is or was incarcerated in Nebraska state prison — returns inmate record, ID (`document-id`), `dob` and custody status.
url: https://dcs-inmatesearch.ne.gov/corrections/cor_input.html
category: public-records
path:
- public-records
bestFor: Locating a person in the Nebraska Department of Correctional Services system by name — confirms incarceration, facility, and inmate ID.
selectorsIn:
- name
selectorsOut:
- name
- dob
- document-id
status: live
pricing: free
costNote: Free official state government inmate lookup; no account or payment.
opsec: passive
opsecNote: Public corrections record; the individual is not notified. It is a state government site — use a puppet browser/IP if you don't want the query tied to your address.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Nebraska Department of Correctional Services — the authoritative source for state inmate custody records.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Nebraska DCS inmate search
- dcs-inmatesearch.ne.gov
- Nebraska corrections
tags:
- court
- inmate
- public-records
- nebraska
- corrections
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Nebraska DCS Inmate Search

> Nebraska's official state prison inmate locator — put in a name, find out whether the person is (or was) in state custody, where, and under what ID.

## When to use
You have a `name` and suspect the subject may be incarcerated in Nebraska. Incarceration explains a person's sudden disappearance from normal life and pins them to a known facility with a fixed record (inmate ID, DOB, sentence). This is a high-value "where did they go" check in missing-person and skip-trace work when Nebraska is a plausible location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://dcs-inmatesearch.ne.gov/corrections/cor_input.html.
2. Enter the subject's last/first `name` (try variations and partial names — nicknames and middle-name ordering trip these systems).
3. Read the result: matching inmate(s) with DCS ID number (`document-id`), `dob`, facility/custody status, and often sentence/offense data.
4. Confirm identity via DOB and any known details before attributing — common names produce multiple hits.
5. Pivot: facility → mail/visitation locating; offense/case → county court records (`[[on-demand-court-records]]`-style state portals); confirmed DOB/name → people-search.

## Inputs → Outputs
- **In:** `name`
- **Out:** `name` (confirmed inmate), `dob`, `document-id` (DCS inmate ID), facility, custody status, offense/sentence
- **Empty/negative result looks like:** "no records found" — the person isn't in **Nebraska state** custody. That does NOT rule out county jail, federal (BOP), or another state; check those separately.

## Gotchas & OpSec
- Scope is **Nebraska state prisons only** — not county jails (check the sheriff/jail rosters) and not federal (use the BOP inmate locator).
- Released inmates may drop from the active view; historical status can differ.
- OpSec: **passive** — public record, no notification.

## Overlaps ("do both")
- Pairs with the Federal BOP inmate locator and county jail rosters — run all three when you don't know the custody level.
- Feed a confirmed offense/case into Nebraska court records to get charges and co-defendants.

## Trust & verifiability
`trust: trusted` — first-party state corrections database; custody records are authoritative and current. Verify the individual match by DOB, since name-only hits over-match.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nebraska |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
