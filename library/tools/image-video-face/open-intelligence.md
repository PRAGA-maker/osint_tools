---
id: open-intelligence
name: open-intelligence
description: Processes security camera footage with object detection, face detection, and license-plate recognition.
url: https://github.com/norkator/open-intelligence
category: image-video-face
path:
- image-video-face
bestFor: Extracting faces, objects, and vehicle plates from CCTV/security-camera imagery
selectorsIn:
- image
- face
- vehicle-plate
selectorsOut:
- face
- vehicle-plate
- physical-description
status: unknown
pricing: free
opsec: passive
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: docker
trust: community
trustNote: 187 stars; self-hosted CCTV analysis stack.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases: []
tags:
- face-detection
- cctv
- license-plate
- object-detection
- video-analysis
source: gh-topic-intelligence-gathering
lastVerified: ''
enrichment: full
---

# open-intelligence

> Processes security camera footage with object detection, face detection, and license-plate recognition.

- **URL:** https://github.com/norkator/open-intelligence
- **Best for:** Extracting faces, objects, and vehicle plates from CCTV/security-camera imagery
- **Source:** harvested from `gh-topic-intelligence-gathering`

Self-hosted pipeline (TypeScript + Python ML) to run face/object/plate detection over security camera images. Relevant for analyzing surveillance footage tied to a missing person or a vehicle of interest. Requires local compute/GPU and image input.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
