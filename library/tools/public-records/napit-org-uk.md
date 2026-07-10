---
id: napit-org-uk
name: NAPIT Installer Search
description: Use when you have a UK tradesperson `name`, `employer-org` or postcode and want to verify NAPIT registration — returns the registered business name, address and trades covered.
url: https://search.napit.org.uk/
category: public-records
path:
- public-records
bestFor: Verifying that a UK electrician/heating/plumbing installer is NAPIT-registered and finding their business name, address and registered trades.
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
costNote: Free public installer-search directory; no account or payment to search.
opsec: passive
opsecNote: A public competent-person register lookup; the subject is not notified and no login is required.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: NAPIT is a UK government-approved competent-person scheme operator; its register is an authoritative source for whether an installer is NAPIT-registered.
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
- National Association of Professional Inspectors and Testers
- NAPIT search
tags:
- professionlicensing
- Profession & Licensing Sites
- uk
- tradesperson
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# NAPIT Installer Search

> NAPIT's public register: confirm a UK electrical/heating/plumbing installer is registered under this competent-person scheme, and find their business name, address and trades.

## When to use
You have a UK tradesperson or firm — an electrician, plumber, heating or renewables installer — identified by `name`, `employer-org`, or working area (postcode), and you want to verify their NAPIT registration or locate registered installers near a place. Use it to check a credential (an unregistered person claiming NAPIT membership is a red flag), to get an authoritative business `address`, or to enumerate installers in an area tied to a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://search.napit.org.uk/.
2. Search by installer/business `name`, or by postcode/location to list registered installers nearby; filter by trade where offered.
3. Read a listing: registered business `name`, `address`, and the specific trades/work categories the installer is registered for.
4. Match the claimed credential to the register — presence confirms current NAPIT registration; absence contradicts the claim.
5. Pivot: a business `address`/`employer-org` feeds Companies House and people-search; a confirmed trade scope corroborates the person's line of work.

## Inputs → Outputs
- **In:** `name`, `employer-org`, or `address`/postcode
- **Out:** registered installer `name`, business `address`, registered trades
- **Empty/negative result looks like:** no match. Meaningful in itself — someone claiming NAPIT registration who is absent may be unregistered or registered with a *different* competent-person scheme (e.g. NICEIC, Gas Safe for gas), so check the right body.

## Gotchas & OpSec
- Registration is trade-specific; being registered for electrical work doesn't imply registration for other trades — read the scope.
- Gas work is covered by the separate Gas Safe Register, not NAPIT — use the correct scheme for the trade claimed.
- UK-only.
- OpSec: passive; a public-register read with no login.

## Overlaps ("do both")
- Pairs with `[[aat-org-uk]]` and other professional/trade registers — different schemes cover different trades; when vetting a firm, check the register that matches the specific credential, then Companies House for the business entity.

## Trust & verifiability
`trust: trusted` — NAPIT is a government-approved competent-person scheme operator, so its register is authoritative for NAPIT registration status. Just ensure you are checking the correct scheme for the specific trade in question.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | napit-org-uk |
</content>
