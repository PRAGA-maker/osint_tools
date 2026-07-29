---
id: how-to-verify
name: How to verify?
description: Use when you have `image`, video, audio, text, or a source to verify and want a guided workflow (an interactive knowledge graph) recommending the right tools and steps — returns a verification methodology.
url: https://www.howtoverify.info/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: An interactive verification knowledge graph that maps step-by-step workflows and recommended tools by media type.
selectorsIn:
- image
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free public resource by DW Innovation (supported by German cultural funding). No account required.
opsec: passive
opsecNote: Fully passive — it's a methodology/guide you read; it performs no lookups and touches no target. OpSec depends on the individual tools it points you to, each of which has its own footprint — apply their respective precautions.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built by DW Innovation drawing on recognized verification experts (Bellingcat, First Draft, Julia Bayer, the OSINT community); a credible, professionally-curated methodology.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- HowToVerify
- howtoverify.info
tags:
- Tools collections/toolkits
- verification
- fact-checking
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# How to verify?

> An interactive knowledge graph for content verification — pick your media type and it walks you through the workflow and the specific tools to confirm whether an image, video, audio clip, source, or claim is genuine.

## When to use
You have a piece of content to verify — an `image`, a video, an audio clip, a suspected synthetic/AI-generated media, a source, or a text claim — and you want a structured method rather than guessing which tool to reach for. How to verify? maps the verification process by media type and points you to the right tools at each step (reverse image search, EXIF/metadata, geolocation, chronolocation, source-tracing). Ideal when you need a repeatable, defensible verification workflow.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.howtoverify.info/.
2. Choose the media type you're verifying (Image, Video, Audio, Source, Text, Synthetic media).
3. Follow the interactive graph through the workflow steps for that type.
4. At each node, use the recommended tools/techniques (applying each tool's own OpSec).
5. Pivot: it launches you into concrete tools — reverse-image and `[[online-metadata-viewer-and-editor]]` for images, geolocation resources for place-finding, etc. — then back to the graph for the next step.

## Inputs → Outputs
- **In:** the media/claim to verify (`image`, video, audio, source, or text)
- **Out:** a step-by-step verification workflow and recommended tools (a methodology, yielding `metadata-exif`/provenance findings once you run the steps)
- **Empty/negative result looks like:** not applicable — it's guidance, not a query; a "dead end" means the workflow's checks were inconclusive, which is itself a verification result to report honestly.

## Gotchas & OpSec
- It's a methodology, not an automated verifier — you still run the tools it recommends and interpret results.
- Tool recommendations can age; confirm a suggested tool still exists/works before relying on it.
- OpSec: the guide is passive; apply each recommended tool's own precautions.

## Overlaps ("do both")
- Complements verification toolkits and Bellingcat's guides — How to verify? is the decision map; the individual tools (reverse image, EXIF, geolocation) are the execution.

## Trust & verifiability
`trust: trusted` — DW Innovation resource built on recognized verification expertise; a credible, well-curated methodology to structure your own checks.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | how-to-verify |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | image → metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
