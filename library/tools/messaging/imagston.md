---
id: imagston
name: IMAGSTON
description: Use when you have a `name`/`username` and want to find the subject's Mastodon accounts across servers — returns matching profiles with avatar, bio, and creation date.
url: https://seintpl.github.io/imagstodon/
category: messaging
path:
- messaging
bestFor: Searching many Mastodon (fediverse) instances at once for accounts matching a name/handle, collecting profile details.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- image
status: live
pricing: free
costNote: Free, open browser tool hosted on GitHub Pages by SEINT (seintpl); no account or payment.
opsec: passive
opsecNote: It queries public Mastodon instance search endpoints from your browser for public profile data — the account owner is not notified. Passive. Your IP hits the instances queried; use a sock-puppet browser/VPN for hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Built by SEINT (Sector035 / seintpl), a well-regarded OSINT developer; open and inspectable, relying on Mastodon's own public search.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- namint
- seintpl-github-io
- amireal
aliases:
- Imagstodon
- IMAGSTODON
tags:
- Social Media
- Mastodon
source: cyb-detective
lastVerified: '2026-07-16'
enrichment: full
---

# IMAGSTON

> A fediverse profile finder — searches multiple Mastodon servers for accounts matching a name or handle and collects each profile's avatar, bio, account type, and creation date.

## When to use
You have a `name` or `username` and suspect the subject is on Mastodon/the fediverse (common for tech, activist, and privacy-minded people who left Twitter/X). Because Mastodon is decentralized across thousands of independent servers, there's no single search box — IMAGSTON fans a query across instances so you don't have to check each one.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the tool in a sock-puppet browser.
2. Enter the target `name` or `username`.
3. It queries multiple Mastodon instances and returns matching profiles.
4. Read each hit: profile picture (`image`), display name/handle, account type, creation date, and bio — use these to judge which account is your subject.
5. Pivot: a confirmed handle/instance links to the subject's posts and followers; a bio often reveals other platforms, a real name, or a location.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** matching Mastodon `social-profile`s with avatar (`image`), bio, account type, and creation date
- **Empty/negative result looks like:** no profiles returned — the subject isn't on the queried instances (the fediverse is huge; not every server is covered), or the handle differs; try name variants.

## Gotchas & OpSec
- Coverage is limited to the instances the tool queries — a null result doesn't rule out the fediverse entirely.
- Handle reuse and impersonation are common; confirm identity with bio/posting content, not the handle alone.
- OpSec: passive; profile owners aren't alerted, but browse under a persona.

## Overlaps ("do both")
- Pairs with `[[namint]]` and general username-search tools — those generate/validate handle variants across platforms; IMAGSTON specializes in resolving them on Mastodon specifically.

## Trust & verifiability
`trust: community` — an open tool from a respected OSINT developer over Mastodon's public search; results are authentic profile data, but confirm the account is your subject before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | imagston |
| category | messaging |
| selectorsIn → selectorsOut | name, username → social-profile, image |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
