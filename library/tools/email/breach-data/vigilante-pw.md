---
id: vigilante-pw
name: Vigilante.pw
description: Use when you want to identify WHICH historical data breaches a domain/site was involved in — returns a catalog of breach entries (source, date, record count, exposed fields).
url: https://www.vigilante.pw/
category: email
path:
- email
- breach-data
bestFor: Browsing a directory/catalog of known data breaches to learn what dumps exist for a given site or domain.
selectorsIn:
- domain
- email
selectorsOut:
- metadata
status: down
pricing: free
costNote: Was free to browse; registration was required to see some entries.
opsec: passive
opsecNote: A catalog of publicly disclosed breaches — browsing it does not touch the target. Note its provenance is dark-web/breach-trading adjacent.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Breach-index site of uncertain/anonymous provenance; has been intermittently offline/defunct for an extended period. Do not assume it is reachable or that its data is current.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- vigilante.pw
tags:
- email
- breach-data
- breach-index
source: arf-seed
lastVerified: ''
enrichment: full
---

# Vigilante.pw

> A directory/catalog of known data breaches — it indexed which dumps exist for which sites (source, date, record count, exposed fields), rather than letting you search a specific person.

## When to use
You have a `domain` or service name (or an `email` whose domain you care about) and want to know whether that site appears in a known breach, and what fields that breach exposed (passwords, addresses, phones, DOBs). For missing-persons work this scopes which breach datasets might contain a subject's exposed `address`/`phone`/`dob` — you then pursue those datasets through other access. **Important: this site has been unreliable/offline for a long time — verify reachability before relying on it.**

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.vigilante.pw/ — first confirm it actually loads (it has been down for extended periods).
2. If up, register/log in (some listings were gated) and browse or search the breach catalog by site/domain name.
3. Read the entry metadata: breach source, date, number of records, and which field types were exposed.
4. Pivot: this only tells you a breach *exists*; to look up an individual within breach data use a record search such as [[vigilante-pw]]'s peers — feed the domain to a have-I-been-pwned-style check and pursue the underlying dataset elsewhere.

## Inputs → Outputs
- **In:** `domain` / `email` (domain of interest), site name
- **Out:** `metadata` — breach catalog entries (source, date, record count, exposed field list)
- **Empty/negative result looks like:** site does not load at all (likely current state), or no catalog entry for the queried domain (no *known* breach indexed — not proof none exists).

## Gotchas & OpSec
- Likely **down/defunct**: treat `status: down` as the default expectation and verify before use. Do not invent results.
- It is an *index of* breaches, not a per-person search engine — it won't return a subject's exposed record directly.
- Provenance is anonymous and breach-trading-adjacent; some content sits in legal grey areas. Browse via sock infrastructure; do not log in with attributable credentials.
- OpSec: browsing is passive (no contact with the target), but the site itself is untrusted — assume it may log or fingerprint visitors.

## Overlaps ("do both")
- Conceptually pairs with breach-lookup engines (Have I Been Pwned, DeHashed, Snusbase): use those to confirm a specific `email` is in a breach, and a breach *catalog* like this to understand what each dump contained.

## Trust & verifiability
`trust: unverified` — anonymous-provenance breach index, intermittently/long offline. Cannot be relied upon as live, and its catalog accuracy cannot be independently confirmed. Verify the site loads and corroborate any finding before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vigilante-pw |
| category | email |
| selectorsIn → selectorsOut | domain, email → metadata |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
