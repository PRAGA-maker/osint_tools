---
id: cipherstick
name: CipherStick
description: Use when you want to practise or teach OSINT investigation technique on realistic puzzles — returns browser-based training challenges, not case data.
url: https://cipherstick.tech
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Sharpening investigator tradecraft with free, browser-based OSINT puzzles.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Completely free — no account, login or payment; PDF completion certificates on solving.
opsec: passive
opsecNote: Passive and training-only — challenges use fictional cases, so no real subject is involved. Still practise good habits (sock-puppet accounts, clean browser) as you would on real work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independently-run OSINT training site with a small set of curated challenges, updated roughly monthly; a learning resource, not a data source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- cipherstick.tech
tags:
- other-resources
- training
- ctf
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# CipherStick

> A free, browser-based OSINT training platform — realistic investigation puzzles (missing-person and journalist scenarios) to build and test tradecraft.

## When to use
You want to learn or teach OSINT method — following clues, examining metadata, cross-referencing public sources — in a safe, gamified setting rather than against a real subject. CipherStick hosts a handful of graded challenges (Medium → Extreme, e.g. "The Vanishing Journalist", "Project Find Rocky"). It's a skills/training resource; it produces no OSINT selectors and holds no real case data.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cipherstick.tech (no signup needed).
2. Pick a challenge by difficulty and read the fictional scenario.
3. Investigate the provided clues using OSINT techniques; submit answers to progress.
4. Earn a PDF certificate on completion; check back for new monthly puzzles.
5. Pivot: techniques you practise here transfer to real casework with the library's actual tools.

## Inputs → Outputs
- **In:** none (you work a provided fictional scenario) — no OSINT selector
- **Out:** training progress, solved-puzzle certificates — skills, not intelligence
- **Empty/negative result looks like:** N/A — it's a learning environment, not a lookup; a "wrong answer" just means keep investigating.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: fictional scenarios, so no real-world exposure — but treat it as practice for good habits.
- It is training only; don't mistake it for a data/search tool.

## Overlaps ("do both")
- Complements other training/CTF resources — use CipherStick to drill technique, then apply it with the real collection tools catalogued here.

## Trust & verifiability
`trust: community` — an independent training site; there's no data-quality risk because it holds no real case data, only exercises.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cipherstick |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
