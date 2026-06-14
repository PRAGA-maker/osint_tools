---
id: in20years-co
name: in20years.co
description: Use when you have a face photo and want to visualize an aged-up version of the same person — returns an AI age-progressed face image.
url: http://in20years.co/
category: image-video-face
path:
- image-video-face
bestFor: AI age-progression of a face photo to estimate how a subject may look years older.
selectorsIn:
- image
- face
selectorsOut:
- image
- physical-description
status: unknown
pricing: freemium
costNote: Typically free for a basic render; some age/quality options may be gated. Unverified.
opsec: passive
opsecNote: You upload a face image to a third-party AI service; assume the upload is retained. Do not upload sensitive case material without consent/authority.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: unverified
trustNote: Consumer novelty age-progression site; uk-osint lists it under "Facial Comparison Sites" but it is an age-progression generator, not a 1:1 comparison/matching service. Output is illustrative, not forensic.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases: []
tags:
- age-progression
- facialcomparison
source: uk-osint
lastVerified: ''
enrichment: full
---

# in20years.co

> A consumer AI age-progression site: upload a face photo, get an aged-up rendering — illustrative, not a forensic age progression.

## When to use
You have a recent `face`/`image` of a long-term missing person and want a rough visual of how they might look older to seed recognition or jog memory among the public. Treat it as a brainstorming aid, not evidence.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://in20years.co/ and upload a clear, front-facing `image` of the subject's `face`.
2. Choose the target age/years-forward option if offered.
3. Download/screenshot the generated aged `image`.
4. Pivot: compare the render qualitatively against any candidate identifications; for serious casework prefer a forensic artist or an official program (e.g., NCMEC age progression).

## Inputs → Outputs
- **In:** `image` / `face`
- **Out:** an aged `image`, a loose `physical-description` cue
- **Empty/negative result looks like:** distorted/artifact-heavy output on low-quality or angled inputs — discard rather than trust.

## Gotchas & OpSec
- This is novelty-grade AI, not validated forensic age progression; do not present output as authoritative or use for elimination.
- Uploaded photos go to a third party and may be retained — get consent/authority before uploading a real subject's image.
- OpSec: passive toward the subject, but consider data-handling risk on your side.

## Overlaps ("do both")
- For credible casework, defer to official/forensic age-progression services; use this only as a quick illustrative pass.

## Trust & verifiability
`trust: unverified` — consumer-grade generator, miscategorized as a "comparison" site by the source list. No accuracy claims should be made from its output.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | in20years-co |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → image, physical-description |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
