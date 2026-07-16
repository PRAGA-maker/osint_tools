---
id: us-east-1-console-aws-amazon-com
name: AWS Rekognition Face Comparison (console)
description: Use when you have two `face` images and want a quantified similarity score to decide if they are the same person — returns a match confidence plus per-face bounding boxes (face selector).
url: https://us-east-1.console.aws.amazon.com/rekognition/home?region=us-east-1#/face-comparison
category: image-video-face
path:
- image-video-face
bestFor: Getting an objective similarity percentage between two candidate face photos.
selectorsIn:
- image
- face
selectorsOut:
- face
status: live
pricing: freemium
costNote: Requires an AWS account. Free tier covers 5,000 images/month for the first 12 months; after that CompareFaces is roughly $1 per 1,000 images. The console demo lets you try comparisons interactively within these limits.
opsec: passive
opsecNote: You upload both images to AWS for processing; you never contact the subject, so it is passive toward the target. But the images (and your AWS account identity) are logged by Amazon — use images you are authorized to process and be aware AWS retains request metadata.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Amazon Web Services product; the CompareFaces model is well-documented and the similarity score is deterministic, though not a legal identification.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
relatedTools:
- amazon-rekognition
- amazon
- amazon-com
- amazon-pay
- amazon-registry-search
- amazon-sns
- aws-public-datasets
tags:
- facialcomparison
- face-matching
- aws
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
---

# AWS Rekognition Face Comparison (console)

> Amazon Rekognition's CompareFaces, run from the AWS console: give it two photos and it returns a numeric similarity score for whether the same person appears in both.

## When to use
You have two `face` images — say a missing-person reference photo and a face pulled from a social profile, CCTV still, or news image — and you want an **objective similarity percentage** rather than a subjective "looks like them." Rekognition detects the largest face in the source image and matches it against faces in the target image, returning a confidence score you can use to triage candidates before committing investigative effort.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign in to the AWS console and open Rekognition → **Face comparison** (the `#/face-comparison` demo in the us-east-1 region). An AWS account is required.
2. Upload the **reference (source)** face on the left and the **candidate (target)** image on the right.
3. Read the result: each detected target face gets a **similarity score** (0–100) and a bounding box; a high score (typically ≥90) is a strong same-person signal, low scores are non-matches.
4. For volume, switch to the API/CLI (`aws rekognition compare-faces`) with the same account — the console demo is for one-off checks.
5. Pivot: a high-confidence match corroborates that a social/CCTV face is your subject; feed the confirmed profile onward to username/associate mapping.

## Inputs → Outputs
- **In:** `image` / `face` (a source face photo + a target image)
- **Out:** similarity confidence score per matched `face`, with bounding boxes
- **Empty/negative result looks like:** "no faces matched" or all similarity scores below your threshold — also occurs when a face is too small, turned, occluded, or low-resolution to detect. A non-match is not proof of different people, only of no confident match.

## Gotchas & OpSec
- Human-in-the-loop: you must have (and log into) an AWS account — this is the account-login gate, not a captcha.
- The score is a probabilistic similarity, **not** a legal identification; treat ≥90 as a strong lead to verify by other means, never as conclusive ID.
- Detection degrades on low-res, angled, aged, or heavily filtered faces.
- OpSec: passive toward the subject, but both images and your account identity are logged by Amazon — only process images you are authorized to use.

## Overlaps ("do both")
- Do both with a reverse-face search engine: a face search *finds* candidate images across the web, while Rekognition *scores* whether two specific faces match. Search to gather candidates, Rekognition to rank them.

## Trust & verifiability
`trust: trusted` — a documented first-party AWS model with a deterministic, repeatable score; reliability is high but the output is a similarity metric, so verdicts still need human confirmation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | us-east-1-console-aws-amazon-com |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → face |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
