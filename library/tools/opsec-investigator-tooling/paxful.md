---
id: paxful
name: Paxful
description: Use when you have a Paxful trader username or a crypto lead and want to inspect a peer-to-peer bitcoin marketplace's public trader profiles, reputation, and offers — returns username/social-profile and crypto-wallet-adjacent context.
url: https://paxful.com/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Inspecting public P2P crypto-trader profiles, feedback, and offers on Paxful.
selectorsIn:
- username
- crypto-wallet
selectorsOut:
- username
- social-profile
status: live
pricing: free
costNote: Free to browse public offers/profiles; trading requires a verified (KYC) account, which is a separate step you generally don't need for OSINT viewing.
opsec: passive
opsecNote: Viewing public trader profiles/offers is passive. Interacting (starting a trade, messaging a trader) is active, ties your account to the contact, and may require KYC — do that only from a sanctioned, well-documented sock-puppet, never your real identity. Never send funds to "verify" anything.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Paxful is a real, operating P2P crypto marketplace; its public profile/feedback data is user-generated and self-asserted, so treat identity claims as leads.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- paxful.com
tags:
- crypto
- p2p-marketplace
source: osint4all
lastVerified: '2026-08-05'
enrichment: full
---

# Paxful

> A peer-to-peer bitcoin marketplace whose public trader profiles, reputation history, and offers can corroborate a crypto-linked identity.

## When to use
Crypto-financial investigations. You have a Paxful `username`, or a lead suggesting a subject trades P2P, and want to inspect their public footprint on the platform — profile, join date, trade volume/feedback, payment methods advertised, and active offers. It helps corroborate that a handle is an active trader and surfaces behavioural context (which fiat methods, which regions) around a crypto lead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://paxful.com/ in a sock-puppet browser.
2. Browse the marketplace/offers, or go to a known trader's public profile URL (`paxful.com/user/<username>`).
3. Read the public data: reputation/feedback, completed-trade count, join date, advertised payment methods, and live offers.
4. Do NOT initiate trades or messages unless via a sanctioned sock-puppet — that's active and account-linked.
5. Pivot: the `username` → cross-platform username search; advertised methods/region → location/payment context; any linked handle → social-profile OSINT.

## Inputs → Outputs
- **In:** Paxful `username` (or a crypto lead pointing to the platform)
- **Out:** public trader `social-profile`, reputation/feedback, offers, advertised methods
- **Empty/negative result looks like:** no such user, or a profile with minimal history — the handle may be unused, banned, or renamed; absence isn't proof of no crypto activity.

## Gotchas & OpSec
- Profile identity is **self-asserted** user content — treat names/claims as leads, not proof.
- Trading/messaging requires login and KYC and is active/account-linked; keep to public viewing for OSINT.
- Never transfer funds; escrow/"verification" requests are common scam vectors.

## Overlaps ("do both")
- Pairs with blockchain-explorer and wallet-clustering tools: Paxful gives the human-facing trader profile, on-chain analysis follows the money.

## Trust & verifiability
`trust: community` — the platform is genuine and operating, but its profile/feedback data is user-generated; corroborate any identity link with independent sources before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | paxful |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | username, crypto-wallet → username, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
