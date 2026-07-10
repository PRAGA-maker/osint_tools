---
id: sightengine-com
name: Sightengine
description: Use when you have an `image` or video (e.g. a suspect profile photo) and want to test whether it is AI-generated/deepfaked or moderate its content — returns AI-likelihood and content-classification `metadata-exif` scores.
url: https://sightengine.com/detect-ai-generated-images
category: image-video-face
path:
- image-video-face
bestFor: Detecting AI-generated / deepfaked images and videos (and content moderation) — flagging sockpuppet/catfish profile photos that were machine-generated.
selectorsIn:
- image
- face
selectorsOut:
- metadata-exif
status: live
pricing: freemium
costNote: Free tier with limited monthly detection credits (sign-up required); paid subscription and API tiers for higher volume. Not an unlimited anonymous tool.
opsec: passive
opsecNote: You upload the image to Sightengine's cloud for analysis, disclosing it to a third party that may retain it. It does not contact the person in the image. Don't upload case-sensitive imagery you can't share with a vendor; use a puppet account for signup.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: web-manual
trust: community
trustNote: Established commercial content-moderation/AI-detection vendor. Detection is probabilistic (confidence scores), so treat "likely AI-generated" as a signal, not proof.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- sightengine.com
- Sightengine AI detector
tags:
- reverseimagesearching
- ai-detection
- deepfake
- image-analysis
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Sightengine

> A commercial AI-image/deepfake detector and content-moderation API — use it to judge whether a profile photo or video was machine-generated, a fast tell for sockpuppets and catfish.

## When to use
You have an `image` (often a profile/`face` photo) or a video and need to know whether it's **AI-generated or manipulated** rather than a photo of a real person. In identity/missing-person work this flags fake personas built on synthetic faces (thispersondoesnotexist-style) and deepfaked media. Reach for it after reverse-image search comes up empty on a too-perfect photo — a "no matches + likely AI-generated" combination strongly implies a fabricated identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://sightengine.com/detect-ai-generated-images; sign up for a free account to get detection credits.
2. Drag-and-drop or URL-submit the image/video (API available for batch).
3. Read the output: a confidence score bucketed as "Likely AI-generated," "Uncertain," or "Not likely to be AI-generated"; deepfake/face-swap and moderation classes are also available.
4. Interpret probabilistically — combine with reverse-image search and EXIF checks; no single score is proof.
5. Pivot: "likely AI-generated" + no reverse-image hits → treat the persona as fabricated; "real photo" → push harder on reverse-image/face search to find the source.

## Inputs → Outputs
- **In:** `image` or video (a `face` photo, a posted image)
- **Out:** `metadata-exif`-style analysis — AI-generation likelihood score, deepfake/manipulation flags, content-moderation classes (no identity, no reverse-search matches)
- **Empty/negative result looks like:** an "Uncertain" score or "Not likely AI-generated." Note it does NOT tell you *who* is in the image — it only judges authenticity/content; use reverse-image/face tools for identity.

## Gotchas & OpSec
- **Not identity/reverse-search:** despite the seed's "reverse image searching" tag, Sightengine does not find where a photo appears — it classifies the image. Pair it with an actual reverse-image tool.
- Detection is probabilistic and adversarial — new generators can evade it; a "real" verdict isn't a guarantee.
- Free credits are limited; heavy use needs an API key/subscription.
- OpSec: passive toward the subject, but you upload to a vendor that may retain the file.

## Overlaps ("do both")
- Pairs with `[[google-reverse-image-search]]` and face-search tools — those find where/who; Sightengine judges whether the image is even real.

## Trust & verifiability
`trust: community` — a reputable commercial detector, but outputs are confidence scores, not verdicts. Corroborate with reverse-image search, EXIF/`[[metadata-viewer]]`, and manual inspection before concluding a photo is fake.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sightengine-com |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → metadata-exif |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (api-key) |
