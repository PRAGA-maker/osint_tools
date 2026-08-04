---
id: online-services-pei-business-corporate-registry
name: PEI Business / Corporate Registry
description: Use when you have a `name` or company operating in Prince Edward Island, Canada and want its registry record — returns corporation status, directors/officers, and addresses.
url: https://www.princeedwardisland.ca/en/feature/pei-business-corporate-registry-original#/service/LegacyBusiness/LegacyBusinessSearch
category: public-records
path:
- public-records
bestFor: Looking up a Prince Edward Island company or business name to link people to corporate entities and addresses.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- name
- address
- associate
status: live
pricing: free
costNote: Free official government search; full certified copies of documents may carry a fee, but the search and basic record view are free.
opsec: passive
opsecNote: Searching a government corporate registry is passive — no subject is notified. The registry is a public record; only your own request is logged by the province's site (which sits behind Radware bot protection).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Government of Prince Edward Island — an authoritative primary source for PEI corporate records.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- PEI Corporate Registry
- Prince Edward Island Business Registry
tags:
- corporate-registry
- canada
- public-records
- business-search
source: osint4all
lastVerified: '2026-08-04'
enrichment: full
---

# PEI Business / Corporate Registry

> Prince Edward Island's official corporate registry search — the authoritative way to tie a person to a PEI company, its officers, and its registered address.

## When to use
Your subject or a company of interest has a connection to Prince Edward Island, Canada, and you want the official corporate record: is the company registered and in good standing, who are its directors/officers, and what registered/mailing `address` is on file? Corporate registries are a high-value people-to-entity bridge — a `name` on a directorship links a person to a business, co-directors (`associate`s), and physical addresses.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the PEI Business / Corporate Registry search (link above); pass the browser bot-check if prompted.
2. Search by business `name`/`employer-org` (or browse the corporate registry search).
3. Open the matched entity: read its status, incorporation date, registered `address`, and listed directors/officers (`name`s and `associate` links).
4. Cross-reference: the same person on multiple filings reveals a business network; a registered address is a physical-location lead.
5. Pivot: officer `name`s → people-search; the `address` → property/maps lookups; co-directors → association mapping.

## Inputs → Outputs
- **In:** business `name` / `employer-org` (or a person to match against filings)
- **Out:** `employer-org` record, director/officer `name`s, `address`, `associate` links
- **Empty/negative result looks like:** no matching entity — the business isn't PEI-registered (try the correct province's registry), or the name/spelling differs; PEI covers only PEI-registered entities.

## Gotchas & OpSec
- Human-in-the-loop: an occasional Radware browser-verification screen; solve it and proceed. Certified document copies may cost a fee.
- OpSec: **passive** — a public government record; the subject is not notified.
- Jurisdiction-bound: this is PEI only. For a company elsewhere, use that province's/country's registry.

## Overlaps ("do both")
- Pairs with federal and other-provincial Canadian registries (e.g. Corporations Canada) — a person may hold directorships across jurisdictions, so run the relevant registries together to see the full corporate footprint.

## Trust & verifiability
`trust: trusted` — a first-party government registry, authoritative for PEI corporate records; the filings are primary-source evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | online-services-pei-business-corporate-registry |
