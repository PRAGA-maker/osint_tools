---
id: youtube-tool
name: yttool (youtube_tool)
description: Use when you have a YouTube video/channel/playlist and want to bulk-extract subtitles, comments, descriptions, and video lists via CLI — returns `metadata-exif`, `associate` (commenters).
url: https://github.com/nlitsme/youtube_tool
category: social-networks
path:
- social-networks
bestFor: Scriptable extraction of YouTube subtitles, comments, video info, live-chat replays, and full channel/playlist listings without the official API.
selectorsIn:
- social-profile
selectorsOut:
- metadata-exif
- associate
status: live
pricing: free
costNote: Free and open source (MIT); `pip3 install youtube-tool`. No API key — it uses YouTube's internal web API.
opsec: passive
opsecNote: Requests hit YouTube's public/internal endpoints as a normal client — no contact with the channel owner. Heavy use from one IP can be throttled; the tool supports proxies, and a VPN helps for sensitive targets.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: cli
trust: community
trustNote: An individual's open-source project (nlitsme); auditable and using YouTube's own internal API, but unofficial and liable to break when YouTube changes.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- youtube-channel-archiver
aliases:
- yttool
- youtube_tool
- nlitsme youtube_tool
tags:
- Social Media
- YouTube
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# yttool (youtube_tool)

> A no-API-key Python/CLI tool that pulls subtitles, comments, descriptions, live-chat replays, and full channel/playlist listings from YouTube — the scriptable companion to a full channel archiver.

## When to use
You have a YouTube video, channel, or playlist (`social-profile`) tied to a subject and want structured data fast: every comment (with commenter handles → `associate`), full subtitle text (searchable transcripts of what was said), video descriptions/metadata, and complete channel/playlist inventories. Ideal for mining a subject's own uploads or the audience engaging with a video, without registering for the official API.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip3 install youtube-tool` (Python 3.8+), giving you the `yttool` command.
2. List a channel's videos: `yttool -l <channel-url>`; get video info/description: `yttool --info <url>`.
3. Extract subtitles: `yttool --subtitles <url>` (multiple languages); pull comments: `yttool --comments <url>`; live-chat replay is also supported.
4. Use `--proxy` for many requests to avoid throttling.
5. Pivot: commenter handles feed username search; subtitle text is keyword-searchable for names/places/dates; channel inventory feeds a full archive.

## Inputs → Outputs
- **In:** `social-profile` (YouTube video/channel/playlist URL or ID)
- **Out:** `metadata-exif` (video info, descriptions, subtitles, upload data), `associate` (commenter handles), and channel/playlist listings.
- **Empty/negative result looks like:** disabled comments or subtitles return nothing; a private/removed video yields no data; breakage/errors usually mean YouTube changed its internal API — update the tool.

## Gotchas & OpSec
- Human-in-the-loop: YouTube rate-limits; use the proxy option and pace large jobs. Being unofficial, it can break when YouTube changes — keep it updated.
- Comment extraction on huge videos is slow and may be partial.
- OpSec: passive (public endpoints); route heavy scraping through proxies/VPN for sensitive targets.

## Overlaps ("do both")
- Pairs with `[[youtube-channel-archiver]]` — this is the flexible CLI extractor for subtitles/comments/metadata; the archiver focuses on bulk video+thumbnail+comment preservation of whole channels.

## Trust & verifiability
`trust: community` — an auditable open-source tool using YouTube's own internal API, so the data is genuine; being one developer's unofficial project, expect occasional breakage and verify output against the live page.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | youtube-tool |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → metadata-exif, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
