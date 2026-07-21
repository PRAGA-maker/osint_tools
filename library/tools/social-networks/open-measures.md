---
id: open-measures
name: Open Measures
description: Use when you have a `username`, keyword or `name` and want to find posts and accounts across fringe/alt platforms (Telegram, Gab, Truth Social, 4chan, Rumble, VK, and more) — returns matching posts and `social-profile`s.
url: https://public.openmeasures.io
category: social-networks
path:
- social-networks
bestFor: Bulk keyword/username search across alternative and fringe social platforms (Telegram, 4chan, Gab, Truth Social, Rumble, Bluesky, VK, etc.).
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free public app and public API require no registration but are rate-limited (~39 requests/day) and date-limited (~last 6 months of data); paid subscriptions unlock full history, higher limits and more datasets.
opsec: passive
opsecNote: You query Open Measures' collected archives, not the platforms directly, so the target account is never touched or notified. Only Open Measures sees your query terms. No login is required for the public tier.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established open-source research organization (widely cited by Bellingcat and academic disinformation researchers); it archives public posts from alt platforms for open-source investigation.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- openmeasures.io
- Open Measures Public App
- formerly Open Measures / Network Contagion
tags:
- bellingcat-toolkit
- multiple-platforms
- fringe-platforms
source: bellingcat-toolkit
lastVerified: '2026-07-21'
enrichment: full
---

# Open Measures

> A search engine over archived posts from alt/fringe platforms — Telegram, Gab, Truth Social, 4chan, Rumble, Bluesky, VK and ~20 others — that mainstream tools and Google don't index.

## When to use
Your subject may be active on platforms that fall outside normal search: a `username` or `name` that turns up nothing on Google/mainstream social may still be posting on Telegram channels, Gab, Truth Social, 4chan/8kun, Parler, Gettr, Rumble, Odysee, VK, Bluesky or the Fediverse. Open Measures lets you run one query across those archives at once — valuable when a person has migrated to alternative platforms after being deplatformed elsewhere, or when tracing extremist/harmful-content trails.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://public.openmeasures.io (no account needed for the public app).
2. Enter your search term — a username, name, phrase, or handle. Basic, Boolean, and advanced query modes are supported.
3. Select which datasets/platforms to search (4chan, 8kun, BitChute, Bluesky, Fediverse, Gab, Gettr, Odysee, MeWe, Minds, OK, Parler, Poal, Rumble, RuTube, Scored, Telegram, TikTok, Truth Social, VK, Wimkin, and more).
4. Read the results: matching posts with platform, timestamp, author handle, and content — timeline and volume views help spot activity spikes.
5. Pivot: an author handle found here becomes a `social-profile`/`username` to run through username-enumeration and platform-specific tools; the source channel/community points to where the subject congregates.

## Inputs → Outputs
- **In:** `username`, `name`, or keyword/phrase
- **Out:** `social-profile` (matching accounts/handles) plus the posts themselves, with platform, timestamp and author
- **Empty/negative result looks like:** zero hits across selected datasets — the subject isn't posting matching content on the covered platforms, or (on the free tier) the activity is older than the ~6-month public window and needs a paid account.

## Gotchas & OpSec
- Free tier is **rate-limited (~39 queries/day) and time-limited (~6 months)** — deep or historical sweeps need a subscription.
- Coverage is broad but not total; each dataset has its own collection lag and gaps, so absence isn't proof.
- OpSec: **passive** — you search an archive, never the live platform, so no account is ever alerted.

## Overlaps ("do both")
- Pairs with mainstream-platform and username-enumeration tools — Open Measures covers the *fringe* platforms those tools miss, so running both closes the gap between mainstream and alt-tech presence.

## Trust & verifiability
`trust: trusted` — a well-regarded open-source research organization featured in Bellingcat's toolkit and cited in academic disinformation work. Data is archived from public posts, so hits are real content, but always confirm a critical result against the live source where it still exists.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | open-measures |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
