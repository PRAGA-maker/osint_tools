---
id: kworb
name: Kworb
description: Use when you have a musician/artist `name` and want to gauge their public streaming and chart footprint across YouTube, Spotify and iTunes — returns aggregate play/view statistics and links to their platform profiles.
url: https://kworb.net/
category: social-networks
path:
- social-networks
bestFor: Corroborating a musician/artist subject's public streaming footprint (Spotify, YouTube, iTunes) via aggregated chart data.
selectorsIn:
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to browse; no account, API key or payment required.
opsec: passive
opsecNote: Purely a read of publicly published chart/streaming aggregates. Nothing you look up is exposed to the subject, and no login is involved.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running independent chart-aggregation site; data is scraped/derived from Spotify, iTunes and YouTube public figures, so treat totals as good-faith aggregates rather than official numbers.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- kworb.net
tags:
- Social Media
- Universal
- music-streaming-stats
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Kworb

> An independent aggregator of public music-streaming and chart data (Spotify, iTunes, YouTube, US radio) — useful for confirming and profiling a musician subject's online footprint.

## When to use
Your subject is (or claims to be) a recording artist, and you have a `name` you want to corroborate against a real, ranked streaming footprint. Kworb lets you check whether an artist actually charts, how big their audience is, and which platforms carry them — a quick reality check on a music-career claim and a pivot to their official platform profiles.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://kworb.net/.
2. Choose a data section: Spotify (artist/song streaming totals and charts), iTunes (per-country top-100), YouTube (music-video view counts), or US radio airplay.
3. Use the site's artist listings/search within a section to locate the subject's name.
4. Read the output: cumulative stream/view counts, chart positions and movement, and country-level breakdowns. Each artist entry links out to their Spotify/YouTube/iTunes pages.
5. Pivot: follow the linked platform profiles to the artist's official Spotify/YouTube accounts, which then feed username- and social-profile-based OSINT.

## Inputs → Outputs
- **In:** `name` (artist or track)
- **Out:** `social-profile` (links to the artist's Spotify/YouTube/iTunes pages) plus aggregate streaming/chart statistics
- **Empty/negative result looks like:** the name doesn't appear in any chart or artist listing — meaning the person has no meaningful public streaming footprint, which itself is evidence against a "successful recording artist" claim.

## Gotchas & OpSec
- Kworb only covers artists with enough public traction to chart or accumulate meaningful streams; unsigned or tiny acts won't appear even if they have profiles.
- It contains **no personal data** — only aggregate music metrics — so it corroborates a persona, it does not identify a person.
- OpSec: **passive**; read-only, no login, nothing exposed to the subject.

## Overlaps ("do both")
- Pairs with direct Spotify/YouTube profile OSINT — Kworb tells you the *scale and reach* of an artist's footprint, while the platform profiles carry the account-level details (bios, links, follower networks).

## Trust & verifiability
`trust: community` — a well-established but independent aggregator. Figures are derived from public platform data and are highly reliable for relative comparison, but they are unofficial, so cite them as aggregates rather than as label- or platform-certified numbers.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kworb |
| category | social-networks |
| selectorsIn → selectorsOut | name → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
