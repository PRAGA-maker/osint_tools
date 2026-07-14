---
id: firefly
name: FireFly
description: Use when you have a `phone` number and want carrier/country/line-type validation via the Numverify API from a simple CLI — returns `phone` metadata (carrier, country, line type).
url: https://github.com/Lexxrt/FireFly
category: phone
path:
- phone
bestFor: Scriptable phone-number validation and enrichment (carrier, country, line type) wrapping the Numverify API.
selectorsIn:
- phone
selectorsOut:
- phone
- address
status: live
pricing: freemium
costNote: The FireFly CLI is free and open-source, but it requires a Numverify API key. Numverify has a free tier (limited monthly lookups); heavy use needs a paid Numverify plan.
opsec: passive
opsecNote: Lookups go to Numverify's API, not to the number's owner, so the subject is not alerted. Your API key and IP are attributable to Numverify. This is metadata validation only — it does not dial or message the number.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: unverified
trustNote: A small open-source wrapper (Lexxrt/FireFly) around Numverify. The data authority is Numverify; the wrapper itself is minor community code — audit before running.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: true
aliases:
- FireFly phone lookup
tags:
- Phone numbers
- numverify
source: cyb-detective
lastVerified: '2026-07-14'
enrichment: full
---

# FireFly

> A lightweight CLI wrapper around the Numverify API — validates a phone number and returns carrier, country, and line type from your terminal.

## When to use
You have a `phone` number and want a quick, scriptable validation: is it a valid number, which country and carrier, and is it mobile/landline/VoIP? This is an early triage step in a phone workflow — it confirms the number is real and narrows geography/line type before you invest in heavier tools or messaging-app checks.

## How to use it (`bestInteractionPattern`: cli)
1. Get a free API key from numverify.com and clone the repo.
2. Put the key in `config.json`; install deps: `pip install -r requirements.txt`.
3. Run: `python3 FireFly.py <number>` (E.164 format, e.g. `+14155552671`).
4. Read output: validity, country, location, carrier, and line type.
5. Pivot: the country/carrier (`address` region) narrows people-search; a valid mobile feeds messaging-app presence checks and breach lookups.

## Inputs → Outputs
- **In:** `phone` (E.164)
- **Out:** validity boolean, country and location (`address` region), carrier, line type
- **Empty/negative result looks like:** "invalid number" or empty fields — the number is malformed, unallocated, or Numverify lacks data. A valid-but-sparse result (no carrier) is common for some regions/VoIP; it doesn't mean the number is fake.

## Gotchas & OpSec
- Human-in-the-loop: requires a Numverify API key; the free tier caps monthly lookups, so batch work needs a paid plan.
- Numverify returns *metadata*, not subscriber identity — it won't give you a name. Pair with a name-lookup tool for that.
- Carrier data reflects the original allocation and may be stale after number porting.
- OpSec: passive against the target; your key/IP are logged by Numverify.

## Overlaps ("do both")
- Pairs with subscriber-name lookups (region-specific, e.g. `[[numspy-api]]` for India) and messaging-app presence checks — FireFly confirms validity/carrier/region, while those attempt to attach an identity or confirm the number is actively used.

## Trust & verifiability
`trust: unverified` — a minor open-source wrapper; the underlying Numverify data is reasonably reliable for validity/carrier but can lag porting. Audit the script before running with your API key, and corroborate carrier/line type where it matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | firefly |
| category | phone |
| selectorsIn → selectorsOut | phone → phone, address |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
