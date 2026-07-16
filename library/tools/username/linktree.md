---
id: linktree
name: Linktree
description: Use when you have a Linktree `username`/handle and want the person's aggregated set of links — returns their linked `social-profile` accounts and `domain` destinations.
url: https://linktr.ee/
category: username
path:
- username
bestFor: Resolving a Linktree handle into the full set of social profiles, sites and contact links a person chose to publish in one place.
selectorsIn:
- username
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Viewing a public Linktree page is free and requires no account; free/paid tiers only affect page owners, not viewers.
opsec: passive
opsecNote: You are viewing a public bio page the subject published themselves; visiting it does not notify them. Passive — but Linktree pages can carry click-tracking, so route through a sock-puppet browser/VPN for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: First-party hosted, self-published link pages; the links are exactly what the account owner chose to expose, so they are authentic but curated (not exhaustive).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- linktr.ee
- link-in-bio
tags:
- username
- link-in-bio
- social-linkage
source: inteltechniques-tools
lastVerified: '2026-07-16'
enrichment: full
---

# Linktree

> The dominant link-in-bio service — a handle resolves to a single page where a person has collected all the profiles, sites and contacts they want to share.

## When to use
You have a `username`/handle that appears on a Linktree URL (`linktr.ee/<handle>`), commonly linked from an Instagram/TikTok/Twitter bio, and you want the person's whole published footprint at once: every social account, personal site, shop, booking page or contact link they aggregated. It is one of the fastest ways to jump from a single handle to a full set of `social-profile` links.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the subject's Linktree at `https://linktr.ee/<handle>` (found in their social bios, or by guessing the handle they reuse elsewhere).
2. Read the list of published links.
3. Capture each destination: linked social accounts (`social-profile`) and websites/shops (`domain`), plus any email/booking/contact links.
4. Note the ordering and labels — people often reveal current priorities (a job, a cause, a new project) by what they put first.
5. Pivot: run each surfaced handle through username-enumeration tools; visit linked domains; feed emails into email OSINT.

## Inputs → Outputs
- **In:** `username` (Linktree handle)
- **Out:** `social-profile` (linked accounts), `domain` (linked sites/shops/contacts)
- **Empty/negative result looks like:** a 404 (no such handle), or a live but sparse page with one or two links — the person maintains it minimally.

## Gotchas & OpSec
- Curated, not exhaustive: it shows only what the owner chose to list, and may omit accounts they want kept separate.
- Links can go stale (dead shops, deleted accounts); verify each destination still resolves.
- OpSec: passive, but pages may include click analytics — use a sock-puppet browser/VPN when discretion matters.
- Note competing services (Beacons, Carrd, Bio.link, Linkin.bio) — a subject may use one of those instead.

## Overlaps ("do both")
- Pairs with username-enumeration tools (Sherlock/WhatsMyName-style): Linktree gives the person's self-declared links, enumeration finds the accounts they did NOT list.

## Trust & verifiability
`trust: community` — first-party self-published pages. The links are authentic (the owner put them there), but the set is deliberately curated, so treat absence of a link as non-informative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | linktree |
| category | username |
| selectorsIn → selectorsOut | username → social-profile, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
