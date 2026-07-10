---
id: search-twitter-bios-and-profiles
name: Search Twitter Bios and Profiles (Followerwonk)
description: Use when you have a `name`, keyword, employer or location and want to find matching X/Twitter and Bluesky accounts by bio text — returns social profiles, usernames and account metadata.
url: https://followerwonk.com/bio
category: social-networks
path:
- social-networks
bestFor: Keyword/boolean search of X/Twitter and Bluesky bios to discover accounts by who they say they are.
selectorsIn:
- name
- username
- employer-org
selectorsOut:
- social-profile
- username
- name
status: live
pricing: freemium
costNote: Now part of Fedica. A free sign-up allows basic bio searches; deeper filtering, sorting, exports and larger result sets require a paid Fedica plan.
opsec: passive
opsecNote: Searches run against Followerwonk/Fedica's index, not against the target's account, so no notification reaches anyone. Free features require creating a Fedica/Followerwonk account — register with a sock-puppet identity, since your searches are tied to that login.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Established social-analytics tool (Moz-era Followerwonk, now under Fedica); reputable but a third-party indexer whose coverage depends on X/Bluesky API access, which has tightened over time.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- Followerwonk
- Followerwonk Bio Search
- Fedica bio search
tags:
- twitter
- x
- bluesky
- bio-search
- social-search
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Search Twitter Bios and Profiles (Followerwonk)

> Search the *bios* — not just handles — of X/Twitter and Bluesky to surface accounts by keyword, employer, location or self-description.

## When to use
You have a `name`, a job title/`employer-org`, a location, an interest, or a distinctive phrase a subject would put in their bio, and you want to find their (or related) social accounts. Because it searches profile text rather than requiring an exact handle, it is strong for discovery when you know *about* someone but not their `username` — e.g. "photographer + Wellington" or a company name plus a first name.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://followerwonk.com/bio (Followerwonk is now delivered through Fedica).
2. Sign up / log in with a sock-puppet Fedica account (a free account is required for searching).
3. Enter keywords — use boolean operators (AND / OR / NOT) to combine a `name`, `employer-org`, location, or interest.
4. Apply filters where available: location, language, follower count, verification, account age.
5. Read the ranked list of matching accounts (`social-profile` + `username` + display `name` + bio). Export requires a paid plan.
6. Pivot: a matched handle feeds a full profile scrape / `[[social-search-tools]]`; a bio location seeds `geolocation`; a linked site feeds domain/WHOIS.

## Inputs → Outputs
- **In:** `name` / keyword / `employer-org` / location (as bio text)
- **Out:** matching `social-profile` links, `username`s, display `name`s and bio snippets on X/Twitter and Bluesky
- **Empty/negative result looks like:** zero matching accounts — means no indexed bio contains your terms (try broader/alternate keywords), not that the person has no account. Coverage is limited to what the tool has indexed via platform APIs.

## Gotchas & OpSec
- Human-in-the-loop: an account login is mandatory even for the free tier; exports/deep filters are paywalled.
- Coverage caveat: X/Bluesky API restrictions mean the index is not exhaustive and can lag; a real account may simply not be indexed.
- OpSec: **passive** — the subject is never touched; but your queries are tied to your Fedica login, so keep it a sock puppet.

## Overlaps ("do both")
- Pairs with native X advanced search and Bluesky search, and with broader `[[social-search-tools]]` — bio search finds accounts by self-description, while native search finds them by posts/interactions. Run both to catch accounts with sparse bios.

## Trust & verifiability
`trust: community` — a well-known analytics vendor, but a third-party indexer; verify any candidate account by opening it directly on X/Bluesky, since bio matches can be coincidental or on impersonation accounts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-twitter-bios-and-profiles |
| category | social-networks |
| selectorsIn → selectorsOut | name, username, employer-org → social-profile, username, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
