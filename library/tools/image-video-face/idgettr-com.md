---
id: idgettr-com
name: idgettr.com
description: Use when you have a Flickr username or profile URL and need the account's numeric NSID to anchor it for API/feed lookups.
url: http://idgettr.com/
category: image-video-face
path:
- image-video-face
bestFor: The original standalone Flickr ID-getter — resolves a Flickr URL/username to its numeric NSID.
selectorsIn:
- username
- social-profile
selectorsOut:
- device-id
- social-profile
status: degraded
pricing: free
costNote: Free; site is old and may be intermittently down (http-only).
opsec: passive
opsecNote: Resolves the ID via Flickr behind the tool; no direct contact with the target account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: The classic Flickr NSID lookup site cited across OSINT directories; the original WebFX-style idGettr. Verify the NSID against the live profile.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- flickr
- Flickr & Similar Linked Sites
- id-lookup
source: uk-osint
lastVerified: ''
enrichment: full
---

# idgettr.com

> The original Flickr ID-getter: paste a Flickr profile and get back its permanent numeric NSID.

## When to use
You have a Flickr `social-profile`/`username` and need the stable NSID (`12345678@N00`) to query the Flickr API, build a photo/RSS feed, or prove two vanity URLs point at one account. Note this is a **Flickr** identifier tool despite living in the image-video-face category; the prior selectors (image/face) were wrong.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://idgettr.com/ (http-only; the page is old).
2. Paste the Flickr profile URL or username.
3. Read the returned numeric NSID.
4. Pivot: feed the NSID into Flickr API/feed URLs to enumerate the subject's public photos, upload dates, and any geotags/EXIF (`geolocation`, `metadata-exif`).

## Inputs → Outputs
- **In:** `username` / `social-profile` (Flickr).
- **Out:** numeric NSID — a stable `device-id`-style account anchor confirming the `social-profile`.
- **Empty/negative result looks like:** site unreachable, blank, or an error — try the WebFX equivalent `[[idgettr]]` instead, or the account is private/deleted.

## Gotchas & OpSec
- The domain is old and http-only; it may be down or slow. Have a fallback.
- Flickr-only.
- OpSec: **passive** — no login, no direct contact with the subject.

## Overlaps ("do both")
- Direct duplicate of `[[idgettr]]` (WebFX-hosted). Use whichever is live; the NSID they return should match exactly.

## Trust & verifiability
`trust: community` — the canonical Flickr NSID lookup. Always confirm by resolving the NSID back to the live Flickr profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | idgettr-com |
| category | image-video-face |
| selectorsIn → selectorsOut | username, social-profile → device-id, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
