---
id: search4faces
name: Search4faces
description: Use when you have a `face`/`image` and want to find matching profiles on VK, Odnoklassniki, TikTok or Clubhouse — returns links to social profiles of the same or similar-looking person.
url: https://search4faces.com/
category: image-video-face
path:
- image-video-face
bestFor: Reverse face search against Russian/Eastern-European social networks (VK, OK) plus TikTok/Clubhouse avatars and a celebrity set.
selectorsIn:
- face
- image
selectorsOut:
- social-profile
- face
- name
status: live
pricing: freemium
costNote: Basic searches are free; some databases/features and higher volume require an account and/or paid credits.
opsec: passive
opsecNote: You upload the target's face to a third-party (Russian-operated) service, which processes and may retain it. The subject is not notified, but assume the image and your query are logged by the operator; use a sock-puppet account and avoid uploading the most sensitive imagery.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known face-search service with real matching power against VK/OK; matches are probabilistic ("same or similar"), so every hit must be confirmed, and the operator's data handling is opaque.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- google-reverse-image-search
- huggingface-co
aliases:
- search4faces.com
tags:
- image-search
- face-recognition
- vk
- tiktok
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Search4faces

> A reverse **face** search engine indexing VKontakte and Odnoklassniki profile photos plus TikTok/Clubhouse avatars — upload a face and it returns social profiles of the same (or similar-looking) person.

## When to use
You have a `face` or a photo of a person and want to find their social-media presence, especially on Russian/Eastern-European networks (VK, OK) where Western reverse-image tools are weak. Unlike Google (which matches the same *file*), Search4faces matches the same *person* across different photos using face recognition — powerful for identifying an unknown subject or linking a photo to a VK/TikTok profile.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://search4faces.com/ and pick the database (VK avatars/photos, OK, TikTok, Clubhouse, or celebrity).
2. Upload a clear, front-facing `face` photo (crop to the face; register a free account if prompted).
3. Review ranked candidate matches with similarity scores and profile links.
4. Confirm each candidate by comparing multiple photos and corroborating details — treat matches as leads, not identifications.
5. Pivot: a matched VK/TikTok `social-profile` opens the full account for enrichment; prep the input with `[[huggingface-co]]` (background removal) and cross-check with `[[google-reverse-image-search]]`.

## Inputs → Outputs
- **In:** `face` / `image`
- **Out:** candidate `social-profile` links (VK/OK/TikTok/Clubhouse), similar `face`s, and sometimes a `name`
- **Empty/negative result looks like:** no candidates above a low similarity — the person may not be in the indexed networks, or the photo is poor angle/quality; absence isn't proof they have no profile.

## Gotchas & OpSec
- Matches are **probabilistic** ("similar-looking") — false positives are real; always verify before attributing.
- Coverage is strongest for VK/OK (Russia/CIS); weaker elsewhere. Poor lighting/angle degrades results.
- OpSec: you upload a face to a third-party (Russian) operator — assume retention; use a sock-puppet account and mind legal/ethical limits on face search.

## Overlaps ("do both")
- Complements `[[google-reverse-image-search]]` and Yandex — those match files/scenes; Search4faces matches faces on VK/OK. Run all; each covers a different index. `[[huggingface-co]]` cleans the input first.

## Trust & verifiability
`trust: community` — genuinely capable but probabilistic and operator-opaque; confirm every match with corroborating photos/details before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search4faces |
| category | image-video-face |
| selectorsIn → selectorsOut | face, image → social-profile, face, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
</content>
