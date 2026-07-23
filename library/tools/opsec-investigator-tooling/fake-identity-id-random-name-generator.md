---
id: fake-identity-id-random-name-generator
name: ElfQrin Fake Identity Generator
description: Use when you need a consistent fabricated persona (name, DOB, address, look-alike ID/card numbers) to stand up an investigator sock-puppet account — returns a full made-up identity.
url: https://www.elfqrin.com/fakeid.php
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Generating a coherent fake persona to register and operate a sock-puppet research account without exposing your own identity.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free web generator; no account required.
opsec: active
opsecNote: This is offensive OpSec *for you*, not target interaction — it manufactures a cover identity so your real details never touch a research account. The generated SSN/credit-card/ID numbers are format-valid fakes for testing personas ONLY; using them for fraud, real financial transactions, or identity deception against real institutions is illegal. Keep personas plausible and internally consistent, and record which persona you use where.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running hobbyist tool (ElfQrin/Valerio Capello); it fabricates random data locally-in-page and stores nothing, but is an unaffiliated third party.
missingPersonsRelevance: low
coverage:
- us
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- us-ssn-driver-license-state-id-passport-tax-id-generator
- this-person-does-not-exist
- fakenamegenerator
aliases:
- ElfQrin Fake ID
- Fake Identity Generator
- fakeid.php
tags:
- sock-puppet
- opsec
- persona
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# ElfQrin Fake Identity Generator

> A one-click fabricated-persona generator — build a coherent cover identity (name, DOB, address, look-alike numbers) for a research sock-puppet so your real self stays out of the account.

## When to use
You are about to stand up a sock-puppet account for passive research and need a *consistent, plausible* fake identity to register it — a full name, date of birth, address, username seed, and format-valid-but-fake ID numbers — instead of improvising details that later contradict each other. This is investigator OpSec: it protects you, not a way to attack anyone.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.elfqrin.com/fakeid.php.
2. Optionally set country/sex/age parameters, then generate. It produces a complete persona: name, DOB, physical descriptors, address, and format-valid fake SSN/credit-card/ID numbers.
3. Record the whole persona in your sock-puppet log so every field stays consistent across accounts and over time.
4. Pair it with a matching AI-generated face from `[[this-person-does-not-exist]]` and a dedicated email/number to complete the cover.
5. Use the persona only to register and operate research accounts — never for real financial, contractual, or identity-verification purposes.

## Inputs → Outputs
- **In:** — (parameters only: country/age/sex)
- **Out:** a fabricated persona — name, DOB, address, descriptors, format-valid fake ID/card numbers (all synthetic, none belonging to a real person)
- **Empty/negative result looks like:** n/a — it always generates; if numbers must pass a real verification, that's a sign you're misusing it (they're fakes).

## Gotchas & OpSec
- The SSN/credit-card/ID values are Luhn/format-valid *fakes* for persona realism only. Using them against real institutions is fraud — don't.
- Consistency is everything: reusing mismatched details across accounts burns a sock puppet. Log and reuse one persona deliberately.
- OpSec: marked **active** because it's part of building an operational cover you'll act through; the generator itself contacts no target.

## Overlaps ("do both")
- Pairs with `[[this-person-does-not-exist]]` (a face for the persona) and `[[us-ssn-driver-license-state-id-passport-tax-id-generator]]` / `[[fakenamegenerator]]` — combine a face, a name, and address/ID fields into one coherent cover identity.

## Trust & verifiability
`trust: community` — a long-running, well-known hobbyist generator; it fabricates data client-side and retains nothing, but it is an unaffiliated third party — treat every field as synthetic by definition.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fake-identity-id-random-name-generator |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
