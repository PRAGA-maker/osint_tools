---
id: spotthem-com
name: spotthem.com
description: Use when you have an email or name and want a quick people/email-search aggregator lookup — purpose inferred from name/listing; outputs unverified.
url: https://spotthem.com/
category: email
path:
- email
bestFor: A people/email lookup aggregator (inferred) for pivoting from an email or name to linked identities.
selectorsIn:
- email
- name
selectorsOut:
- name
- social-profile
- username
status: unknown
pricing: freemium
costNote: Pricing not confirmed; aggregator sites of this type are commonly freemium with paid full reports.
opsec: passive
opsecNote: Submitting a target email/name to a third-party aggregator means the query is logged by an operator you do not control; use a sock-puppet session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Listed on uk-osint.net under "Email Related Sites" but the operator, data sources, and current status are unconfirmed; capabilities are inferred from the name and category and were not verified.
missingPersonsRelevance: high
coverage: []
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- email
- Email Related Sites
source: uk-osint
lastVerified: ''
enrichment: full
---

# spotthem.com

> A people/email-search aggregator (inferred from name and listing) — capabilities not independently verified.

## When to use
You have an `email` or `name` and want a fast aggregator check for linked profiles or identities. Because the tool is unverified, treat any output as a lead to confirm elsewhere, not as a source of record.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://spotthem.com/ in a sock-puppet browser session.
2. Enter the `email` or `name` in the search field.
3. Read whatever the site returns — likely linked `social-profile`s, `username`s, or associated `name`s if it behaves like a typical aggregator.
4. Pivot: corroborate any hit with a tool of known provenance before relying on it.

## Inputs → Outputs
- **In:** `email`, `name` (inferred)
- **Out:** `name`, `social-profile`, `username` (inferred — unverified)
- **Empty/negative result looks like:** no matches, a paywall before results, or the site being offline.

## Gotchas & OpSec
- Capabilities, data freshness, and even live status are unconfirmed — do not assume accuracy.
- OpSec: passive, but you are handing a target identifier to an unknown operator; never query from case-linked infrastructure.

## Overlaps ("do both")
- Use alongside verified email/people-search tools; never rely on an unverified aggregator alone.

## Trust & verifiability
`trust: unverified` — appears only on a curated link list; operator and data provenance are unknown, so all output requires independent confirmation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | spotthem-com |
| category | email |
| selectorsIn → selectorsOut | email, name → name, social-profile, username (inferred) |
| pricing / cost | freemium (unconfirmed) |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
