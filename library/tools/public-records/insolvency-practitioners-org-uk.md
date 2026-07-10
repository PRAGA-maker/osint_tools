---
id: insolvency-practitioners-org-uk
name: IPA Member Directory (insolvency-practitioners.org.uk)
description: Use when you have a `name` or firm and want to confirm a UK insolvency practitioner's licence, firm, and business address — returns name, employer-org, and address.
url: https://insolvency-practitioners.org.uk/ipa-search-members/
category: public-records
path:
- public-records
bestFor: Confirming a UK-licensed insolvency practitioner and their firm/business address.
selectorsIn:
- name
- employer-org
- address
selectorsOut:
- name
- employer-org
- address
status: live
pricing: free
costNote: Free, public directory operated by the Insolvency Practitioners Association. No account.
opsec: passive
opsecNote: Public professional directory; the search is anonymous and does not alert the subject. Returns business (not home) contact details.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Insolvency Practitioners Association (IPA), a UK Recognised Professional Body; the licence data is authoritative.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- companies-house
- gov-uk-find-an-insolvency-practitioner
aliases:
- IPA search members
- Insolvency Practitioners Association directory
tags:
- professionlicensing
- Profession & Licensing Sites
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# IPA Member Directory (insolvency-practitioners.org.uk)

> The Insolvency Practitioners Association's official member search — confirms a UK insolvency practitioner's licence, firm, and business address.

## When to use
You have a `name` (or firm/town) for someone who may work as a UK insolvency practitioner and want to confirm their professional identity and place of work. Useful for tying a person to an employer and a verifiable business `address`, or corroborating a claimed profession.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://insolvency-practitioners.org.uk/ipa-search-members/.
2. Search by surname, firm name, town/city, or postcode.
3. Read the result: practitioner name, firm name, full business address, contact details (phone/website/email), and membership type.
4. Pivot: the firm name feeds `[[companies-house]]` for directorships and filings; a no-match sends you to the government's cross-RPB register.

## Inputs → Outputs
- **In:** `name`, `employer-org` (firm), or `address` (town/postcode)
- **Out:** `name`, `employer-org` (firm), `address` (business), contact details
- **Empty/negative result looks like:** no listing — but note members can opt out of the directory, and IPs licensed by other Recognised Professional Bodies aren't here, so absence is not proof the person isn't a practitioner.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive**; anonymous public search. Addresses returned are business, not residential.
- Coverage gap: opt-outs and other RPBs mean this is not the full population — fall back to the gov.uk register.

## Overlaps ("do both")
- Pairs with `[[companies-house]]` — cross-reference the practitioner and firm for directorships, appointments, and registered addresses.
- Pairs with `[[gov-uk-find-an-insolvency-practitioner]]` — the government's cross-body register catches practitioners licensed by other RPBs and those who opted out here.

## Trust & verifiability
`trust: trusted` — first-party data from the IPA, an official Recognised Professional Body; a listing is authoritative for licence and firm, subject only to the opt-out/coverage caveat.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | insolvency-practitioners-org-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, address → name, employer-org, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
