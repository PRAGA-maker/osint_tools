---
id: idgettr
name: idGettr
description: Use when you have a Flickr username or profile URL and need the account's stable numeric NSID for API calls, feeds, or de-duplicating the account.
url: https://www.webfx.com/tools/idgettr/
category: image-video-face
path:
- image-video-face
- images
- flickr
bestFor: Converting a Flickr username/URL into the account's numeric NSID (the "user@N00" Flickr ID).
selectorsIn:
- username
- social-profile
selectorsOut:
- device-id
- social-profile
status: live
pricing: free
costNote: Free, no account.
opsec: passive
opsecNote: The lookup queries Flickr through WebFX's tool; you never contact the target account directly, so it is passive from the subject's perspective.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: WebFX is a well-known marketing firm; their idGettr is a long-standing free Flickr NSID lookup utility. Output is mechanically verifiable.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- idgettr-com
aliases: []
tags:
- flickr
- id-lookup
source: arf-seed
lastVerified: ''
enrichment: full
---

# idGettr

> A free utility that turns a Flickr username or profile URL into the account's permanent numeric ID (NSID, e.g. `12345678@N00`).

## When to use
You have a `social-profile`/`username` on **Flickr** (note: this is a Flickr tool, not Instagram) and need its underlying numeric NSID. The NSID is stable even if the user changes their display name/vanity URL, so it lets you re-find the same account, build RSS/photo feeds, query the Flickr API, and confirm two differently-named URLs are the same person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.webfx.com/tools/idgettr/.
2. Paste the Flickr profile URL or username into the input box.
3. Click to look up; read the returned numeric ID / NSID.
4. Pivot: use the NSID with the Flickr API or feed URLs to enumerate the subject's public photos, dates, and any geotags/EXIF, which can yield `geolocation` and `metadata-exif`.

## Inputs → Outputs
- **In:** `username` or `social-profile` (Flickr URL).
- **Out:** the numeric NSID (`device-id`-style stable account identifier) confirming/anchoring the `social-profile`.
- **Empty/negative result looks like:** an error or no ID returned — the username is wrong, the account is deleted/private, or you pasted a non-Flickr URL.

## Gotchas & OpSec
- Flickr-specific. Do not use for Instagram/other networks despite any mislabeling.
- Free third-party tool: if WebFX's page changes or Flickr's API shifts, it may break; verify the NSID by loading the Flickr profile.
- OpSec: **passive** — no direct contact with the target; nothing to log in to.

## Overlaps ("do both")
- Pairs with `[[idgettr-com]]`, the original standalone Flickr ID-getter — use whichever is live; cross-check the NSID matches.

## Trust & verifiability
`trust: community` — reputable provider, mechanically verifiable result. Confirm by resolving the NSID back to the live Flickr profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | idgettr |
| category | image-video-face |
| selectorsIn → selectorsOut | username, social-profile → device-id, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
