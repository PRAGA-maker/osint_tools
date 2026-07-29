---
id: imo-registry
name: IMO Registry
description: Use when you have an IMO number, ship name or shipping-company name (`document-id` / `employer-org`) and want official maritime particulars — returns owner/operator company and flag/geolocation detail.
url: http://webaccounts.imo.org/
category: transportation
path:
- transportation
bestFor: Authoritative lookups of ships, shipping companies and maritime incidents via the IMO's GISIS databases.
selectorsIn:
- document-id
- employer-org
selectorsOut:
- employer-org
- geolocation
status: live
pricing: free
costNote: Free public account. IMO Web Accounts is the single sign-on gateway to GISIS and other IMO apps; registration is required but costs nothing.
opsec: passive
opsecNote: Passive toward any individual — you are searching official vessel/company records, not contacting a person. Note that access is tied to your registered IMO Web Account, so use a research identity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the International Maritime Organization (a UN agency); GISIS is the authoritative registry of vessel and shipping-company data.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- IMO Web Accounts
- GISIS
tags:
- bellingcat-toolkit
- transport
- maritime
source: bellingcat-toolkit
lastVerified: '2026-07-29'
enrichment: full
---

# IMO Registry

> The International Maritime Organization's account gateway to GISIS — the official databases of ships, shipping companies and maritime incidents.

## When to use
You are working a maritime lead — a vessel name or IMO number, or the name of a shipping/management company — and want authoritative particulars: who owns/operates a ship, its flag state, IMO/company identifiers, and incident history. Useful in sanctions/vessel-tracking and, occasionally, missing-persons cases involving crew or shipping firms. Individuals are not directly listed, so relevance is to entities and vessels, not people.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://webaccounts.imo.org/ and create a free **Public Account** (this is the human-in-the-loop login gate) or sign in.
2. From the linked applications, open **GISIS** (Global Integrated Shipping Information System).
3. Choose the relevant GISIS module — e.g. Ship & Company particulars — and search by IMO number, ship name, or company name.
4. Read the record: registered owner/operator (`employer-org`), managing company, flag state and IMO identifiers (`geolocation` at flag/registry level).
5. Pivot: the owner/manager company name feeds corporate-registry and sanctions research; the flag state and IMO number feed live vessel-tracking tools (AIS/MarineTraffic).

## Inputs → Outputs
- **In:** IMO number / ship name (`document-id`) or shipping-company name (`employer-org`)
- **Out:** `employer-org` (registered owner, operator, manager), `geolocation` (flag state, registry)
- **Empty/negative result looks like:** "no records found" for a mistyped IMO/name, or a module that shows only summary data unless you drill into the specific sub-registry.

## Gotchas & OpSec
- Human-in-the-loop: a (free) IMO Web Account login is required before GISIS will open (`account-login`).
- OpSec: passive — you query official records, not a person. Access is logged to your account; use a research identity, not a personal one.
- GISIS spans several modules (ship particulars, company particulars, casualties, port reception, etc.) — pick the right one; a blank result in one module doesn't mean the vessel is absent from others.

## Overlaps ("do both")
- Use alongside live AIS trackers (MarineTraffic/VesselFinder) — this gives the authoritative owner/flag record, those give real-time position; together they tie a static registry entry to current movement.

## Trust & verifiability
`trust: trusted` — GISIS is maintained by the IMO (UN) and is the authoritative source for vessel/company particulars; it is the record other maritime tools derive from.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | imo-registry |
| category | transportation |
| selectorsIn → selectorsOut | document-id, employer-org → employer-org, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
