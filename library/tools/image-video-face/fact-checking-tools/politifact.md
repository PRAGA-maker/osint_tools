---
id: politifact
name: PolitiFact
description: Use when you have a claim or a public figure's `name` and want to check whether a statement was fact-checked — returns rated fact-check articles with sourced `associate` references.
url: https://www.politifact.com/
category: image-video-face
path:
- image-video-face
- fact-checking-tools
bestFor: Checking whether a viral claim or a US political/media figure's statement has an independent, source-backed rating.
selectorsIn:
- name
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free to read; no account. Operated by the nonprofit Poynter Institute.
opsec: passive
opsecNote: Read-only use of a published news site; the subject is not contacted and there is no query trail beyond the host's logs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Pulitzer-winning, IFCN-signatory fact-checker run by the Poynter Institute; editorially accountable primary reporting.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- politifact.com
- Truth-O-Meter
tags:
- fact-checking
- disinformation
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# PolitiFact

> A Pulitzer-winning US fact-checking outlet that rates public statements on its "Truth-O-Meter" — the place to check whether a claim tied to a person or a viral post has already been independently verified.

## When to use
You are assessing a claim, a viral image/video caption, or a statement attributed to a US politician or media figure, and you need to know if it has been fact-checked and how it rated. PolitiFact's articles cite their sources, so beyond the True/False rating you get a trail of primary references (documents, other people quoted) that can corroborate context around a `name`. Use it as a disinformation/context check, not as a people-locator.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.politifact.com/ and search the claim's key phrase or the speaker's `name`.
2. Open the matching fact-check: read the Truth-O-Meter rating (True → Pants on Fire) and the "Our Sources" section.
3. Follow the cited sources to the underlying primary evidence rather than relying on the summary alone.
4. Check the article date — ratings reflect facts known at publication and can be superseded.
5. Pivot: use the cited documents and named `associate`s to extend your research; cross-check with other IFCN fact-checkers for agreement.

## Inputs → Outputs
- **In:** a claim/phrase or public figure `name`
- **Out:** rated fact-check article, its `social-profile`/source links and named `associate`s in the cited evidence
- **Empty/negative result looks like:** no article — the claim hasn't been checked by PolitiFact (try Snopes/AP/Reuters/other IFCN members). Absence is not a verdict on the claim.

## Gotchas & OpSec
- OpSec: **passive** — reading a public site; nothing reaches the subject.
- US-centric and focused on political/viral claims; niche or non-US claims may be uncovered.
- A rating is an editorial judgment at a point in time; always read the cited primary sources yourself.

## Overlaps ("do both")
- Pairs with other fact-checking tools (Snopes, AFP/Reuters/AP fact-check) — consult several; agreement across independent checkers strengthens confidence.

## Trust & verifiability
`trust: trusted` — an editorially accountable, IFCN-signatory outlet that shows its sources, so its ratings are auditable against the underlying evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | politifact |
| category | image-video-face |
| selectorsIn → selectorsOut | name → social-profile, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
