---
id: protosint
name: ProtOSINT
description: Use when you have a ProtonMail `email` (or a Proton-related `ip-address`) and want to confirm the account exists and pull its public PGP key details — returns account existence and key metadata as a social-profile signal.
url: https://github.com/pixelbubble/ProtOSINT
category: email
path:
- email
bestFor: Confirming a ProtonMail account exists and extracting its public PGP key creation date / encryption type.
selectorsIn:
- email
- ip-address
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free, open-source Python CLI; no account or API key. Constrained by ProtonMail's tight rate limits (see below).
opsec: passive
opsecNote: Queries Proton's public key-lookup endpoint — it does not send mail to or otherwise alert the account owner. Only your IP touches Proton's servers. Aggressive querying will get your IP temporarily blocked, not the target notified.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: cli
trust: community
trustNote: A community open-source tool (pixelbubble). Since ProtonMail's Nov 2021 API changes it is unreliable — invalid emails can return plausible-looking results, so treat every hit as needing manual confirmation.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- ProtOSINT
- protosint
tags:
- protonmail
- email-verification
- cli
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# ProtOSINT

> A Python CLI for Proton services — check whether a ProtonMail account exists and read its public PGP key metadata, plus flag ProtonVPN IPs.

## When to use
You have a ProtonMail `email` and want to know whether it corresponds to a real Proton account, and if so extract its public key details (key creation date, RSA 2048/4096 vs X25519). Because Proton is privacy-focused and reveals little, even confirming existence plus a key-creation date is a useful signal (e.g. a rough account-age estimate). It also has a module to test whether an `ip-address` belongs to ProtonVPN.

## How to use it (`bestInteractionPattern`: cli)
1. Clone and set up: `git clone https://github.com/pixelbubble/ProtOSINT && cd ProtOSINT && pip install -r requirements.txt`.
2. Run the account module against the `email` to test existence and pull the public PGP key (creation date, key type).
3. Optionally run the VPN module against an `ip-address` to check ProtonVPN affiliation.
4. **Verify** any "exists" result against ProtonMail's web interface — the tool can return false positives with random timestamps since the API changes.
5. Pivot: a confirmed account + key age helps date the identity; combine with breach/email tools for a fuller picture.

## Inputs → Outputs
- **In:** ProtonMail `email` (or `ip-address` for the VPN check)
- **Out:** account-exists signal + public PGP key metadata (creation date, encryption type) — a Proton `social-profile` indicator
- **Empty/negative result looks like:** "not found" — but note the inverse is also unreliable: since 2021 the API may fabricate a plausible result for a non-existent address, so a "hit" is not proof. Confirm manually.

## Gotchas & OpSec
- **Degraded:** ProtonMail's Nov 2021 API changes limit you to ~10–15 requests before a ~1-hour IP block, and can return misleading results for invalid emails. The maintainer recommends leaning on the account-existence and VPN modules and cross-checking via Proton's web UI.
- Rate-limit is the main friction — space out queries.
- Passive: the account owner is never contacted.

## Overlaps ("do both")
- Pairs with generic email-existence/breach checkers — Proton hides most signals, so corroborate ProtOSINT's existence result with a second method and always the Proton web login page.

## Trust & verifiability
`trust: community` — a legitimate open-source tool whose reliability degraded with Proton's API lockdown. Treat outputs as leads requiring manual confirmation, not facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | protosint |
| category | email |
| selectorsIn → selectorsOut | email, ip-address → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
