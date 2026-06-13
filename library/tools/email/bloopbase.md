---
id: bloopbase
name: Bloopbase
description: Use as a (currently unreachable) Keybase-hosted email/OSINT resource — the host does not resolve, so treat as down and substitute another email tool.
url: https://bloopbase.keybase.pub/
category: email
path:
- email
bestFor: (Historically) an email-related OSINT resource hosted on a Keybase public folder.
selectorsIn:
- email
selectorsOut:
- email
status: down
pricing: free
costNote: Keybase public-folder hosting is free; no account needed to view, when it resolves.
opsec: passive
opsecNote: A static Keybase public folder would be read-only and passive. Not assessable further while unreachable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Hosted on a personal keybase.pub folder ("bloopbase"); individual-published, not an institution. The URL did not resolve on 2026-06-13 (connection failed / host not found), so capabilities cannot be confirmed.
missingPersonsRelevance: low
coverage: []
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- breach-vip
aliases:
- bloopbase.keybase.pub
tags:
- email
- Email Related Sites
source: osint4all
lastVerified: '2026-06-13'
enrichment: full
---

# Bloopbase

> A personal Keybase-hosted ("keybase.pub") email/OSINT resource — currently unreachable, so treat as down.

## When to use
Was listed (via osint4all) as an email-related OSINT resource on a Keybase public folder. On 2026-06-13 the host did not resolve, so there is no usable capability right now. Reach for `[[breach-vip]]` or another email tool instead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Attempt to open https://bloopbase.keybase.pub/.
2. If it resolves, browse the listed files/resource (Keybase public folders are static read-only listings).
3. As observed (host not found / connection failed), it does not load — abandon and use an alternative.

## Inputs → Outputs
- **In:** `email` (intended)
- **Out:** unknown — could not be confirmed while the host is unreachable
- **Empty/negative result looks like:** the URL fails to resolve entirely (current state).

## Gotchas & OpSec
- Status **down**: the host did not resolve on 2026-06-13. Keybase's public-folder service has had availability/sunset issues, so this may be permanently gone.
- OpSec: a static public folder would be passive; not further assessable while down.

## Overlaps ("do both")
- For breach/credential lookups by email, use `[[breach-vip]]` instead.

## Trust & verifiability
`trust: unverified` — a personal Keybase folder with no institutional backing, and currently unreachable; do not rely on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bloopbase |
| category | email |
| selectorsIn → selectorsOut | email → email |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
