---
id: eagleeye-image-recognition
name: EagleEye Image Recognition
description: Use when you have a person's name plus reference face photos and want to discover their social-media profiles — returns social-profile links validated by face match.
url: https://github.com/thoughtfuldev/eagleeye
category: image-video-face
path:
- image-video-face
bestFor: Find someone's social profiles by combining a name search with face-recognition matching against known photos.
selectorsIn: [name, face, image]
selectorsOut: [social-profile, username, image]
status: degraded
pricing: free
opsec: active
opsecNote: Runs live searches against Google and (historically) ImageRaider/social platforms from your IP; uses Selenium-driven browsing. Run from a VPN/sock-puppet environment.
humanInLoop: true
humanInLoopReason: [api-key, rate-limit]
bestInteractionPattern: cli
trust: community
trustNote: Public open-source project (thoughtfuldev/eagleeye) recommended across many OSINT lists, but it is largely unmaintained and depends on now-defunct services (ImageRaider, dlib/face_recognition pinning).
missingPersonsRelevance: high
coverage: [global]
auth: none
api: false
localInstall: true
registration: false
aliases: [eagleeye]
tags: [reverse-image, open-source, cli, face-recognition]
source: metaosint
lastVerified: ''
enrichment: full
---

# EagleEye Image Recognition

> A Python CLI that takes a name and a folder of known face photos, searches for the person online, then uses face recognition to confirm which discovered profiles are actually them.

## When to use
You have a `name` plus at least one good `face`/`image` reference and want to enumerate the subject's `social-profile` accounts — EagleEye's value is that it filters search hits by facial match, cutting down false positives from common names.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo and install deps (`pip install -r requirements.txt`); it needs `dlib`/`face_recognition`, Selenium/geckodriver, and an ImageRaider-style reverse search backend.
2. Drop reference photos into the `known` folder.
3. Run `python3 eagleEye.py -f "First" -l "Last"` (flags for first/last name).
4. It searches the name, gathers candidate profile images, runs face comparison, and writes matched `social-profile` results to an HTML report.
5. Pivot: feed confirmed usernames into username-enumeration tools and confirmed photos into `[[exiftool]]`/reverse-image engines.

## Inputs → Outputs
- **In:** `name`, `face`, `image`
- **Out:** `social-profile`, `username`, `image`
- **Empty/negative result looks like:** no faces clear the match threshold, or the reverse-image backend errors out (its external dependency, ImageRaider, has shut down).

## Gotchas & OpSec
- Human-in-the-loop: depends on third-party reverse-image services that may be dead — expect to patch the backend; rate limits and CAPTCHAs from Google are common.
- OpSec: ACTIVE — it drives a real browser and hits search engines/social sites from your machine. Use a VPN and a disposable environment; never run from an attributable IP.

## Overlaps ("do both")
- Pairs with `[[faceagle]]` and reverse-image tools like `[[dupli-checker]]` because those crawl indexes EagleEye does not, while EagleEye adds the name+face cross-validation step.

## Trust & verifiability
`trust: community` — credible open-source provenance and broad list recognition, but aging and dependency-fragile; verify it still runs before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | eagleeye-image-recognition |
| category | image-video-face |
| selectorsIn → selectorsOut | name, face, image → social-profile, username, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes |
