---
id: instaloader-3
name: Instaloader
description: Use when you have an Instagram `username` (or hashtag) and want to bulk-archive its posts, captions, comments and metadata — returns images, EXIF/timestamps, tagged associates and profile data.
url: https://instaloader.github.io/
category: social-networks
path:
- social-networks
bestFor: Reliable command-line archiving of a public Instagram profile's media and metadata for timeline and associate analysis.
selectorsIn:
- username
selectorsOut:
- image
- metadata-exif
- social-profile
- associate
status: live
pricing: free
costNote: Free and open-source (MIT). Works anonymously for public profiles; some features (stories, private accounts, full follower lists) require logging in with an account.
opsec: active
opsecNote: Anonymous downloads of public content are low-touch, but any authenticated use hits Instagram's API as a logged-in client and risks rate-limiting or banning that account. Use a burner/sock-puppet login and a clean IP; never your own account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Mature, actively maintained open-source project (listed in Trace Labs awesome-osint); widely used and reliable, though it breaks intermittently when Instagram changes its private API.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- osintgram
- instagram-search-engine
aliases:
- instaloader
tags:
- python
- instagram
- social-media
- scraping
source: tracelabs-repos
lastVerified: '2026-07-10'
enrichment: full
---

# Instaloader

> A mature Python CLI that downloads an Instagram profile's photos, videos, captions, comments and metadata to disk — the most reliable way to archive a subject's Instagram for timeline and associate work.

## When to use
You have an Instagram `username` for a public account (or a hashtag/location) and want a clean, structured local archive rather than the ephemeral web UI. Instaloader captures post timestamps, captions, comment authors and tagged users — exactly the raw material for building an activity timeline and mapping `associate` relationships. It is the go-to when you need durable, scriptable Instagram capture.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install instaloader`.
2. Anonymous public grab: `instaloader profile <target_username>` downloads posts + metadata JSON to a per-profile folder.
3. For stories, tagged posts, or a private-but-followed account, log in with a **sock-puppet** account: `instaloader --login <burner> ...`.
4. Useful flags: `--comments`, `--geotags`, `--stories`, `--tagged`; each post's JSON carries timestamp, caption and tagged users.
5. Pivot: mine the downloaded metadata for `associate` handles and post times; run saved `image` files through `[[google-reverse-image-search]]` and EXIF checks.

## Inputs → Outputs
- **In:** `username` (public profile; or hashtag/location)
- **Out:** `image`/video media, `metadata-exif` (timestamps, geotags, captions in JSON), `social-profile` data, and `associate` lists (taggers/commenters)
- **Empty/negative result looks like:** a `401`/login-required or rate-limit error, or an empty folder for a private account — access was blocked, which is not evidence the account is empty.

## Gotchas & OpSec
- Instagram throttles aggressively; space out runs and expect occasional breakage until the tool updates to Instagram's latest API.
- OpSec: **active** once authenticated — isolate the burner account and IP. Anonymous public grabs are lighter-touch but still visible to Instagram.
- Geotags are only present if the poster added them; absence isn't proof of location.

## Overlaps ("do both")
- Pairs with `[[osintgram]]` — Instaloader excels at robust bulk *download*, Osintgram's shell is quicker for interactive network/tag pivots; when one breaks against Instagram's current API, try the other.
- `[[instagram-search-engine]]`-style discovery helps you find the handle before Instaloader archives it.

## Trust & verifiability
`trust: trusted` — well-maintained, widely-audited open-source tool; data is pulled directly from Instagram so it's first-party content, though counts can lag and the tool may need updating after platform changes.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | instaloader-3 |
| category | social-networks |
| selectorsIn → selectorsOut | username → image, metadata-exif, social-profile, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
</content>
