---
id: keybase
name: Keybase
description: Use when you have a `username` and want to pivot to the same person's verified other accounts, PGP key and crypto wallets — returns cross-platform social-profile proofs and wallet addresses.
url: https://keybase.io/
category: username
path:
- username
- specific-sites
bestFor: Turning one handle into a cryptographically-verified cluster of that person's other identities (Twitter/X, GitHub, Reddit, HN, websites) plus PGP key and crypto addresses.
selectorsIn:
- username
selectorsOut:
- social-profile
- crypto-wallet
- domain
- device-id
status: live
pricing: free
costNote: Free public directory; no account needed to view a profile or query the API.
opsec: passive
opsecNote: Viewing keybase.io/<user> or hitting the public user/lookup API is a passive read of self-published data and does not notify the target. Avoid logging in or following, which would attribute activity to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Keybase (now owned by Zoom) maintains a publicly auditable key directory; the identity proofs are cryptographically verified, so a green proof is strong evidence the accounts are controlled by the same key-holder.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- gosearch
- whatsmyname-python
aliases:
- keybase.io
tags:
- username
- identity-verification
- pgp
- crypto
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Keybase

> A publicly auditable directory that ties a username to that person's *cryptographically proven* other accounts, PGP key, websites and crypto wallets — one of the few sources where a cross-platform link is verifiable rather than a guess.

## When to use
You have a `username` and want to confirm which other accounts genuinely belong to the same person. Unlike a name-collision guess, a Keybase profile carries signed proofs: the user posted a signature on their Twitter/X, GitHub, Reddit, Hacker News, or website to prove control. It also exposes their PGP public key and any Stellar/Bitcoin wallet they linked. Best when the subject is technical/privacy-aware (developers, crypto users, security folk) — the demographic most likely to have a Keybase.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open `https://keybase.io/<username>` directly.
2. Read the **proofs** column: each listed account (twitter, github, reddit, hackernews, a domain, etc.) with a checkmark is verified as controlled by the same key.
3. Note the **crypto** section for linked Stellar/Bitcoin addresses and the **devices** list (device names can leak naming conventions).
4. For automation, query the public API: `https://keybase.io/_/api/1.0/user/lookup.json?usernames=<username>` returns the same proofs as JSON.
5. Pivot: each proven account is a fresh `social-profile` to enrich; a linked domain feeds domain OSINT; a wallet feeds chain analysis.

## Inputs → Outputs
- **In:** `username`
- **Out:** verified `social-profile` proofs across platforms, `crypto-wallet` addresses, controlled `domain`(s), and `device-id` names
- **Empty/negative result looks like:** `keybase.io/<user>` returns "user not found" / the API returns `them: null` — the person simply has no Keybase, which is common; absence proves nothing.

## Gotchas & OpSec
- Human-in-the-loop: none — profiles are public.
- OpSec: passive. Don't sign in or "follow," which would tie your identity to the lookup.
- Coverage is skewed toward technical users; most missing-persons subjects won't have a Keybase, so treat a hit as a bonus, not an expectation.
- Proofs can be revoked or a linked account deleted — check the proof still resolves before relying on it.

## Overlaps ("do both")
- Pairs with `[[whatsmyname-python]]` and `[[gosearch]]` — those enumerate where a username *might* exist across many sites; Keybase tells you which links are cryptographically *proven* for the technical subset.

## Trust & verifiability
`trust: trusted` — the directory is publicly auditable and proofs are signed, so verified links are high-confidence; the only caveat is coverage, not accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | keybase |
| category | username |
| selectorsIn → selectorsOut | username → social-profile, crypto-wallet, domain, device-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
