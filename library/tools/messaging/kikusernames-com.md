---
id: kikusernames-com
name: Kikusernames.com
description: Use when you have a Kik `username`/`name` and want to find a matching self-listed Kik profile — returns the profile `social-profile` and stated `geolocation`.
url: https://kikusernames.com/search
category: messaging
path:
- messaging
bestFor: Searching a user-submitted directory of Kik messenger usernames by handle or location.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- geolocation
status: live
pricing: freemium
costNote: Free to search/browse; some features (posting, contacting, online status) require creating a free account.
opsec: passive
opsecNote: Passive lookup against a third-party directory — Kik itself is not queried and the subject is not notified. It is unaffiliated with Kik. Only self-submitted profiles appear; do NOT create an account with real details or contact anyone during recon — use a sock puppet if account features are needed.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party, user-submitted Kik-username directory (unaffiliated with Kik Interactive); listings are self-posted and unverified, and the population skews toward dating/adult self-promotion.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Kik Usernames
tags:
- Messengers
- Kik
- username-search
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# Kikusernames.com

> A user-submitted directory of Kik messenger usernames, searchable by handle or location — a way to check whether a Kik handle is publicly self-listed.

## When to use
Kik is deliberately anonymous (no phone/real-name required), which makes handles hard to pivot. This third-party directory helps when a subject has *self-listed* their Kik `username` here (often to promote themselves): you can confirm the handle, read any self-provided profile text, and note a stated `geolocation`. Only covers people who chose to post, so it's a supplementary check, not a comprehensive Kik lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://kikusernames.com/search.
2. Search by the target `username` (or browse by country/location, or `name`/keyword).
3. Open a matching listing to read the self-submitted profile: handle, any bio text, stated location, and links.
4. Some features (online status, messaging) need a free account — use a sock puppet if you must, and never contact the target during recon.
5. Pivot: reused handles feed cross-platform username enumeration; stated location is a `geolocation` lead to corroborate.

## Inputs → Outputs
- **In:** Kik `username` (or `name`/location to browse).
- **Out:** self-listed profile `social-profile`, bio text, and stated `geolocation`.
- **Empty/negative result looks like:** no listing — the handle simply isn't self-posted here (the norm for most Kik users), not proof the handle doesn't exist on Kik.

## Gotchas & OpSec
- Self-submitted only: absence means unlisted, not nonexistent; presence is a lead, not verified identity.
- Unverified/adult-skewed: listings are user-posted and the directory leans toward dating/adult promotion — corroborate before asserting anything.
- Account features: contacting/online-status need signup — use a sock puppet, never real details.
- OpSec: passive to the target as long as you don't initiate contact.

## Overlaps ("do both")
- Pairs with cross-platform username-enumeration tools — those check where a handle exists broadly, this adds any Kik-specific self-listing and stated location.

## Trust & verifiability
`trust: community` — an unofficial, user-submitted directory unaffiliated with Kik; treat listings as unverified self-promotion and confirm identity through independent signals.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kikusernames-com |
| category | messaging |
| selectorsIn → selectorsOut | username, name → social-profile, geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
