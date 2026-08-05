---
id: password-generator
name: Password Generator
description: Use when creating sock-puppet accounts and you need strong unique credentials — returns random high-entropy passwords; it hardens the investigator, not a subject.
url: https://passgenerator.com/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Generating strong, unique passwords for the sock-puppet accounts an investigation depends on.
selectorsIn: []
selectorsOut:
- password
status: live
pricing: free
costNote: Free web password generator; no account or payment.
opsec: passive
opsecNote: Defensive tooling for the investigator. Best practice is a LOCAL generator (your password manager) so a secret never leaves your machine — a web generator is convenient but the value is generated in your browser; still, prefer your manager's built-in generator for anything you'll actually use, and never reuse a puppet password across identities.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A generic third-party web password generator; for real credentials prefer an audited local password manager rather than trusting any website with generation.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- epic-online-guide-to-practical-privacy-tools
aliases:
- passgenerator.com
tags:
- opsec-hygiene
- sockpuppet
- credentials
source: metaosint
lastVerified: '2026-08-05'
enrichment: full
---

# Password Generator

> A quick strong-password generator — small but real OpSec hygiene for the throwaway accounts an investigation runs on, so each puppet gets a unique, uncrackable credential.

## When to use
You're standing up sock-puppet accounts (email, social, forum logins) and need a distinct strong password for each. Reusing or hand-picking weak passwords across puppets is how identities get correlated or taken over. This generates random high-entropy strings on demand. It's investigator hygiene — it produces a `password` for you, not any data about a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://passgenerator.com/ and set length/character options (max length, include symbols/numbers).
2. Generate and copy a password for the specific puppet account.
3. Store it in your password manager against that identity — never in plaintext, never reused across puppets.
4. Prefer your password manager's own built-in generator when possible, so the secret is created and stored locally without a website in the loop.

## Inputs → Outputs
- **In:** none (you set entropy options)
- **Out:** a strong random `password`
- **Empty/negative result looks like:** N/A — it always produces a string. The real failure is operational: reusing it, storing it insecurely, or trusting a website with a credential you should have generated locally.

## Gotchas & OpSec
- **Prefer local generation:** an audited password manager generating offline is safer than any website; use this only for convenience, and regenerate critical passwords locally.
- One unique password per puppet identity — reuse links identities together.
- Being defensive, it never touches or alerts a subject.

## Overlaps ("do both")
- Fits within a broader OpSec setup — see `[[epic-online-guide-to-practical-privacy-tools]]` for the surrounding privacy stack, and pair puppet credentials with a dedicated password manager and separate browser profiles.

## Trust & verifiability
`trust: unverified` — a generic third-party generator; for anything operational, trust an audited local password manager instead, and treat this as a convenience only.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | password-generator |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  → password |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
