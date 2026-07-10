---
id: citma-org-uk
name: CITMA – Find a Chartered Trade Mark Attorney
description: Use when you have a `name`, `employer-org` or location and want to verify a UK chartered trade mark attorney — returns the attorney's name, firm and business address.
url: https://www.citma.org.uk/find-a-chartered-trade-mark-attorney.html
category: public-records
path:
- public-records
bestFor: Verifying that someone is a chartered trade mark attorney (CITMA member) and finding their firm and business address.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- name
- address
- employer-org
status: live
pricing: free
costNote: Free public "find an attorney" directory; no account or payment.
opsec: passive
opsecNote: A public professional-directory lookup; the subject is not notified and no login is required.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: CITMA is the UK professional body for trade mark attorneys; its member directory is the authoritative source for chartered-status verification.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- aat-org-uk
aliases:
- Chartered Institute of Trade Mark Attorneys
- CITMA directory
tags:
- professionlicensing
- Profession & Licensing Sites
- uk
- legal
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# CITMA – Find a Chartered Trade Mark Attorney

> The Chartered Institute of Trade Mark Attorneys' directory: confirm someone really is a chartered trade mark attorney and find their firm and address.

## When to use
You have a `name` (or firm `employer-org`, or a location) for someone presented as a UK trade mark / IP attorney and want to verify the credential and locate them. CITMA's directory confirms chartered membership and returns the attorney's firm and business `address`. Use it to validate a professional claim (a bogus "chartered attorney" is a red flag), get an authoritative work address, or find IP attorneys in an area tied to a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.citma.org.uk/find-a-chartered-trade-mark-attorney.html.
2. Search by attorney `name`, firm (`employer-org`), or location.
3. Read the listing: attorney `name`, firm, and business `address`.
4. Match the claimed credential to the directory — presence confirms CITMA membership; absence contradicts a "chartered trade mark attorney" claim.
5. Pivot: the firm/`address` feeds Companies House and people-search; a confirmed name anchors professional identity.

## Inputs → Outputs
- **In:** `name`, `employer-org`, or `address`/location
- **Out:** attorney `name`, firm (`employer-org`), business `address`
- **Empty/negative result looks like:** no match. Meaningful in itself — a person claiming to be a chartered trade mark attorney who isn't listed is a discrepancy (they may be a patent attorney under CIPA, or unqualified). Check the right professional body.

## Gotchas & OpSec
- Specific to chartered *trade mark* attorneys — patent attorneys are a separate body (CIPA), and solicitors are on the SRA roll. Match the register to the exact credential claimed.
- UK-focused.
- OpSec: passive; a public-directory read with no login.

## Overlaps ("do both")
- Pairs with `[[aat-org-uk]]` and other professional registers — verify the specific credential against its own body, then use Companies House to link the person to their firm.

## Trust & verifiability
`trust: trusted` — CITMA is the UK professional body for trade mark attorneys, so its directory is authoritative for chartered status. Just confirm you're checking the correct body for the specific professional title in question.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | citma-org-uk |
</content>
