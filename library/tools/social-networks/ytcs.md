---
id: ytcs
name: YTCS (YouTube Comment Search)
description: Use when you have a `username` or `name` and a YouTube video and want to find their comments — a browser extension that keyword-searches a video's comments in-page.
url: https://github.com/lettapp/ytcs
category: social-networks
path:
- social-networks
bestFor: Searching the comments on a specific YouTube video by keyword or commenter name, directly on the page.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free and open-source; requires your own (free) YouTube Data API key to run.
opsec: passive
opsecNote: Searching comments is read-only and does not notify the commenter. The extension runs locally in your browser using your API key; keep the key private. Use a sock-puppet browser profile and avoid replying/interacting, which would expose you.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: browser-extension
trust: community
trustNote: A small open-source Chrome extension (lettapp/ytcs); source is auditable on GitHub. It surfaces existing public YouTube comments via the official Data API, so results are authentic to YouTube.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
aliases:
- ytcs
- YouTube Comment Search
tags:
- Social Media
- YouTube
- browser-extension
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# YTCS (YouTube Comment Search)

> A browser extension that adds keyword search to a YouTube video's comments — find a specific commenter or phrase without scrolling thousands of comments, right on the page.

## When to use
You have a `username` or `name` and a YouTube video (or a subject's own channel) and want to check whether they commented, or find what they said. YouTube offers no native comment search, so pinpointing a subject's comment — which can carry self-disclosed detail, other handles, or timing — normally means endless scrolling. YTCS keyword-searches the loaded comments in-page, turning a video's comment section into something you can query.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install from the Chrome Web Store, or load the unpacked extension folder via Extensions → Developer Mode → Load unpacked.
2. Supply your own free YouTube Data API key when prompted (the extension needs it to fetch comments).
3. Open the target video; press `Ctrl-S` or click the extension icon to open the search box.
4. Search by commenter name/handle or by keyword; review matching comments and jump to the commenter's channel.
5. Pivot: a matched commenter's channel/handle (`social-profile`) feeds YouTube-channel OSINT and username sweeps.

## Inputs → Outputs
- **In:** `username`/`name` (commenter) or keyword, within a chosen video
- **Out:** matching comments → commenter `social-profile` (channel), `username`, and comment text/timestamps
- **Empty/negative result looks like:** no matching comment — the person didn't comment on that video, used a different display name, or the comment was deleted/hidden. Absence is per-video only.

## Gotchas & OpSec
- Human-in-the-loop: you must obtain and enter a YouTube Data API key (`api-key`); heavy use can hit API quota.
- OpSec: **passive** — reading comments notifies no one; runs locally with your key. Don't reply/interact, and keep the key private.
- It searches comments the API returns for that video; very large or comment-limited videos may not expose everything. Absence isn't proof.

## Overlaps ("do both")
- Pairs with YouTube-channel and username tools — a matched commenter's channel becomes a handle you can sweep across platforms.

## Trust & verifiability
`trust: community` — open-source and auditable, drawing on the official YouTube Data API, so the comments it surfaces are authentic to the platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ytcs |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | yes (api-key) |
