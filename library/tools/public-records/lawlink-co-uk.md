---
id: lawlink-co-uk
name: Lawlink NI
description: Use when you have a `name` or `address` in Northern Ireland and want registered/unregistered land, charges, bankruptcy and court-judgement records — returns address, employer-org, name, and document-id via a paid professional search.
url: http://www.lawlink.co.uk/
category: public-records
path:
- public-records
bestFor: Ordering authoritative Northern Ireland property, deeds, bankruptcy and court-judgement searches (Registry of Deeds / Land Registry).
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- address
- employer-org
- name
- document-id
status: live
pricing: freemium
costNote: Commercial law-search firm, not a free public database. You order searches (Registry of Deeds, Land Registry, Statutory Charges, bankruptcy, Queen's/King's Bench & Chancery judgements) and pay per search; results are returned next-day or same-day by email/post. No instant self-serve lookup.
opsec: active
opsecNote: Ordering a search discloses the subject's name/address to a commercial firm and creates a client paper trail tied to you. It is built for solicitors/lenders doing conveyancing due diligence — not anonymous research. Assume the order is logged against your account.
humanInLoop: true
humanInLoopReason:
- manual-review
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Established Northern Ireland law-search company (60+ years), handling roughly a third of NI property-transaction searches. Authoritative for NI land/charges/court records, but B2B — access requires being a client, not a public API.
missingPersonsRelevance: high
coverage:
- uk
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
relatedTools:
- gov-uk-land-registry
aliases:
- lawlink.co.uk
- Lawlink Northern Ireland
tags:
- propertysites
- Property Related Sites
- northern-ireland
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Lawlink NI

> Northern Ireland's long-established law-search bureau — the professional route to NI deeds, land, charges, bankruptcy and court-judgement records that aren't in a public web search.

## When to use
Your subject has a Northern Ireland connection and you need authoritative land/property ownership, statutory charges, bankruptcy status, or Queen's/King's Bench and Chancery judgements tied to a `name` or `address`. This is a paid, professional-grade route used in conveyancing due diligence — reach for it when free registers (e.g. GB Land Registry) don't cover NI and the record is worth paying for.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.lawlink.co.uk/ and review the search types (Registry of Deeds for unregistered property, Land Registry for registered land, Statutory Charges, company/bankruptcy, court judgements).
2. Set up a client account / make contact (they serve solicitors, lenders and professional bodies).
3. Submit the search request with the `name`/`address`/`employer-org` you hold.
4. Receive results next-day or same-day by email and/or post.
5. Pivot: a `document-id` (deed/title) or co-owner `name` feeds further land-registry and associate mapping.

## Inputs → Outputs
- **In:** `name`, `address`, or `employer-org`
- **Out:** `address` (property/title), `employer-org` (company records), `name` (owners/associates), `document-id` (deed/judgement references)
- **Empty/negative result looks like:** a nil-return search report meaning no matching charge/judgement/title — that is itself evidentially useful, not a failed lookup.

## Gotchas & OpSec
- Human-in-the-loop: it is a manually-fulfilled paid service (payment + turnaround), not an instant lookup — plan for the delay and cost.
- Scope is **Northern Ireland only**; for England & Wales use HM Land Registry, for Scotland use Registers of Scotland.
- OpSec: active — ordering ties the query to your client identity; unsuitable for covert research.

## Overlaps ("do both")
- Pairs with HM Land Registry / gov.uk tools which cover GB but not NI — Lawlink fills the Northern Ireland gap.
- Combine with Companies House lookups when the subject is tied to a business, to cross-reference directors and charges.

## Trust & verifiability
`trust: community` — a decades-established, reputable NI search bureau drawing on official registers, so record quality is high; the limitation is access (paid/B2B) not accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lawlink-co-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → address, employer-org, name, document-id |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (manual-review, payment-wall-partial) |
