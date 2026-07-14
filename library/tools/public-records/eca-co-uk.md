---
id: eca-co-uk
name: ECA — Find a Member (Electrical Contractors' Association)
description: Use when you have a company `name`, `address`/area, or trade and want to confirm a UK electrical contractor is an ECA member — returns the member `employer-org` with location and areas of work.
url: https://www.eca.co.uk/find-a-member
category: public-records
path:
- public-records
bestFor: Verifying that a UK electrical/electrotechnical contractor is a registered ECA member and finding its location and scope of accredited work.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- employer-org
- address
- name
status: live
pricing: free
costNote: The member directory search is free and public; some deeper member-only content requires an employer-linked registration, but the find-a-member lookup does not.
opsec: passive
opsecNote: A read-only search of a trade-association directory — no subject notification. The site sees your IP/query like any website; a sock-puppet browser suffices for sensitive lookups.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The ECA (Electrical Contractors' Association) is the recognised UK trade body; membership listings are first-party and reliable for who is an accredited member.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Electrical Contractors' Association find a member
- eca.co.uk
tags:
- professionlicensing
- Profession & Licensing Sites
- uk
- trade-association
- electrical
source: uk-osint
lastVerified: '2026-07-13'
enrichment: full
---

# ECA — Find a Member (Electrical Contractors' Association)

> The UK electrotechnical trade body's public member directory — confirms whether a contractor is an accredited ECA member and where it operates.

## When to use
You have a company `name`, a rough `address`/area, or a trade description and want to establish whether a UK electrical/electrotechnical contractor is a bona-fide ECA member. This corroborates a subject's stated employer or business, checks the legitimacy of a contractor, or ties a person to a registered firm operating in a given area.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.eca.co.uk/find-a-member.
2. Search by company name, or by location with a distance radius (0–5 miles up to nationwide), and optionally filter by area of work (e.g. fire detection, HVAC) or company size.
3. Read the results: member company names with location and accredited areas of work.
4. Pivot: a confirmed member `employer-org` + `address` feeds Companies House and other business-registry lookups; the location narrows a person-to-firm tie.

## Inputs → Outputs
- **In:** `name` (company), `address`/area, or trade (`employer-org` context)
- **Out:** member `employer-org`, `address`/location, accredited areas of work
- **Empty/negative result looks like:** no matching member — the firm is not an ECA member (many legitimate electricians belong to other bodies like NICEIC/NAPIT instead), not proof the business doesn't exist.

## Gotchas & OpSec
- Membership is voluntary: absence from ECA does not mean unqualified — cross-check other UK competent-person schemes.
- This is a business/company directory, not a people register; use it to anchor a firm, then pivot to person-level records.
- OpSec: passive; a routine directory lookup.

## Overlaps ("do both")
- Pairs with UK company registries and other profession/licensing registers — ECA confirms trade-body accreditation, while Companies House gives the legal entity, directors and address.

## Trust & verifiability
`trust: trusted` — first-party listings from the recognised UK trade association; authoritative for ECA membership specifically.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | eca-co-uk |
