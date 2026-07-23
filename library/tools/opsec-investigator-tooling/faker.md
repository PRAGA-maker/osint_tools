---
id: faker
name: Faker
description: Use when you need a consistent, locale-correct fake persona for a sock-puppet account — generates plausible `name`, `address`, `phone`, and `email` data offline, in dozens of languages/countries.
url: https://github.com/joke2k/faker
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Generating coherent fake identity details (name, address, DOB, company, user-agent) to build believable sock-puppet personas for OSINT accounts.
selectorsIn: []
selectorsOut:
- name
- address
- phone
- email
status: live
pricing: free
costNote: Free, open-source Python library (joke2k/faker); install via pip.
opsec: passive
opsecNote: Generation is 100% local — nothing is sent anywhere, so it leaks nothing. The OpSec value is in the output: use it to keep a sock puppet internally consistent. Do NOT use fabricated identities to commit fraud, forge documents, or bypass verification in ways that break the law or platform terms.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: community
trustNote: One of the most widely used Python libraries (tens of thousands of GitHub stars, actively maintained); reliable for its purpose — generating clearly synthetic data.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- joke2k/faker
- Python Faker
tags:
- Sock Puppets
- persona-generation
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Faker

> A local library that mints coherent fake identity data — names, addresses, phone numbers, companies, dates — in dozens of locales, for building consistent sock-puppet personas.

## When to use
You're standing up a sock-puppet account for investigation and need it to look real and stay internally consistent: a `name` that matches the locale, a plausible `address` and `phone` for the right country, a birth date, an employer, a user-agent string. Faker generates all of it offline and reproducibly (seed it to regenerate the same persona), so your decoy's details don't contradict each other across platforms.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install: `pip install faker`.
2. In Python: `from faker import Faker; fake = Faker('en_GB')` (pick the locale that matches the persona's country).
3. Generate fields: `fake.name()`, `fake.address()`, `fake.phone_number()`, `fake.email()`, `fake.date_of_birth()`, `fake.company()`, `fake.user_agent()`.
4. **Seed for consistency:** `Faker.seed(1234)` reproduces the same values, so you can regenerate a persona's details later.
5. Store the generated persona in your case's sock-puppet register so every account uses matching details. A CLI (`faker <provider>`) exists for one-off values.

## Inputs → Outputs
- **In:** none (a generator — you choose locale and field types)
- **Out:** synthetic `name`, `address`, `phone`, `email`, plus DOB, company, user-agent, etc.
- **Empty/negative result looks like:** N/A — it always returns a value; the failure mode is *unrealistic* output (wrong locale, an address that doesn't geocode) rather than an empty one.

## Gotchas & OpSec
- Output is **plausible but not valid** — generated phone numbers/addresses may not exist; don't rely on them passing real verification (that's by design, and abusing them can be illegal).
- Match the **locale** to the persona's claimed country or details will read as fake (a US address on a "German" account is a tell).
- It's a persona-building aid only; combine with genuinely separate infrastructure (email, IP, browser profile) for real compartmentalisation.
- Purely local — no network leak.

## Overlaps ("do both")
- Complements sock-puppet infrastructure tooling (burner email, VPN, isolated browser profiles): Faker supplies the *identity details*, those tools supply the *environment* — you need both for a durable puppet.

## Trust & verifiability
`trust: community` — a mature, heavily used open-source library; dependable at producing clearly synthetic data, which is exactly (and only) what it's for.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | faker |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  → name, address, phone, email |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | no |
