---
id: pbs-search
name: PBS Search
description: Use when you have a `name` or topic and want to check if a person appears in PBS documentary/news content — returns video episodes and mentions, not face matching.
url: https://www.pbs.org/search/
category: image-video-face
path:
- image-video-face
bestFor: Searching PBS's video archive by name/keyword to find documentary, news or interview appearances of a person or subject.
selectorsIn:
- name
selectorsOut:
- metadata-exif
- image
status: live
pricing: free
costNote: Free to search and stream most PBS content; no account required for searching.
opsec: passive
opsecNote: Searching a public media archive is passive and doesn't touch the subject. Nothing sensitive is disclosed beyond your query terms.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: PBS is a reputable US public broadcaster; its search returns its own catalog. Note it is a media/video search, NOT the face/reverse-image tool the seed data implied.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- google-reverse-image-search
aliases:
- pbs.org/search
tags:
- toddington
- curated-directory
- media-search
- video
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# PBS Search

> PBS's video-archive search — find whether a person or topic appears in a PBS documentary, news segment or interview. It is a media search by keyword, **not** a face-recognition or reverse-image tool.

## When to use
You have a `name` or a topic and want to see if the subject featured in PBS content — as an interviewee, subject of a documentary, expert, or in news coverage. A televised appearance is a rich lead: it can yield video of the person, quotes, affiliations, and a datable public record of their activity. Use it as a targeted media-archive check, not as a general image search (the seed miscategorised it as face search — it isn't).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.pbs.org/search/ and enter the `name` (in quotes) or topic.
2. Filter to video/episodes; open results to see whether the person appears and in what context.
3. Note the show, date, and any affiliations/quotes attributed to them; capture a screenshot/thumbnail if useful.
4. For broader coverage, repeat the name search on other broadcaster archives and a general web search.
5. Pivot: a video thumbnail/still can go to `[[google-reverse-image-search]]`; named affiliations feed people/organisation searches.

## Inputs → Outputs
- **In:** `name` or topic keywords
- **Out:** matching PBS episodes/segments → `metadata-exif`-style context (show, date, role) and video `image` stills
- **Empty/negative result looks like:** no results — the person simply isn't in PBS content (most people aren't); absence means nothing beyond "not on PBS."

## Gotchas & OpSec
- It is **not** a face/reverse-image search despite the seed tags — it matches text/metadata in PBS's catalog only.
- US public-broadcasting scope; niche/most individuals won't appear — low hit rate, hence low MP relevance.
- OpSec: fully passive archive search.

## Overlaps ("do both")
- Complements `[[google-reverse-image-search]]` and general web search — PBS is one media archive among many; run name searches across broadcaster archives, and reverse-search any still you capture.

## Trust & verifiability
`trust: trusted` — reputable broadcaster returning its own catalog; results are authoritative for "did they appear on PBS," but expect few hits for ordinary subjects.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pbs-search |
| category | image-video-face |
| selectorsIn → selectorsOut | name → metadata-exif, image |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
