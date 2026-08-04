---
id: 2-682-783-free-ai-generated-photos
name: Generated Photos (free AI faces)
description: Use when you need a realistic face for a sock-puppet account (or a control image to study GAN faces) — returns free AI-generated portrait photos of non-existent people.
url: https://generated.photos/faces
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Sourcing royalty-free AI-generated faces for sock-puppet avatars, filterable by age/gender/ethnicity/pose.
selectorsIn: []
selectorsOut:
- image
- face
status: live
pricing: freemium
costNote: A large free gallery of AI faces (free tier with attribution/limits for non-commercial use); bulk/commercial use and the API/custom generation are paid.
opsec: passive
opsecNote: Using a generated face avoids stealing a real person's photo (which reverse-image search would expose). Note these libraries are themselves indexed — a determined analyst can sometimes match a face back to generated.photos; vary/lightly edit images and do not reuse one face across personas.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Operated by Generated Photos (Generated Media, Inc.); a well-known, legitimate source of synthetic faces widely used for sock-puppet avatars.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- face-anonimyzer
- face-generator
aliases:
- Generated Photos
- generated.photos
tags:
- Sock Puppets
- synthetic-faces
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Generated Photos (free AI faces)

> A large gallery of AI-generated faces of people who do not exist — the standard source for sock-puppet avatars that won't reverse-image-search back to a real person.

## When to use
You are building a sock-puppet/research persona and need a profile picture that is not a real person's stolen photo (which a reverse-image search would immediately unmask). Also handy as a source of known-synthetic control images when practising GAN-face detection.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://generated.photos/faces and filter by age, gender, ethnicity, emotion, or head pose.
2. Download a face that fits the persona (respect the free-tier attribution/usage terms).
3. Lightly edit (crop/recolour) so the exact file is not byte-identical to the gallery copy, and never reuse the same face across multiple personas.
4. Pair with a full sock-puppet identity (name, backstory, burner accounts) rather than a lone photo.

## Inputs → Outputs
- **In:** none (a persona requirement, not a selector)
- **Out:** a synthetic portrait `image`/`face`
- **Empty/negative result looks like:** filters too narrow return few faces — loosen them or use the paid custom-generation API.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: a generated face defeats naive reverse-image search, but these galleries are indexable — an advanced analyst can sometimes trace a face to generated.photos, so edit images and never reuse one across accounts.
- Mind the licence: the free tier has attribution/non-commercial limits.

## Overlaps ("do both")
- The mirror image of `[[amireal]]`: this *creates* synthetic faces for your own personas, while AmIReal helps *detect* synthetic faces on a subject's account. Pairs with dedicated `[[face-generator]]` alternatives for variety.

## Trust & verifiability
`trust: community` — a legitimate, widely-used synthetic-face provider; the images are genuinely AI-generated (no real person depicted), which is exactly the property you want for a sock puppet.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | 2-682-783-free-ai-generated-photos |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  → image, face |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
