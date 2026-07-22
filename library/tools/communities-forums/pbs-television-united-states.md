---
id: pbs-television-united-states
name: PBS (United States)
description: Use when you have a `name` and want US public-broadcasting coverage, documentaries or program credits mentioning a subject — returns `social-profile`/mention and `associate` context.
url: http://www.pbs.org
category: communities-forums
path:
- communities-forums
bestFor: Searching US public-television news, documentaries and program archives for a person named, interviewed, or credited.
selectorsIn:
- name
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free public-broadcaster content and archives; no paywall, no account needed.
opsec: passive
opsecNote: Reading and dorking a public broadcaster site is passive and invisible to any subject; only PBS's servers log the visit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A major US public broadcaster with strong editorial and documentary standards; credible content, still secondary to primary records.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- PBS
- pbs.org
- Public Broadcasting Service
tags:
- news-media
- documentary
- united-states
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
relatedTools:
- pbs-search
---

# PBS (United States)

> US public television — news (PBS NewsHour, FRONTLINE), documentaries and program archives that may name, interview or credit a subject, often in depth.

## When to use
You have a `name` and suspect a public-affairs, documentary, educational or local-station angle. PBS content ranges from investigative journalism (FRONTLINE) and interviews to documentaries and program credits — useful when a subject was a documentary subject/interviewee, an expert source, a producer/contributor, or featured by a local PBS member station. Hits give a date, the program context, named associates, and quotes establishing role or perspective.

## How to use it (`bestInteractionPattern`: web-manual)
1. Use PBS's search, or Google-dork it: `site:pbs.org "<full name>"` (add a program or topic term to cut noise).
2. Open matching pages — news transcripts, documentary pages, program credits — and read for the connection, date and named associates.
3. Check relevant local PBS member-station sites for community-level coverage.
4. Pivot: named `associate`s/interviewees feed relationship mapping; a documentary appearance feeds further media and social lookups; transcripts provide quotable, dated statements.

## Inputs → Outputs
- **In:** `name`
- **Out:** `social-profile`/mention, named `associate`s (interviewees/contributors), program date and context
- **Empty/negative result looks like:** no hits — the subject has no PBS footprint (common unless connected to public-affairs/documentary content); disambiguate same-name matches by context.

## Gotchas & OpSec
- Skews public-affairs/documentary/educational; irrelevant for most ordinary subjects.
- Same-name collisions; confirm identity from program context.
- Journalism/documentary is interpretation — corroborate with primary records.

## Overlaps ("do both")
- Pairs with `[[nbc-united-states]]`/`[[cnn-news-united-states]]`, local news and program-credit databases — PBS adds in-depth documentary/public-affairs coverage; those add breaking and local reporting.

## Trust & verifiability
`trust: trusted` — a major public broadcaster with strong standards; credible content, still secondary journalism to anchor against primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pbs-television-united-states |
| category | communities-forums |
| selectorsIn → selectorsOut | name → social-profile, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
