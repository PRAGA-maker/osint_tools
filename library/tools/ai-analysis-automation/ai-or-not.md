---
id: ai-or-not
name: AI or Not
description: Use when you have an `image`/`face` or audio clip and want to judge whether it's AI-generated — returns an AI-vs-real classification with a confidence score.
url: https://www.aiornot.com/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Flagging likely AI-generated profile photos, faces, and audio during media verification and catfish/scam checks.
selectorsIn:
- image
- face
selectorsOut: []
status: live
pricing: freemium
costNote: Free tier for occasional checks; higher volume and API access are paid.
opsec: active
opsecNote: You upload the media to a third-party server for analysis, so the file leaves your machine. Don't submit sensitive/confidential case imagery; and never upload a victim's private photos you aren't entitled to share.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial AI-detection service; useful as a signal, but AI-vs-real detectors are probabilistic and error-prone — treat the verdict as a lead, never proof.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- AI or Not
- aiornot.com
tags:
- ai-detection
- media-verification
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# AI or Not

> An AI-generation detector for images and audio: upload a photo, face, or clip and get a probability that it was machine-generated — a verification signal, not a verdict.

## When to use
You're vetting a profile photo or media that might be fabricated — a suspected catfish/romance-scam avatar, an AI-generated face used to front a fake account, a doctored image in a disinformation trail. AI or Not gives a fast AI-vs-real score to prioritise which images to scrutinise further. It classifies media authenticity; it does not identify a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.aiornot.com/.
2. Upload the `image`/`face` (or audio), or paste an image URL.
3. Read the classification and confidence score (AI-generated vs real).
4. Treat it as one signal: corroborate a "likely AI" flag with a reverse-image search (does it appear anywhere with history?) and manual artefact inspection.

## Inputs → Outputs
- **In:** `image` / `face` (or audio clip)
- **Out:** AI-vs-real classification with a confidence percentage
- **Empty/negative result looks like:** a low-confidence or "likely real" score — inconclusive; not proof the image is genuine, only that this detector didn't flag it.

## Gotchas & OpSec
- **Probabilistic** — false positives and negatives are common, especially on compressed/edited or novel-model images; never treat the score as definitive.
- Uploads go to a third party — keep sensitive imagery off it.
- Detectors lag generators; a brand-new model may evade it entirely.

## Overlaps ("do both")
- Pairs with reverse-image search (Google/Yandex/PimEyes) and manual forensics — an AI-generated face typically has *no* reverse-image history, so a "likely AI" flag plus "no matches anywhere" is a much stronger combined signal than either alone.

## Trust & verifiability
`trust: unverified` — a useful commercial signal, but AI-detection is inherently uncertain; corroborate every verdict with independent checks before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ai-or-not |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | image, face →  |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
