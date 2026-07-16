---
id: oklahoma-voters-search
name: Oklahoma Voters Search
description: Use when you have a `name` in Oklahoma and want voter-registration details — returns registration data (address/precinct) from Oklahoma voter records.
url: http://oklahomadata.com/voters.asp
category: public-records
path:
- public-records
bestFor: Looking up an Oklahoma resident's voter registration by name to confirm an address.
selectorsIn:
- name
selectorsOut:
- address
- name
status: degraded
pricing: free
costNote: Free third-party site presenting Oklahoma voter data; hosted on GoDaddy and periodically under maintenance (noted maintenance in 2025).
opsec: passive
opsecNote: A public-records lookup — you query a voter database, not the subject, and nobody is notified. Voter registration is public record in Oklahoma. Use a sock-puppet browser; this is a third-party presentation of state data, not the official election board site.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party/hobbyist site republishing Oklahoma voter-registration data, not the official State Election Board; data may lag the official rolls and the site's uptime is inconsistent.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Oklahoma voter lookup
- oklahomadata.com voters
tags:
- voter-records
- oklahoma
- public-records
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- oklahoma-registered-voter-verification
---

# Oklahoma Voters Search

> A free lookup of Oklahoma voter registrations by name — a route to confirm a subject's address via public voter rolls.

## When to use
You have a `name` for someone in Oklahoma and want to confirm a current/recent address. Voter registration is public record and is one of the more reliable address sources (people update it to vote), so it's valuable for placing a subject geographically in a missing-person or skip-trace workflow.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://oklahomadata.com/voters.asp (expect occasional maintenance downtime).
2. Enter the last `name` **exactly** as registered, plus a first name or partial first name (e.g. "J" to catch Joe/Jack/Jim).
3. Review the returned registration record(s) for the matching person.
4. Read the fields: registered `name` and `address` (and, where shown, precinct/status).
5. Pivot: the registration `address` feeds property/people-search cross-checks; multiple same-name results need disambiguation by middle name/age where available.

## Inputs → Outputs
- **In:** `name` (exact last name required)
- **Out:** voter-registration `name` and `address` (precinct/status where shown)
- **Empty/negative result looks like:** no match — the person isn't a registered OK voter, the last name is misspelled (exact match required), or the site is mid-maintenance. Absence doesn't disprove residence.

## Gotchas & OpSec
- **Exact last-name match required** — variant spellings return nothing; try known variants.
- Third-party site, not the official State Election Board — data may lag and uptime is patchy (it was under maintenance in 2025). Cross-check with the official OK Voter Portal for authoritative status.
- OpSec: **passive**, public record; nothing reaches the subject.

## Overlaps ("do both")
- Pairs with the official Oklahoma State Election Board voter portal and general US brokers (`[[thats-them]]`, `[[radaris-people-and-business-search-north-america]]`) — voter rolls give a well-maintained address; brokers add phones and relatives. Confirm against the official portal.

## Trust & verifiability
`trust: community` — a third-party republication of Oklahoma voter data; the underlying records are official but this presentation may lag and isn't authoritative. Verify address/status on the state portal.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | oklahoma-voters-search |
| category | public-records |
| selectorsIn → selectorsOut | name → address, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
