---
id: citizen-evidence-lab-toolbox
name: Citizen Evidence Lab Toolbox
description: Use when you have an `image`/video and want Amnesty International's curated list of verification tools (metadata viewers, reverse-image search, video verification) — returns a toolset, not data.
url: http://citizenevidence.org/toolbox
category: image-video-face
path:
- image-video-face
bestFor: A curated, trusted directory of image/video verification tools for authenticating visual evidence.
selectorsIn:
- image
selectorsOut:
- metadata-exif
- social-profile
status: degraded
pricing: free
costNote: Free resource from Amnesty International's Citizen Evidence Lab. Note the exact /toolbox path may 404 / have moved — navigate from citizenevidence.org to the current tools/resources section.
opsec: passive
opsecNote: The page is a directory of tools — reading it is passive. OpSec depends on whichever linked tool you then use (some reverse-image/metadata tools upload your image to a third party); check each tool's own handling before submitting sensitive media.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by Amnesty International's Citizen Evidence Lab, a highly reputable human-rights verification unit; the curation is trustworthy, though specific links/pages can move or go stale over time.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Citizen Evidence Lab
- Amnesty verification toolbox
tags:
- toddington
- curated-directory
- image-video-multimedia-search
- verification
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
relatedTools:
- citizen-evidence-lab
---

# Citizen Evidence Lab Toolbox

> Amnesty International's curated toolbox for authenticating images and videos — a trusted starting point for metadata extraction, reverse-image search, and video verification.

## When to use
You have an `image` or video and need to *verify* it — extract `metadata-exif`, find where else it appears, check when it was really uploaded, or confirm a claimed location/date — and you want a vetted list of the right tools rather than guessing. The Citizen Evidence Lab is built for exactly this in a human-rights/verification context, so its toolbox points to reputable, current tools.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to citizenevidence.org (if the /toolbox URL 404s, navigate to the current Tools/Resources section from the homepage).
2. Pick the task: metadata/EXIF extraction, reverse-image search, video verification (e.g. upload-time/thumbnail checks), or geolocation aids.
3. Follow the linked tool and run your `image`/video through it — the toolbox is a signpost; the analysis happens in the destination tool.
4. Cross-verify with more than one tool (verification best practice) before drawing conclusions.
5. Pivot: extracted metadata/geolocation and reverse-image hits feed identity/location OSINT; a matched earlier upload can debunk a "first-hand" claim.

## Inputs → Outputs
- **In:** `image`/video to verify (you bring the media)
- **Out:** a curated toolset that yields `metadata-exif`, prior-appearance/`social-profile` hits, and provenance signals (via the linked tools)
- **Empty/negative result looks like:** a dead/moved link on the directory — the Lab's site persists but individual entries can rot; use it as a menu, and go to the current tool directly if a link is stale.

## Gotchas & OpSec
- It's a directory, not an analysis engine — value is the curation; the actual work happens in the linked tools.
- The /toolbox page may have moved (degraded link); reach the tools via the current site navigation.
- OpSec: reading is passive, but some linked tools upload your image to third parties — check each before submitting sensitive media.

## Overlaps ("do both")
- Pairs with the specific tools it curates — e.g. [[jpegsnoop-2]] for offline EXIF/forensics and reverse-image engines ([[pimeyes-com]]) for prior appearances.

## Trust & verifiability
`trust: trusted` — curated by Amnesty International's verification lab; the guidance is authoritative, with the only caveat that individual links can age — confirm you're on the current tool.
