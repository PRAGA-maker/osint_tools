---
id: osintcurious
name: OSINTCurious
description: Use when you have a technique gap (image, audio, geolocation, verification) and want a trusted method — returns a free archived library of OSINT tradecraft articles and videos.
url: https://osintcurio.us/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Learning vetted OSINT methodology — investigation technique, verification, and tool workflows — from a respected community archive.
selectorsIn: []
selectorsOut: []
status: degraded
pricing: free
costNote: Entirely free; the project closed in February 2023 but its articles and YouTube videos remain publicly online for reference.
opsec: passive
opsecNote: This is reference reading, not a lookup — you query no target. The only footprint is your own visit to the blog/YouTube; nothing about your subject is transmitted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A well-regarded, practitioner-run OSINT education project (2018–2023); content is authored by named community experts. Now an archive — some tool-specific steps may be dated even though the methodology holds.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- cosint-osint-on-cars
- the-osint-puppeteer
aliases:
- OSINT Curious
- The OSINT Curious Project
- osintcurio.us
tags:
- osint-blogs
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# OSINTCurious

> A free, respected archive of OSINT tradecraft — articles, "10-minute tips," and videos on investigation technique, verification and tooling. The project is closed but the knowledge stays online.

## When to use
This is a method reference, not a data source. Reach for it when you have a *technique* gap rather than a selector: how to geolocate a photo, verify a video, approach audio OSINT, reduce investigation bias, or structure a workflow. Good for grounding an approach in vetted community practice before you pick tools from the rest of the library.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://osintcurio.us/ and browse the article archive (topics: image/video analysis, geolocation, verification, OpSec, bias, methodology).
2. For walkthroughs, follow the linked OSINTCurious YouTube channel and livestream recordings.
3. Read the relevant tip/article, then apply the method with concrete tools from this library.
4. Pivot: methodology here feeds tool choice elsewhere — e.g. a geolocation article points you to mapping/imagery tools.

## Inputs → Outputs
- **In:** none (no selector; you bring a technique question)
- **Out:** methodology, checklists, and worked examples — knowledge, not data about a subject
- **Empty/negative result looks like:** a topic not covered by the archive, or an article whose named tool has since changed/disappeared — the technique usually still transfers even when the specific tool is dated.

## Gotchas & OpSec
- **Archived (project closed Feb 2023):** tool names, UIs and links inside older posts may be stale; treat the *method* as durable and re-check any named tool's current state.
- Not a lookup service — it never returns information about a person; don't expect selector-in/out behaviour.

## Overlaps ("do both")
- Sits alongside other OSINT education/blog resources like [[cosint-osint-on-cars]] and [[the-osint-puppeteer]] — use these to learn the method, then the tool skills in this library to execute it.

## Trust & verifiability
`trust: trusted` — authored by recognised practitioners with a strong community reputation; authoritative as methodology, though now a frozen archive rather than a maintained source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osintcurious |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
