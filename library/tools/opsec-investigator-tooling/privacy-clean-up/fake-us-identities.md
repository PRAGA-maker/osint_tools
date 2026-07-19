---
id: fake-us-identities
name: Fake US Identities
description: Use when you need a synthetic US persona for sock-puppet/OPSEC work — returns a fabricated name, address, and biographical data (no real person).
url: https://xdd2.org/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- privacy-clean-up
bestFor: Generating a coherent synthetic US identity (name, address, DOB, biographical filler) to seed a sock-puppet account or honeypot dataset.
selectorsIn: []
selectorsOut:
- name
- address
- dob
status: live
pricing: free
costNote: Free static identity-generator site; no account or payment.
opsec: passive
opsecNote: Generates fabricated data only; nothing you do touches any real person. IMPORTANT — use synthetic identities strictly for lawful sock-puppet/OPSEC/testing; using fabricated SSNs, IDs, or personas to commit fraud or impersonation is illegal. This is for building non-attributable research personas, not deception of real institutions.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running fake-identity generator (derived from an open-source whole-country generator project, originally built for corporate honeypots); output is deliberately random and non-real.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- xdd2.org fake identity
- synthetic US identity generator
tags:
- opsec
- sockpuppet
- persona
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Fake US Identities

> A synthetic-persona generator: it invents internally consistent US identities — name, address, DOB, biographical filler — with no connection to any real person, for building sock puppets and honeypot data.

## When to use
You're setting up a non-attributable research persona (a sock-puppet account for passive OSINT collection) and need believable but fabricated filler: a plausible name, a real-looking US street address, a date of birth, and supporting biographical detail. Consistent fake identities keep your investigative accounts from tracing back to you and from colliding with a real person's data.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://xdd2.org/ (a fabricated-identity generator).
2. Generate an identity; it returns a coherent synthetic profile (`name`, `address`, `dob`, and related fields).
3. Reuse the same generated identity consistently across your persona's accounts so details don't contradict.
4. Pivot: pair with a dedicated email, a sock-puppet browser profile, and a fresh IP so the persona is fully isolated from your real identity.

## Inputs → Outputs
- **In:** none (generator)
- **Out:** synthetic `name`, `address`, `dob`, biographical filler
- **Empty/negative result looks like:** n/a — it always outputs a fabricated identity; the data is meaningless as "real," which is the point.

## Gotchas & OpSec
- LEGAL/ETHICAL: synthetic identities are for lawful persona/OPSEC/testing only. Do not use fabricated SSNs or IDs to defraud, impersonate, or deceive institutions — that is a crime.
- Generated "addresses" may coincidentally resemble real ones; do not attach a persona to a genuine address/phone.
- OpSec: passive (nothing is queried about a real target), but sound persona hygiene (separate email/browser/IP) is what actually protects you.

## Overlaps ("do both")
- Pairs with sock-puppet browser and disposable-email tooling — this supplies the identity, those supply the isolated infrastructure to use it.

## Trust & verifiability
`trust: community` — a known generator producing deliberately random, non-real data; there is nothing to "verify" beyond confirming the identity is fabricated (which it always is).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fake-us-identities |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | (none) → name, address, dob |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
