---
id: support-rootsweb-com
name: support.rootsweb.com
description: Use when reading full email headers in RootsWeb genealogy mailing lists — a list-admin help article on viewing full headers to trace a poster's routing metadata.
url: https://support.rootsweb.com/s/article/listadmins-headersfull
category: email
path:
- email
bestFor: Viewing full email headers for RootsWeb mailing-list messages to extract a poster's routing/IP metadata.
selectorsIn:
- email
selectorsOut:
- ip-address
- domain
- metadata-exif
status: degraded
pricing: free
costNote: Free Ancestry/RootsWeb support documentation (RootsWeb services have been largely curtailed/archived).
opsec: passive
opsecNote: Reading headers of a list message you have is passive; no contact with the poster. RootsWeb mailing-list services are mostly discontinued, so the live workflow may not apply.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official RootsWeb/Ancestry support article; authoritative for its procedure, but RootsWeb mailing lists have been deprecated, so practical applicability is limited.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- email
- email-headers
- genealogy
- Email Header Related Sites
source: uk-osint
lastVerified: ''
enrichment: full
---

# support.rootsweb.com

> RootsWeb's help article on viewing full email headers for genealogy mailing-list messages.

## When to use
You are working a genealogy/family-history angle and hold a RootsWeb mailing-list `email` from or about a relative of a missing person, and want to read its full headers for the poster's `ip-address`, sending `domain`, and routing `metadata-exif`. Note RootsWeb mailing lists are now largely deprecated, so this is mostly relevant for archived correspondence.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read the article at the URL for the steps to display full headers on a RootsWeb list message.
2. Apply it to a list message in hand to expose the `Received:` chain and other routing fields.
3. Read bottom-to-top for the originating `ip-address`, plus `From`/`Return-Path` and the sending `domain`.
4. Pivot: the IP/domain feed geolocation and reputation checks; the genealogy context can surface family `associate`s.

## Inputs → Outputs
- **In:** `email` (a RootsWeb list message you possess)
- **Out:** `ip-address`, `domain`, routing `metadata-exif`
- **Empty/negative result looks like:** the list service is offline, the message routes only through RootsWeb relays (no real poster IP), or the article links are dead.

## Gotchas & OpSec
- RootsWeb mailing-list functionality has been discontinued; treat this as relevant to archived material rather than a live capability.
- OpSec: passive; you only inspect a message you already have.

## Overlaps ("do both")
- Same goal as `[[support-google-com]]` (header extraction) but specific to RootsWeb; use whichever matches the source of the message.

## Trust & verifiability
`trust: trusted` — official RootsWeb/Ancestry documentation, but degraded relevance because the underlying mailing-list service is deprecated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | support-rootsweb-com |
| category | email |
| selectorsIn → selectorsOut | email → ip-address, domain, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
