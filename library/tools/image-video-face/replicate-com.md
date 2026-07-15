---
id: replicate-com
name: replicate.com (Bringing Old Photos Back to Life)
description: Use when you have a degraded/old `image` of a face and want it restored/enhanced for identification — runs Microsoft's photo-restoration model on Replicate, returning a cleaner image.
url: https://replicate.com/microsoft/bringing-old-photos-back-to-life
category: image-video-face
path:
- image-video-face
bestFor: Restoring and enhancing old, scratched, faded or low-quality photos of a person to improve face-recognition and identification.
selectorsIn:
- image
- face
selectorsOut:
- image
- face
status: live
pricing: freemium
costNote: Replicate runs models pay-per-second of compute (fractions of a cent to a few cents per image); new accounts get some free credit. Signing in (often via GitHub) is required to run a model.
opsec: active
opsecNote: You upload the subject's photo to Replicate's cloud, where it is processed on third-party GPUs and may be retained/logged. This exposes the image (and your account) to a third party — use a sock-puppet account and avoid uploading images you're not authorized to process; for maximum control, run the open-source model locally instead.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Replicate is a reputable model-hosting platform; this model is Microsoft Research's published "Bringing Old Photos Back to Life." The tooling is trustworthy — but restoration is generative, so outputs are reconstructions, not ground truth.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Bringing Old Photos Back to Life
- Microsoft photo restoration
- Replicate
tags:
- photosites
- Photo Related Sites
- photo-restoration
- image-enhancement
- ai
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# replicate.com (Bringing Old Photos Back to Life)

> A hosted run of Microsoft Research's photo-restoration model — feed it an old, scratched or faded face photo and get back a cleaned-up image better suited to face search.

## When to use
You have the only photo of a missing person / subject and it's degraded — an old print, a scan with scratches, faded colour, low resolution, or heavy noise — and reverse-image and face-recognition tools are failing on it. This model repairs scratches, denoises, and enhances faces, producing a clearer image that downstream face/reverse-image searches can actually match. It's an *enhancement* step that makes your other tools work, not an identification tool itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://replicate.com/microsoft/bringing-old-photos-back-to-life and sign in (a sock-puppet account).
2. Upload the degraded `image`; enable the "with scratch" option if the photo is physically damaged.
3. Run the model; download the restored `image`.
4. Pivot: feed the enhanced face into reverse-image (Yandex, Google Lens) and face-recognition (PimEyes) tools — the cleaner input materially raises match odds. (For batch/automated use, Replicate also exposes an API.)

## Inputs → Outputs
- **In:** `image` / `face` (old, damaged, or low-quality)
- **Out:** a restored/enhanced `image` (`face`) — same person, cleaned up
- **Empty/negative result looks like:** an output that's blurry, hallucinated, or altered where the input was too far gone. The model *reconstructs* detail, so treat restored features as plausible, not forensic — never present an enhanced face as a definitive likeness.

## Gotchas & OpSec
- **Generative, not forensic:** it invents plausible detail to fill damage; fine for jogging recognition and improving search hits, unreliable as courtroom-grade evidence of appearance.
- **Active upload:** the subject's photo leaves your machine to Replicate's cloud (`account-login`); use a sock puppet, and prefer running the open-source model locally when the image is sensitive.
- Costs are tiny but non-zero after free credit; a login is required.

## Overlaps ("do both")
- Pairs with reverse-image and face-recognition engines — this is the pre-processing step; run it first, then feed the result into [[google-com-84]]-style image search and dedicated face tools.

## Trust & verifiability
`trust: trusted` — reputable platform, published Microsoft model. The pipeline is reliable; the *output* is a reconstruction, so verify any identification against an original, unaltered photo before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | replicate-com |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → image, face |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
