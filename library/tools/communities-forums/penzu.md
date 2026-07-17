---
id: penzu
name: Penzu
description: Use when a lead points to a Penzu journal or you are enumerating a `username` across platforms — returns a `social-profile` only when the diarist chose to make an entry public.
url: https://penzu.com
category: communities-forums
path:
- communities-forums
bestFor: Checking whether a username exists on Penzu and reading the rare deliberately-shared public journal entry.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free tier with unlimited private entries; paid tiers ($19.99–$49.99/year) add encryption locking and customisation. Reading a shared entry is free.
opsec: passive
opsecNote: Viewing a public shared-entry link is passive and anonymous. Do not sign up and attempt to contact or follow a diarist — Penzu is a private-by-design product and interaction is intrusive and conspicuous.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A legitimate, long-running (since 2008) private-journaling service; its OSINT surface is intentionally tiny because content is private and encrypted by default.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Penzu
- penzu.com
tags:
- toddington
- online-communities-blogs
- private-journal
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Penzu

> A private-by-default online journal/diary — mostly a closed surface, useful in OSINT only for username enumeration and the rare entry a diarist chose to publish.

## When to use
You are enumerating a `username`/handle across platforms and want to know whether it also exists on Penzu, or a lead (a link in a bio, a forum post, an email) points at a specific Penzu shared-entry URL. Because Penzu entries are private and encrypted by default, there is almost nothing to scrape — the value is confirming account existence and reading any entry the owner deliberately made public or shared.

## How to use it (`bestInteractionPattern`: web-manual)
1. If you have a direct shared-entry URL, open it and read/capture the content immediately (the owner can unshare it at any time).
2. For enumeration, run the handle through a username-search tool rather than probing Penzu by hand — Penzu itself exposes little public profile surface.
3. If an entry is public, extract selectors from the text (locations, names, dates) as leads.
4. Pivot: a confirmed handle strengthens cross-platform identity correlation; a shared entry's content feeds your timeline.

## Inputs → Outputs
- **In:** `username` / a shared-entry link
- **Out:** `social-profile` — account existence and, only if the owner published it, the text of a shared journal entry
- **Empty/negative result looks like:** nothing accessible — which is the normal case here, since journals are private by default. Absence tells you almost nothing about the person.

## Gotchas & OpSec
- Private by design: the vast majority of Penzu content is unreachable; do not expect a feed of entries.
- Ephemeral shares: a public entry can be unshared or deleted, so archive on first sight.
- Do not attempt to log in, guess passwords, or otherwise access non-public journals — that crosses from OSINT into unauthorised access.
- OpSec: passive only for public links.

## Overlaps ("do both")
- Best paired with a dedicated username-enumeration tool for the existence check; on its own Penzu yields little, so treat it as one checkbox in a cross-platform handle sweep rather than a standalone source.

## Trust & verifiability
`trust: unverified` — the platform is legitimate, but because content is private and encrypted, there is rarely anything to verify; treat any public entry's claims as unverified self-authored text.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | penzu |
| category | communities-forums |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
