---
id: okcaller
name: OKCaller
description: Use when you have a US `phone` number and want caller-ID / reverse-lookup context — returns an associated name and community-reported caller reputation.
url: https://www.okcaller.com/
category: phone
path:
- phone
bestFor: Free reverse phone lookup with caller name ID and crowd-sourced spam/scam reports.
selectorsIn:
- phone
selectorsOut:
- name
- phone
status: live
pricing: free
costNote: Free to look up; a Google sign-in is now required to view real-time Caller Name ID at no charge.
opsec: passive
opsecNote: Reverse-lookup queries are read-only and the number's owner is not notified. Signing in with Google ties the lookup to that account; use a sock-puppet Google account. OKCaller also lets people opt out / manage how their number appears, so absence of data can be an opt-out, not a dead number.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Established free caller-ID service with a user-contributed database; name matches and spam labels are community/aggregated data and should be corroborated.
missingPersonsRelevance: medium
coverage:
- us
auth: account
api: false
localInstall: false
registration: false
relatedTools:
- truecaller
- thatsthem-phone-search
- sync-me
aliases:
- okcaller.com
tags:
- phone
- reverse-phone
- caller-id
source: inteltechniques-tools
lastVerified: '2026-07-17'
enrichment: full
---

# OKCaller

> A free reverse-phone / caller-ID service: enter a US number and get an associated name plus crowd-sourced reports on whether the number is spam, a scam, or a known caller.

## When to use
You have a US `phone` number — from a missed call, a listing, a leaked contact, a note — and want to attach a `name` to it and gauge its reputation. OKCaller draws on a large caller-ID database and community reports, so it's a quick first pass to see whether a number resolves to a person, a business, or a flagged spam/scam line before spending effort on paid people-search tools.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.okcaller.com/ and enter the phone number (US format).
2. Sign in with a (sock-puppet) Google account when prompted — this is now required for free real-time Caller Name ID.
3. Read the result: any associated name, line type/carrier hints, and community-posted comments flagging spam/scam/robocall behaviour.
4. Treat the name as a lead and confirm it against a second source (a paid reverse-phone tool or people-search) before relying on it.
5. Pivot: a resolved `name` feeds people-search; a "spam/scam" flag tells you the number is likely not a real personal contact worth chasing.

## Inputs → Outputs
- **In:** `phone` (US number)
- **Out:** `name` (associated caller), `phone` confirmation, community spam/scam reputation
- **Empty/negative result looks like:** "no information" / no name — an unlisted number, a number the owner opted out of, or one simply not in the database. Absence is not proof the number is unused.

## Gotchas & OpSec
- US-focused; coverage of mobile and VoIP numbers is patchy and names can be stale or wrong.
- Owners can opt out and manage their listing, so a blank result may be a deliberate suppression rather than a genuinely unknown number.
- Human-in-the-loop: a Google login is required for the free lookup — use a puppet account. OpSec: **passive** — the lookup does not alert the number's owner.

## Overlaps ("do both")
- Pairs with `[[truecaller]]` and `[[thatsthem-phone-search]]` — each caller-ID database has different coverage, so run the number through more than one; agreement across sources raises confidence in the name.

## Trust & verifiability
`trust: community` — a real, established free service, but name matches and spam labels come from aggregated/user-contributed data, so corroborate any name before treating it as the number's true owner.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | okcaller |
| category | phone |
| selectorsIn → selectorsOut | phone → name, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
