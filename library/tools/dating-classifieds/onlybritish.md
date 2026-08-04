---
id: onlybritish
name: OnlyBritish
description: Use when you have a `name` or `username` and want to check whether the subject runs a UK OnlyFans account — returns a directory profile with handle, bio, and outbound links.
url: https://onlybritish.uk/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Finding whether a UK subject has an OnlyFans presence and pivoting from their handle/bio.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free to browse and search; no account needed for the directory itself.
opsec: passive
opsecNote: You browse a third-party aggregator's public pages — the subject is not notified. It is an adult-content site; use a sock-puppet browser/session and avoid clicking through to OnlyFans itself (which can require login and may leave a footprint). No case data is submitted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Independent third-party directory with no affiliation to onlyfans.com; it aggregates publicly listed creators, so listings can be stale, self-submitted, or promotional.
missingPersonsRelevance: low
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- OnlyBritish directory
tags:
- onlyfans
- uk
- adult
source: osintambition-social
lastVerified: '2026-08-04'
enrichment: full
---

# OnlyBritish

> A third-party directory of UK OnlyFans creators — searchable by handle and browsable by category, useful as an existence-check and handle/bio pivot.

## When to use
You have a `name` or `username` for a UK-linked subject and want to confirm or rule out an OnlyFans presence, or you already have an OnlyFans handle and want the surrounding bio, links, and self-described niche without logging into OnlyFans directly. Relevant for lifestyle/associate mapping; for missing-persons work it is a corroboration/pivot source, not a locator.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://onlybritish.uk/ in a clean/sock-puppet browser session.
2. Search the `username`/handle, or browse the categorised listings and filters (free-trial, niche) to find a `name` match.
3. Read the directory profile: handle, self-written bio, listed niche, and any outbound links (other socials, Linktree, etc.).
4. Confirm identity carefully — a matching display name is a lead, not proof; corroborate via the linked profiles.
5. Pivot: the handle and outbound links feed username-search and social-profile tools; a reused handle often chains to accounts on other platforms.

## Inputs → Outputs
- **In:** `name`, `username`
- **Out:** `social-profile` (the OnlyFans/linked accounts), `username` (confirmed handle)
- **Empty/negative result looks like:** no listing found — meaning the subject is not in this directory, NOT that they have no OnlyFans account (the directory is a curated subset, not exhaustive).

## Gotchas & OpSec
- Listings are self-submitted or promotional, so bios can be marketing copy and links can be affiliate-tagged.
- Adult-content context: keep it to a dedicated investigative browser/identity; do not sign into OnlyFans from your real account.
- UK-scoped by design — non-UK creators will not appear even if they exist elsewhere.

## Overlaps ("do both")
- Pairs with a general username-search tool: OnlyBritish confirms the OnlyFans handle, then run that handle across platforms to widen the footprint.

## Trust & verifiability
`trust: unverified` — an independent aggregator unaffiliated with OnlyFans; treat every listing as a lead to confirm against the actual linked profiles.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | onlybritish |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, username → social-profile, username |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
