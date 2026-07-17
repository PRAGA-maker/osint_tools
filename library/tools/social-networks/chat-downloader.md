---
id: chat-downloader
name: Chat Downloader
description: Use when you have a `social-profile` / livestream or VOD URL and want the full chat log — returns commenter `username`s, `name`s, and timestamped messages as JSON for network/behaviour analysis.
url: https://github.com/xenova/chat-downloader
category: social-networks
path:
- social-networks
bestFor: Pulling complete chat/comment logs from YouTube and Twitch livestreams, premieres, and past broadcasts into structured JSON — no login required.
selectorsIn:
- social-profile
selectorsOut:
- username
- name
status: live
pricing: free
costNote: Free and open-source (MIT), installed from PyPI. No account or API key needed for public streams.
opsec: passive
opsecNote: It reads public chat via the platforms' own endpoints without authenticating, so nothing ties the pull to you or alerts the streamer. Run from a clean IP if you want the requests themselves unattributable; do not authenticate with a personal account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Well-maintained open-source project (600+ commits, active through 2023, widely used); accuracy depends on the platforms not changing their unofficial chat endpoints.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- yt-dlp
aliases:
- chat-downloader
- xenova/chat-downloader
tags:
- social-media
- livestream-chat
- python
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Chat Downloader

> A Python CLI/library that dumps the entire chat of a YouTube/Twitch stream (live, VOD, premiere, or clip) to JSON — turning ephemeral scrolling chat into a searchable dataset of who said what, when.

## When to use
Your subject runs or frequents a livestream and the community around it is the lead. Chat is where regulars, aliases, and off-hand personal details surface — but it scrolls away. Pull the full log to (a) enumerate the `username`s of a streamer's active community, (b) find a specific person's messages across many streams, or (c) build a timeline of when an account was present. Especially useful for missing-persons work where a subject was active in a streaming community.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install chat-downloader`.
2. Run against a URL: `chat_downloader "https://www.youtube.com/watch?v=VIDEO_ID"`.
3. Save structured output: add `--output chat.json` to get JSON with author name, author id/handle, timestamp, and message.
4. Filter/scope with flags (`--message_types`, `--start_time`, `--end_time`) to narrow to a window or a message type.
5. Pivot: grep the JSON for a target `username`/`name` → confirm presence and quotes; enumerate frequent chatters → new `social-profile`s to run through username tools.

## Inputs → Outputs
- **In:** `social-profile` / a stream, VOD, premiere, or clip URL (YouTube, Twitch; Facebook in development)
- **Out:** `username` and display `name` of each chatter, plus timestamped message text (JSON)
- **Empty/negative result looks like:** an empty/near-empty log — chat was disabled, the VOD's chat replay is unavailable, or the platform changed its endpoint (upgrade the package). Not proof no chat existed.

## Gotchas & OpSec
- Relies on the platforms' unofficial chat endpoints; a platform change can break it until the package is updated. Keep it current.
- Passive — no authentication, so no alert to the streamer and no tie to your accounts.
- Display names ≠ stable identifiers; use the author id/handle field for reliable pivoting.

## Overlaps ("do both")
- Pairs with `[[yt-dlp]]` — yt-dlp grabs the video/metadata while Chat Downloader grabs the conversation; run both to capture the full context of a stream.

## Trust & verifiability
`trust: community` — a mature, widely used open-source tool. Output is the platform's real chat data, so it is as accurate as the source; verify identities via stable id fields, not display names.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | chat-downloader |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → username, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
