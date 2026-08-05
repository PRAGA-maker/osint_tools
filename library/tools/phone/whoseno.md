---
id: whoseno
name: WhoseNo
description: Use when you have a `phone` number and want crowd-sourced caller identity and spam/scam reports — returns a safety rating plus community notes (possible `name`/`employer-org`).
url: https://www.whoseno.com/
category: phone
path:
- phone
bestFor: Free reverse-phone lookup driven by community spam/scam reports and caller-ID votes.
selectorsIn:
- phone
selectorsOut:
- name
- employer-org
status: live
pricing: free
costNote: Free reverse lookup on the website (also a mobile app); no account needed for basic searches. States it does not sell personal data.
opsec: passive
opsecNote: You submit only the target number to a third-party lookup — nothing links it to you or alerts the number's owner. Standard sock-puppet browsing is enough; avoid contributing your own reports from an attributable account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Crowd-sourced — entries are user-submitted reports and votes, so identities and labels are indicative, not authoritative; corroborate before relying on a name.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- WhoseNo.com
- Whose Number
tags:
- phone
- reverse-phone
- caller-id
source: metaosint
lastVerified: '2026-08-05'
enrichment: full
---

# WhoseNo

> A free, community-driven reverse-phone lookup: enter a number and see how the crowd has labelled it — safe, spam, telemarketer, or a reported caller identity.

## When to use
You have a `phone` number (an unknown caller, a number tied to a listing, an ad, or a case) and want a first read on who or what it belongs to and whether others have flagged it. Best for triage — confirming a number is a known spammer/business or surfacing a community-reported `name`/`employer-org` to chase further.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.whoseno.com/ (or the mobile app).
2. Enter the phone number in the search box.
3. Read the result: a safety indicator (safe / likely spam / unknown) plus any community reports, labels, and comments.
4. Pivot: a reported name or business feeds people-search and company tools; a "spam/scam" consensus tells you the line is not a personal lead.

## Inputs → Outputs
- **In:** `phone`
- **Out:** `name`, `employer-org` (community-reported identity/labels + spam rating)
- **Empty/negative result looks like:** "unknown" / no reports means nobody has flagged the number — common for private lines; it's not evidence the number is unused, just unreported.

## Gotchas & OpSec
- Human-in-the-loop: none for lookups; results are only as rich as community activity, which skews toward spam/robocall numbers.
- Crowd data can be wrong or malicious — treat a reported name as a lead to verify, never as confirmation.
- Coverage is broad but uneven by country; a blank abroad doesn't mean much.

## Overlaps ("do both")
- Pair with other reverse-phone tools and carrier/HLR lookups: WhoseNo gives crowd reputation, those give line type/carrier and different identity sources — cross-check for a confident read.

## Trust & verifiability
`trust: community` — entirely user-submitted reports and votes; useful for spam reputation and leads, but any identity it suggests must be corroborated against an authoritative source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whoseno |
| category | phone |
| selectorsIn → selectorsOut | phone → name, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
