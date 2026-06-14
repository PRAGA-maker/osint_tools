---
id: osint-rocks
name: osint.rocks
description: Use when you have an email, username, or phone and want a fast free sweep across many account-discovery tools (Holehe/Sherlock-style) in one place — returns where the identifier is registered.
url: https://osint.rocks/
category: email
path:
- email
bestFor: One-stop free reverse lookup of an email/username/phone against many platforms.
selectorsIn:
- email
- username
- phone
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free web front-end aggregating open-source OSINT checks; no account needed for basic use.
opsec: active
opsecNote: Some account-existence checks (Holehe-style) probe target platforms' password-reset / signup endpoints; these can touch the subject's accounts indirectly. Run from a non-attributable connection.
humanInLoop: false
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: osint.rocks is a popular free web aggregator wrapping well-known open-source tools (Holehe, Sherlock, Maigret, etc.). Reliability tracks the underlying tools; some modules go stale.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- osint rocks
tags:
- email
- Email Related Sites
source: uk-osint
lastVerified: ''
enrichment: full
---

# osint.rocks

> A free browser front-end that runs an email/username/phone through many open-source account-discovery checks at once.

## When to use
You have an `email`, `username`, or `phone` and want a quick, no-cost first pass on which platforms it's registered on — a fast way to seed a footprint before paying for `[[osint-industries]]`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://osint.rocks/.
2. Pick the lookup type (email / username / phone) and enter the value.
3. Run it; read the per-platform results (registered / not registered / unknown).
4. Pivot confirmed `social-profile` / `username` hits to deeper enumeration and to people search (`[[pipl]]`).

## Inputs → Outputs
- **In:** `email`, `username`, `phone`
- **Out:** `social-profile`, `username`
- **Empty/negative result looks like:** all modules return "not found"/"error" — or modules time out (the upstream tool broke).

## Gotchas & OpSec
- Modules wrap open-source tools that break as sites change CAPTCHAs/APIs — expect some false negatives.
- OpSec: marked active — email-existence checks can hit platforms' reset/signup flows tied to the subject's accounts. Use a clean connection; avoid for adversarial targets.
- Rate limits may throttle large or repeated runs.

## Overlaps ("do both")
- Cross-validate paid results from `[[osint-industries]]`; corroborate breach exposure with `[[osintcat]]`.

## Trust & verifiability
`trust: community` — popular free aggregator; each hit links back to the platform so it is independently checkable, but module freshness varies.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-rocks |
| category | email |
| selectorsIn → selectorsOut | email, username, phone → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
