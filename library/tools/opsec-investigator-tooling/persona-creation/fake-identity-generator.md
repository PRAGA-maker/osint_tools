---
id: fake-identity-generator
name: Fake Identity Generator
description: Use when you are building a sock-puppet persona and need consistent synthetic details — returns a generated `name`, `address`, `dob`, `username` and `password` to register anonymous accounts.
url: https://backgroundchecks.org/justdeleteme/fake-identity-generator/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- persona-creation
bestFor: Spinning up a coherent synthetic persona (name, address, DOB, username, password) for an investigative sock-puppet account.
selectorsIn: []
selectorsOut:
- name
- address
- dob
- username
- password
status: live
pricing: free
costNote: Free web generator; no account, no payment.
opsec: passive
opsecNote: Generation happens in your browser and no data is submitted, so the tool itself leaks nothing. The OpSec discipline is in USE — never attach a synthetic identity to real payment/phone/biometric data, keep each persona's details recorded and consistent, and follow the target platform's rules and your engagement's legal authorisation before creating accounts.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A simple client-side generator hosted by backgroundchecks.org (via the JustDelete.Me project); output is random synthetic data with no tie to real people — treat it as scaffolding, not vetted identities.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- backgroundchecks-org
- just-delete-me
aliases:
- JustDeleteMe Fake Identity Generator
- fake name generator
tags:
- persona-creation
- sock-puppet
- opsec
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Fake Identity Generator

> A one-click synthetic-persona generator — produces a random name, address, date of birth, username and password to seed a sock-puppet account, so you don't reuse or invent (and forget) details.

## When to use
You are setting up an investigative sock puppet — a research account that isn't tied to your real identity — and want a **coherent, recorded** set of fictional details rather than making them up ad hoc. Generate a `name`, `address`, `dob`, `username` and `password`, log them in your persona sheet, and use them consistently so the account looks plausible and you can maintain it over time. This is persona *creation* / OpSec hygiene, not a source of intelligence about a real person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://backgroundchecks.org/justdeleteme/fake-identity-generator/.
2. Click to generate; it produces a synthetic name, address, DOB, username, password and short bio. Regenerate until the details suit the persona's intended region/age.
3. **Record every field** in a dedicated, secured persona document — consistency across sites is what makes a puppet durable.
4. Provision the rest of the persona separately: a fresh email (via a separate provider), a non-personal phone/VoIP number if required, and a clean browser profile/VPN — the generator does not create working email or phone.
5. Use the persona only within your engagement's legal and platform rules.

## Inputs → Outputs
- **In:** none (no query)
- **Out:** synthetic `name`, `address`, `dob`, `username`, `password` (and a short bio)
- **Empty/negative result looks like:** n/a — it always returns randomised data. Remember the output is **fictional**; it must never be presented as, or matched against, a real identity.

## Gotchas & OpSec
- Human-in-the-loop: none to generate.
- OpSec: the tool is **passive**, but persona *operations* are where risk lives — don't cross the synthetic identity with any real-world identifier (your phone, card, IP, face), and keep personas siloed from each other.
- It does **not** provision a working email or phone number; you must obtain those separately for accounts that verify them.
- Generated addresses/DOBs are random and may be internally implausible (e.g. an address that doesn't exist) — sanity-check before use.
- Creating accounts under a false identity can breach a platform's terms or local law; confirm authorisation for your specific engagement.

## Overlaps ("do both")
- Pairs with `[[just-delete-me]]` and `[[backgroundchecks-org]]` (same host/project family) for persona lifecycle, and with a separate disposable-email and VoIP-number service to complete a usable sock puppet.

## Trust & verifiability
`trust: community` — a lightweight client-side utility; its output is deliberately fake and unverifiable by design, which is exactly the point for persona scaffolding.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fake-identity-generator |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | (none) → name, address, dob, username, password |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
