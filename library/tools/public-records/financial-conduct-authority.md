---
id: financial-conduct-authority
name: Financial Conduct Authority
description: Use when you have a `name` or firm and want to check UK financial regulation status — the FCA Register returns regulated firms/individuals, their status and `employer-org` links.
url: https://register.fca.org.uk
category: public-records
path:
- public-records
bestFor: Verifying whether a person or firm is FCA-authorised in the UK and pulling their regulatory history, roles and linked firms.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
status: live
pricing: free
costNote: Free and public; no account needed to search the FCA Financial Services Register.
opsec: passive
opsecNote: An official public register — searching it is passive, anonymous, and never notifies the subject. Safe to query directly; no sock puppet required for the lookup itself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official register of the UK's financial regulator (FCA); authoritative for authorisation status, approved-person roles, and regulatory actions in the UK.
missingPersonsRelevance: low
coverage:
- gb
auth: none
api: true
localInstall: false
registration: false
aliases:
- FCA Register
- FCA Financial Services Register
- register.fca.org.uk
tags:
- corporate
- regulatory
- uk
source: metaosint
lastVerified: '2026-07-29'
enrichment: full
---

# Financial Conduct Authority

> The UK regulator's official register — the authoritative check on whether a person or firm is FCA-authorised, and a source of their regulatory roles, history and firm links.

## When to use
You have a `name` or firm (`employer-org`) connected to UK financial services — an adviser, broker, lender, insurer, crypto/e-money firm — and need to confirm they're **authorised**, see their permitted activities, and pull their regulatory history. Strong for due diligence, fraud/scam checks (unauthorised firms are a red flag), and identity corroboration: the register ties individuals to the firms they hold approved roles at, exposing an `associate`/employment network.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://register.fca.org.uk and search the individual's `name` or the firm name.
2. Open the record: authorisation status (authorised / no longer authorised / never authorised), permitted activities, and dates.
3. For a person, read their **approved/controlled functions** — which firms they're linked to and in what roles (the employment/association trail).
4. Note any regulatory actions, warnings, or "unauthorised firm" flags.
5. Pivot: linked firms → Companies House and corporate research; an unauthorised/clone-firm warning → scam investigation.

## Inputs → Outputs
- **In:** `name` or `employer-org` (firm)
- **Out:** authorisation status, regulatory history, and `employer-org`/`associate` links (individual↔firm roles)
- **Empty/negative result looks like:** "no results" or "not authorised" — the person/firm isn't FCA-regulated; for financial services that's itself a significant (often adverse) finding, not a dead end.

## Gotchas & OpSec
- UK-only scope — for other jurisdictions use their national regulators.
- "Not on the register" for a firm claiming to be regulated is a strong fraud signal (check for **clone firm** warnings using exact names).
- Individuals only appear if they hold/held a regulated role; ordinary customers won't be listed.

## Overlaps ("do both")
- Pairs with Companies House and corporate-registry tools — the FCA gives regulatory status and person↔firm roles; those give ownership, directorships and filings for the linked firms.

## Trust & verifiability
`trust: trusted` — the UK financial regulator's official first-party register; authoritative for authorisation status and regulatory actions within the UK.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | financial-conduct-authority |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
