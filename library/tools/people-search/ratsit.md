---
id: ratsit
name: Ratsit
description: Use when you have a `name` or `phone` in Sweden and want the person's address, age, and household — returns `address`, `phone`, `dob`, `associate`, and `employer-org`.
url: https://www.ratsit.se/
category: people-search
path:
- people-search
bestFor: Resolving a Swedish person to a current address, age, neighbours, and company/vehicle links from a name or number.
selectorsIn:
- name
- phone
selectorsOut:
- address
- phone
- dob
- associate
- employer-org
status: live
pricing: freemium
costNote: Basic person and address search (name, age, address, phone) is free without login. Full credit-history reports, previous addresses, and detailed profiles require a paid subscription or one-off purchase, and pulling a formal credit report notifies the subject by law.
opsec: passive
opsecNote: Free searches are passive against the subject — you query Ratsit, not the person. BUT a formal "kreditupplysning" (credit check) triggers a legally mandated notice letter to the subject; never run one during a covert inquiry. Ratsit itself logs your session; use a sock-puppet browser and consider whether your own IP/account matters.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Commercial aggregator, but its data is drawn from official Swedish registries (Skatteverket/tax agency, SCB, Bolagsverket, Transportstyrelsen, Lantmäteriet) under Sweden's freedom-of-information framework; registered as a media outlet.
missingPersonsRelevance: high
coverage:
- se
auth: none
api: false
localInstall: false
registration: false
aliases:
- Ratsit.se
- Ratsit Personsök
tags:
- bellingcat-toolkit
- people
source: bellingcat-toolkit
lastVerified: '2026-07-11'
enrichment: full
---

# Ratsit

> Sweden's largest open people-and-company search: name or number in, address / age / neighbours / vehicles out — thanks to Sweden's unusually open personal-data laws.

## When to use
Your subject is (or was) resident in Sweden and you have a `name` or `phone`. Because Swedish tax, address, vehicle, and company registers are legally public, Ratsit turns even a common name into a shortlist with birth year, current address, phone, household members, and links to companies and cars they own — a level of detail rarely available elsewhere for free.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.ratsit.se/ (Swedish; use browser translation if needed).
2. Enter the `name` (or `phone`, or personnummer if you already have it) in the search box.
3. Pick the matching person from the results — disambiguate by birth year and locality.
4. Read the profile: current `address`, birth year (`dob`), gender, registered `phone`, number of recent address changes, neighbours/household (`associate`), and any company or vehicle ownership (`employer-org`).
5. Stop at the free tier for covert work. Pivot: feed the address into Swedish map/property tools, the company into `[[bolagsverket]]`-style registries, neighbours into further Ratsit lookups.

## Inputs → Outputs
- **In:** `name` (best with a city/region) or `phone` / personnummer
- **Out:** `address`, `dob` (birth year), `phone`, `associate` (household/neighbours), `employer-org` (companies owned), vehicle links
- **Empty/negative result looks like:** "Inga träffar" (no hits) — the person may be under 16, have a protected-identity marker (skyddad identitet), or not be Swedish-registered. Protected identities are deliberately suppressed and their absence is not proof of anything.

## Gotchas & OpSec
- A formal credit check (kreditupplysning) sends the subject a notification letter — do **not** trigger one covertly. The free person/address search does not.
- Common names return many hits; always confirm with birth year + location before trusting a result.
- Data reflects the official registered address, which can lag a real move by weeks.

## Overlaps ("do both")
- Pairs with `[[hitta-se]]`/`[[eniro]]`-style Swedish directories and `[[merinfo-se]]` — cross-check the same person across aggregators because each buys slightly different register slices and one fills the other's gaps.

## Trust & verifiability
`trust: trusted` — the underlying data is sourced from Swedish government registries, so address/age fields are authoritative; only recency (registered vs. actual address) is the caveat.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ratsit |
| category | people-search |
| selectorsIn → selectorsOut | name, phone → address, phone, dob, associate, employer-org |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
