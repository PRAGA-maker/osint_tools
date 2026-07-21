---
id: yaseeker
name: YaSeeker
description: Use when you have a Yandex `username`/`email` and want to resolve the account — returns the owner `name`, profile `image`, linked `social-profile`s and account IDs.
url: https://github.com/HowToFind-bot/YaSeeker
category: social-networks
path:
- social-networks
bestFor: Enriching a Yandex login or email into a full profile — real name, photo, public ID, and connected services.
selectorsIn:
- username
- email
selectorsOut:
- name
- image
- social-profile
status: degraded
pricing: free
costNote: Free open-source Python CLI. No fees; you run it yourself. May need occasional fixing as Yandex changes endpoints.
opsec: passive
opsecNote: The tool queries public Yandex service endpoints for the account; it does not log into or notify the target. Run it from a VPN/sock-puppet network so the lookups aren't tied to your own IP. Yandex may rate-limit or block scraping IPs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A known community OSINT tool (222+ stars) but only lightly maintained — Yandex API/UI changes can break it. Verify current functionality on a known account before trusting negative results.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- osint-tools-howtofind-bot
aliases:
- YaSeeker
- Yandex account seeker
tags:
- Social Media
- Yandex
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# YaSeeker

> An open-source CLI that turns a Yandex login or email into a rich profile — real name, avatar, public ID, and connected Yandex services — by querying multiple Yandex endpoints at once.

## When to use
Your subject uses a Yandex account (common for Russian/CIS-region subjects, or anyone with a `@yandex.ru`/`@ya.ru` email). Give YaSeeker the login or email and it pulls together identity signals from across the Yandex ecosystem (Music, Collections, Reviews, Marketplace, Zen), often yielding a real name, a profile photo (for reverse-image/face work), the Yandex UID/Public ID, and links to connected social accounts.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `https://github.com/HowToFind-bot/YaSeeker` and install requirements (Python 3.6+).
2. Run it with the target's Yandex login/username or email (or a known Yandex public ID).
3. Read the output: full name, avatar URL, gender, UID/Public ID, account status (verified/banned/deleted), activity metrics, and any linked social media.
4. Verify the tool still works by running a known-good account first — a dormant scraper can silently return empties after Yandex changes.
5. Pivot: the avatar feeds `[[pimeyes-com]]`/reverse-image; the real name feeds people-search; the Public ID stabilises cross-referencing; linked socials feed `[[sherlock]]`/`[[whatsmyname]]`.

## Inputs → Outputs
- **In:** `username` (Yandex login) or `email`
- **Out:** `name`, `image` (avatar), `social-profile` (linked accounts), Yandex UID/Public ID, account status
- **Empty/negative result looks like:** the tool reports the account not found or returns blanks — could be a genuinely nonexistent account OR the tool being out of date / rate-limited. Confirm against a live Yandex profile view before concluding the account doesn't exist.

## Gotchas & OpSec
- Lightly maintained — Yandex endpoint changes can break it; always sanity-check on a known account so a stale scraper doesn't produce false negatives.
- Scraping can be rate-limited/blocked — run from a VPN, expect occasional failures.
- Passive to the target; only your own scraping IP is exposed to Yandex.

## Overlaps ("do both")
- Pairs with `[[osint-tools-howtofind-bot]]` (same author's tool suite) and general email/username tools — YaSeeker is Yandex-specific depth; combine with broad cross-platform enumeration for full coverage.

## Trust & verifiability
`trust: community` — a well-known community tool, but dormant enough that results must be re-verified against live Yandex; treat its output as leads confirmed on the platform, not gospel.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yaseeker |
| category | social-networks |
| selectorsIn → selectorsOut | username, email → name, image, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
