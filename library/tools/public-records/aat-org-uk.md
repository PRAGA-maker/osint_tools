---
id: aat-org-uk
name: AAT Licensed Members Directory
description: Use when you have an accountant/bookkeeper `name` or a UK location and want to verify AAT-licensed status — returns member/firm name, business address and services.
url: https://www.aat.org.uk/licensed-members/directory
category: public-records
path:
- public-records
bestFor: Confirming a person or firm is an AAT-licensed accountant/bookkeeper and finding their business address and offered services.
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
costNote: Free public "find a licensed member" directory; no account or payment to search.
opsec: passive
opsecNote: A public professional-register lookup; the subject is not notified and no login is required, so activity is not tied to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: AAT (Association of Accounting Technicians) is an established UK professional body; its licensed-members register is the authoritative source for who it licenses.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- ukas-com
aliases:
- Association of Accounting Technicians
- AAT directory
tags:
- professionlicensing
- Profession & Licensing Sites
- uk
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# AAT Licensed Members Directory

> The Association of Accounting Technicians' public register: verify that a UK accountant/bookkeeper is AAT-licensed and find their practice address and services.

## When to use
You have a `name` (or firm `employer-org`) claiming to be an AAT-licensed accountant or bookkeeper, or you want to find licensed practitioners in a UK `address`/area. Use it to verify a professional credential (an unlicensed person claiming AAT membership is a fraud flag), to get an authoritative business `address`, or to enumerate practitioners near a location tied to a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.aat.org.uk/licensed-members/directory.
2. Search by member/firm `name`, or by location (town/postcode) to list licensed members nearby.
3. Read a listing: member or practice `name`, business `address`, and the accountancy/bookkeeping services they are licensed to provide.
4. Match the claimed credential to the register — presence confirms current AAT licensure; absence contradicts a membership claim.
5. Pivot: a business `address`/`employer-org` feeds Companies House and people-search; a confirmed name anchors identity.

## Inputs → Outputs
- **In:** `name`, `employer-org`, or `address`/location
- **Out:** licensed member/firm `name`, business `address`, licensed services
- **Empty/negative result looks like:** no match. Meaningful in itself — someone claiming to be an AAT licensed member who is absent from the register is a discrepancy worth flagging (they may be a student/affiliate member, which is not the same as licensed).

## Gotchas & OpSec
- Only *licensed* members in practice appear; AAT has other membership grades (student, affiliate) that are not the same as a practising licence.
- UK-only; other accountancy bodies (ICAEW, ACCA, etc.) maintain separate registers — check the right one for the credential claimed.
- OpSec: passive; a public-register read with no login.

## Overlaps ("do both")
- Pairs with `[[ukas-com]]` and other licensing registries — AAT verifies an *individual* practitioner; UKAS verifies an *organisation's* accreditation. Do both when vetting a finance professional and their firm.
- Follow with Companies House to link the practitioner to registered companies.

## Trust & verifiability
`trust: trusted` — AAT is a recognised UK professional body and this is its official licensed-members register, so licensure status is authoritative. Just confirm you are checking the correct professional body for the specific credential claimed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | aat-org-uk |
</content>
