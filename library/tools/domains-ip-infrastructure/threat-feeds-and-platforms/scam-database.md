---
id: scam-database
name: ScamDB
description: Use when you have a `phone`, `email`, `domain`, social handle, or `crypto-wallet` and want to check crowd-reported scam activity — returns community fraud reports tied to that identifier.
url: https://www.scamdb.net/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- threat-feeds-and-platforms
bestFor: Quickly checking whether a contact identifier has been reported as a scam by the public.
selectorsIn:
- phone
- email
- domain
- crypto-wallet
- username
selectorsOut:
- phone
- email
- domain
- crypto-wallet
status: live
pricing: free
costNote: Free to search; submitting a report may require an account, but lookups are open.
opsec: passive
opsecNote: You are searching community reports about an identifier — the subject is not contacted or notified. Only your own request is logged.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Crowd-sourced and explicitly unverified — the site states all reports are unverified user submissions. Treat hits as allegations/leads, never as established fact.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- scamdb.net
- Scam Database
tags:
- scam
- fraud
- threat-intel
- reputation
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# ScamDB

> A crowd-sourced scam-report database: paste a phone, email, website, handle, or crypto wallet and see whether the public has flagged it as fraudulent.

## When to use
You have a contact identifier — a `phone`, `email`, `domain`/website, social `username`, or `crypto-wallet` — surfacing in an investigation (a dating-scam contact, a suspicious seller, a "recovery" service) and want a fast read on whether others have reported it as a scam. It's a reputation/triage check that can corroborate a fraud pattern and sometimes links one identifier to others used by the same operation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.scamdb.net/.
2. Search the identifier you have (`phone`, `email`, `domain`, handle, or `crypto-wallet`).
3. Read matching reports: the scam type (romance, phishing, crypto, marketplace, dating), narrative details, and any other identifiers the reporter tied to it.
4. Treat every report as an unverified allegation — corroborate with independent sources before acting.
5. Pivot: additional `phone`/`email`/`crypto-wallet` values named in a report become new selectors to trace across breach, blockchain, and search tools.

## Inputs → Outputs
- **In:** `phone`, `email`, `domain`, `username`, or `crypto-wallet`
- **Out:** community scam reports, scam type, and linked identifiers (`phone`/`email`/`domain`/`crypto-wallet`)
- **Empty/negative result looks like:** no reports found — means nobody has reported this identifier here, NOT that it's safe (a fresh scam identifier has no reports yet). Absence is weak evidence.

## Gotchas & OpSec
- Human-in-the-loop: none to search; posting a report may require registration.
- OpSec: **passive** — searching community reports doesn't touch the subject.
- Reliability: reports are unverified user submissions and can be wrong, malicious, or retaliatory. Never treat a hit as proof; use it as a lead to corroborate.

## Overlaps ("do both")
- Pairs with other reputation/report sources (scam-tracker sites, breach lookups, blockchain explorers for wallets) — ScamDB is one crowd's view; convergence across several report databases is what makes a fraud finding credible.

## Trust & verifiability
`trust: unverified` — explicitly crowd-sourced and unvetted; treat every report as an allegation to independently confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scam-database |
