---
id: illegal-unreported-unregular-fishing-vessels-list
name: Illegal, unreported, unregular fishing Vessels List
description: Use when you have a vessel `name`, IMO/registration `document-id`, or call sign and want to check IUU-fishing blacklists — returns listing status, identifiers and owner leads.
url: https://iuu-vessels.org/Home/Search
category: transportation
path:
- transportation
bestFor: Checking whether a fishing vessel appears on the combined regional IUU (illegal/unreported/unregulated) blacklists and pulling its identifiers.
selectorsIn:
- name
- document-id
selectorsOut:
- document-id
- employer-org
- associate
status: live
pricing: free
costNote: Free and publicly searchable; no account required. Maintained by TMT (Trygg Mat Tracking) as an aggregated public reference.
opsec: passive
opsecNote: A read-only query against a public reference database — you are searching a blacklist, not contacting any vessel or owner, so nothing leaks to the subject. Standard web hygiene (optional VPN) is sufficient; the sensitivity here is in how you handle the findings, not the lookup.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Aggregates official IUU designations from 12 regional fisheries management organizations (CCAMLR, ICCAT, IOTC, NEAFC, NAFO, IATTC and others) via TMT; the underlying listings are authoritative government/RFMO records.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- IUU Vessel List
- Combined IUU vessels database
- iuu-vessels.org
tags:
- bellingcat-toolkit
- transport
- maritime
source: bellingcat-toolkit
lastVerified: '2026-07-29'
enrichment: full
---

# Illegal, unreported, unregular fishing Vessels List

> A combined, searchable database of vessels blacklisted for illegal, unreported and unregulated (IUU) fishing by the world's regional fisheries bodies.

## When to use
You have a fishing/maritime vessel identifier — current or historic `name`, IMO number, registration number (`document-id`), or IRCS call sign — and want to know whether it is flagged for IUU fishing and by which authority. Useful in maritime investigations, sanctions/compliance checks, supply-chain due diligence, and any case where a vessel's legitimacy is in question. Listed vessels frequently rename and reflag, so the historic-name search is the real value.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://iuu-vessels.org/Home/Search.
2. Search by current or historic vessel `name`, call sign, owner, or registration/IMO number.
3. Filter by the listing organization (CCAMLR, ICCAT, IOTC, etc.) or between currently- and previously-listed vessels.
4. Read the record: vessel names (including aliases), IMO, IRCS call sign, and which RFMO listed it and when.
5. Pivot: the IMO number is a stable key into vessel registries and AIS tracking; an owner/company name feeds corporate-registry and `employer-org`/`associate` research.

## Inputs → Outputs
- **In:** vessel `name` (current or historic) or `document-id` (IMO / registration / call sign)
- **Out:** listing status + `document-id` set (IMO, IRCS, aliases); leads to owner `employer-org` and `associate` links
- **Empty/negative result looks like:** no matching record — the vessel is not on any aggregated IUU list (which is not proof of legality, only that no RFMO has blacklisted that identifier).

## Gotchas & OpSec
- Passive lookup; nothing reaches the vessel or owner.
- IUU vessels routinely change name, flag and call sign to evade lists — always search historic names and the IMO (which does not change) rather than the current name alone.
- Coverage is limited to the participating RFMOs; a clean result only means "not on these lists."

## Overlaps ("do both")
- Pairs with AIS vessel-tracking and IMO/registry tools — this tells you a vessel is blacklisted; those tell you where it is and who owns it now.

## Trust & verifiability
`trust: trusted` — TMT compiles the list directly from official RFMO IUU designations, so entries are authoritative government-sourced records rather than crowd claims.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | illegal-unreported-unregular-fishing-vessels-list |
| category | transportation |
| selectorsIn → selectorsOut | name, document-id → document-id, employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
