---
id: chosic-com
name: Chosic.com
description: Use when you have a `social-profile` (a public Spotify playlist URL/username) and want to profile the owner's taste — returns genres, moods, decades and top artists as behavioural signal.
url: https://www.chosic.com/spotify-playlist-analyzer/
category: social-networks
path:
- social-networks
bestFor: Analyzing a public Spotify playlist to characterize its owner's musical taste, era and mood.
selectorsIn:
- social-profile
- username
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free to analyze public playlists in-browser; no login required. The site is ad-supported and sells unrelated music tools, but the analyzer itself is free.
opsec: passive
opsecNote: You submit a playlist URL to a third-party site, not to the target. The playlist owner is not notified. Only ever paste PUBLIC playlist links; do not authenticate with the subject's Spotify account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Chosic is a small independent music-tools site that reads Spotify's public API; the taste breakdown is a derived profile, useful as soft corroboration, not hard identity evidence.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Chosic Spotify Playlist Analyzer
tags:
- Social Media
- Spotify
- lifestyle-profiling
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Chosic.com

> Paste a public Spotify playlist and get its taste fingerprint — genres, moods, decades and favorite artists — as a soft behavioural profile of the owner.

## When to use
You've found a subject's public Spotify profile or a playlist link (via a bio link, a shared post, or a username pivot) and want to characterize them: what genres and eras they lean to, the emotional "mood" of their listening, and which artists recur. This is lifestyle/behavioural context — useful to corroborate that two accounts belong to the same person (matching taste), to humanize a profile, or to spot cultural/regional signals. It is never a hard identifier.

## How to use it (`bestInteractionPattern`: web-manual)
1. Get a public Spotify playlist URL (right-click a playlist in Spotify → Share → Copy link), or the subject's public profile and pick a playlist they made.
2. Open https://www.chosic.com/spotify-playlist-analyzer/ and paste the playlist link.
3. Read the breakdown: genre distribution, decade spread, mood/energy stats, and most-featured artists.
4. Pivot: recurring niche artists or a distinctive decade profile can help match this account to another (e.g. a Last.fm or YouTube account with the same taste), or add colour to a lifestyle picture.

## Inputs → Outputs
- **In:** `social-profile` / `username` (a public Spotify playlist or profile link)
- **Out:** taste profile (genres, moods, decades, top artists) that helps confirm or link a `social-profile`
- **Empty/negative result looks like:** an error that the playlist is private/unavailable, or a near-empty breakdown for a very short playlist — no owner identity is ever returned.

## Gotchas & OpSec
- Human-in-the-loop: none, but the playlist MUST be public — private playlists error out.
- This is derived behavioural data, not an identifier; treat matches as suggestive, not proof.
- Do not log in with, or request, the subject's Spotify credentials — only use public links.

## Overlaps ("do both")
- Pairs with any Spotify username/profile enumeration or a Last.fm lookup — those find the account, this characterizes the taste behind it.

## Trust & verifiability
`trust: community` — independent third-party site reading Spotify's public data; the analysis is reproducible but is a soft profile, so weight it accordingly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | chosic-com |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile, username → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
