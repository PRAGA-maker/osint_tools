---
id: email-reputation
name: Email Reputation
description: Use when you have an email address and want a reputation/risk score plus profile signals (breaches, social presence, deliverability) — returns metadata, social-profile hints.
url: https://emailrep.io/
category: email
path:
- email
- email-verification
bestFor: Quick reputation/risk triage of a single email address.
input: Email address
output: Reputation score, risk level, breach history, profile signals
selectorsIn:
- email
selectorsOut:
- social-profile
- metadata
status: live
pricing: freemium
costNote: Free interactive lookups and a free API tier with daily limits; paid/commercial keys for higher volume.
opsec: passive
opsecNote: Passive database/aggregation lookup; queries EmailRep's own data, does not email or alert the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: trusted
trustNote: EmailRep.io is a well-known service from Sublime Security; widely used in security tooling and documented API.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- holehe
- epieos-email-tool
aliases:
- emailrep
- EmailRep.io
tags:
- email
- reputation
- risk
source: arf-seed
lastVerified: ''
enrichment: full
---

# Email Reputation

> EmailRep.io scores a single email address for reputation/risk and surfaces aggregated profile signals — useful as a fast first-pass on an unknown address.

## When to use
You have an `email` and want a quick read on whether it is a real, established personal address vs. a disposable/throwaway, plus any aggregated signals (known breaches, whether it appears tied to social/online profiles, deliverability). Good triage step before investing time pivoting an address in a missing-persons workup.

## How to use it (`bestInteractionPattern`: api)
1. Get a free API key by registering at emailrep.io (interactive single lookups also work from the homepage without a key, subject to tighter limits).
2. Query: `GET https://emailrep.io/{email}` with header `Key: <your-key>` (and optional `User-Agent`).
3. Parse the JSON: `reputation` (high/medium/low/none), `suspicious` (bool), and the `details` block (e.g. `blacklisted`, `malicious_activity`, `credentials_leaked`, `data_breach`, `first_seen`, `last_seen`, `profiles` list of services where the address is registered).
4. Pivot: the `profiles` array names platforms to check next; feed the address into `[[holehe]]` or `[[epieos-email-tool]]` for account-existence enumeration.

## Inputs → Outputs
- **In:** `email`
- **Out:** `metadata` (reputation/risk, breach flags, first/last seen), `social-profile` (list of services the address is registered on)
- **Empty/negative result looks like:** `reputation: none`, empty `profiles`, `first_seen: never` — the address is unseen by EmailRep, not proof it is fake.

## Gotchas & OpSec
- Free tier is rate-limited (low daily quota); batch work needs a commercial key.
- Reputation is EmailRep's aggregate opinion, not ground truth — absence of signal is not absence of the person.
- OpSec: passive; nothing is sent to the target. Use over a clean IP/key as you would any API.

## Overlaps ("do both")
- Pairs with `[[holehe]]` / `[[epieos-email-tool]]`: EmailRep gives a risk/profile summary; those enumerate specific account existence the summary may miss.

## Trust & verifiability
`trust: trusted` — operated by Sublime Security (EmailRep.io), a recognized vendor with a stable, documented API used across the security community.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | email-reputation |
| category | email |
| selectorsIn → selectorsOut | email → social-profile, metadata |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | api |
| opsec | passive |
| human-in-loop | no |
