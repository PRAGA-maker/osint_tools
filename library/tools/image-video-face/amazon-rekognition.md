---
id: amazon-rekognition
name: Amazon Rekognition
description: Use when you have two or more face photos and want programmatic face comparison/similarity scoring, or want to detect faces, attributes, and objects across a batch of images at scale.
url: https://aws.amazon.com/rekognition/
category: image-video-face
path:
- image-video-face
bestFor: Programmatic face comparison/similarity and bulk face/attribute/object detection over an image or video set.
selectorsIn:
- image
- face
selectorsOut:
- face
- physical-description
- metadata-exif
status: live
pricing: freemium
costNote: AWS pay-per-image API with a 12-month free tier (limited monthly image quota); beyond that it is billed per image/minute analyzed.
opsec: passive
opsecNote: Images are uploaded to AWS cloud and processed by Amazon; assume storage/logging within your AWS account and Amazon's infrastructure. Use a dedicated investigative AWS account, not a personal one.
humanInLoop: true
humanInLoopReason:
- api-key
- account-login
- payment-wall-partial
bestInteractionPattern: api
trust: community
trustNote: Production-grade AWS service widely used in OSINT/forensics workflows; CompareFaces returns a similarity score, but accuracy varies with pose/quality and it is not a substitute for human/forensic confirmation.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: false
registration: true
aliases:
- AWS Rekognition
- Rekognition CompareFaces
tags:
- bellingcat-toolkit
- facial-recognition
source: bellingcat-toolkit
lastVerified: ''
enrichment: full
---

# Amazon Rekognition

> AWS's cloud face/image-analysis API: compare two faces, detect faces and attributes, and label objects across image and video sets.

## When to use
You have an `image`/`face` of a subject and one or more candidate photos and want a similarity score (CompareFaces), or you have a large set of images/video and need to detect/cluster faces and attributes at scale — work that is impractical by hand. It does NOT search the open web or any public database; you supply both sides of the comparison.

## How to use it (`bestInteractionPattern`: api)
1. Create/sign in to an AWS account (use a dedicated investigative account) and generate API credentials.
2. Call the API via the AWS SDK or CLI, e.g. `aws rekognition compare-faces --source-image ... --target-image ...`, or `detect-faces` / `detect-labels` for attributes and objects.
3. Read the JSON: `Similarity` score for CompareFaces; bounding boxes, `AgeRange`, `Gender`, emotions, and labels for detection.
4. Pivot: high-similarity pairs warrant human confirmation; detected attributes feed `physical-description` for BOLO/notices.

## Inputs → Outputs
- **In:** `image`, `face` (you provide both the probe and the candidate(s))
- **Out:** `face` matches/similarity, `physical-description` (age range, gender, attributes), `metadata-exif`-adjacent labels (objects/scene)
- **Empty/negative result looks like:** low `Similarity`, `NoFaceDetected`, or empty label set — poor pose/lighting commonly causes this; recrop and retry.

## Gotchas & OpSec
- Human-in-the-loop: requires an AWS account, API key, and billing setup; usage beyond the free tier costs money.
- OpSec: passive toward the target, but images go to Amazon's cloud — use an investigative account and mind data-handling rules. Treat similarity scores as leads, never as identification; pose/age/quality drive false matches.

## Overlaps ("do both")
- Pairs with reverse-image search (`[[bing-images]]`, `[[baidu-images]]`) which finds candidate photos on the web that you can then score with Rekognition; and with `[[betaface]]` as an alternative face-analysis engine.

## Trust & verifiability
`trust: community` — a mature, documented AWS service used widely in OSINT; reliable as a scoring/detection engine, but outputs require human verification and have no evidentiary standing on their own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | amazon-rekognition |
| category | image-video-face |
| selectorsIn → selectorsOut | image, face → face, physical-description, metadata-exif |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | api |
| opsec | passive |
| human-in-loop | yes |
