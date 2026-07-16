---
id: trevorfox-com-2
name: trevorfox.com
description: Use when you have a LinkedIn post/activity URL (a `social-profile` artifact) and want its true publication timestamp — returns the exact `dob`-style creation date/time decoded from the post ID.
url: https://trevorfox.com/linkedin-post-date-extractor.html
category: social-networks
path:
- social-networks
bestFor: Extracting the exact date/time a LinkedIn post was published from its URL, even when LinkedIn only shows "3w ago."
selectorsIn:
- social-profile
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: The post-date extractor is free and needs no login; the site also promotes a paid analytics product ("Flux"), which is unrelated to this single-purpose tool.
opsec: passive
opsecNote: Decoding happens locally in your browser from the post ID embedded in the URL — LinkedIn is not queried and the poster gets no notification. Fully passive. You do need to have obtained the post URL first (viewing the post on LinkedIn is a separate, logged action if done from an attributable account).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A single-purpose utility by developer Trevor Fox; the timestamp math (decoding the epoch millis from the first 41 bits of the post ID) is deterministic and verifiable, so results are reliable regardless of who hosts the page.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- matthewcassinelli-com
- trevorfox-com
aliases:
- LinkedIn Post Date Extractor
- Trevor Fox LinkedIn timestamp
tags:
- linkedin
- LinkedIn & Similar Sites
- timestamp
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# trevorfox.com — LinkedIn Post Date Extractor

> Turns a LinkedIn post URL into its exact publish timestamp — the same trick as Twitter/Snowflake IDs, applied to LinkedIn activity IDs.

## When to use
You have a LinkedIn post, comment, or activity URL and LinkedIn only shows a fuzzy "2mo" / "3w ago." You need the precise date and time — to place the subject's last verified online activity, to build a timeline, or to confirm whether a "recent" post actually predates a disappearance.

## How to use it (`bestInteractionPattern`: web-manual)
1. On LinkedIn, copy the post's shareable URL (it contains a long numeric activity/post ID, e.g. `...activity-7160000000000000000-xxxx`).
2. Open https://trevorfox.com/linkedin-post-date-extractor.html.
3. Paste the URL. The tool extracts the numeric ID, converts it to binary, and reads the first 41 bits as milliseconds since the Unix epoch.
4. Read the output: the creation timestamp in both UTC and your local time.
5. Pivot: drop the timestamp into your timeline; cross-check against other dated activity ([[matthewcassinelli-com]] for Mastodon, or platform-native timestamps elsewhere).

## Inputs → Outputs
- **In:** a LinkedIn post/activity URL (`social-profile` artifact)
- **Out:** exact publication date/time (UTC + local) — a `metadata-exif`-style timestamp
- **Empty/negative result looks like:** if the URL has no decodable numeric ID (e.g. a profile URL, a shortened `lnkd.in` link, or a reshare wrapper), it returns nothing or a nonsensical date — resolve the link to the canonical post URL first.

## Gotchas & OpSec
- Works only on URLs that actually embed the numeric post/activity ID; profile links and some share-wrappers won't decode. Expand shortened links first.
- The timestamp is the post's *creation*, not last edit — an edited post still shows original publish time.
- OpSec: **passive** — the extraction is pure client-side math on the ID; LinkedIn is never contacted and the poster is not alerted. (Obtaining the URL by viewing the post is a separate step; use a sock-puppet/logged-out view if attribution matters.)

## Overlaps ("do both")
- Pairs with `[[matthewcassinelli-com]]` and other ID-decoding utilities — same principle (recover hidden metadata from an embedded ID) across different platforms; use whichever matches the URL you hold.

## Trust & verifiability
`trust: community` — a hobbyist single-purpose page, but the underlying decode is deterministic and independently checkable (the ID→epoch conversion is public math), so the output is trustworthy even though the site itself is informal.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | trevorfox-com-2 |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
