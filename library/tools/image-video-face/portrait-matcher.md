---
id: portrait-matcher
name: Portrait Matcher
description: Use when you have a `face` and want to see which historical portrait paintings it resembles — returns physical-description-style lookalikes, not identities.
url: http://zeus.robots.ox.ac.uk/portraitmatcher/index?error=agree
category: image-video-face
path:
- image-video-face
bestFor: A novelty face-similarity demo (Oxford VGG + Art UK) that matches an uploaded face to look-alike portrait paintings — useful for testing/teaching face-embedding behaviour, not for identification.
selectorsIn:
- face
- image
selectorsOut:
- physical-description
status: live
pricing: free
costNote: Free academic demo from Oxford's Visual Geometry Group; no account or payment.
opsec: active
opsecNote: You upload a face image to a University of Oxford server and, per the on-page consent, grant Oxford rights to retain and use it for academic purposes. Never upload a real target's or victim's face here — it leaves your control. Only use throwaway/test images.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Genuine academic project by Oxford's VGG in collaboration with Art UK; first-party and non-commercial, but purpose-built as a novelty, not an investigative tool.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- Oxford Portrait Matcher
- Art UK face match
tags:
- Image Search and Identification
- Reverse Image Search Engines and automation tools
source: cyb-detective
lastVerified: '2026-07-15'
enrichment: full
---

# Portrait Matcher

> An Oxford VGG × Art UK demo that finds the historical portrait paintings most similar to an uploaded face — a face-embedding novelty, not a person-identification tool.

## When to use
Reach for this only to understand or demonstrate how face-similarity/embedding models behave, or as a curiosity. It matches a `face` against a corpus of ~200k portrait paintings and returns lookalike artworks. It does **not** identify real people, so it has essentially no direct investigative value — do not use it to try to name or locate a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the URL and accept the academic-use consent.
2. Upload a face image or paste an image URL.
3. The tool returns the closest-matching portrait paintings with similarity scores.
4. There is nothing to pivot to for an investigation — the outputs are artworks, not identities. Treat any resemblance as coincidence.

## Inputs → Outputs
- **In:** `face` / `image` (a single frontal face)
- **Out:** ranked lookalike portrait paintings (a `physical-description`-style resemblance signal only)
- **Empty/negative result looks like:** no face detected / poor-quality upload rejected — and even a "match" is only a visual-similarity artwork, never a confirmed person.

## Gotchas & OpSec
- Not an identification tool: results are paintings, so a "match" tells you nothing about the person's real identity.
- OpSec: **active** — uploads go to Oxford and are retained under the consent clause; use only disposable test images, never a live target's face.
- For actual face identification use dedicated reverse-face engines, not this.

## Overlaps ("do both")
- Not a substitute for real face search — if you need to identify a person from a face, use a genuine reverse-face-search engine instead; this only surfaces artistic lookalikes.

## Trust & verifiability
`trust: trusted` — it is a real, first-party University of Oxford academic demo, so the tool is legitimate; the "trusted" rating reflects provenance, not investigative usefulness, which is minimal.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | portrait-matcher |
| category | image-video-face |
| selectorsIn → selectorsOut | face, image → physical-description |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
