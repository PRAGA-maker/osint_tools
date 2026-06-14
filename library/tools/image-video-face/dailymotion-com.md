---
id: dailymotion-com
name: dailymotion.com
description: Use when you want to find videos of or uploaded by a person on Dailymotion — returns videos, channels, and profile info to mine for faces, locations, and timestamps.
url: https://www.dailymotion.com/
category: image-video-face
path:
- image-video-face
bestFor: Search a major video-sharing platform for footage of, or channels run by, a person of interest.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- image
- name
status: live
pricing: free
costNote: Free to search and watch; account only needed to upload/comment.
opsec: passive
opsecNote: Searching and viewing is passive; if logged in, your watches/likes are tied to your account. Use a sock account or logged-out session for sensitive casework.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Dailymotion is a long-established mainstream video platform; the platform itself is reliable, though uploaded content's accuracy must still be judged case by case.
missingPersonsRelevance: high
coverage: [global]
auth: none
api: true
localInstall: false
registration: false
relatedTools: [deturl-com, dogpile]
aliases:
- Dailymotion
tags:
- videosites
- Video Related Sites
source: uk-osint
lastVerified: ''
enrichment: full
---

# dailymotion.com

> A mainstream video-sharing platform — a secondary corpus to YouTube where footage of, or by, a person may live (especially content removed from or never posted to YouTube).

## When to use
You have a `name` or `username` and want to check whether a video-sharing presence exists outside YouTube. Dailymotion hosts reuploads, regional content, and material that has been pulled from larger platforms — videos can yield a current face, background locations, vehicles, voices, and upload timestamps that anchor a timeline.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.dailymotion.com/ and search the person's name, handle, or a distinctive phrase.
2. Filter to videos / channels; open candidate uploads.
3. Inspect: the uploader channel (`social-profile`), thumbnails and frames (`image`), description text, and the upload date.
4. Pivot: download a frame/thumbnail and reverse-search it, geolocate backgrounds, and check whether the same channel handle resurfaces on other platforms.

## Inputs → Outputs
- **In:** `name`, `username`
- **Out:** `social-profile` (channel), `image` (frames/thumbnails), `name`
- **Empty/negative result looks like:** no relevant channels or videos — common, since Dailymotion is far smaller than YouTube; treat as "not here," not "doesn't exist anywhere."

## Gotchas & OpSec
- Smaller index than YouTube; many searches return nothing or off-topic regional content.
- A reupload is not the original source — trace provenance before relying on a video.
- OpSec: passive. Search logged-out or via a sock account so views/history are not linked to you.

## Overlaps ("do both")
- Always run the same query on YouTube/Vimeo and a video meta-search (`[[dogpile]]`); use `[[deturl-com]]` if you need to download a Dailymotion clip for frame analysis.

## Trust & verifiability
`trust: trusted` — the platform is a long-established, reputable service. Content reliability is per-video: verify uploader identity and provenance before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dailymotion-com |
| category | image-video-face |
| selectorsIn → selectorsOut | name, username → social-profile, image, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
