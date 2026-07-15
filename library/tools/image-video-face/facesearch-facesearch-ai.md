---
id: facesearch-facesearch-ai
name: FaceSearch (facesearch.ai)
description: Use when you have a `face`/`image` and want to find matching people across the web — but this domain is now parked/for-sale and non-functional; historically pitched as an AI face-search engine returning social-profile matches.
url: https://facesearch.ai
category: image-video-face
path:
- image-video-face
bestFor: (Defunct) AI face-search over public web images — now offline; use an established face-search engine instead.
selectorsIn:
- face
- image
selectorsOut:
- social-profile
status: down
pricing: freemium
costNote: Not usable — as of this check the domain `facesearch.ai` is parked and listed "for sale," with no working face-search service behind it. Recorded here to steer you to real alternatives.
opsec: passive
opsecNote: There is nothing to query. For the intended task, note that real face-search engines are highly intrusive: they can deanonymise the subject and, on some services, notify no one — but you expose your query image to the operator. Use those behind a sock puppet and mind the serious privacy/legal implications.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: The domain is now a for-sale parking page; whatever service once existed is gone and was never independently verified. Do not rely on it — prefer known face-search tools.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: true
relatedTools:
- pimeyes
- facecheck-id
- lenso-ai
aliases:
- facesearch.ai
tags:
- kimi-2026
- face-search
source: kimi-faces
lastVerified: '2026-07-15'
enrichment: full
---

# FaceSearch (facesearch.ai)

> Advertised as an AI face-search engine, but the domain is now parked and for sale — there is no working service. This entry redirects you to face-search tools that actually function.

## When to use
You have a `face` or photo and want to find where that person appears online. **facesearch.ai is not the tool** — the domain is a for-sale parking page with no service behind it. Reach for an established face-search engine instead; this record exists only to stop you burning time on a dead link.

## How to use it (`bestInteractionPattern`: web-manual)
1. Do **not** rely on facesearch.ai — confirm for yourself that it now shows only a domain-sale page.
2. For the actual task, use a working face-search engine:
   - `[[pimeyes]]` — broad web face search (freemium, paywalled results).
   - `[[facecheck-id]]` — face search skewed to social/news/mugshots.
   - `[[lenso-ai]]` — AI reverse-image/face search.
3. Feed your query image into one of those, from a sock-puppet session.
4. Pivot: a face match yields a `social-profile`, name, or location to chase.

## Inputs → Outputs
- **In:** `face` / `image` (intended)
- **Out:** `social-profile` matches (intended)
- **Empty/negative result looks like:** **always empty** — the site is a parking page. Any "results" here would be domain-sale content, not face matches.

## Gotchas & OpSec
- **Defunct:** parked/for-sale domain; no functionality.
- Face search in general is legally sensitive (GDPR/BIPA) and highly intrusive — apply that caution to whichever working tool you substitute.
- OpSec: with real tools, your query image is exposed to the operator — sock-puppet it.

## Overlaps ("do both")
- Use `[[pimeyes]]`, `[[facecheck-id]]` and `[[lenso-ai]]` together — face engines index different corpora, so run more than one.

## Trust & verifiability
`trust: unverified` — the domain is now for sale with no service; treat as **down** and substitute a verified face-search engine.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facesearch-facesearch-ai |
| category | image-video-face |
| selectorsIn → selectorsOut | face, image → social-profile |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
