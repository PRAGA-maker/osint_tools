---
id: raditube
name: RadiTube
description: Use when you have a phrase or claim and want to find where it was spoken across hundreds of radical/fringe YouTube channels — returns transcript hits linked to the exact video timecode.
url: https://tool.raditube.com/
category: social-networks
path:
- social-networks
bestFor: Full-text searching the subtitles/transcripts of hundreds of radical YouTube channels to locate who said a given phrase and when.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- associate
status: degraded
pricing: free
costNote: Free research tool; the public version is being rebuilt and is currently in private beta (request access via info@raditube.com).
opsec: passive
opsecNote: Searching an external transcript index is passive and never touches the target channel. Following result links opens YouTube, which logs the view against your account/IP — use a sock-puppet/logged-out session for the click-through.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: A Bellingcat-listed research tool for monitoring radical-channel discourse; indexes are built by the maintainer, so coverage is a curated (not exhaustive) channel set.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- tool.raditube.com
- RadiTube search
tags:
- bellingcat-toolkit
- youtube
- extremism-research
- transcript-search
source: bellingcat-toolkit
lastVerified: '2026-07-20'
---

# RadiTube

> A transcript search engine over hundreds of radical/fringe YouTube channels — find the exact video and timecode where a phrase, claim, or name was spoken.

## When to use
You have a distinctive phrase, claim, or a subject's `name`/`username` and want to locate where it appears in the spoken content of fringe/radical YouTube channels — for extremism research, disinformation tracing, or placing a person within a radical media network. RadiTube indexes the subtitles of roughly 380 curated right/left radical channels across ~170,000 videos and returns hits linked to the precise timecode. Its missing-persons value is niche (radicalization/associate-network contexts), not general people-finding.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://tool.raditube.com/ — note the public tool is being rebuilt and is currently in **private beta**; request access at info@raditube.com if the open search isn't available.
2. Enter your query — an exact phrase (in quotes), a name, or a claim.
3. Read the results: which channel/video, and jump to the linked timecode to hear the context.
4. Note the channel and speaker to map who is echoing a claim and how it spreads (`associate` network of channels).
5. Pivot: identified channels/speakers feed further YouTube and social OSINT; the phrase's spread feeds disinformation analysis.

## Inputs → Outputs
- **In:** a phrase/claim, `name`, or `username`
- **Out:** transcript hits → source `social-profile` (channel/video + timecode), cross-channel `associate` spread
- **Empty/negative result looks like:** no transcript hit — the phrase may simply not have been spoken on the ~380 indexed channels; this is a curated set, so absence ≠ never said anywhere.

## Gotchas & OpSec
- Currently gated: the public tool is in private beta (manual access request), so it may be temporarily unavailable.
- Curated channel set (~380), not all of YouTube — coverage is deliberately bounded to radical channels.
- Subtitle/ASR errors can miss or garble phrases; try variants.
- OpSec: search is passive; click through to YouTube only from a sock-puppet session.

## Overlaps ("do both")
- Pairs with general YouTube search/transcript tools — RadiTube is tuned to radical channels and phrase-level timecodes; broader tools cover the rest of YouTube.

## Trust & verifiability
`trust: community` — a respected, Bellingcat-listed research tool, but a maintainer-curated index; verify each hit by listening at the linked timecode before quoting it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | raditube |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
