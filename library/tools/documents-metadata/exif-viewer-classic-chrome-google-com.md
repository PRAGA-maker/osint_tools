---
id: exif-viewer-classic-chrome-google-com
name: EXIF Viewer Classic (Chrome)
description: Use when you have an `image` on a web page and want its EXIF metadata without downloading it — right-click to see camera, timestamp and any GPS `geolocation` embedded in the photo.
url: https://chrome.google.com/webstore/detail/exif-viewer-classic/nafpfdcmppffipmhcpkbplhkoiekndck
category: documents-metadata
path:
- documents-metadata
bestFor: In-browser EXIF/metadata inspection of images on any web page, including GPS coordinates when present.
selectorsIn:
- image
selectorsOut:
- metadata-exif
- geolocation
status: live
pricing: free
costNote: Free Chrome extension; no account.
opsec: passive
opsecNote: EXIF is parsed locally in your browser from the image already loaded on the page — no upload to a third party. Viewing the page itself is a normal visit; the metadata read leaks nothing further.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: unverified
trustNote: Third-party community browser extension; convenient, but as with any extension review its permissions before installing.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- exif viewer classic
- EXIF Viewer Classic extension
tags:
- exifdata
- EXIF Data Related Sites
source: uk-osint
lastVerified: '2026-07-23'
enrichment: full
---

# EXIF Viewer Classic (Chrome)

> A Chrome extension that reveals an image's embedded EXIF metadata — camera, timestamp and GPS coordinates — right from the page, via right-click, with no download or upload.

## When to use
You're viewing photos on a web page (a listing, a profile, a forum post) and want to check what metadata the images carry: the capture `metadata-exif` (camera model, date/time, software) and, crucially, any GPS `geolocation` left in the file. Doing it inline is faster than saving each image and running a desktop tool, and it keeps the image local to your browser.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "EXIF Viewer Classic" from the Chrome Web Store.
2. Browse to the page with the image(s).
3. Right-click an image (or hover, per the extension's mode) and choose the EXIF viewer option.
4. Read the metadata panel — camera/device, date/time, and a map/coordinates if GPS EXIF is present.
5. Pivot: GPS coordinates feed a mapping tool for exact `geolocation`; camera + timestamp help corroborate or debunk a photo's claimed origin.

## Inputs → Outputs
- **In:** an `image` displayed on a web page
- **Out:** `metadata-exif` (camera, timestamp, software) and embedded GPS `geolocation` when present
- **Empty/negative result looks like:** no EXIF shown — most social platforms and CDNs strip metadata on upload, so a blank is the norm for platform images, not a tool failure. Original/unprocessed images are where EXIF survives.

## Gotchas & OpSec
- The big caveat: major platforms (Facebook, Instagram, X, most CDNs) strip EXIF, so you'll usually only find GPS on images from personal sites, forums, listings or direct file links.
- Metadata can be edited/spoofed — treat EXIF timestamps and coordinates as claims to corroborate, not proof.
- OpSec: passive — parsing is local; no upload. Review the extension's permissions before installing (as with any extension).

## Overlaps ("do both")
- Pairs with a standalone EXIF tool/`exiftool` and reverse-image search — the extension is the fast in-page check, while exiftool gives the exhaustive tag dump and reverse-image search geolocates photos whose EXIF was stripped.

## Trust & verifiability
`trust: unverified` — a community browser extension; the metadata it shows comes straight from the image file so the data is reliable, but vet the extension's permissions yourself before trusting it in your browser.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | exif-viewer-classic-chrome-google-com |
| category | documents-metadata |
| selectorsIn → selectorsOut | image → metadata-exif, geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
