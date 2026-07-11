---
id: doximity-united-states
name: Doximity (United States)
description: Use when you have a `name` and believe the subject is a US clinician (doctor, PA, NP) and want their verified professional profile, specialty and workplace — returns `social-profile`, `employer-org`, `address`.
url: https://www.doximity.com
category: social-networks
path:
- social-networks
bestFor: Confirming and locating a US healthcare professional — specialty, credentials and practice location.
selectorsIn:
- name
- employer-org
selectorsOut:
- social-profile
- employer-org
- address
status: live
pricing: freemium
costNote: Free for verified US clinicians (identity-gated). Non-clinicians can view public "Doximity Dialer"/directory profile pages surfaced via search engines, but full network features require a verified clinician account.
opsec: passive
opsecNote: Public profile pages can be read passively (often via Google) without logging in. Do NOT try to register as a clinician you are not — verification is identity-checked and impersonation is both detectable and a legal/ethics problem.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Doximity is a publicly traded, verified network of US healthcare professionals; profiles are credential-checked, so specialty/licensure data is high quality.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Doximity
tags:
- toddington
- curated-directory
- social-media
- healthcare
- medical
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# Doximity (United States)

> The LinkedIn of US medicine: a credential-verified network of 3M+ US clinicians, useful for confirming that a subject is a real practitioner and where they practice.

## When to use
You have a `name` and reason to think the subject is a US physician, PA, NP or medical student, and you want to verify that professionally and locate their practice. Because membership is identity/credential-verified, a Doximity profile is strong corroboration of specialty, training and current employer — valuable when a missing person or a person of interest is a healthcare worker whose workplace narrows their whereabouts.

## How to use it (`bestInteractionPattern`: web-manual)
1. Search a public engine for the subject on Doximity: `site:doximity.com "First Last"` or `"First Last" doximity <specialty/city>`. Many profile pages are indexed and readable without login.
2. Open the profile page: read name, specialty, credentials (MD/DO/PA/NP), medical school, residency, and listed practice location/employer.
3. If you have a verified clinician account (and are entitled to one), the in-network directory lets you search by name, specialty and location directly.
4. Corroborate the listed workplace with the practice's own site and state licensing board records.
5. Pivot: feed the `employer-org` and practice `address` into mapping/records tools; feed the full credentialed name into state medical board and NPI lookups.

## Inputs → Outputs
- **In:** `name` (+ optional specialty/`employer-org`)
- **Out:** `social-profile`, specialty/credentials, `employer-org`, practice `address`
- **Empty/negative result looks like:** no indexed Doximity page — the subject may not be a clinician, may keep their profile private, or may practice outside the US; fall back to NPI registry and state board lookups.

## Gotchas & OpSec
- Full search requires a verified clinician login you cannot legitimately fake; work from the publicly indexed profile pages instead.
- Location shown is the professional practice, not a home address.
- US-only coverage; non-US medics won't appear.

## Overlaps ("do both")
- Pairs with the NPI registry and state medical licensing boards — Doximity gives the narrative profile, those give authoritative licensure and address-of-record data.

## Trust & verifiability
`trust: trusted` — Doximity credential-verifies its members, so profile specialty/training is reliable; still confirm current workplace against a second source, as jobs change faster than profiles update.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | doximity-united-states |
| category | social-networks |
| selectorsIn → selectorsOut | name, employer-org → social-profile, employer-org, address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
