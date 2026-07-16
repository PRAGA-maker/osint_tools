---
id: followerwonk-tools-for-twitter-analytics-bio-search-and-more
name: 'Followerwonk: Twitter/X Bio Search & Analytics'
description: Use when you have a `name`, keyword, or `username` and want to find or profile social accounts by bio text and analyze their followers — returns social-profile, geolocation and associate leads.
url: https://followerwonk.com/
category: social-networks
path:
- social-networks
bestFor: Searching social-media bios by keyword/location to discover accounts, and analyzing a handle's followers and activity.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- geolocation
- associate
status: live
pricing: freemium
costNote: Free tier allows bio search and basic account analysis; deeper analytics, comparisons, and exports require a paid plan.
opsec: passive
opsecNote: Analyzes public profile and follower data; the target is not notified. Deeper features require a Followerwonk account (login) — use a sock-puppet account, and note connecting your own social account authorizes API access from it.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing social-analytics tool (formerly Moz, now independent); reliable for what public APIs expose, though platform API limits affect completeness.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Followerwonk
- followerwonk.com
tags:
- twitter
- bio-search
- social-analytics
source: metaosint
lastVerified: '2026-07-16'
enrichment: full
relatedTools:
- moz-analytics-open-site-explorer
- moz-link-explorer
---

# Followerwonk: Twitter/X Bio Search & Analytics

> A social-bio search and follower-analytics tool: find accounts whose bios contain a keyword, name, or location, and profile a handle's followers, activity, and demographics. Now independent and covering X, Bluesky, Mastodon, and Pixelfed.

## When to use
Two jobs. (1) **Bio search** — find accounts by what people write about themselves: search a `name`, employer, town, or interest to surface candidate `social-profile`s (great for locating a person's account when you only know biographical details). (2) **Analyze** a known `username`: its followers, most-active times, and follower `geolocation`/demographic breakdown, which can reveal `associate`s and where a person is based.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://followerwonk.com/.
2. **Search bios:** enter keywords (name, city, job, interest) to get a ranked list of accounts whose profiles match.
3. **Analyze:** enter a handle to see follower counts, activity patterns, follower locations, and account demographics (deeper views need a login/paid plan).
4. Compare two accounts to find shared followers (overlap → likely community/`associate`s).
5. Pivot: candidate profiles → username enumeration and profile enrichment; follower locations → `geolocation` lead; shared-follower overlap → network mapping.

## Inputs → Outputs
- **In:** keyword/`name` (bio search) or `username` (analysis)
- **Out:** matching `social-profile`s, follower `geolocation`/demographics, and shared-follower `associate` overlaps.
- **Empty/negative result looks like:** few/no bio matches, or thin analytics — the biographical terms aren't in anyone's bio, or platform API limits capped the data; broaden keywords or try another platform.

## Gotchas & OpSec
- Depends on platform APIs; X/Twitter API restrictions can limit depth and freshness of results.
- Bio search only finds what people *write* in their bio — many real accounts have sparse or joke bios and won't match.
- Deeper analytics and exports are gated behind a paid plan and a login; free tier is limited.

## Overlaps ("do both")
- Pairs with `[[followgraph-for-mastodon]]` and username-enumeration tools — Followerwonk finds accounts by bio and profiles followers; those expand a known account's network across platforms.

## Trust & verifiability
`trust: community` — an established analytics tool surfacing public profile/follower data; the data is real but API-limited, so treat counts and demographics as approximate and verify a specific account directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | followerwonk-tools-for-twitter-analytics-bio-search-and-more |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, geolocation, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
