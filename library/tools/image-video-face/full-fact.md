---
id: full-fact
name: Full Fact
description: Use when you have a viral claim, image or story and want an evidence-based verification — returns the UK charity's fact-checks, sourcing, and AI-media/edit assessments.
url: https://fullfact.org
category: image-video-face
path:
- image-video-face
bestFor: Checking whether a widely shared claim, quote, statistic, or image has been independently fact-checked and debunked/confirmed.
selectorsIn:
- image
selectorsOut: []
status: live
pricing: free
costNote: Free to read; run by a UK registered charity funded by donations. No account needed to browse or search fact-checks.
opsec: passive
opsecNote: You read published fact-checks and never contact any subject — fully passive. Standard browsing hygiene is enough; nothing about your query is exposed to a target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Full Fact is the UK's established independent fact-checking charity, a signatory of the International Fact-Checking Network's code; its checks cite primary sources.
missingPersonsRelevance: low
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- FullFact
- Full Fact UK
tags:
- fact-checking
- verification
- disinformation
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# Full Fact

> The UK's independent fact-checking charity — a searchable archive of evidence-based checks on viral claims, political statements, statistics, and manipulated media.

## When to use
You've encountered a claim, quote, statistic, story, or image circulating around a case (social-media rumours in a missing-persons appeal, a viral photo, a politician's or official's statement) and need to know whether it's true, misleading, or already debunked. Full Fact is a verification backstop: search it before amplifying or acting on something viral, and use its cited sources to trace a claim back to primary evidence. It also covers detection of AI-generated or edited images.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://fullfact.org and use the search box, or browse topic sections (health, crime, immigration, economy, online hoaxes).
2. Enter keywords from the claim/quote, or describe the viral image, to find any existing fact-check.
3. Read the verdict and — crucially — the cited primary sources it links; the value is the sourcing, not just the label.
4. For images, check their media-verification coverage on whether a viral image is genuine, miscaptioned, edited, or AI-generated.
5. Pivot: follow the primary sources to authoritative records; if no check exists, treat the claim as unverified and check it yourself.

## Inputs → Outputs
- **In:** a claim/quote/statistic or a viral `image` to verify
- **Out:** a sourced fact-check verdict (true / misleading / false / needs-context) with primary references
- **Empty/negative result looks like:** no matching fact-check — the claim simply hasn't been reviewed here (common for niche/local items); absence is not a verdict, so verify independently.

## Gotchas & OpSec
- UK-focused: coverage skews to British politics/media; a non-UK claim may not appear.
- It's a curated archive, not a live reverse-search — if a specific claim hasn't been checked, you get nothing and must verify manually.
- Fact-checks are point-in-time; a verdict can be superseded as facts evolve — note the date.
- OpSec: fully passive reading.

## Overlaps ("do both")
- Pairs with reverse-image and media-forensics tools — Full Fact tells you if a claim/image was already debunked; those let you independently test an image's origin and integrity.

## Trust & verifiability
`trust: trusted` — an IFCN-signatory charity with transparent methodology and primary-source citations. Still, treat each check as a sourced argument: follow its references rather than accepting the headline verdict blindly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | full-fact |
| category | image-video-face |
| selectorsIn → selectorsOut | image → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
