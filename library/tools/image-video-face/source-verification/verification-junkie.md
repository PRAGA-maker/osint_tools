---
id: verification-junkie
name: Verification Junkie
description: Use when you have an `image`, video, or claim to verify and want a curated menu of the right verification tools — returns links to tools, not data itself.
url: https://verificationjunkie.com/
category: image-video-face
path:
- image-video-face
- source-verification
bestFor: Discovering, by category, the verification/forensics tools to reach for when checking media or eyewitness claims.
selectorsIn:
- image
selectorsOut: []
status: degraded
pricing: free
costNote: Free directory; hosts no data, only categorized links to third-party verification tools.
opsec: passive
opsecNote: Browsing the directory is passive. Note it currently has a TLS certificate mismatch, so the site throws a security warning — inspect links carefully and don't submit anything on the page itself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A practitioner-built directory (by journalist Josh Stearns) of verification tools; useful as a map, but link rot and the current certificate issue mean you must verify each linked tool independently.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- verificationjunkie.com
tags:
- source-verification
- media-forensics
- directory
source: arf-seed
lastVerified: '2026-07-21'
enrichment: full
---

# Verification Junkie

> A categorized directory of tools for verifying images, video, eyewitness reports, and real-time claims — a "where do I even start" map for media verification rather than a data source.

## When to use
You have a piece of media or a claim (a photo purporting to show a location, a viral video, an eyewitness account) and you're deciding *which* verification technique/tool to apply. Verification Junkie groups tools by task — verifying images, verifying video, verifying real-time information, verifying people/accounts — so you can jump to the right category instead of guessing. Useful when your own toolkit has a gap and you need a vetted starting list.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://verificationjunkie.com/ — **expect a certificate warning** (the TLS cert currently mismatches the hostname); proceed only if you're comfortable, and treat the page as read-only.
2. Browse the category that matches your task (e.g. "verifying images and photos", "verifying video").
3. Follow the linked tools out to their own sites; verify each one still exists and works (the directory predates some closures).
4. Apply the chosen tool to your `image`/video/claim.
5. Pivot: for image work specifically, jump straight to the dedicated tools already in this library (reverse-image, EXIF/metadata, ELA) rather than relying on possibly-stale links here.

## Inputs → Outputs
- **In:** the *task* of verifying an `image`/video/claim (you bring the media)
- **Out:** a categorized list of third-party verification tools to try — no data about a subject
- **Empty/negative result looks like:** a category whose links are dead or a page you can't reach past the cert warning; fall back to this library's own verification tools.

## Gotchas & OpSec
- **Degraded:** current certificate mismatch triggers browser warnings; the resource is a link index, not a data tool, so don't enter anything on it.
- Link rot: some listed tools have shut down — always confirm the destination is live before trusting it.
- It's a directory, not an engine — it points you at tools, it doesn't verify anything itself.

## Overlaps ("do both")
- Pairs with the concrete verification tools in this library (reverse-image search, EXIF/metadata viewers, `[[perceptual-image-analysis]]`) — Verification Junkie is the map; those are the instruments.

## Trust & verifiability
`trust: unverified` — a respected practitioner's curated list, but its value is only as current as its links, and the certificate issue means you should treat the site cautiously and verify each linked tool yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | verification-junkie |
| category | image-video-face |
| selectorsIn → selectorsOut | image → (tool directory) |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
