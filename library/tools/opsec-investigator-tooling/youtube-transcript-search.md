---
id: youtube-transcript-search
name: YouTube Transcript Search
description: Use when you have a YouTube `social-profile`/channel and want to search across its videos' spoken content — a Chrome extension that collects and full-text-searches transcripts.
url: https://chromewebstore.google.com/detail/eeebipnojmgobognppffkenhdoidendi
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Full-text searching the spoken words across a channel's videos, instead of watching them all.
selectorsIn:
- social-profile
selectorsOut: []
status: live
pricing: free
costNote: Free Chrome extension; no account required.
opsec: passive
opsecNote: Passive — it pulls publicly available transcripts/captions and searches them locally; you are not interacting with the channel owner. Watching the source videos afterwards is normal public viewing (use a sock-puppet/logged-out session if you don't want it in your watch history).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: unverified
trustNote: A third-party Chrome extension listed via Toddington's curated directory; relies on YouTube's auto/creator captions, which can be inaccurate or missing, and extension availability can change.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- YouTube transcript search extension
tags:
- toddington
- curated-directory
- add-ons-apps-extensions
- youtube
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# YouTube Transcript Search

> A Chrome extension that grabs transcripts across a channel's videos and lets you keyword-search the spoken content — so you can find where a topic, name, or place is mentioned without watching everything.

## When to use
You have a YouTube channel (a `social-profile`) and need to find where in its videos something is said — a name, an address, a phone number read aloud, a location, a claim. Reach for this to turn hours of video into searchable text: collect the transcripts and grep for your term, then jump to the exact video/timestamp. Far faster than manual viewing when a channel has many long videos.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the extension from the Chrome Web Store (the linked listing).
2. Go to the target channel or a set of its videos and let the extension collect the available transcripts/captions.
3. Search your keyword across the collected transcripts.
4. Use the hits to jump to the specific video and timestamp, then watch that segment to confirm context.
5. Pivot: a spoken name/place/number becomes a new selector for the rest of your workflow; the timestamp is your citation.

## Inputs → Outputs
- **In:** a YouTube channel/`social-profile` (its videos)
- **Out:** searchable transcript text with video+timestamp locations of your keyword (leads, not new selectors by itself)
- **Empty/negative result looks like:** videos with captions disabled or no auto-transcript return nothing to search; and auto-captions mis-transcribe names/numbers, so a miss may be a transcription error — verify by listening.

## Gotchas & OpSec
- Depends on captions: auto-generated transcripts are often wrong on proper nouns and numbers; treat a keyword miss cautiously and spot-check by ear.
- Extension availability/permissions can change; review what it accesses before installing.
- OpSec: passive; but watch source videos logged-out or on a sock puppet to keep them out of your account history.

## Overlaps ("do both")
- Pairs with transcript/caption downloaders and manual review — this finds *where* to look, then you confirm by listening. Combine with general YouTube-channel OSINT (about page, links, comments) for the full picture.

## Trust & verifiability
`trust: unverified` — a third-party extension relying on YouTube captions; the transcript is a lead, and the authoritative source is the video itself, so always confirm a hit by watching/listening to the segment.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | youtube-transcript-search |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | social-profile →  |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
