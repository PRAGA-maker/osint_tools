---
id: picdetective-com
name: picdetective.com
description: Use when you have a photo of a person and want a quick reverse-image lookup across multiple engines — returns matching/visually-similar pages and possible profiles.
url: https://picdetective.com/
category: image-video-face
path:
- image-video-face
bestFor: Lightweight multi-engine reverse-image search from a single uploaded photo.
selectorsIn:
- image
- face
selectorsOut:
- social-profile
- name
- image
status: unknown
pricing: free
costNote: Appears free to use; pricing not independently confirmed.
opsec: active
opsecNote: The image is uploaded to a third-party site; assume it leaves your control once submitted.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: unverified
trustNote: Listed on uk-osint.net under "Reverse Image Searching". An obscure reverse-image utility; capabilities, match quality, and operator are not independently verified.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- reverse-image
source: uk-osint
lastVerified: ''
enrichment: full
---

# picdetective.com

> An obscure reverse-image search utility — useful as one more lens to pivot from a photo, but unverified in quality and reach.

## When to use
You have an `image` or `face` of a missing person and want a fast reverse-image pass to find where else that photo (or a similar one) appears online. Use it alongside, not instead of, mainstream engines. Tie-in: `image`/`face` in, `social-profile`/`name`/`image` out.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://picdetective.com/.
2. Upload the `image` (or paste an image URL if supported).
3. Review returned matches/visually-similar results; open candidate pages to read names and profile context.
4. Manually confirm any hit is the same person — reverse-image matches frequently surface lookalikes or unrelated reuse.
5. Pivot confirmed profiles/names to people-search and social tools.

## Inputs → Outputs
- **In:** `image`, `face`
- **Out:** `social-profile`, `name`, `image`
- **Empty/negative result looks like:** no matches, or only generic/stock results — common for low-profile subjects; treat as inconclusive and run other engines.

## Gotchas & OpSec
- Human-in-the-loop: every match needs manual identity verification.
- OpSec: active — the photo is uploaded to an unknown third party; do not submit sensitive case images you would not share externally.
- Reliability and the operator behind the site are unverified; do not depend on it as a sole source.

## Overlaps ("do both")
- Pairs with Google/Yandex/Bing reverse image and [[pimeyes-2]] (true biometric face search) — picdetective is a low-cost extra net, not a replacement.

## Trust & verifiability
`trust: unverified` — directory-listed only; match quality, coverage, and ownership are not independently confirmed. Corroborate every result.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | picdetective-com |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → social-profile, name, image |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
