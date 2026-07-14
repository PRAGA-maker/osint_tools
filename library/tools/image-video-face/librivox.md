---
id: librivox
name: LibriVox
description: Use when you have a `name`/`username` you suspect narrates public-domain audiobooks and want their reader profile, forum activity and voice samples — returns social-profile leads.
url: https://librivox.org
category: image-video-face
path:
- image-video-face
bestFor: Identifying and profiling volunteer audiobook narrators — reader pages, forum accounts, and recorded voice samples.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Entirely free and non-commercial; all recordings are public-domain and downloadable without an account.
opsec: passive
opsecNote: You browse a public volunteer catalogue and forum; nothing target-facing is sent. Fully passive — reader and forum pages are open to anyone.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running, reputable non-profit volunteer project; reader profiles and forum posts are self-published by the volunteers themselves.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- LibriVox audiobooks
tags:
- toddington
- curated-directory
- image-video-multimedia-search
- audio
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# LibriVox

> A free, volunteer-run public-domain audiobook library — useful in OSINT as a source of narrator identities, forum accounts, and recorded voice samples.

## When to use
You have a `name` or `username` and reason to think the subject records audiobooks (a hobbyist reader, voice-work interest, or a matching handle), and you want their LibriVox reader page, catalogue of recordings, and forum activity. The distinctive payoff is a **voice sample**: a confirmed reader page gives you recordings you can compare against other audio, plus a forum account that often links to other contact points.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://librivox.org and search the catalogue by reader `name`/`username`, or search the LibriVox forum where volunteers coordinate.
2. Open the reader's page: their list of contributed recordings and any self-published links.
3. Download recordings for voice comparison; read forum posts for handles, timezones, and linked accounts.
4. Pivot: a forum `username` feeds cross-platform username search; voice samples feed voice-matching; the LibriVox API/catalogue can be queried programmatically for a reader's full contribution history.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** `social-profile` (reader page, forum account, self-linked sites) plus downloadable voice recordings
- **Empty/negative result looks like:** no matching reader or forum account — most people have never narrated for LibriVox, so a miss is expected and not informative.

## Gotchas & OpSec
- The population is tiny and self-selected (public-domain audiobook volunteers); relevance is high only when there is a specific reason to suspect involvement.
- Reader "names" are often pseudonyms; treat a handle as a lead, not a legal identity.
- OpSec: passive; a fully public catalogue and forum.

## Overlaps ("do both")
- Pairs with username-enumeration tools — carry the LibriVox forum handle to other platforms — and with any voice-analysis workflow that needs a reference sample.

## Trust & verifiability
`trust: community` — a reputable non-profit, but reader/forum content is volunteer self-published; corroborate any identity claim against the linked accounts before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | librivox |
| category | image-video-face |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
