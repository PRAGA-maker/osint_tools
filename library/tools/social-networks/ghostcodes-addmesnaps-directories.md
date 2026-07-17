---
id: ghostcodes-addmesnaps-directories
name: GhostCodes/AddMeSnaps directories
description: Use when you have a `name`, interest, or handle and want to find someone's Snapchat account — returns public Snapchat usernames from opt-in "add me" directories.
url: https://www.addmesnaps.com
category: social-networks
path:
- social-networks
bestFor: Discovering public Snapchat handles that users self-listed, filterable by age/gender/interest.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free public directory (addmesnaps.com now redirects to addmes.io); no registration required to browse.
opsec: passive
opsecNote: Browsing an opt-in directory of self-submitted handles is passive; the listed user chose to be public and isn't told you looked. No login. Adding/contacting a person on Snapchat would be active — stay at the directory-lookup stage.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-run "add me" directory of self-submitted Snapchat usernames; entries are user-provided and unverified.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- snapchat
- snap-map
aliases:
- AddMeSnaps
- addmes.io
- GhostCodes
tags:
- snapchat
- username-directory
- social-media
source: kimi-tiktok-snap
lastVerified: '2026-07-17'
enrichment: full
---

# GhostCodes/AddMeSnaps directories

> Opt-in Snapchat "add me" directories — where users publicly list their handles, letting you pivot from an interest, name, or partial handle to a Snapchat account.

## When to use
Snapchat has no public profile search, which makes it hard to find someone's account. "Add me" directories like AddMeSnaps (and the former GhostCodes) collect handles that users submitted themselves, sometimes with age, gender, and interests. Use one when you have a subject's likely `username`/`name` or know their interests and want to locate a self-listed Snapchat handle to confirm an account exists and grab the exact handle.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.addmesnaps.com (redirects to addmes.io) — the largest such directory; GhostCodes is largely defunct, so AddMeSnaps is the live option.
2. Browse or filter by age range, gender, and interest/category, and search for a name/handle.
3. Read the listing: Snapchat username plus whatever the user self-declared.
4. Confirm identity via corroborating signals (matching handle/photos/bio elsewhere), not a single listing.
5. Pivot: a confirmed handle → check activity via `[[snapchat]]`; public geotagged content → `[[snap-map]]`; reused username → cross-platform search.

## Inputs → Outputs
- **In:** `username`, `name`, or an interest/category
- **Out:** self-listed Snapchat `username`(s)/`social-profile`, plus self-declared age/gender/interests
- **Empty/negative result looks like:** no listing — most Snapchat users never submit to these directories, so a null is very weak evidence the person has no Snapchat.

## Gotchas & OpSec
- Coverage is tiny and skews toward people seeking new contacts — the vast majority of accounts aren't here; absence proves little.
- Entries are self-submitted and unverified; anyone can list any handle, so confirm independently.
- GhostCodes (the app) is effectively dead; treat AddMeSnaps/addmes.io as the current directory.
- Passive to browse; don't cross into adding/messaging the person.

## Overlaps ("do both")
- Pairs with `[[snap-map]]` — the directory finds a *handle*; Snap Map finds public *content* by location. Different angles on Snapchat.
- Pairs with `[[snapchat]]` to check whether a discovered handle is a live, active account.

## Trust & verifiability
`trust: community` — a self-submission directory with no vetting. A listing tells you a handle was posted, not that it belongs to your subject; verify via corroborating cross-platform signals.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ghostcodes-addmesnaps-directories |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
