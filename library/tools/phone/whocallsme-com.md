---
id: whocallsme-com
name: whocallsme.com
description: Use when you have a `phone` number and want crowdsourced reports on who it belongs to — returns user comments identifying the caller, often exposing scam/spam or a business.
url: https://whocallsme.com/
category: phone
path:
- phone
bestFor: Checking a phone number against a crowdsourced complaint database to see if others have identified it (commonly spam/scam or a business caller).
selectorsIn:
- phone
selectorsOut:
- name
status: live
pricing: free
costNote: Free, ad-supported, community-reported directory; no account needed to read reports (posting a comment may need one).
opsec: passive
opsecNote: A read-only lookup of a public complaint forum; the number's owner is not notified. Do not post the target's number into the forum yourself — that publishes it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Crowdsourced user comments of highly variable reliability. Best for flagging known spam/scam/business numbers, not for confidently identifying a private individual.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- emobiletracker-com
aliases:
- Who Calls Me
- whocallsme
tags:
- mobilephone
- Mobile & Phone Related
- crowdsourced
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# whocallsme.com

> A crowdsourced "who called me?" forum: look up a number and read what other people have reported about it — most useful for unmasking spam, scams, and business callers.

## When to use
You have a `phone` number and want quick, free context on it before investing in a paid lookup: has anyone else reported this number, and did they identify it as a business, a robocaller, or a scam? Think of it as reputation/triage for a number. It rarely names a *private* individual, but it excels at telling you "this is a known Booking.com-impersonation scam" or "this is XYZ company's outbound line."

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://whocallsme.com/ and enter the `phone` number.
2. Read the reports: user comments describing calls from that number — claimed caller identity, purpose, and scam warnings.
3. Weigh the crowd: multiple consistent reports are more trustworthy than a single comment.
4. Do **not** post the target's number yourself if you don't want it publicized.
5. Pivot: a business name in comments feeds company search; a "no reports" result means fall back to a carrier/reverse-lookup tool like `[[emobiletracker-com]]`.

## Inputs → Outputs
- **In:** `phone`
- **Out:** crowdsourced `name`/identity of the caller (often a business or scam label) and call context
- **Empty/negative result looks like:** "no reports for this number." Common and unremarkable — most private numbers have no complaints; absence tells you nothing about the owner, only that it hasn't been reported.

## Gotchas & OpSec
- Reliability is low and uneven — comments are anonymous and unverified; corroborate before believing an identification.
- Strong for spam/scam/business numbers, weak for identifying private individuals.
- Skews US; coverage of other countries is thin.
- OpSec: passive to read; don't post the number and inadvertently publish it.

## Overlaps ("do both")
- Pairs with `[[emobiletracker-com]]` and higher-trust reverse-lookup tools — whocallsme gives crowd reputation, those give carrier/region or identity signals. Use it to quickly rule a number in/out as spam.

## Trust & verifiability
`trust: unverified` — a crowdsourced forum with no vetting. Treat identifications as leads, weight by corroboration across multiple reports, and confirm anything actionable with a more authoritative source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whocallsme-com |
</content>
