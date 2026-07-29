---
id: 800notes
name: 800notes
description: Use when you have a `phone` number and want crowdsourced reports on who's calling from it — returns caller-identity guesses, scam/spam tags, and commenter details.
url: https://800notes.com/
category: phone
path:
- phone
bestFor: Checking a phone number against a crowdsourced directory of caller complaints and identity reports.
selectorsIn:
- phone
selectorsOut:
- phone
- name
- associate
status: live
pricing: free
costNote: Free to search and read; no account needed to view. Posting a comment requires registration.
opsec: passive
opsecNote: You search a public complaints database — you do NOT call or contact the number, so the owner is never alerted. Fully passive. Use a clean browser if you don't want the lookup in your local history.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running crowdsourced reverse-phone complaint site; entries are anonymous user reports, so treat identity claims as leads, not fact.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- 800notes
- 800 notes
tags:
- phone
- reverse-phone
- scam-reports
source: inteltechniques-tools
lastVerified: '2026-07-29'
enrichment: full
---

# 800notes

> A crowdsourced reverse-phone directory: paste a number and read what other people say about who's been calling from it.

## When to use
You have a `phone` number — one that called a subject, appears in records, or is otherwise a lead — and you want to know whether the community has already identified it. 800notes aggregates user complaints and comments tied to a number, which can surface the caller's claimed name/business, whether it's a known scam/robocall, and occasionally a real person or `associate` mentioned in the threads. Best for U.S. numbers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://800notes.com/.
2. Enter the `phone` number in the search box (works for the number in various formats).
3. Read the thread: user-submitted reports about who called, what they said, and scam/spam tags.
4. Mine the comments for names, company names, or corroborating details other reporters supplied.
5. Pivot: any claimed caller `name`/business becomes a new selector to verify against a separate source.

## Inputs → Outputs
- **In:** `phone`
- **Out:** crowdsourced caller `name`/business guesses, scam/spam classification, commenter-supplied `associate` details
- **Empty/negative result looks like:** "no comments" for that number — common for personal/mobile numbers that haven't been reported. Absence means "not reported," not "not in use."

## Gotchas & OpSec
- **Anonymous crowdsourced claims** — identity attributions are unverified and sometimes wrong or malicious; corroborate before relying on any name.
- Skews toward telemarketing/scam numbers; personal mobiles are usually absent.
- OpSec: **passive** — you never contact the number; the owner isn't notified.

## Overlaps ("do both")
- Complements formal reverse-phone/carrier lookups — 800notes gives *human context* (what the caller said, scam status) that a data-only lookup misses; run both and reconcile.

## Trust & verifiability
`trust: community` — a real, established site, but its content is anonymous user reports; treat as a lead generator and verify identity claims independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | 800notes |
| category | phone |
| selectorsIn → selectorsOut | phone → phone, name, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
