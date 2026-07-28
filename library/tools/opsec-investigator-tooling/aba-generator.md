---
id: aba-generator
name: ABA Generator
description: Use when you need to validate or generate a syntactically-valid US bank routing (ABA) number for a sock-puppet — returns a checksum-valid ABA number, no target data.
url: https://www.fakenamegenerator.com/aba-validator.php
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Generating/validating plausible ABA routing numbers when building a sock-puppet identity or checking a number's checksum.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free web utility on FakeNameGenerator.com; no login. (The site runs ads.)
opsec: passive
opsecNote: Purely a local checksum utility on a public page — it touches no target and reveals nothing about anyone. OpSec relevance is only that it helps you keep a consistent, non-real sock-puppet identity; never use a generated number to commit fraud or open real financial accounts.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Part of the long-standing FakeNameGenerator suite; the ABA checksum algorithm is public, so output validity is trivially checkable.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- credit-card-generator
- fake-name-generator
- nino-generator
- sin-generator
- ssn-generator
- vin-generator
aliases:
- ABA routing number validator
- FakeNameGenerator ABA
tags:
- sock-puppet
- identity-tooling
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# ABA Generator

> A FakeNameGenerator utility that validates and generates checksum-valid US ABA bank routing numbers — a small piece of sock-puppet identity hygiene, not an investigative lookup.

## When to use
You're building or maintaining a consistent sock-puppet persona and need a plausible-looking, format- and checksum-valid US bank routing number to fill a field, or you have a routing number and want to confirm it passes the ABA checksum. This is investigator-side tooling: it produces no data about any subject and takes no selectors. Include it for identity-management consistency, never as a source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.fakenamegenerator.com/aba-validator.php.
2. To **validate**: paste a 9-digit routing number; it reports whether the ABA checksum is valid.
3. To **generate**: use the generator to produce a checksum-valid number for your sock-puppet's profile.
4. Store the value with the rest of that persona's details so the identity stays internally consistent.

## Inputs → Outputs
- **In:** none investigative (an optional routing number to validate)
- **Out:** none investigative — a validity verdict or a generated checksum-valid ABA number
- **Empty/negative result looks like:** "invalid" for a number that fails the checksum; it does not tell you whether a number is actually issued to a real bank.

## Gotchas & OpSec
- A "valid" result only means the checksum is correct — it is not proof the number maps to a real, active bank account.
- Do not use generated numbers for anything real: opening accounts or moving money with fabricated details is fraud. This is strictly for filling test/decoy fields on a sock-puppet.
- No target is queried; nothing here yields intelligence about others.

## Overlaps ("do both")
- Part of the FakeNameGenerator identity suite — pair with `[[fake-name-generator]]`, `[[ssn-generator]]`, and `[[credit-card-generator]]` to build one coherent, non-real persona.

## Trust & verifiability
`trust: community` — a simple public utility implementing a published checksum; you can verify any output against the ABA routing-number algorithm yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | aba-generator |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
