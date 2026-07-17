---
id: scamsearch
name: ScamSearch
description: Use when you have an `email`, `phone`, `username`, `image` or `crypto-wallet` and want to check it against reported-scammer records — returns matched scammer identifiers.
url: https://scamsearch.io/
category: email
path:
- email
bestFor: Checking whether a contact identifier appears in a global database of reported scammers.
selectorsIn:
- email
- phone
- crypto-wallet
- username
- image
selectorsOut:
- email
- phone
- social-profile
- username
status: live
pricing: freemium
costNote: Basic search is free and needs no account; PDF reports, monitoring and live reverse-profile lookups require a paid membership.
opsec: passive
opsecNote: Queries ScamSearch's own reported-scammer dataset; the search does not contact the identifier's owner. Do not submit a report casually — reports are public and could expose your interest.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Crowd-sourced/aggregated scam reports; entries are user-submitted and unverified, so a hit is a lead to corroborate, and an absence proves nothing.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- ScamSearch.io
- Scam Search
tags:
- email
- phone
- scam
- fraud
- crypto
source: inteltechniques-tools
lastVerified: '2026-07-17'
enrichment: full
---

# ScamSearch

> A free public database of reported scammer identifiers — check an email, phone, username, crypto address or photo against millions of fraud reports.

## When to use
You have an `email`, `phone`, `username`, `crypto-wallet`, website, or `image` and want to know whether it has been reported in connection with scams — romance fraud, investment/crypto scams, fake sellers. Useful for vetting a contact a subject was interacting with, or for tying several identifiers together through a shared scam report.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://scamsearch.io/ and choose the search type (email, phone, username, crypto address, website, or reverse-image).
2. Enter the identifier and run the free search.
3. Read the result: whether it matches a reported scammer profile and the basic linked identifiers shown for free (other emails/phones/`username`s tied to the same report).
4. Note that full report detail, PDF export, monitoring and live cross-site reverse lookups are gated behind a paid membership — capture the free signal first.
5. Pivot: linked identifiers from a shared report feed email/phone/username enumeration; a matched crypto address feeds blockchain OSINT.

## Inputs → Outputs
- **In:** `email`, `phone`, `username`, `crypto-wallet`, website, or `image`
- **Out:** scammer-report match plus linked `email`/`phone`/`username`/`social-profile` identifiers
- **Empty/negative result looks like:** "no results" — the identifier is simply not in the reported set, which is weak evidence of legitimacy given the database is far from exhaustive.

## Gotchas & OpSec
- Human-in-the-loop: none for free search; premium features prompt registration/payment.
- OpSec: **passive** to search. Reports are public and user-submitted — do not file one during an active investigation, and treat existing reports as unverified allegations.
- A single scammer often recycles identifiers; treat a match as one node in a network, not a closed case.

## Overlaps ("do both")
- Combine with a breach-lookup or email-recon tool: ScamSearch tells you if an identifier is *reported for fraud*, while breach tools tell you where it is *registered/exposed*.
- Pairs with reverse-image search when checking a profile photo used in romance-scam personas.

## Trust & verifiability
`trust: community` — crowd-sourced reports with no verification gate; valuable as a lead source but never as sole proof that someone is (or is not) a scammer.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scamsearch |
| category | email |
| selectorsIn → selectorsOut | email, phone → email, phone, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
