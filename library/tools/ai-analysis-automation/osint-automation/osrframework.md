---
id: osrframework
name: OSRFramework
description: Use when you have a `username`, `email`, `name`, or `phone` and want to enumerate it across many platforms at once — returns matching `social-profile`s, candidate emails, and linked accounts.
url: https://github.com/i3visio/osrframework
category: ai-analysis-automation
path:
- ai-analysis-automation
- osint-automation
bestFor: One-command multi-platform enumeration of a username/email/name via usufy/mailfy/searchfy/phonefy.
selectorsIn:
- username
- email
- name
- phone
selectorsOut:
- social-profile
- email
- username
status: degraded
pricing: free
costNote: Free and open-source (AGPLv3+, i3visio); `pip install osrframework`. No account.
opsec: active
opsecNote: usufy/mailfy check each account by actually requesting the profile URL on each target platform, so those platforms see requests. This is active enumeration — run it from a sock-puppet egress/VPN, not an attributable IP, if the targets matter.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A long-standing, well-known i3visio project (usufy/mailfy lineage); still installable, but many of its platform checkers have bit-rotted as sites changed, so expect false negatives — hence status degraded.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- OSRFramework
- usufy
- mailfy
tags:
- username-enumeration
- osint-automation
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# OSRFramework

> i3visio's classic enumeration suite: point usufy/mailfy/searchfy/phonefy at an identifier and sweep dozens of platforms at once — powerful, but aging.

## When to use
You have a `username`, `email`, `name`, or `phone` and want a fast, broad first sweep for where it appears online, rather than checking platforms by hand. usufy hunts a nickname across sites, mailfy works emails, searchfy takes a full name, phonefy checks phone numbers. Good as a wide net early in a case — then verify hits individually, because coverage is uneven.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip3 install osrframework` (Python 3).
2. Enumerate a username: `usufy -n johndoe -p twitter instagram github ...` (or all platforms).
3. Work an email: `mailfy -n johndoe` (generates/checks candidate addresses) or feed a known email.
4. Search a name: `searchfy -q "John Doe"`; check a number: `phonefy -n +1...`.
5. Pivot: confirmed `social-profile` hits feed profile-level OSINT; candidate emails feed email verification/breach checks.

## Inputs → Outputs
- **In:** `username`, `email`, `name`, or `phone`
- **Out:** matched `social-profile`s, candidate/confirmed `email`s, linked `username`s (plus Maltego-compatible output)
- **Empty/negative result looks like:** few or no hits — often because a platform's checker is outdated (false negative), not because the account doesn't exist; always spot-check manually.

## Gotchas & OpSec
- **Bit-rot:** many usufy checkers break as sites change their "user not found" responses — treat non-hits as unreliable and confirm key platforms by hand.
- **Active:** it requests profile URLs on each platform; use a sock-puppet egress.
- False positives happen where a platform returns a soft 200 for missing users — verify hits, don't trust the list blindly.

## Overlaps ("do both")
- Overlaps heavily with modern username-enumeration tools (Sherlock, Maigret) — run one of those alongside OSRFramework, since each keeps a different (and differently-stale) site list.

## Trust & verifiability
`trust: community` — mature, open-source, and inspectable, but no longer actively keeping every checker current; verify each hit at the source rather than relying on the aggregate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osrframework |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | username, email, name, phone → social-profile, email, username |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
