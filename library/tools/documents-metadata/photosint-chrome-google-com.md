---
id: photosint-chrome-google-com
name: photosint (Chrome extension)
description: Use when you have an `image` (or a web page full of images) and want to surface embedded EXIF metadata and jump to reverse-image search — returns metadata-exif and geolocation hints.
url: https://chromewebstore.google.com/detail/photosint/gonhdjmkgfkokhkflfhkbiagbmoolhcd
category: documents-metadata
path:
- documents-metadata
bestFor: Passively flagging EXIF-bearing images as you browse and reading their metadata/geotags in one click.
selectorsIn:
- image
selectorsOut:
- metadata-exif
- geolocation
status: live
pricing: free
costNote: Free Chrome/Chromium extension; no account or payment. Open-source (support/source on GitHub).
opsec: passive
opsecNote: Metadata parsing happens locally in your browser, so no query is sent to the target. But it fires on every page you load, so the images it inspects are whatever you browse — do reconnaissance from a sock-puppet browser profile to avoid mixing target sites into your real history.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Third-party extension by an independent developer (Haris87); ~3k users, source published on GitHub. Not a first-party or vendor tool — treat parsed values as leads.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- exif-data-viewer
- jimpl
- exiftool
aliases:
- PhotOSINT
- photosint extension
tags:
- exifdata
- EXIF Data Related Sites
- browser-extension
source: uk-osint
lastVerified: '2026-07-28'
enrichment: full
---

# photosint (Chrome extension)

> A browser extension that watches the pages you visit, flags any images carrying EXIF metadata, and gives you one-click metadata view + reverse-image search.

## When to use
You are browsing a target's site, forum, listing, or social page and want to know — without downloading every image and running a desktop tool — which images still carry EXIF (camera make/model, timestamps, and sometimes GPS `geolocation`). Good for a fast first pass over a page full of photos where most will be stripped but one might not be.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install from the Chrome Web Store into a Chromium-based browser (ideally a dedicated sock-puppet profile).
2. Browse to the page holding the target images; the extension scans the page and collects images that contain EXIF data.
3. Open the extension popup to see the list of EXIF-bearing images found on the page.
4. Right-click any image for the context-menu options: view its metadata, or send it to reverse-image search across multiple engines.
5. Pivot: a GPS tag → map the coordinates; a camera serial/timestamp → corroborate a device or timeline; no-EXIF images → run reverse image search instead.

## Inputs → Outputs
- **In:** `image` (in-page, or any image you right-click)
- **Out:** `metadata-exif` (camera, timestamps, software), and `geolocation` when GPS EXIF survives
- **Empty/negative result looks like:** the popup lists no images, or an image opens with no EXIF fields — meaning metadata was stripped (most social platforms strip on upload). Absence is not proof the photo was never geotagged; it just wasn't preserved here.

## Gotchas & OpSec
- Most large platforms (Instagram, Facebook, Twitter/X) strip EXIF on upload, so expect empties on social content; original-file sources (personal sites, classified listings, cloud galleries, forum attachments) are where GPS survives.
- Parsing is client-side and passive — nothing is sent to the target — but the extension runs on every page, so keep target browsing inside a clean profile.
- Community extension: confirm anything actionable (especially GPS) with a second parser before relying on it.

## Overlaps ("do both")
- Pairs with `[[exif-data-viewer]]` and `[[jimpl]]` — upload the original file to a dedicated web parser to confirm what the extension flags in-browser.
- For batch/local work use `[[exiftool]]` on downloaded originals, which reads far more tags than a browser popup.

## Trust & verifiability
`trust: community` — an independent open-source extension, not a vendor tool. Useful as a fast in-browser triage layer, but confirm EXIF/GPS findings with an authoritative parser before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | photosint-chrome-google-com |
| category | documents-metadata |
| selectorsIn → selectorsOut | image → metadata-exif, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
