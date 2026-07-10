---
id: surfface-face-and-people-search-engine
name: Surfface Face & People Search Engine
description: Use when you have a `face`/photo of an unknown person and want to find where else they appear online — returns matched `social-profile`s, names and source links with similarity scores.
url: https://surfface.com/
category: image-video-face
path:
- image-video-face
- images
- search
bestFor: Identifying an unknown person from a face photo by matching it across public web sources.
selectorsIn:
- face
- image
- name
selectorsOut:
- social-profile
- name
status: live
pricing: freemium
costNote: Freemium — 4 free searches/month after signup; more require credits or a subscription. Account required.
opsec: active
opsecNote: You upload the subject's face/photo to Surfface's servers for matching against its index — the biometric/image data leaves your control and is processed by a third-party vendor. Use only for lawful purposes, strip metadata from uploads, and be aware of facial-recognition legality in your jurisdiction. The subject is not notified.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A newer commercial face/people-search vendor (100M+ profiles, ~10B images from 900+ sources); coverage claims are self-reported and match quality/accuracy is unverified — expect false positives.
missingPersonsRelevance: high
coverage:
- us
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
relatedTools:
- reverse-image-search
- tineye
aliases:
- Surfface
tags:
- face-search
- facial-recognition
- people-search
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Surfface Face & People Search Engine

> A face-search / people-finder that matches a photo of an unknown person against a large index of public web images and profiles — a PimEyes/FaceCheck-style tool.

## When to use
You have a `face` (a photo of an unknown or unidentified person) and need to find where that face appears online — to put a name to it, connect it to social profiles, or corroborate an identity. Surfface combines reverse-image matching, facial analysis, and knowledge-based lookups over a claimed ~10B images and 100M+ profiles. This is high-value for missing-persons and unknown-subject identification, with the usual face-search caveats about false positives and privacy law.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create an account at https://surfface.com/ (a **sock-puppet** account is advisable) — 4 free searches/month.
2. Upload up to 5 photos of the same face; optionally add context (`name`, email, username) to sharpen results.
3. Read the results: matched profiles, names, source platform links, and a similarity percentage per match.
4. **Verify every hit** — open the source, compare the face carefully, and corroborate before asserting an identity. High similarity ≠ confirmed match.
5. Pivot: a matched `social-profile` feeds profile enrichment; a candidate `name` feeds people-search; run the same photo through other engines to cross-check.

## Inputs → Outputs
- **In:** `face`/`image` (up to 5 photos) + optional `name`/email/username context
- **Out:** matched `social-profile`s, candidate `name`s, source links, similarity scores
- **Empty/negative result looks like:** no matches or only low-similarity ones — the face may not be indexed, the photo may be low-quality/off-angle, or the person keeps a small footprint. Treat low-similarity results as noise.

## Gotchas & OpSec
- Human-in-the-loop: **account required** and the free tier is capped (4/month); more needs payment.
- **False positives are common** in face search — always verify at the source; never act on a match alone.
- **Privacy/legal**: uploading a third party's biometric image is regulated in some jurisdictions — ensure lawful basis.
- OpSec: **active** — the subject's face is sent to a third-party vendor.

## Overlaps ("do both")
- Pairs with `[[reverse-image-search]]` and `[[tineye]]`, and with other face engines — face-search indexes differ widely, so run several and cross-check any candidate identity before relying on it.

## Trust & verifiability
`trust: unverified` — a commercial vendor with self-reported coverage and unverified accuracy; treat every match as a lead requiring independent confirmation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | surfface-face-and-people-search-engine |
| category | image-video-face |
| selectorsIn → selectorsOut | face, image, name → social-profile, name |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
