---
id: goris
name: GORIS
description: Use when you have an `image` URL and want to script Google reverse image search at scale — returns links to matching images and web pages hosting the photo.
url: https://github.com/tanaikech/goris
category: image-video-face
path:
- image-video-face
bestFor: Command-line/scripted Google reverse image search over an image URL, returning up to ~100 matching links.
selectorsIn:
- image
selectorsOut:
- social-profile
- image
status: live
pricing: free
costNote: Free, open-source Go tool. No account or API key; it drives Google's public reverse-image endpoint.
opsec: active
opsecNote: Every run sends a query to Google from your IP. Google may rate-limit or serve CAPTCHAs on repeated automated searches — route through a sock-puppet IP/proxy if you are running many lookups, and never point it at the target's own site logs (use a neutral image host for the URL).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Actively maintained open-source project by developer tanaikech (v3.0.5, June 2025); updated to track Google's changing reverse-search spec. It is an unofficial scraper of Google, so it can break when Google changes its interface.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
aliases:
- goris Google reverse image search
- tanaikech/goris
tags:
- reverse-image-search
- Image Search and Identification
- Reverse Image Search Engines and automation tools
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# GORIS

> A Go command-line tool that automates Google reverse image search from an image URL — scriptable when you need to run reverse lookups in bulk rather than one at a time in a browser.

## When to use
You have a photo of a subject (a profile picture, a found image) hosted at a URL and want to know where else on the web it appears — matching images, and the pages that carry them. GORIS is the right pick when you need this scripted: batching many images, feeding results into a pipeline, or automating a workflow, rather than clicking through Google Images by hand.

## How to use it (`bestInteractionPattern`: cli)
1. Install Go, then `go install github.com/tanaikech/goris@latest` (or grab a prebuilt binary from the Releases page).
2. Run it against an image URL, e.g. `goris -u "https://host.example/photo.jpg"` — output is the list of matching image URLs and related web pages (up to ~100 results).
3. Parse/redirect the output into your notes or next tool.
4. Pivot: matching pages often reveal a `social-profile`, a name caption, or a different context for the same face — follow those links.

## Inputs → Outputs
- **In:** an `image` **URL** (the subject's photo hosted somewhere reachable).
- **Out:** URLs of visually matching images and the web pages hosting them; often `social-profile` links.
- **Empty/negative result looks like:** zero matches — either the image genuinely isn't indexed by Google, or Google returned only "visually similar" noise. Absence is not proof the photo is unique.

## Gotchas & OpSec
- **Local file search is currently broken** due to Google spec changes — only image **URLs** work reliably. Upload the photo to a neutral host first if you only have a local file.
- It scrapes Google's public interface, so it can break without warning when Google changes things; check for a newer release if it stops returning results.
- Active: runs hit Google from your IP; heavy use invites rate-limits/CAPTCHAs — proxy or throttle.

## Overlaps ("do both")
- Google indexing misses faces that Yandex/PimEyes catch — always run the same image through a second reverse-image engine.
- Feed found pages into username/social-profile tools to widen the identity picture.

## Trust & verifiability
`trust: community` — a maintained open-source Go project, but an unofficial wrapper around Google. Results are Google's; the tool's reliability tracks how current it is with Google's interface, so keep it updated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | goris |
| category | image-video-face |
| selectorsIn → selectorsOut | image → social-profile, image |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
