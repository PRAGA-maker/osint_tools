---
id: screenshot-full-page-screen-capture
name: Screenshot - Full Page Screen Capture
description: Use when you need to preserve on-screen web evidence as a screenshot or screen recording before it changes — a browser capture extension, not a lookup on a subject.
url: https://chrome.google.com/webstore/detail/screen-recorder/jgmmgiojkjopgnanopiamhbhnpaednfg/related
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Capturing a screenshot or screen recording of a web page/app in-browser to preserve evidence before it's edited or deleted.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free browser extension with optional paid tiers; captures save locally to your machine.
opsec: passive
opsecNote: Capture happens locally in your browser — nothing about the target is transmitted by the act of capturing. Two cautions: (1) a browser extension can see page content, so install only reputable ones and disable them on sensitive internal work; (2) a screenshot alone is weak evidence — pair it with a timestamped archive (Wayback/archive.today) and record the URL, date/time, and your method for chain-of-custody.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: unverified
trustNote: A third-party capture extension; convenient for quick preservation, but not a tamper-evident evidence tool on its own.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- Full Page Screen Capture
- screen recorder extension
tags:
- evidence-capture
- screenshot
- browser-extension
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# Screenshot - Full Page Screen Capture

> A one-click browser capture extension — grab a full-page screenshot or screen recording of web content before it disappears. Evidence preservation, not subject research.

## When to use
You're viewing something online that matters to a case — a profile, a post, a listing, a comment thread — and it could be edited or deleted at any moment. This captures the page (full-length screenshot or a screen recording of an interaction) directly from your browser so you keep a copy. It preserves what *you* see; it returns no data about any subject on its own.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the extension from the Chrome Web Store (link above).
2. Navigate to the page you need to preserve; make sure the relevant content and the URL bar are visible/loaded.
3. Trigger a full-page screenshot, or start a screen recording to capture a dynamic interaction (scrolling, playing media, expanding threads).
4. Save the capture locally and immediately record the URL, date/time (UTC), and how you captured it.
5. Pivot: back the capture with an independent timestamped archive so the evidence isn't only your own screenshot.

## Inputs → Outputs
- **In:** none about a target — you capture what's on your screen
- **Out:** a local screenshot/recording of the web content (a preserved artifact, not a harvested selector)
- **Empty/negative result looks like:** a broken/partial capture — lazy-loaded or infinite-scroll content may not render fully; scroll to load everything first, or use a dedicated full-page archiver.

## Gotchas & OpSec
- A screenshot is **easily faked and weak alone** — always pair it with an independent timestamped archive (Wayback/archive.today) and a note of URL + time + method.
- Extensions can read page content; install only reputable ones and disable on sensitive/internal sites.
- Dynamic/lazy-loaded pages may capture incompletely — verify the artifact shows what you intended.

## Overlaps ("do both")
- Do both with archive.today / the Wayback Machine: your local capture is instant and complete, while an external archive provides an independent, citable timestamp you don't control.

## Trust & verifiability
`trust: unverified` — a convenient third-party capture extension. Fine for fast preservation, but not tamper-evident; treat its output as your working copy and corroborate with independent archives for anything evidentiary.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | screenshot-full-page-screen-capture |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
