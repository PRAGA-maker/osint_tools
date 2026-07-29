---
id: this-baseball-player-does-not-exist
name: This Baseball Player Does Not Exist
description: Use when you need a disposable synthetic `face`/`image` for a sock-puppet account and want a photo that no reverse-image search will tie to a real person — returns a fresh AI-generated portrait.
url: https://thisbaseballplayerdoesnotexist.com/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Generating a throwaway AI face for a sock-puppet/research account that can't be reverse-searched to a real identity.
selectorsIn: []
selectorsOut:
- face
- image
status: live
pricing: free
costNote: Free public generator; no account or payment needed. Each page load / "Next Face" click yields a new image.
opsec: passive
opsecNote: Generation happens on the vendor's site; you download a synthetic image. Never reuse the same generated face across multiple personas — GAN faces have recurring artifacts (mismatched earrings, warped backgrounds) and duplicates can be clustered. Screenshot/crop to strip any site watermark before use.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Hobby StyleGAN generator (tied to the Pennant Wars baseball game, tech credited to carefree.ai); no provenance guarantees, but that is irrelevant since you only want a non-real face.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- this-person-does-not-exist
aliases:
- thisbaseballplayerdoesnotexist
- fake baseball player face generator
tags:
- Sock Puppets
- sock-puppet-avatar
- gan-face
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# This Baseball Player Does Not Exist

> A StyleGAN portrait generator (baseball-themed) used the same way as ThisPersonDoesNotExist: to mint a face for a sock puppet that ties back to nobody.

## When to use
You are standing up a research/sock-puppet account and need a profile photo that (a) belongs to no real person you could be accused of impersonating and (b) returns nothing on a reverse-image search. Load the page, grab a face, done. It has no investigative lookup value — it produces avatars, it does not find people.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://thisbaseballplayerdoesnotexist.com/ in a clean browser session.
2. A synthetic portrait renders on load. Click **Next Face ⚾** to cycle until you get one that fits the persona's apparent age/appearance.
3. Save the image, then crop out any site chrome/watermark and lightly recompress so the raw GAN file (with its predictable dimensions/artifacts) isn't uploaded verbatim.
4. Before committing it to a persona, reverse-search it once via `[[pimeyes]]` or Google Images to confirm it returns zero matches.
5. Pivot: the finished avatar feeds your persona setup; pair with a synthetic name/identity workflow.

## Inputs → Outputs
- **In:** nothing — it is a generator, not a search.
- **Out:** `face`, `image` (a single AI-generated portrait per click).
- **Empty/negative result looks like:** the page fails to render an image (JS blocked or site down) — fall back to `[[this-person-does-not-exist]]`.

## Gotchas & OpSec
- Human-in-the-loop: none, but you must eyeball each face for GAN artifacts (asymmetric glasses, melted ear/collar, garbled crowd background) that give it away as synthetic.
- OpSec: **passive** for the target — you touch only the generator. The real risk is operational hygiene: never reuse one face across personas, and never pass off a synthetic face as a real named individual.
- The baseball theme means many outputs wear caps/uniforms; for a neutral head-and-shoulders avatar, `[[this-person-does-not-exist]]` gives more usable variety.

## Overlaps ("do both")
- Pairs with `[[this-person-does-not-exist]]` — same GAN-avatar purpose; use whichever produces a face that suits the persona, and cross-check both against a reverse-image engine.

## Trust & verifiability
`trust: unverified` — a hobbyist generator with no stated provenance, but trust is moot: the entire point is that the face corresponds to no real, verifiable person.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | this-baseball-player-does-not-exist |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | — → face, image |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
