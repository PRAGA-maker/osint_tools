---
id: scamwatch
name: Scamwatch
description: Use when you have a suspected scam, scam phone/email, or fraud pattern and want Australia's official guidance, scam-type reference and reporting channel — returns fraud-context and reporting leads.
url: https://www.scamwatch.gov.au
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Reference on current scam types, statistics, and the official channel to report a scam in Australia.
selectorsIn:
- phone
- email
selectorsOut:
- associate
status: live
pricing: free
costNote: Free Australian government service (ACCC / National Anti-Scam Centre). No account required.
opsec: passive
opsecNote: Passive — reading public scam-awareness content is invisible. Submitting a scam report shares details with an Australian government agency, so only report from an appropriate account and understand the data goes to the ACCC/NASC.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official ACCC / National Anti-Scam Centre site; authoritative for Australian scam trends and reporting.
missingPersonsRelevance: low
coverage:
- au
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- scamwatch.gov.au
- ACCC Scamwatch
tags:
- fraud
- scams
- australia
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# Scamwatch

> Australia's official scam-awareness and reporting hub (ACCC / National Anti-Scam Centre) — reference for how scams work and the channel to report one.

## When to use
You're assessing a suspected scam or fraud with an Australian angle — a subject who was scammed, a scam `phone`/`email` targeting a person, or a fraud pattern you need to identify — and you want authoritative reference on the scam type, current trends and statistics, and the official reporting path. It's an educational/reporting resource, not a lookup database: you won't query a phone number and get an owner, but you can classify the scam, learn its playbook, and route a report to the right agency.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.scamwatch.gov.au.
2. Browse **types of scams** to classify the one you're seeing (romance, investment, remote-access, etc.) and learn its method.
3. Read **statistics/trends** for current prevalence and targeting patterns.
4. If appropriate, use **Report a scam** to submit details to the ACCC/NASC.
5. Pivot: the identified scam pattern → search for the same script/handles elsewhere; guidance on "what to do if scammed" → victim-support steps and other agencies (cyber.gov.au, eSafety).

## Inputs → Outputs
- **In:** a suspected scam / scam `phone` or `email` / fraud description
- **Out:** scam-type classification and method, trend statistics, official reporting channel, victim guidance
- **Empty/negative result looks like:** no exact match for a niche scam — the site is educational, not a searchable incident database, so treat it as reference, not confirmation of a specific actor.

## Gotchas & OpSec
- Not a data lookup — it won't resolve a number/email to an identity; use it to classify and report.
- Australia-focused; scam types generalize globally but statistics and reporting are AU-specific.
- OpSec: passive to browse; reporting shares data with a government agency.

## Overlaps ("do both")
- Complements scam-number/email reputation tools and other national fraud reporting bodies (e.g. Action Fraud UK, FTC US) — use the relevant country's reporting site alongside identity-lookup tools.

## Trust & verifiability
`trust: trusted` — official Australian government (ACCC/NASC) resource; authoritative for scam trends and reporting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scamwatch |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | phone, email → associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
