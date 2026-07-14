---
id: osinttools-linayorda
name: OSINTtools (LinaYorda)
description: Use when you're running a missing-persons investigation (Trace Labs style) and want a curated toolset/workflow — returns pointers to social-media and locate tools for turning a `name`/`username`/`image` into a `social-profile` or `address`.
url: https://github.com/LinaYorda/OSINTtools
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: A missing-persons-focused (Trace Labs Search Party CTF) curation of social-media OSINT tools and workflow.
selectorsIn:
- name
- username
- image
- geolocation
selectorsOut:
- social-profile
- address
status: live
pricing: free
costNote: Free public GitHub repository; no account or payment. Individual tools it links to have their own pricing.
opsec: passive
opsecNote: Reading the repo is passive. It's a catalog — the OpSec profile of each activity depends on the specific linked tool you then run, so evaluate those individually (some are active/attributable).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community GitHub curation by LinaYorda, explicitly assembled for Trace Labs missing-persons CTFs; well-aligned to the use case, though it's a personal list that may age.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- LinaYorda OSINTtools
- Trace Labs OSINT tools
tags:
- trace-labs
- missing-persons
- ctf
- catalog
source: gh-topic-osint-resources
lastVerified: '2026-07-14'
enrichment: full
---

# OSINTtools (LinaYorda)

> A GitHub toolset curated specifically for missing-persons work — the Trace Labs Search Party CTF context, where the whole point is turning thin selectors into locate-grade leads.

## When to use
You're investigating a missing person (or practicing on a Trace Labs CTF) and want a starting kit aligned to exactly that goal, rather than a generic OSINT dump. This curation groups social-media, image, and locate tools around the missing-persons workflow — useful when you have a `name`, `username`, `image`, or last-known `geolocation` and need the right instruments to reach a current `social-profile` or `address`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the repo on GitHub and skim the README/sections (social platforms, image/face, geolocation, people-search).
2. Match your available selector to the relevant section and pick tools to run.
3. Follow the workflow cues — it's organized around the Trace Labs scoring model (locate the subject, their social presence, and associates).
4. Run each chosen tool (vet its trust/OpSec first) and feed results forward.
5. Pivot: use it as a checklist to make sure you've covered platforms/selectors you might otherwise skip under time pressure.

## Inputs → Outputs
- **In:** none directly (a catalog) — you bring `name`/`username`/`image`/`geolocation`
- **Out:** pointers to tools that yield `social-profile`, `address`, and associate leads
- **Empty/negative result looks like:** sections listing tools you already use, or stale links — cross-check with other missing-persons resources and confirm each tool is live.

## Gotchas & OpSec
- It returns *tools and workflow*, not subject data — a listing is a lead to an instrument, not a result.
- A personal GitHub list can age; some tools may be dead. Verify liveness before relying on any entry.
- Evaluate each linked tool's OpSec separately — the catalog is passive, but the tools it points to are not all passive.

## Overlaps ("do both")
- Pairs with broad directories like `[[cyb-detective-osint-stuff-tool-collection]]` and `[[osint-stash]]` — those are exhaustive and general, while this is tightly scoped to the missing-persons mission and its scoring model. Use this to stay on-task, the big directories to fill gaps.

## Trust & verifiability
`trust: community` — a respected, mission-aligned personal curation, not an authoritative index. Its value is focus; judge each linked tool independently and confirm it still works.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osinttools-linayorda |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | name, username, image, geolocation → social-profile, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
