---
id: instabot
name: InstaBot
description: Use when you have a public Instagram post/profile URL and want the raw media inside Telegram — returns the downloaded photos/videos as files.
url: https://telegram.me/InstaBot
category: messaging
path:
- messaging
bestFor: Grabbing Instagram media (photos, videos, stories) via a Telegram bot without a browser.
selectorsIn:
- social-profile
- username
selectorsOut:
- image
- metadata-exif
status: live
pricing: free
costNote: Free Telegram bot. Requires a Telegram account; no payment, though it may show ads/promo messages.
opsec: passive
opsecNote: You send the target's Instagram link to an anonymous Russian-operated Telegram bot, which fetches the media from Instagram's CDN (the poster is not notified). The bot operator sees every link you submit and it is tied to your Telegram identity — use a sock-puppet Telegram account, never your real one, and don't submit sensitive targets.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Anonymous third-party Telegram bot (~25k monthly users, Russian-language) with no transparency on operator or data handling. Fine for pulling public media; treat the bot itself as untrusted.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
relatedTools:
- instaloader
- threadsdownloader-com
aliases:
- InstaBot Telegram
- '@InstaBot'
tags:
- telegram
- instagram
- media-download
source: awesome-osint
lastVerified: '2026-07-14'
enrichment: full
---

# InstaBot

> A Telegram bot that downloads Instagram media on demand — paste a link in chat, get the photos/videos back as files.

## When to use
You have a public Instagram post, reel, story or profile (`social-profile`/`username`) and want the underlying media without opening a browser or scraper — you're already working in Telegram, or you want a quick throwaway pull. Send the link, the bot returns the files. It's a media-acquisition convenience, not a search or profiling tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. In a sock-puppet Telegram account, open https://telegram.me/InstaBot and press Start.
2. Paste the Instagram post/reel/profile URL into the chat.
3. The bot fetches and returns the media as downloadable photo/video files (mirror bots like `@InstaDevBot` exist if the main one is rate-limited).
4. Save the files and analyse them offline.
5. Pivot: the downloaded media feeds reverse-image search and EXIF/metadata extraction.

## Inputs → Outputs
- **In:** an Instagram post/reel/story/profile URL (`social-profile`) or `username`
- **Out:** downloaded `image`/video files, plus any surviving `metadata-exif`
- **Empty/negative result looks like:** the bot erroring, returning nothing, or asking you to retry — typically for private accounts, removed posts, rate-limits, or when Instagram changes and the bot lags. Public content only.

## Gotchas & OpSec
- Human-in-the-loop: needs a Telegram account; use a sock-puppet, because every link you send is logged against your Telegram identity by an unknown operator.
- Private Instagram accounts won't download.
- Instagram strips most EXIF on upload, so don't rely on GPS from the returned files; still worth checking.
- Anonymous Russian-language operator — don't feed it sensitive investigations.

## Overlaps ("do both")
- Pairs with `[[instaloader]]` (a transparent open-source CLI for structured Instagram downloads — preferable when provenance matters) and `[[threadsdownloader-com]]` (same idea for Meta Threads).

## Trust & verifiability
`trust: unverified` — an anonymous Telegram bot with no accountability. The media it returns comes from Instagram's CDN and is authentic, but the bot itself is untrusted; for anything you need to stand behind, use an open-source downloader you can audit.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | instabot |
| category | messaging |
| selectorsIn → selectorsOut | social-profile, username → image, metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
