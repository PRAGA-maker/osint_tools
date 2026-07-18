---
id: cybernews-personal-data-leak-check
name: Cybernews Personal Data Leak Check
description: Use when you have an `email` and want to know if it appears in known breaches — returns how many leaks it's in and which categories of data were exposed.
url: https://check.cybernews.com/
category: email
path:
- email
bestFor: Fast, free check of whether an email (or username) is present in aggregated breach datasets, with a breakdown of exposed data types.
selectorsIn:
- email
selectorsOut:
- email
- password
status: live
pricing: free
costNote: Free to run a check; no account or payment. Cybernews monetizes via its media site, not the checker.
opsec: passive
opsecNote: Passive to the subject — the target is not notified. But you are submitting the subject's email to a third-party service that logs queries; use a clean session and avoid entering data you must keep fully contained.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Run by Cybernews, an established security-media outlet; it aggregates publicly known breach corpora. Coverage differs from HIBP, so treat a clean result as "not in their set," not "never breached."
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- personal-data-leak-checker
aliases:
- Cybernews
- check.cybernews.com
tags:
- email
- breach
- leak
source: inteltechniques-tools
lastVerified: '2026-07-18'
enrichment: full
---

# Cybernews Personal Data Leak Check

> A free breach-exposure oracle: drop in an email and see whether — and roughly how badly — it shows up across aggregated leak datasets.

## When to use
You have an `email` (the checker also accepts usernames/phones) and want a quick read on its breach exposure: is it in known leaks, in how many, and what kinds of data (passwords, addresses, phones) were exposed. Useful early in email-OSINT to confirm an address is real and active, to gauge whether credential-stuffing leads exist, and to decide whether to pull the specific breach records from another source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://check.cybernews.com/ in a clean/sock-puppet session.
2. Enter the target `email` and run the check.
3. Read the result: the number of leaks the address appears in and a categorized summary of exposed data types (e.g. passwords, IP, physical address).
4. Cross-check against a second checker (coverage varies by provider), then pull the actual breach details from a dedicated source if you need specifics.
5. Pivot: confirmed exposure feeds credential/username OSINT and tells you which breaches to look up; exposed data categories hint at what else may be recoverable.

## Inputs → Outputs
- **In:** an `email` (also username/phone)
- **Out:** breach count and categories of exposed data (may indicate `password` and other PII exposure, without necessarily revealing the values)
- **Empty/negative result looks like:** "no leaks found" means the address isn't in Cybernews's aggregated set — not a guarantee it was never breached; another tool with different corpora may still show hits.

## Gotchas & OpSec
- **Coverage ≠ complete:** each checker holds a different mix of breach data; always corroborate a clean or a positive result against another (e.g. HIBP-style tools).
- You are handing a third party the subject's address; it may be logged. Use a clean session and don't submit data you can't risk exposing.
- Summarizes exposure by category; it typically won't hand you plaintext credentials — pair with a breach-detail source for specifics.

## Overlaps ("do both")
- Pairs with `[[personal-data-leak-checker]]` and HIBP-style tools — run more than one, because their datasets differ and one will surface breaches the others miss.

## Trust & verifiability
`trust: community` — operated by a known security-media outlet aggregating public breach corpora; results are indicative and should be confirmed against an independent checker before you rely on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cybernews-personal-data-leak-check |
| category | email |
| selectorsIn → selectorsOut | email → email, password |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
