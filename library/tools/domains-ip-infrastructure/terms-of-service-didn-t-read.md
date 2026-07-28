---
id: terms-of-service-didn-t-read
name: Terms of Service; Didn't Read (ToS;DR)
description: Use when you have a service `domain` and want a plain-language, graded summary of what its terms and privacy policy actually do to users — returns policy/privacy context.
url: https://tosdr.org/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Quickly understanding the privacy/data practices baked into a website or app's terms without reading the legalese.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free, community/non-profit project; browser add-on and API also available at no cost.
opsec: passive
opsecNote: Passive lookup of pre-analysed public policies; you don't touch the target service, only ToS;DR's own site. Nothing about a subject is disclosed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A volunteer-driven non-profit that peer-reviews service terms; coverage and grade freshness vary by service, and analyses reflect community judgement.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- ToS;DR
- tosdr.org
tags:
- privacy
- terms-of-service
- website-analysis
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# Terms of Service; Didn't Read (ToS;DR)

> A crowd-reviewed database that grades websites' and apps' terms and privacy policies and flags the clauses that actually affect users — legalese turned into plain-language points.

## When to use
You're assessing a service on some `domain` — one a subject uses, or one you're about to use yourself as an investigator — and want to know what its terms and privacy policy really do: what data it collects, whether it shares/sells it, how it handles law-enforcement requests, deletion, and account termination. ToS;DR summarises this into graded, plain-language points, saving you from reading the full legal text. Use it for OpSec (vetting a tool before you trust it with data) and for context on how much a service might know/retain about a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://tosdr.org/ and search the service name/`domain`.
2. Read the letter grade and the itemised good/bad/neutral points (data sharing, retention, tracking, LE cooperation).
3. Click through to the source clause for anything you'll rely on.
4. For frequent use, install the browser add-on to see grades inline as you browse.
5. Pivot: use the data-practice findings to judge whether a service is safe for your own OpSec, or to reason about what records it may hold on a subject.

## Inputs → Outputs
- **In:** a service name / `domain`
- **Out:** graded, plain-language summary of that service's terms/privacy points (policy context for the `domain`)
- **Empty/negative result looks like:** "not yet reviewed"/no grade — many services aren't covered or are only partially analysed; absence isn't a verdict, just a gap.

## Gotchas & OpSec
- OpSec: passive; you query ToS;DR, not the target service.
- Coverage is uneven and analyses can lag policy changes — check the source clause and the review date before relying on a point.
- Grades reflect community judgement, not legal advice; treat as orientation, not adjudication.

## Overlaps ("do both")
- Complements website-analysis/privacy tools in `domains-ip-infrastructure` — ToS;DR covers the *policy* surface (what they say they do with data), while technical tools cover the *implementation* (trackers, cookies, hosting).

## Trust & verifiability
`trust: community` — a peer-reviewed non-profit resource; verifiable via the linked source clauses, but coverage and freshness vary, so confirm anything critical against the current policy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | terms-of-service-didn-t-read |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
