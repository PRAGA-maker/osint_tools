---
id: national-center-for-state-courts-united-states
name: National Center for State Courts (United States)
description: Use when you have a US `address`/jurisdiction and want to find the correct state or county court-record system to search — returns pointers to official court portals, not case records directly.
url: http://www.ncsc.org
category: public-records
path:
- public-records
bestFor: Routing an investigation to the right US state/county court system and understanding how that court publishes records.
selectorsIn:
- address
- name
selectorsOut:
- document-id
- address
status: live
pricing: free
costNote: Free reference and research organization; no account or payment to read its directories, statistics, and guides.
opsec: passive
opsecNote: You are browsing a professional-association reference site, not querying anyone. Nothing about the subject is submitted here — the target is never touched. The actual record lookups happen later on the individual court portals this points you to.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: NCSC is a long-established nonprofit serving US state court administrators; its jurisdiction directories and Court Statistics Project are authoritative, but it is a pointer/reference, not a record index.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- NCSC
- ncsc.org
tags:
- toddington
- curated-directory
- specialty-search
- court-records
source: toddington-resources
lastVerified: '2026-07-20'
enrichment: full
---

# National Center for State Courts (United States)

> A reference/routing layer for the fragmented US state-court system — it tells you *which* court holds records and how they're published, so you can go query the right portal.

## When to use
You have a subject tied to a US location (`address`, city, or state) and need to find the correct state or county court system to search for case records — but the US has no single national court index, and you don't yet know whether the relevant records live in a state trial court, a municipal court, or a state-run e-filing portal. NCSC is where you orient: it maintains directories of state court websites, the Court Statistics Project, and guides on how each state publishes case data. It does **not** let you search a person's name for cases — treat it as the map, not the destination.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.ncsc.org.
2. Use the site's "State Court Websites" / court directory resources to drill from the subject's state down to the relevant trial or appellate court.
3. Follow the outbound link to that court's official record portal (many states run public case-search sites; NCSC links to them).
4. Consult NCSC's Court Statistics Project or "Privacy/Public Access to Court Records" guides to understand what that jurisdiction exposes publicly vs. seals.
5. Pivot: run the actual name/case search on the state portal you landed on; a hit there yields `document-id` (case numbers) and often party `address` details.

## Inputs → Outputs
- **In:** `address` / jurisdiction (which state/county), optionally a `name` to search once you reach the right portal
- **Out:** the correct court-portal URL, `document-id` (case numbers found downstream), party `address`
- **Empty/negative result looks like:** NCSC never returns a person — an "empty" result is simply that it points you to a portal which itself has no matching case. Do not treat NCSC's lack of a person record as evidence of anything.

## Gotchas & OpSec
- This is a **pointer**, not a search engine — agents expecting to type a name and get cases will be disappointed. Its value is jurisdiction routing.
- Court-record availability varies wildly by state; some downstream portals charge or require registration even though NCSC itself is free.
- OpSec: passive and safe — browsing NCSC leaks nothing about the subject.

## Overlaps ("do both")
- Pairs with jurisdiction-specific court portals and case aggregators — NCSC tells you which state system to use; those actually return the records.

## Trust & verifiability
`trust: trusted` — NCSC is an authoritative nonprofit for US state-court administration, so its jurisdiction directories and statistics are reliable; just remember it indexes *courts*, not *people*.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | national-center-for-state-courts-united-states |
| category | public-records |
| selectorsIn → selectorsOut | address, name → document-id, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
