---
id: thentiacloud-net
name: thentiacloud.net
description: Use when you have a `name` and want to confirm a person's professional registration/licence on a regulator's public register — returns registration status, registrant number, and profession/employer details.
url: https://coru.portaleu.thentiacloud.net/webs/portal/register/#/
category: public-records
path:
- public-records
bestFor: Searching a regulator's official public register (hosted on Thentia Cloud) to verify a practitioner's licence.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
- document-id
status: live
pricing: free
costNote: Free public register search; no account. Thentia Cloud is the platform vendor — the data belongs to the specific regulator hosting on it.
opsec: passive
opsecNote: Public regulatory registers are meant to be searched; doing so does not notify the registrant. Queries are logged by the platform/regulator; use a sock-puppet browser if attribution matters. Fully passive and non-intrusive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Thentia Cloud is a licensing platform used by official professional regulators to publish their public registers; the data is authoritative regulator data. This specific instance is a regulator's live register (e.g. CORU, Ireland's health & social care regulator).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- cpaverify-org
aliases:
- Thentia Cloud register
- CORU register
tags:
- professionlicensing
- Profession & Licensing Sites
- public-records
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# thentiacloud.net

> A regulator's official public register hosted on the Thentia Cloud platform: confirm whether a name is a registered, in-good-standing licensed professional.

## When to use
You have a `name` and need to verify a professional licence/registration against the issuing regulator's authoritative public register. Many professional regulators (this instance is CORU, Ireland's health & social care regulator) publish their registers on Thentia Cloud. A hit confirms the person's profession, registration number (`document-id`), status, and often the registered division/employer context — strong corroboration of identity and occupation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the regulator's register at its `*.thentiacloud.net` URL (e.g. the CORU register).
2. Search by surname/name (and profession/division where offered).
3. Read the registrant record: full name, registration number, status (registered / lapsed / removed / conditions), profession, and any public sanctions.
4. Pivot: the confirmed profession and registration number anchor identity; for US CPAs use `[[cpaverify-org]]`, and search the correct regulator's Thentia instance for other professions/countries.

## Inputs → Outputs
- **In:** `name` (optionally + profession)
- **Out:** confirmed `name`, registration `document-id`, profession/division (`employer-org` context), registration status
- **Empty/negative result looks like:** no match — the person isn't on *this* register (wrong regulator/country/profession), the name differs from the registered form, or they were removed; check the correct regulator before concluding.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — a public register; the registrant is not notified.
- Scope trap: each Thentia instance is one regulator's register only — a "not found" here says nothing about other professions or jurisdictions. Identify the right regulator first.

## Overlaps ("do both")
- Pairs with `[[cpaverify-org]]` (US CPAs) and other national regulator registers — together they cover different professions/countries; pick the register matching the claimed profession.

## Trust & verifiability
`trust: trusted` — the platform publishes official regulator data, so a confirmed registration is authoritative. The only caveat is choosing the correct regulator's instance; the record itself is first-party.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | thentiacloud-net |
| category | public-records |
| selectorsIn → selectorsOut | name → name, employer-org, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
