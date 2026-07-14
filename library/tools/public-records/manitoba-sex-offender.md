---
id: manitoba-sex-offender
name: Manitoba High-Risk Sex Offender Notification
description: Use when you have a name or photo and want to check whether the subject is a publicly notified high-risk sex offender in Manitoba — returns name, photo, offence history and expected residence area.
url: https://www.gov.mb.ca/justice/commsafe/notification/index.html
category: public-records
path:
- public-records
bestFor: Confirming whether a person is a Manitoba-notified high-risk sex offender and reading their last-known residence area.
selectorsIn:
- name
- image
selectorsOut:
- name
- image
- physical-description
- address
status: live
pricing: free
costNote: Free official Government of Manitoba notification page; no account or payment. Access is gated to Manitoba residents (self-attested).
opsec: passive
opsecNote: Reading a government notification page is passive and leaves no trace with the subject. You must click through a Manitoba-residency confirmation; the page logs standard web-server access only. Do not republish offender details outside your investigation — misuse of notification data can breach the terms of release.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published directly by the Province of Manitoba (Justice / Manitoba Integrated High Risk Sex Offender Unit) using police-supplied data.
missingPersonsRelevance: high
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- Manitoba Justice offender notification
- Manitoba high risk sex offender registry
- commsafe notification
tags:
- public-records
- sex-offender-registry
- canada
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# Manitoba High-Risk Sex Offender Notification

> The Province of Manitoba's public-warning page for offenders judged so likely to re-offend that the public is actively notified — searchable by browsing current and past notices.

## When to use
You have a `name` (or a `image`/photo) for a subject connected to Manitoba and want to check whether they are the target of an active or past high-risk offender notification. A hit gives you a confirmed recent photo, past offence types, victim-type profile and the general area where the offender is expected to reside — all useful for corroborating identity, timeline and location in a missing-persons or safeguarding context.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.gov.mb.ca/justice/commsafe/notification/index.html.
2. Confirm the Manitoba-residency gate (a self-attestation click) to reach the offender details.
3. Browse the two sections: **Current Notifications** (issued within the past year) and **Previous Notifications** (older). There is no free-text name box — scan the listed names/photos.
4. Open a notice to read the offender's name, recent photo, offence history, risk description and expected residence area.
5. Pivot: the residence area + name feeds Canadian people-search and address tools; the photo feeds reverse-image/face search to link other profiles.

## Inputs → Outputs
- **In:** `name` or `image` to match against the posted notices
- **Out:** `name`, recent `image`, `physical-description`, offence history, and an approximate residence `address` (area, not street)
- **Empty/negative result looks like:** the subject does not appear in either list. This means they are not *currently notified* as high-risk — NOT that they have no record (only a small, high-risk subset is ever published here).

## Gotchas & OpSec
- Human-in-the-loop: you must pass the residency confirmation and manually eyeball the lists — there is no search API.
- Only high-risk offenders subject to community notification appear; absence proves nothing about lesser or historical convictions.
- Residence is deliberately given as an area, not an exact address — treat it as a lead, not a pinpoint.
- Data is time-limited: notices roll from "current" to "previous" and can be removed, so record the date you viewed it.

## Overlaps ("do both")
- Pairs with national/provincial people-search and address tools to turn the notified residence area into a fuller location picture.
- Complements reverse-image and face-search tools — run the posted photo to find social profiles under the same face.

## Trust & verifiability
`trust: trusted` — a first-party Government of Manitoba page sourced from the Winnipeg Police Service / RCMP high-risk offender unit, so identity and offence facts are authoritative as of the posting date.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | manitoba-sex-offender |
| category | public-records |
| selectorsIn → selectorsOut | name, image → name, image, physical-description, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
