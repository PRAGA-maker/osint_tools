---
id: osint-github-com-2
name: osint (eenblam/github)
description: Use when you are on a TikTok video page and want its embedded metadata, or need a quick Yandex reverse-image jump — returns extracted page metadata via a browser extension/bookmarklet.
url: https://github.com/eenblam/osint
category: social-networks
path:
- social-networks
bestFor: Pulling metadata off a TikTok video page and one-click Yandex reverse image search while browsing.
selectorsIn:
- social-profile
- image
selectorsOut:
- metadata-exif
- username
status: live
pricing: free
costNote: Free and open source; install the extension/bookmarklet locally, no account.
opsec: passive
opsecNote: The TikTok metadata extractor reads data already present in the page you loaded — it adds no extra request to TikTok, so it is passive. The Yandex bookmarklet, however, sends the image to Yandex (a Russian service), which then holds and may retain that image; avoid it for sensitive imagery and use a sock-puppet browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Small personal utility repo (eenblam) of scripts/bookmarklets for QuizTime-style OSINT; inspect the short source before installing. Not a maintained product.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- yandex-images
- exiftool
aliases:
- eenblam osint
- TikTok metadata bookmarklet
tags:
- tiktok
- TikTok Related Sites
- bookmarklet
- browser-extension
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# osint (eenblam/github)

> A tiny collection of browser utilities: a Chrome extension / Firefox bookmarklet that extracts metadata from a TikTok video page, plus a Yandex reverse-image bookmarklet.

## When to use
You are already viewing a TikTok video (`social-profile`/video URL) and want the metadata the page carries — author handle, IDs, and other fields embedded in the DOM — without manually digging through page source. Or you have an `image` open and want a one-click jump to a Yandex reverse-image search. This is a browsing companion, not a bulk collector.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Clone/download https://github.com/eenblam/osint and read the short source (it's small — verify before trusting).
2. Load the Chrome extension (unpacked) or add the Firefox bookmarklet; add the Yandex image bookmarklet the same way.
3. Navigate to a TikTok video page, trigger the extension/bookmarklet, and read the extracted metadata (username, IDs, page fields).
4. For an image, click the Yandex bookmarklet to send the current image into Yandex reverse search.
5. Pivot: the extracted TikTok `username`/IDs feed username enumeration and profile correlation; Yandex hits feed face/scene matching.

## Inputs → Outputs
- **In:** an open TikTok video page (`social-profile`) or an `image`
- **Out:** extracted page `metadata-exif`-style fields and `username`; a Yandex reverse-image result set
- **Empty/negative result looks like:** the extension returning no fields (TikTok changed its page structure and the selectors broke) or Yandex returning no visual matches. TikTok markup churn is the usual cause of empty metadata.

## Gotchas & OpSec
- TikTok changes its page structure often; a scraping bookmarklet can silently go stale, so sanity-check the fields it returns.
- The TikTok extractor is passive (reads the loaded page). The Yandex bookmarklet is not neutral — it hands your image to Yandex; don't use it for sensitive photos.
- Install only after reading the source; browser extensions run with page access.

## Overlaps ("do both")
- Pairs with `[[yandex-images]]` (do the reverse search directly for more control) and `[[exiftool]]` (for real file-level EXIF once you've downloaded the media, rather than page-level fields).

## Trust & verifiability
`trust: community` — a small personal repo, unaudited and unmaintained as a product, but the code is short and inspectable. Verify the source before installing and confirm extracted fields against the live page.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-github-com-2 |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile, image → metadata-exif, username |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
