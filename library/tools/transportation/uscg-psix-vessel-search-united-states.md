---
id: uscg-psix-vessel-search-united-states
name: USCG PSIX Vessel Search (United States)
description: Use when you have a US vessel `name`, official number, HIN, or call sign and want the documented vessel and its owner — returns name, address, document-id.
url: https://cgmix.uscg.mil/PSIX/PSIXSearch.aspx
category: transportation
path:
- transportation
bestFor: Resolving a US-documented vessel to its particulars and documented (managing) owner via the Coast Guard's PSIX register.
selectorsIn:
- name
- document-id
selectorsOut:
- name
- address
- document-id
status: live
pricing: free
costNote: Free public US Coast Guard service; no account required. FOIA is available for records not exposed in the online form.
opsec: passive
opsecNote: A passive query against a public federal register — the vessel owner is not notified. No login, so no account trail; standard clean-browser hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the U.S. Coast Guard (CGMIX/PSIX) — authoritative first-party federal vessel-documentation data.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- uscg-maritime-search-investigation-reports-united-states
aliases:
- USCG PSIX
- Port State Information Exchange
- CGMIX vessel search
tags:
- toddington
- specialty-search
- maritime
- transportation
source: toddington-resources
lastVerified: '2026-07-16'
enrichment: full
---

# USCG PSIX Vessel Search (United States)

> The US Coast Guard's public vessel register: a vessel name/number returns its particulars and — via the contact search — its documented owner.

## When to use
You have a US-flagged vessel tied to a subject — a `name` on a hull, an official/documentation number, a Hull Identification Number (HIN), or a radio call sign — and you want to confirm the vessel and reach its documented (managing) owner. Useful for linking a person to a boat, corroborating an ownership claim, or seeding an owner `name`/`address` from a vessel photographed or referenced in an investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cgmix.uscg.mil/PSIX/PSIXSearch.aspx.
2. Search by any known field: Vessel Name, Primary Vessel (official) Number, HIN, Call Sign, flag, service type, or build year.
3. Open the matching vessel for particulars: official number, HIN, call sign, service classification, tonnage, build year, and status.
4. Use the linked **PSIX Vessel Contact Search** to retrieve the documented/managing owner and mailing details where published.
5. Pivot: owner `name`/`address` feeds people-search; the call sign cross-references the ITU register; for records not shown online, note the vessel ID for a FOIA request.

## Inputs → Outputs
- **In:** vessel `name`, or a `document-id`-class identifier (official number, HIN, call sign)
- **Out:** owner `name` and mailing `address` (via contact search), plus the vessel's cross-identifiers (`document-id`: official number/HIN/call sign) and particulars
- **Empty/negative result looks like:** "no vessels found" — the vessel isn't federally documented (small/state-registered craft go through state DMV/boat registries instead, not PSIX).

## Gotchas & OpSec
- Human-in-the-loop: none; public web form.
- OpSec: **passive** — no owner notification.
- PSIX covers **federally documented** vessels (generally 5+ net tons); state-registered recreational boats won't appear — check the relevant state boat registry. Owner contact detail is the *documented* owner (often a company or managing owner), not necessarily the day-to-day operator.

## Overlaps ("do both")
- Pairs with `[[uscg-maritime-search-investigation-reports-united-states]]` — PSIX gives identity/ownership; the investigation reports give incidents/casualties involving the vessel.
- Cross-check the call sign against the ITU ship-station register for international corroboration.

## Trust & verifiability
`trust: trusted` — first-party US Coast Guard documentation data; identifiers and ownership are authoritative and independently checkable (with FOIA backing for deeper records).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | uscg-psix-vessel-search-united-states |
| category | transportation |
| selectorsIn → selectorsOut | name, document-id → name, address, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
