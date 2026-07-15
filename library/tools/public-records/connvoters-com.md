---
id: connvoters-com
name: Connvoters.com
description: Use when you have a `name` (and roughly a Connecticut location) and want the subject's registered address, town, party and DOB from the state voter list — returns address, dob, associate.
url: https://connvoters.com/
category: public-records
path:
- public-records
bestFor: Free lookup of a Connecticut resident's voter-registration record — current address, town, party and approximate DOB — plus household co-registrants.
selectorsIn:
- name
- address
selectorsOut:
- address
- dob
- name
- associate
status: live
pricing: free
costNote: Free-to-access; the site republishes a purchased copy of Connecticut's statewide voter file as a public-interest/genealogy resource.
opsec: passive
opsecNote: Querying a republished public voter list is passive and does not notify the subject. It is a third-party site, so assume queries may be logged; use a clean browser/IP and enter only the selectors you need.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Privately run site republishing an official Connecticut voter file; the underlying data is government-sourced but the snapshot can be dated between purchases, and it is not the state's own portal.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- Connvoters
- Connecticut voter lookup
tags:
- voter-records
- public-records
source: osint4all
lastVerified: '2026-07-15'
enrichment: full
---

# Connvoters.com

> A free, searchable copy of Connecticut's statewide voter registration file — resolve a name to a current CT address, town, party and approximate date of birth.

## When to use
You have a `name` for someone likely registered to vote in Connecticut and want their registration address, town and DOB — or you have an `address` and want who is registered there. US voter files are one of the most reliable free address/DOB sources for adults, and this site exposes CT's without the state portal's per-record friction, making it strong for locating a subject or confirming an address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://connvoters.com/.
2. Search by `name` (add town to disambiguate common names) or by `address`.
3. Read the record: registrant name, residential `address`, town, party affiliation and date of birth (often full or year).
4. Note others registered at the same address — likely household `associate`s (spouse, adult children).
5. Pivot: the address feeds property/reverse-address tools; DOB + name sharpens people-search and record matching; household co-registrants become new `name` leads.

## Inputs → Outputs
- **In:** `name` (optionally + town) or `address`
- **Out:** `address`, `dob`, `name`, party, town, `associate` (co-registered household members)
- **Empty/negative result looks like:** no match — meaning the person isn't in this CT snapshot (moved, out of state, unregistered, or newly registered after the file was purchased), not proof they don't exist.

## Gotchas & OpSec
- Connecticut only — no coverage outside CT.
- The data is a snapshot; recent moves or registrations may be missing until the site refreshes its purchased file.
- Voter records are public, but handle the DOB/address responsibly; use for legitimate location work.
- OpSec: passive to the subject; it's a third-party republisher, so treat the operator as untrusted infrastructure.

## Overlaps ("do both")
- Pairs with a multi-state voter-records aggregator — this is a free CT-specific source, while a national tool extends the same address/DOB pivot to other states.

## Trust & verifiability
`trust: community` — a privately operated site republishing an official Connecticut voter file; the data originates from the state (reliable) but the snapshot may lag and it is not the government's own lookup.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | connvoters-com |
| category | public-records |
| selectorsIn → selectorsOut | name, address → address, dob, name, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
