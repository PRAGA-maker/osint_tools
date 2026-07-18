---
id: random-user-generator
name: Random User Generator (randomuser.me)
description: Use when you need believable filler persona data to build an investigator sock-puppet — returns name, address and a placeholder identity.
url: https://randomuser.me/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- persona-creation
bestFor: Generating realistic-but-fake persona fields (name, address, DOB, photo) to seed and flesh out sock-puppet accounts.
selectorsIn: []
selectorsOut:
- name
- address
- dob
status: live
pricing: free
costNote: Free and open API; no key or account required (fair-use rate limits apply).
opsec: passive
opsecNote: This creates YOUR cover identity, not a target lookup — it touches no subject. Never reuse the AI-generated stock portrait as a puppet's avatar (it is reverse-image-searchable and flagged); generate a fresh face elsewhere. Do not use fabricated identities to commit fraud or unlawful access.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: trusted
trustNote: Well-known, long-running free open-source persona/test-data API; widely used in development.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- randomuser.me
- Random User API
tags:
- persona-creation
- sock-puppet
- test-data
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# Random User Generator (randomuser.me)

> A free API that spits out plausible fake people — names, addresses, birthdates, logins — to give an investigator's sock-puppet identity consistent, believable filler details.

## When to use
You are standing up a sock-puppet for passive collection and need coherent, throwaway biographical filler so the account doesn't look empty or obviously fake: a consistent `name`, a plausible `address`/locale, a `dob`, and login/contact scaffolding. This is OPSEC tooling for *your* cover identity — not a way to look up a real subject. It ensures the persona's details are internally consistent across the profiles you create.

## How to use it (`bestInteractionPattern`: api)
1. Call the API: `https://randomuser.me/api/` returns one JSON persona; add `?results=10` for a batch, `?nat=gb,us` to constrain nationality/locale, `?gender=female`, or `?seed=xyz` for reproducible output.
2. Take the coherent fields — name, address, DOB, phone, username/email pattern — and record them in your persona dossier so every account you create uses the same details.
3. **Replace the supplied portrait** — its stock faces are known and reverse-image-searchable. Generate a fresh, non-reversible face separately.
4. Register puppet accounts using the consistent persona, from a compartmented browser/IP.

## Inputs → Outputs
- **In:** (none — you request generated data, optionally constrained by nationality/gender/seed)
- **Out:** `name`, `address`, `dob`, plus phone/username/login filler for a cover identity
- **Empty/negative result looks like:** rate-limit/HTTP error under heavy use — slow down; the data is always synthetic, so there is no "not found."

## Gotchas & OpSec
- **Never** use the built-in profile photos as avatars — swap in a freshly generated face; the stock images are fingerprinted and flagged by platforms.
- Keep the persona consistent across accounts (a mismatched DOB/location is what gets puppets caught) — store the generated identity and reuse it.
- Legal/ethical: cover identities are for lawful passive research only; do not use fabricated details to defraud or gain unauthorized access.

## Overlaps ("do both")
- Pair with a fresh-face generator (e.g. a GAN portrait tool) and a persona-dossier workflow — this supplies the biographical fields, the face generator supplies a non-reversible avatar, together making a coherent puppet.

## Trust & verifiability
`trust: trusted` — a mature, widely used open API; output is deliberately synthetic, so "trust" here is about reliability of the service, not accuracy of any real-world data (there is none by design).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | random-user-generator |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | (none) → name, address, dob |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | api |
| opsec | passive |
| human-in-loop | no |
