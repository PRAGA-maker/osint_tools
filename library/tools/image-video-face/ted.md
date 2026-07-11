---
id: ted
name: TED
description: Use when you have a `name` and think the subject gave a TED/TEDx talk, and you want their video, bio, headshot and topic — returns `image`, `face`, `social-profile`, `physical-description`.
url: https://www.ted.com
category: image-video-face
path:
- image-video-face
bestFor: Finding a subject's TED/TEDx talk — video (voice + appearance), speaker bio and linked profiles.
selectorsIn:
- name
selectorsOut:
- image
- face
- social-profile
- physical-description
status: live
pricing: free
costNote: Free to browse and watch; no account needed.
opsec: passive
opsecNote: Fully passive — you are viewing a public media library, and TED does not notify a speaker that their page was viewed. Standard browser hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: TED is a well-known nonprofit media organization; speaker pages are editorially curated, so identity and bio data are reliable.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- TED Talks
- TEDx
tags:
- toddington
- curated-directory
- image-video-multimedia-search
- video
- speaker
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# TED

> The TED talk library as an OSINT source: if a subject has spoken at TED or TEDx, you get a clean video (voice + face), a curated bio, their field, and links to their other profiles.

## When to use
You have a subject `name` and evidence (or a hunch) they are an academic, founder, activist or expert who may have given a TED or TEDx talk. A talk page yields a high-quality `face`/`image`, a spoken sample for voice, a `physical-description`, a professionally written bio (employer, field, affiliations) and often links to the speaker's site/socials — strong corroboration of identity and background.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.ted.com and use the site search, or the speaker directory at `/speakers`, for the subject's `name`.
2. If nothing appears, try a search engine `site:ted.com "First Last"` — TEDx talks in particular are sometimes easier to find via Google.
3. Open the speaker page: read the bio, watch the talk (face, voice, mannerisms), and note field/affiliation and any external links.
4. Capture the headshot/video frames for reverse-image work and the bio's employer/affiliation claims.
5. Pivot: reverse-image the headshot, feed the bio's `employer-org` into records tools, and follow linked socials.

## Inputs → Outputs
- **In:** `name`
- **Out:** `image`/`face` (headshot + video), `physical-description`, `social-profile` and bio (field, `employer-org`, affiliations)
- **Empty/negative result looks like:** no speaker page — the subject hasn't given a TED/TEDx talk (or it's indexed only under a TEDx event site); absence here says nothing about other public speaking.

## Gotchas & OpSec
- TEDx (independently organized) talks are far more numerous than main-stage TED and are sometimes hosted on event-specific pages or only on YouTube; broaden the search there.
- Bios are curated as of the talk date and may be years stale — treat employer/title as point-in-time.
- Common names can collide; confirm via the face/field, not the name alone.

## Overlaps ("do both")
- Pairs with YouTube and reverse-image search — the same talk often lives on YouTube with comments/engagement, and the headshot is a good reverse-image seed.

## Trust & verifiability
`trust: trusted` — TED is a reputable, editorially curated organization, so a speaker page reliably confirms the person spoke and their stated field; still date-check the bio.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ted |
| category | image-video-face |
| selectorsIn → selectorsOut | name → image, face, social-profile, physical-description |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
