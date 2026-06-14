---
id: flickr
name: Flickr
description: Use when a person of interest may have a Flickr account and you want their public photos, tags, EXIF/geolocation, and account context.
url: https://www.flickr.com/
category: image-video-face
path:
- image-video-face
- images
- flickr
bestFor: Mining public Flickr photos for geolocation, EXIF metadata, and account/social context.
selectorsIn:
- username
- name
- geolocation
selectorsOut:
- image
- geolocation
- metadata
- social-profile
- associate
status: live
pricing: freemium
costNote: Browsing and search are free; a free account is needed for some views, and the API requires a free API key.
opsec: passive
opsecNote: Public browsing/search is low-risk and looks like ordinary web traffic. Logging in or using the API ties activity to an account/key — use a sock puppet for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Flickr is a major, long-running photo-sharing platform; the data it serves is first-party from the platform itself.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- flickr-map
- flickr-hive-mind
aliases: []
tags:
- photo-sharing
- geolocation
- exif
source: arf-seed
lastVerified: ''
enrichment: full
---

# Flickr

> A major photo-sharing platform whose public photos, tags, and geotags are a rich OSINT source.

## When to use
You have a `username`, real `name`, or a `geolocation` and want to find a person's public photos, see where/when they were taken, and read account context (contacts, groups, comments). Flickr photos often retain EXIF and geotags that other platforms strip, making it valuable for placing a person at a location and time.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.flickr.com/ and use **People** search for a `username`/`name`, or **Photos** search for tags/places.
2. Open a profile to review the photostream, albums, groups, contacts (`associate`), and "about" details.
3. On a photo, open its info panel for the **camera/EXIF** `metadata`, capture date, and any map `geolocation`.
4. For bulk/automated work, register and use the Flickr API (free key) to pull a user's photos and metadata.
5. Pivot: feed geotags into `[[flickr-map]]`, reuse the `username` across other platforms, and run any clear `face` through a face engine.

## Inputs → Outputs
- **In:** `username` / `name` / `geolocation`
- **Out:** `image`, `geolocation`, `metadata` (EXIF/date), `social-profile`, `associate` (contacts/commenters).
- **Empty/negative result looks like:** no matching account, or an account with all photos private/contacts-only.

## Gotchas & OpSec
- Username collisions are common; confirm the right account via photo content, location, and contacts.
- OpSec: **passive** for browsing; the API/account ties to your identity — use a sock puppet. Geotags can be intentionally faked.

## Overlaps ("do both")
- Pairs with `[[flickr-map]]` (geographic discovery) and `[[flickr-hive-mind]]` (tag/keyword aggregation across the corpus).

## Trust & verifiability
`trust: trusted` — first-party platform data; the caveat is user-supplied metadata (tags/geotags) can be inaccurate or spoofed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | flickr |
| category | image-video-face |
| selectorsIn → selectorsOut | username, name, geolocation → image, geolocation, metadata, social-profile, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
