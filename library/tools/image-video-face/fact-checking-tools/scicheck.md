---
id: scicheck
name: SciCheck
description: Use when you have a scientific or health claim and want an evidence-based verdict — returns FactCheck.org explanatory articles debunking or confirming the claim.
url: https://www.factcheck.org/scicheck/
category: image-video-face
path:
- image-video-face
- fact-checking-tools
bestFor: Vetting scientific, medical, and public-health claims against evidence-backed fact-check reporting.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free feature of FactCheck.org, a nonprofit at the Annenberg Public Policy Center; no account.
opsec: passive
opsecNote: Reading fact-check articles is passive and reveals nothing about your subject. Don't paste confidential case text into any third-party site out of habit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by FactCheck.org (Annenberg Public Policy Center), a long-established, nonpartisan, well-regarded fact-checking organization.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- debunking-false-stories-archives
- fact-check
tags:
- fact-checking
- science
- health
- verification
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# SciCheck

> FactCheck.org's science-and-health desk — evidence-based debunks of scientific, medical, and public-health claims from a reputable nonpartisan fact-checker.

## When to use
An investigation or a source you're evaluating repeats a scientific or health claim (a viral medical assertion, a public-health rumor, a pseudo-scientific "study") and you need to know whether it holds up. SciCheck's archive of explanatory fact-checks lets you assess the credibility of such claims and, by extension, the reliability of whoever is spreading them. Its person-locating value is low; it's a source-credibility and misinformation tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.factcheck.org/scicheck/.
2. Search or browse for the specific claim, topic, or keyword you're checking.
3. Read the relevant article: the claim, the evidence, cited experts/studies, and the verdict.
4. Follow the article's cited primary sources to verify the reasoning yourself.
5. Use the finding to weigh how much credibility to give the claim — and the account/source promoting it.
6. Pivot: a debunked claim spread by your subject/source → adjust trust; cited experts/studies → deeper primary-source reading.

## Inputs → Outputs
- **In:** a scientific/health claim or topic (no data selector)
- **Out:** evidence-backed FactCheck.org articles that confirm, contextualize, or debunk the claim, with citations
- **Empty/negative result looks like:** no article on your specific claim — SciCheck covers what its journalists have addressed, so a gap means "not yet fact-checked here," not "true." Check other fact-checkers or primary literature.

## Gotchas & OpSec
- Coverage is editorial: it addresses notable claims, not every possible one; absence isn't a verdict.
- US-centric in topic selection though science is global.
- It's reporting, not an automated checker — you read articles rather than submit arbitrary claims.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with `[[fact-check]]` and misinformation-archive tools — cross-check a claim across multiple reputable fact-checkers, and follow each one's cited primary sources.

## Trust & verifiability
`trust: trusted` — FactCheck.org is an established, nonpartisan fact-checker with transparent sourcing; its verdicts are reliable, and the cited primary studies let you verify the reasoning independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scicheck |
| category | image-video-face |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
