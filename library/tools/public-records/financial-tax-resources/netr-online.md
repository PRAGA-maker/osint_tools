---
id: netr-online
name: NETR Online
description: Use when you have a US address or property-owner name and want county deeds, tax-assessor records, and parcel data — returns address, associates, and ownership history.
url: https://publicrecords.netronline.com/
category: public-records
path:
- public-records
- financial-tax-resources
bestFor: Finding the right county assessor/recorder site and jumping straight to property, deed, and tax records for a US parcel or owner.
input: Address, county name, owner name
output: Property deeds, tax records, assessments
selectorsIn:
- address
- name
selectorsOut:
- address
- associate
- name
status: live
pricing: free
costNote: Free, ad-supported portal; an optional paid tier removes ads. The county records it links to are free to browse, though some counties charge for full document images.
opsec: passive
opsecNote: NETR is a directory; searches happen on the destination county site. County record systems commonly log lookups and some require accepting a disclaimer. No target is notified. Use a clean browser for sensitive parcels.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-established, widely cited portal maintained by NETROnline; the actual records are first-party county/government data.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- NETROnline
- NETR Public Records Online
- publicrecords.netronline.com
tags:
- public-records
- property
- real-estate
- us-counties
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# NETR Online

> A nationwide directory that routes you to the correct US county assessor, treasurer, and recorder websites — the fastest way to reach real property, deed, and tax data for a given parcel or owner.

## When to use
You have a US `address` or an `name` (property owner) and want to establish who owns a parcel, its transaction history, and tax details. Because deeds name grantors, grantees, and often spouses or co-owners, property records are a strong source of `associate` links and confirmed `address` history for a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://publicrecords.netronline.com/ and drill down: choose the state, then the county.
2. NETR shows what that county publishes online — Assessor (ownership + valuation), Recorder/Register of Deeds (deeds, mortgages, liens), Treasurer/Tax (bills, delinquencies), and parcel maps (GIS). Pick the office you need.
3. Follow the link into the county's own system and search by owner name or property address (accept any disclaimer the county requires).
4. Read the record: current owner, mailing vs. situs address, sale/deed history with named parties, and assessed value. Pivot: a co-grantee is an `associate`; a mailing address that differs from the property is a lead to where the owner actually lives.

## Inputs → Outputs
- **In:** `address` or owner `name`
- **Out:** `address` (situs + mailing), `associate` (co-owners, grantors/grantees), `name` (confirmed owner)
- **Empty/negative result looks like:** "no data online for this county" (NETR provides a phone number instead), or a county search that returns no matching parcel/owner — coverage genuinely varies county to county.

## Gotchas & OpSec
- Human-in-the-loop: none on NETR itself; individual county sites may add a disclaimer click, a CAPTCHA, or a fee for full document images.
- OpSec: passive; nothing notifies the owner. County portals may log your IP — use a clean browser for sensitive work.
- Coverage is uneven: rural counties may have little or nothing online. A blank result reflects that county's digitization, not the absence of a record.

## Overlaps ("do both")
- Pairs with people-search and address-history tools — NETR gives you authoritative deed/owner data from the source, while a people-search aggregator adds phones and relatives that property records omit.

## Trust & verifiability
`trust: community` — NETR is a reputable, long-running index, and the records it links to are first-party government data you can verify directly on the county site.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | netr-online |
| category | public-records |
| selectorsIn → selectorsOut | address, name → address, associate, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
