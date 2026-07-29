---
id: fakeinfo
name: Fakeinfo
description: Use when you need mock social-media/chat screenshots for authorised sock-puppet cover or fake-detection training — generates fabricated profile/chat images (clearly fictional; never for deception).
url: https://fakeinfo.net/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Generating example fake social/chat screenshots to build sock-puppet cover or to study how fabricated screenshots are made.
selectorsIn:
- face
- image
selectorsOut: []
status: live
pricing: freemium
costNote: Free web generators (some templates/exports may be gated); no account for basic use.
opsec: passive
opsecNote: Generating an image is local/passive. The danger is downstream: fabricated screenshots can deceive, defame, or fabricate evidence. Use ONLY for authorised sock-puppet cover or fake-recognition training, keep outputs clearly fictional, and never present a generated image as genuine — doing so may be fraud/forgery.
humanInLoop: false
humanInLoopReason:
- legal-gate
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party novelty/generator site (cyb-detective listing); it produces fabricated content by design, so nothing it outputs is evidence.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- fake-company-name-generator
- fake-drivers-license-generator
- fake-tiktok-profile-generator
- fake-youtube-channel-generator
- fakeinfo-net
- random-face-generator
- twitter-profile-generator
aliases:
- Fakeinfo
- fakeinfo.net
tags:
- Sock Puppets
- fabricated-content
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Fakeinfo

> A generator of fabricated social-media and chat screenshots (Facebook/Instagram/TikTok/X/Telegram/WhatsApp/LinkedIn) — dual-use, and only defensible for authorised cover-building or fake-detection study.

## When to use
Two legitimate cases, both narrow. (1) **Sock-puppet cover:** building a plausible but clearly-fictional research persona for defensive OSINT. (2) **Fake-detection training:** seeing exactly how convincing fabricated screenshots can be, so you can recognise faked "evidence" a subject or adversary might circulate. It is *not* an investigative data source and produces nothing real. Never use it to deceive, defame, fabricate evidence, or impersonate a real person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://fakeinfo.net/ and pick a template (profile, post, or chat for the target platform).
2. Fill in the fields; optionally supply a `face`/`image` for the avatar.
3. Generate and export the screenshot.
4. Treat the result strictly as fictional cover or a training example — label it as such.

## Inputs → Outputs
- **In:** template fields + optional avatar `face`/`image` (no real OSINT selector)
- **Out:** a fabricated screenshot image (no real data)
- **Empty/negative result looks like:** not applicable — it always produces a fake; "success" is a convincing mock, which is precisely why it must never be passed off as real.

## Gotchas & OpSec
- **Legal/ethical gate:** presenting a generated image as genuine can be fraud, forgery, or defamation — keep every output clearly fictional and never attribute it to a real person.
- As a fake-detection aid, note the tell-tales it leaves (fonts, spacing, timestamps) so you can spot the same artefacts in hostile "screenshots."
- Third-party site: don't upload a real person's face/photos you aren't entitled to use.

## Overlaps ("do both")
- Sits with the other sock-puppet generators (`[[random-face-generator]]`, `[[fake-company-name-generator]]`) for building consistent cover — and, in reverse, informs image-forensics/screenshot-verification work.

## Trust & verifiability
`trust: unverified` — by design it fabricates; there is nothing to trust as data. Its only sound uses are cover-building and learning to detect fakes.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fakeinfo |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | face, image →  |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (legal-gate) |
