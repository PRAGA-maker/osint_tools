---
id: nidirect-gov-uk-3
name: NI Landlord Registration Scheme (Public Register)
description: Use when you have a landlord's name or a Northern Ireland property and want to confirm registration — returns whether a landlord/property is on the NI register.
url: https://www.communities-ni.gov.uk/articles/landlord-registration-scheme
category: public-records
path:
- public-records
bestFor: Checking whether a person is a registered NI landlord, or who is registered against a Northern Ireland rental property.
selectorsIn:
- name
- address
selectorsOut:
- name
- address
- employer-org
status: live
pricing: free
costNote: Free public register search; no account required.
opsec: passive
opsecNote: Searching a public government register is passive and does not alert the landlord. The service logs standard web access; use a VPN for sensitive lookups and stay within lawful public-record use.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the NI Department for Communities; the register is an official government record of landlords registered under the statutory scheme.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- Northern Ireland Landlord Registration
- NI landlord register search
- Landlord Registration Scheme NI
tags:
- propertysites
- Property Related Sites
- landlord-register
- northern-ireland
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# NI Landlord Registration Scheme (Public Register)

> Northern Ireland's statutory landlord register — search by a landlord's name or a property to confirm who is registered as letting it.

## When to use
You have a `name` you think lets property in Northern Ireland, or an NI rental `address` and want to know who is behind it. Every private landlord in NI must register, and the public can search that register two ways: **by landlord name** (confirming a person is a registered landlord) or **by property** (finding the registered landlord for an address). That link between a person and a property is strong corroboration for location, assets and identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the scheme page at https://www.communities-ni.gov.uk/articles/landlord-registration-scheme and follow the register search links.
2. Choose **Landlord Search** (enter a `name`) or **Property Search** (enter `address`/property details).
3. Read the result: whether a matching landlord/property is registered, and the registration details shown.
4. Treat a confirmed registration as tying that person to letting activity at/around that property.
5. Pivot: a confirmed landlord name + property feeds Land Registry/property tools and people-search; a property feeds address-history and electoral-roll work.

## Inputs → Outputs
- **In:** a landlord `name`, or an NI property `address`
- **Out:** registration status, registered landlord `name`, and property `address` (a landlord may register as an individual or `employer-org`)
- **Empty/negative result looks like:** no matching registration — the person may not be an NI landlord, may let via an agent/company, or may be non-compliant. Absence is not proof they own no NI property.

## Gotchas & OpSec
- Covers **Northern Ireland only** — not England/Wales/Scotland, which have separate (and mostly non-public) schemes.
- Registration is per the landlord's declared details; a property let through a letting agent or company may show the agent/company, not the beneficial owner.
- Passive and lawful public-record use; the register does not notify the landlord.

## Overlaps ("do both")
- Pairs with Land Registry / property tools to move from "registered landlord" to registered title ownership.
- Feeds people-search once a landlord name and property are confirmed.

## Trust & verifiability
`trust: trusted` — an official NI Department for Communities statutory register, so a positive match is authoritative for registration status; confirm ownership separately via Land Registry, since registration and legal title are different things.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nidirect-gov-uk-3 |
| category | public-records |
| selectorsIn → selectorsOut | name, address → name, address, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
