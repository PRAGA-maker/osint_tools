---
id: gowitness
name: gowitness
description: Go web screenshot utility using Chrome Headless for bulk page capture.
url: https://github.com/sensepost/gowitness
category: evidence-capture
path:
- evidence-capture
bestFor: Bulk screenshotting lists of URLs/hosts to visually triage and preserve evidence
selectorsIn:
- domain
- ip-address
selectorsOut:
- image
- metadata-exif
status: unknown
pricing: free
opsec: active
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: SensePost (Orange Cyberdefense) project, 4.3k+ stars.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases: []
tags:
- screenshot
- recon
- evidence
- headless-chrome
source: gh-topic-footprinting
lastVerified: ''
enrichment: full
---

# gowitness

> Go web screenshot utility using Chrome Headless for bulk page capture.

- **URL:** https://github.com/sensepost/gowitness
- **Best for:** Bulk screenshotting lists of URLs/hosts to visually triage and preserve evidence
- **Source:** harvested from `gh-topic-footprinting`

Actively connects to targets to render pages. Useful for capturing a subject's web presence (personal site, profile pages) as evidence, but it's infra-oriented.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
