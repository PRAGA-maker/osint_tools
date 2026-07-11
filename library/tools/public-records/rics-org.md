---
id: rics-org
name: RICS Find a Member/Firm
description: Use when you have a `name` or `employer-org` and want to verify a chartered surveyor's RICS membership — returns the member/firm's professional standing and regulated-firm details.
url: https://www.rics.org/networking/find-a-member
category: public-records
path:
- public-records
bestFor: Confirming that a person or firm is genuinely RICS-qualified/regulated (chartered surveyor, valuer) and surfacing the associated firm.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
status: live
pricing: free
costNote: Free public directory from the professional body; no account required.
opsec: passive
opsecNote: An official membership directory — searching it is passive and notifies no one. It exposes professional, not personal-home, details, so privacy risk is low.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Royal Institution of Chartered Surveyors (RICS), the professional body itself; authoritative on who is a current member/regulated firm.
missingPersonsRelevance: medium
coverage:
- uk
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- rics.org find a member
- RICS find a surveyor
tags:
- professionlicensing
- Profession & Licensing Sites
- surveyor
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# RICS Find a Member/Firm

> The Royal Institution of Chartered Surveyors' own directory — the authoritative way to confirm a "chartered surveyor" claim and tie the person to a regulated firm.

## When to use
You have a `name` (or `employer-org`) and need to verify a professional claim in the property/surveying/valuation world — a frequent vector for fraud (bogus valuers, fake surveys). RICS's directory lists current members and RICS-regulated firms, so a hit confirms the credential and links the individual to a firm; a miss undercuts the claim. Reach for it when a subject presents as a chartered surveyor or valuer.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.rics.org/networking/find-a-member.
2. Search by member `name`, firm (`employer-org`), or location/specialism.
3. Read the result: membership grade/standing and the regulated firm's details.
4. Cross-check the firm against Companies House for ownership and status.
5. Pivot: a confirmed firm (`employer-org`) opens corporate-records and colleague research; a *no-match* is evidence against a claimed chartered status.

## Inputs → Outputs
- **In:** `name` or `employer-org`
- **Out:** confirmed member `name`, membership standing, and regulated firm (`employer-org`)
- **Empty/negative result looks like:** no match — the person/firm is not a current RICS member/regulated firm (or is listed under a different name); treat absence as a red flag against a chartered-surveyor claim, after checking name variants.

## Gotchas & OpSec
- Scope: covers RICS membership only — a genuine surveyor might belong to a different body, so absence isn't absolute disqualification, just a flag.
- Professional data only: no home addresses or personal contact — this verifies credentials, it doesn't locate people.
- OpSec: passive official directory.

## Overlaps ("do both")
- Pairs with `[[justice-gov-uk]]` and other professional registers — the same verify-the-credential pattern across professions.
- Pairs with Companies House-style company lookups to connect the member to their firm's filings.

## Trust & verifiability
`trust: trusted` — a first-party professional-body directory; membership facts are authoritative, with the only caveat being scope (RICS-specific).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rics-org |
