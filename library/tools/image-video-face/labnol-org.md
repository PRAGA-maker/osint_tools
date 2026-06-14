---
id: labnol-org
name: Labnol.org
description: Use when you have an image (especially on mobile) and want to push it into Google/Bing/Yandex reverse image search in one place — returns links to where the image appears online.
url: http://img.labnol.org/files/images.html
category: image-video-face
path:
- image-video-face
bestFor: A lightweight web front-end that runs a photo through multiple reverse-image-search engines, including from a phone.
selectorsIn:
- image
- face
selectorsOut:
- social-profile
- name
status: degraded
pricing: free
costNote: Free, ad-supported personal project page.
opsec: active
opsecNote: The image is handed off to Google/Bing/Yandex reverse-image engines; those queries are logged by the search providers. Use a sock-puppet browser session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running reverse-image helper page by Amit Agarwal (Digital Inspiration / Labnol). The HTTP (non-HTTPS) URL and reliance on third-party engines mean it may break; verify it still loads.
missingPersonsRelevance: high
coverage: [global]
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Reverse Image Search by Labnol
tags:
- reverse-image
- face
source: metaosint
lastVerified: ''
enrichment: full
---

# Labnol.org

> A simple web page that lets you upload a photo and fire it at Google, Bing and Yandex reverse image search — handy on mobile where native reverse search is awkward.

## When to use
You have an `image`/`face` of an unidentified or missing person and want fast coverage across the major reverse-image engines without juggling each site's upload UI yourself — particularly from a phone in the field. Output is "where else does this picture appear," which can surface a `name` or linked `social-profile`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://img.labnol.org/files/images.html (works on desktop and mobile browsers).
2. Upload the target photo (`selectorsIn`: image, face), or paste an image URL if the page supports it.
3. It hands the image to the selected engine(s); review hits on Google / Bing / Yandex (`selectorsOut`: social-profile, name).
4. Pivot: a matching profile or named webpage feeds people-search, social enumeration, or the original-source page.

## Inputs → Outputs
- **In:** `image` / `face`
- **Out:** links to pages and profiles where the image appears (`social-profile`, `name`)
- **Empty/negative result looks like:** "no other sizes/matches found" per engine — note that Yandex often finds faces the others miss, so check all three.

## Gotchas & OpSec
- It is only a launcher: the real matching is done by Google/Bing/Yandex, so results equal whatever those engines return.
- The page is plain HTTP and a one-person side project; it can go offline or break.
- OpSec: active — your image/query is logged by the underlying search engines; use a sock-puppet session and clean IP.

## Overlaps ("do both")
- Yandex is the strongest engine for faces; run faces directly there too, and use a dedicated face-search service (e.g. `[[lenso-ai]]`) for AI face matching the generic engines miss.

## Trust & verifiability
`trust: community` — well-known helper page, but it depends entirely on third-party engines and uses an insecure URL; confirm it loads before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | labnol-org |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
