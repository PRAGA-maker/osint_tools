---
id: a-small-world
name: ASMALLWORLD
description: Use when you have a `name`/`username` for an affluent-travel subject and want to check for a members-club profile — returns a `social-profile` and event/travel activity (requires joining).
url: https://www.asmallworld.com
category: communities-forums
path:
- communities-forums
bestFor: Checking whether a subject holds a profile in the ASMALLWORLD luxury-travel members community and reading their public-to-members activity.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: A free account tier exists; the core "membership" (events, full benefits) is a paid annual club. You must register to see member content.
opsec: active
opsecNote: To search members you must create an account and log in, so your presence and searches happen from that identity — use a fully built-out sock-puppet, never a personal account, and expect that a niche community may notice odd behaviour. Viewing a member's profile may be visible to them depending on settings.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A real, established members-only travel network; profiles are self-created by members, so identity and travel claims are self-reported and need corroboration.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- ASW
- asmallworld.com
- A Small World
tags:
- toddington
- curated-directory
- online-communities-blogs
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# ASMALLWORLD

> A members-only luxury-travel social community (100k+ members, 100+ countries) — a niche surface where an affluent, well-travelled subject may keep a profile you won't find on mainstream networks.

## When to use
Your subject fits ASMALLWORLD's demographic — high-net-worth, frequent luxury travel, event-going — and you want to check for a members-club profile, event attendance, or travel activity that mainstream social networks don't show. It is a supplementary social surface, most useful when a subject's lifestyle points to exclusive-community membership.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create a sock-puppet account at https://www.asmallworld.com (free tier) — you cannot see member content logged out.
2. Use the member search / directory (where available on your tier) for the subject's `name`/`username`.
3. Open any matching `social-profile` — read bio, location, events attended, and connections.
4. Note that deeper features and some visibility are gated behind paid membership.
5. Pivot: a confirmed profile → cross-reference photos/details with other social accounts; listed events/locations → place-and-time leads.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** a member `social-profile` (bio, location, events, connections) if one exists
- **Empty/negative result looks like:** no member match — the subject likely isn't a member (this is a small, exclusive base, so absence is common and not meaningful on its own).

## Gotchas & OpSec
- **Human-in-the-loop: account-login.** Registration is mandatory to see anything; isolate the account.
- Small community — investigative behaviour can stand out; move carefully.
- Profiles are self-reported vanity content; treat claims (locations, lifestyle) as leads to verify.

## Overlaps ("do both")
- Complements mainstream social-profile searches — those cover the broad networks; ASMALLWORLD catches the exclusive-community footprint they miss for an affluent subject.

## Trust & verifiability
`trust: community` — a genuine members network, but all content is member-authored and self-reported; corroborate any identity/location detail against independent sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | a-small-world |
| category | communities-forums |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
