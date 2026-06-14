---
id: sylva-identity-discovery-2
name: Sylva Identity Discovery
description: Use when you have an email/username/PGP fingerprint and want to correlate linked identities via public GitHub and PGP keyservers — returns linked profiles and keys.
url: https://sylva.pfeister.dev/
category: email
path:
- email
- email-search
bestFor: Correlating an identity across public GitHub commit data and PGP keyservers from an email, username, or key fingerprint.
selectorsIn:
- email
- username
- document-id
selectorsOut:
- email
- username
- social-profile
- name
status: unknown
pricing: free
costNote: Free, open developer-built tool; runs locally so no per-query cost.
opsec: passive
opsecNote: Queries public GitHub and PGP keyservers, not the subject — the person is not alerted. Running it locally keeps queries on your own machine, though keyserver/GitHub requests come from your IP unless proxied.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: An individual developer's project (pfeister.dev); the exact feature set and data sources are inferred from its description and not independently verified. Confirm behavior against its repo/docs before relying on it.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases: []
tags:
- email
- email-search
- github
- pgp
source: arf-seed
lastVerified: ''
enrichment: full
---

# Sylva Identity Discovery

> A CLI tool that correlates an identity across public GitHub and PGP keyserver data from an email, username, or key fingerprint.

## When to use
You have an `email`, `username`, or a PGP key fingerprint (`document-id`) for a technically-inclined subject and want to discover linked identities — other emails on the same PGP key, GitHub accounts, and the names attached to them. Strong for developer/privacy-conscious personas where GitHub and PGP leave a public trail.

## How to use it (`bestInteractionPattern`: cli)
1. Install Sylva locally from https://sylva.pfeister.dev/ (follow its repo/docs for setup).
2. Run the CLI against your identifier (e.g. an email, GitHub username, or PGP fingerprint).
3. Read the output: linked `email`s, `username`s/GitHub `social-profile`s, and `name`s associated with the same person across PGP keys and commits.
4. Pivot: newly-discovered emails feed `[[snov-io]]` verification and breach search; GitHub handles feed username-correlation tools.

## Inputs → Outputs
- **In:** `email`, `username`, or PGP fingerprint (`document-id`)
- **Out:** `email`, `username`, `social-profile`, `name` (correlated identities)
- **Empty/negative result looks like:** no PGP key or GitHub footprint for the identifier — common for non-technical subjects.

## Gotchas & OpSec
- Only useful when the subject has a public GitHub/PGP presence; returns nothing for most general-population cases.
- Feature set and accuracy are inferred — verify against the project's documentation.
- OpSec: passive to the subject; queries hit GitHub/keyservers from your IP, so use a proxy/sock-puppet network if attribution matters.

## Overlaps ("do both")
- Pairs with the `[[sourcecon-com]]` GitHub-email technique (manual) — Sylva automates similar correlation; cross-check results between them.

## Trust & verifiability
`trust: unverified` — single-developer project; capabilities described here are inferred from its summary and require confirmation against the source before operational reliance.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sylva-identity-discovery-2 |
| category | email |
| selectorsIn → selectorsOut | email, username, document-id → email, username, social-profile, name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
