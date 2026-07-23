---
id: screencast-o-matic
name: Screencast-O-Matic (ScreenPal)
description: Use when you need to capture ephemeral online content (stories, live streams, scrolling profiles) as a video/screenshot record before it disappears — returns a saved recording for your evidence file.
url: https://screencast-o-matic.com
category: documents-metadata
path:
- documents-metadata
bestFor: Recording ephemeral or hard-to-save web content (live streams, disappearing stories, scrolling pages) into a timestamped video or screenshot for the case file.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free tier records up to 15-minute clips with a watermark and basic screenshots; longer recordings, editing, and hosting need a paid Solo/Team plan. The browser recorder needs no account.
opsec: passive
opsecNote: Runs locally in your browser/desktop — capture happens on your machine, so nothing is sent to the target. If you use ScreenPal's cloud hosting to store or share a recording, that copy leaves your control; keep sensitive evidence local.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: Established commercial screen-recording product (rebranded from Screencast-O-Matic to ScreenPal); reliable as a capture utility, but it is a vendor tool, not an evidentiary chain-of-custody system.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- ScreenPal
- Screencast-o-matic
- screencast o matic
tags:
- toddington
- curated-directory
- useful-websites-tools-documents
- evidence-capture
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# Screencast-O-Matic (ScreenPal)

> A quick screen/webcam recorder for preserving content that can't be right-click-saved — live video, disappearing stories, scrolling feeds — as a timestamped clip for your file.

## When to use
This is investigator *tooling*, not a lookup source: it produces no selectors, it preserves them. Reach for it when you've found something online that is live, animated, or set to expire — an Instagram/Snapchat story, a livestream, a map fly-through, a scrolling profile — and a static screenshot won't hold it. Record it before it's gone so the finding survives in the case file.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Go to https://screencast-o-matic.com (redirects to screenpal.com) and launch the free browser recorder, or install the ScreenPal desktop app for longer captures.
2. Set the capture region (full screen, a browser window, or a fixed rectangle) and choose whether to include system audio and/or webcam.
3. Start recording, then perform the actions on-screen — play the video, scroll the feed, open the story — narrating the date/URL on the audio track for provenance.
4. Stop and save the file **locally** (MP4). Note the source URL, capture time, and your name alongside it; the recording itself is the artifact.
5. For a single frame instead of video, use its screenshot + annotation tool to mark up the relevant detail.

## Inputs → Outputs
- **In:** none (a capture utility — you point it at whatever is on your screen)
- **Out:** none as selectors — produces an MP4/screenshot evidence artifact
- **Empty/negative result looks like:** N/A; failure mode is a corrupted/short recording — verify playback before you close the source page.

## Gotchas & OpSec
- Free clips are watermarked and capped at ~15 minutes; plan long captures around that or use a paid tier.
- Capturing is passive and local, but **hosting/sharing via ScreenPal's cloud uploads your evidence to a third party** — keep sensitive material local.
- A screen recording is not tamper-proof evidence on its own; pair it with the source URL, a timestamp, and (ideally) a hash if chain-of-custody matters.
- Recording DRM-protected streams may capture black frames.

## Overlaps ("do both")
- Complements metadata/archival tools: use an archiver to freeze a static page, and Screencast-O-Matic to capture the *dynamic* content an archiver can't — they preserve different failure modes of the same page.

## Trust & verifiability
`trust: community` — a mature, widely used commercial recorder; dependable for capture, but treat its output as an investigator-made artifact whose provenance you must document, not a certified record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | screencast-o-matic |
| category | documents-metadata |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
