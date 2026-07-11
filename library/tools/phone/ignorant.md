---
id: ignorant
name: ignorant
description: Use when you have a `phone` number and want to know if it's registered on Instagram, Amazon, or Snapchat — returns account-existence signals without alerting the owner.
url: https://pypi.org/project/ignorant/
category: phone
path:
- phone
bestFor: Checking whether a phone number is tied to accounts on Instagram, Amazon, and Snapchat, silently.
selectorsIn:
- phone
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free and open-source (Python CLI); no account or API key.
opsec: passive
opsecNote: Like holehe for phones, it probes each site's registration/recovery endpoints to infer whether the number is registered — WITHOUT triggering a password reset or notifying the owner. Requests originate from your IP to those platforms, so run behind a VPN. It does not log in and does not alert the target, but heavy use can rate-limit your IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Well-known open-source tool from the same author lineage as holehe (megadose/sundowndev); inspectable code, but its checks break when the target platforms change their endpoints.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
aliases:
- ignorant phone osint
tags:
- phone
- account-existence
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# ignorant

> The phone-number equivalent of holehe: feed it a number and it silently checks whether that number is registered on Instagram, Amazon, and Snapchat — confirming the line is real, in use, and tied to accounts, without tipping off the owner.

## When to use
You have a `phone` number and want low-noise confirmation that it belongs to an active person with online accounts, plus a few concrete platforms to pivot to. A positive on Instagram/Snapchat says the number is tied to a social identity worth chasing; a positive on Amazon says it's a live commerce account. Reach for it right after acquiring a number, as a passive triage before more intrusive phone work.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install ignorant`.
2. Run against the number with country code, e.g. `ignorant 33 644637111` (country code + national number).
3. Read the per-site output: whether the number is registered on Instagram, Amazon, Snapchat.
4. Run behind a VPN and don't hammer it (rate limits).
5. Pivot: an Instagram/Snapchat hit → search those platforms for the account; combine with `[[countrycallingcodes-com]]` (origin) and reverse-phone tools for identity.

## Inputs → Outputs
- **In:** `phone` (country code + number)
- **Out:** `social-profile` (registered/not on Instagram, Amazon, Snapchat)
- **Empty/negative result looks like:** all "not registered" — the number isn't on those specific sites, uses a different number there, or a platform changed its endpoint (breaking the check). Only three services are covered; absence is narrow, not proof of no online presence.

## Gotchas & OpSec
- Human-in-the-loop: none; but keep it **updated** — checks rot when Instagram/Amazon/Snapchat change registration flows.
- Only **three platforms** are covered — treat it as a quick signal, not comprehensive.
- OpSec: passive — no reset triggered, owner not notified; still probes from your IP, so use a VPN and go slow.

## Overlaps ("do both")
- The phone-side companion to `[[holehe-2]]` (email account-existence) — run both on a linked email+phone to widen platform coverage; pair with reverse-phone tools for identity.

## Trust & verifiability
`trust: trusted` — a respected, inspectable open-source tool; results are reliable when its endpoint checks are current, and simply stale (not false-positive-prone) when a platform changes.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ignorant |
| category | phone |
| selectorsIn → selectorsOut | phone → social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
