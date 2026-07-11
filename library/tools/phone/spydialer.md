---
id: spydialer
name: SpyDialer
description: Use when you have a US `phone` number and want the owner name, line type, and location context — returns name and address-area leads (also reverse name/email/address search).
url: https://www.spydialer.com/
category: phone
path:
- phone
bestFor: Free US reverse-phone lookup — owner name, carrier/line type, and general location, with up to 50 free lookups a day and no signup.
selectorsIn:
- phone
- name
- email
selectorsOut:
- name
- address
status: live
pricing: free
costNote: Free with no account and no credit card; up to 50 lookups per day. Some deeper results may hand off to a paid partner, but core reverse-phone lookup is free.
opsec: passive
opsecNote: Database-driven lookup — SpyDialer states searches are anonymous and the person you look up is not notified. You only expose your query/IP to SpyDialer; use a VPN/sock-puppet browser for sensitive work. Avoid its "listen to voicemail greeting" feature against a live target, which could place a call.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established free people/phone-lookup service drawing on public records and proprietary data; results are lead-quality and vary in freshness, so corroborate.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- truecaller-search-engine
- moriarty-project
aliases:
- Spy Dialer
- spydialer.com
tags:
- phone
- reverse-phone
- people-search
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# SpyDialer

> A free, no-signup US reverse-phone lookup — enter a number and get the likely owner name, line type, and location, up to 50 times a day.

## When to use
You have a US `phone` number and want fast attribution: who it likely belongs to, whether it's cell/landline/VOIP, and roughly where. Good early move in phone OSINT because it's genuinely free and requires no account. It also offers reverse **name**, **email**, and **address** search modes, so you can pivot in either direction.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.spydialer.com/ and pick the search type (phone / name / address / email).
2. Enter the US phone number (or other selector) and submit — no login needed.
3. Read the result: owner `name` (when in public records), carrier/line type, city/state, and any spam/scam flags.
4. Stay within ~50 lookups/day; heavier use may be throttled or pushed to a paid partner.
5. Pivot: confirm the name against a second phone source ([[truecaller-search-engine]]) and feed the name/area into people-search and address tools.

## Inputs → Outputs
- **In:** `phone` (primary), or `name` / `email` / `address` in the other modes
- **Out:** owner `name`, line type/carrier, city/state (`address` area), spam indicators
- **Empty/negative result looks like:** "no name found" / carrier-only data — common for cell numbers and newer VOIP lines; absence of a name doesn't mean the number is invalid.

## Gotchas & OpSec
- US-only coverage; results skew toward landlines and older records — cell/VOIP attribution is weaker.
- The voicemail-greeting feature can actually dial the number — avoid it against a live target unless you accept that risk.
- Data is lead-quality (public records + proprietary), so corroborate a name before relying on it.
- OpSec: passive — the subject isn't notified; only SpyDialer sees your query.

## Overlaps ("do both")
- Pairs with [[truecaller-search-engine]] (crowd-sourced caller-ID that often names cells SpyDialer misses) and [[moriarty-project]] (multi-source CLI) — run several, since each source's coverage differs.

## Trust & verifiability
`trust: community` — an established free lookup, but built on aggregated public/proprietary data of varying freshness. Treat a returned name as a strong lead to confirm, not proof of ownership.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | spydialer |
| category | phone |
| selectorsIn → selectorsOut | phone, name, email → name, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
