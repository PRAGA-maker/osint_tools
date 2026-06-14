---
id: dropbox
name: Dropbox
description: Use when you have a name/username/keyword and want public files leaked on Dropbox's old shared-link domains — returns documents, images, metadata-exif.
url: https://www.google.com/?q=site:dl.dropbox.com+%3Csearchterm%3E
category: image-video-face
path:
- image-video-face
- documents
- search
- common-googledorks
bestFor: Find publicly-indexed files hosted on legacy Dropbox shared-link domains via a Google dork.
input: ''
output: ''
selectorsIn: [name, username, email]
selectorsOut: [image, document-id, metadata-exif, address]
status: degraded
pricing: free
opsec: passive
opsecNote: You query Google, not Dropbox — the subject is never contacted. The legacy dl.dropbox.com host is largely retired, so most results are stale/archived.
humanInLoop: true
humanInLoopReason: [captcha]
bestInteractionPattern: web-manual
trust: community
trustNote: Standard OSINT-Framework Google-dork entry; the technique is sound but the dl.dropbox.com index is shrinking.
missingPersonsRelevance: high
coverage: [global]
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags: [google-dork, file-search]
source: arf-seed
lastVerified: ''
enrichment: full
---

# Dropbox

> A canned Google dork (`site:dl.dropbox.com <searchterm>`) for surfacing files a subject left publicly shareable on Dropbox's old CDN domain.

## When to use
You have a `name`, `username`, or `email` and want to catch documents, photos, or scans the subject shared via a Dropbox public link that got indexed by Google. Useful when you suspect the person stored resumes, ID scans, or geotagged photos in a shared folder.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the URL and replace `<searchterm>` with the subject's name/username/email in quotes.
2. Vary the host: also try `site:dropbox.com`, `site:www.dropbox.com/s`, and `site:dropboxusercontent.com` — Dropbox migrated link hosting over the years.
3. Add file-type narrowing: `filetype:pdf`, `filetype:jpg`, etc.
4. Pivot: download any image and run it through `[[exiftool]]` for geolocation/EXIF, or feed names found in documents back into people-search.

## Inputs → Outputs
- **In:** `name`, `username`, `email`
- **Out:** `image`, `document-id`, `metadata-exif`, `address` (from document contents)
- **Empty/negative result looks like:** zero Google hits — expected for most subjects since `dl.dropbox.com` is mostly decommissioned.

## Gotchas & OpSec
- Human-in-the-loop: Google will throw a CAPTCHA after repeated dork queries — slow down or rotate.
- OpSec: passive against the subject (you only touch Google's index). The `dl.dropbox.com` host is legacy; treat low hit rates as normal, not as proof of absence.

## Overlaps ("do both")
- Pairs with other common-googledork entries (Google Drive, OneDrive) because each cloud host indexes differently.

## Trust & verifiability
`trust: community` — a long-standing OSINT-Framework dork; technique is reliable but the target index is degrading over time.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dropbox |
| category | image-video-face |
| selectorsIn → selectorsOut | name, username, email → image, document-id, metadata-exif, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
