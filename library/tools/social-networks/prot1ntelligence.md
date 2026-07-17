---
id: prot1ntelligence
name: Prot1ntelligence
description: Use when you have a ProtonMail/Proton `email` or custom domain and want to confirm it uses Proton and read its PGP-key metadata — returns domain mail config and account-age hints.
url: https://github.com/C3n7ral051nt4g3ncy/Prot1ntelligence
category: social-networks
path:
- social-networks
bestFor: Validating a ProtonMail address, detecting Proton-hosted custom domains, and pulling PGP key creation timestamps that approximate account age.
selectorsIn:
- email
selectorsOut:
- domain
status: live
pricing: free
costNote: Free open-source Python script (MIT-style community tool); no account or API key required.
opsec: active
opsecNote: The script queries Proton's public key/API endpoints for the target address, so requests touch Proton infrastructure (not the target's mailbox — the owner is not notified). Run from a research host/VPN. Do not use it to harass a Proton user; it only reads public key metadata.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Maintained by C3n7ral051nt4g3ncy, a known OSINT developer; single-author open-source project, so review the code before running and verify results independently.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- curl-for-osint
- masto
- osint-tactical
- webosint
- whatsmyname-python
aliases:
- protintel
- Prot1ntelligence
tags:
- Social Media
- Protonmail
- proton
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Prot1ntelligence

> A Python CLI that interrogates Proton's public PGP-key infrastructure to validate a ProtonMail address and extract account-age and encryption metadata.

## When to use
You have an `email` you suspect is a ProtonMail/Proton address, or a custom `domain` you think is Proton-hosted, and you want to (a) confirm the address exists/uses Proton, (b) detect a catch-all domain and extract its primary address, and (c) read the PGP key's creation timestamp — which often approximates when the Proton account was created. Useful for corroborating an anonymous email identity and estimating its age.

## How to use it (`bestInteractionPattern`: cli)
1. Clone and install:
   ```
   git clone https://github.com/C3n7ral051nt4g3ncy/Prot1ntelligence
   cd Prot1ntelligence
   pip install -r requirements.txt
   ```
2. Run: `python3 protintel.py` and provide the target `email` (e.g. `someone@protonmail.com`, `@proton.me`, `@protonmail.ch`, or a custom domain).
3. Read the output: whether the domain uses Proton for mail, whether it's a catch-all (and the primary address), the PGP key creation date/time, and the encryption type (RSA vs ECC/Curve25519).
4. Confirm the address is real first — invalid addresses may return randomized/placeholder key data.
5. Pivot: the key creation timestamp is an account-age lead; a confirmed Proton domain feeds domain OSINT; a catch-all's primary address is a new `email` to investigate.

## Inputs → Outputs
- **In:** `email` (ProtonMail/Proton address or Proton-hosted custom domain)
- **Out:** Proton mail-config for the `domain`, catch-all detection + primary address, PGP key creation timestamp (≈ account age), encryption algorithm
- **Empty/negative result looks like:** no PGP key returned / domain not on Proton, or randomized-looking key data for an address that doesn't actually exist — treat as "not a live Proton address."

## Gotchas & OpSec
- **Active:** queries hit Proton's public endpoints; run from a research host/VPN. The mailbox owner is not notified, but don't hammer the API.
- The key-creation timestamp approximates account creation but isn't a guarantee (keys can be regenerated).
- Single-author tool — read the script and pin the version before running; verify any finding against Proton's key server directly.

## Overlaps ("do both")
- Pairs with a general email-existence checker: this confirms the Proton-specific technical facts (key age, catch-all), while a broader email OSINT tool ties the address to breaches, profiles and gravatar.

## Trust & verifiability
`trust: community` — an open-source tool from a recognised OSINT author; results are derived from Proton's own key infrastructure, so they're reliable when the address is confirmed real, but review the code and corroborate independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | prot1ntelligence |
| category | social-networks |
| selectorsIn → selectorsOut | email → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
