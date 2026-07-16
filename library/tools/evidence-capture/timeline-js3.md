---
id: timeline-js3
name: TimelineJS3
description: Use when you have a set of dated events/evidence and want to build an interactive multimedia chronology — returns a shareable/embeddable web timeline.
url: https://timeline.knightlab.com/
category: evidence-capture
path:
- evidence-capture
bestFor: Turning a spreadsheet of dated events into an interactive, multimedia investigative timeline.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (Northwestern Knight Lab); build from a Google Sheet with no account, or self-host the JSON/JS.
opsec: passive
opsecNote: Building a timeline is a local/offline authoring act. The OpSec risk is publishing — a timeline made from a public Google Sheet, or the default hosted embed, can be publicly accessible. For sensitive cases self-host the JSON or keep the sheet private and export, so case data isn't exposed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by Northwestern University's Knight Lab; widely used, open-source (verifiable code). It's a visualization tool, so it adds no data — it only renders what you supply.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- storymap
- timeline
- twxplorer
aliases:
- TimelineJS
- Knight Lab TimelineJS
tags:
- timeline
- chronology
- visualization
- case-management
source: arf-seed
lastVerified: '2026-07-16'
enrichment: full
---

# TimelineJS3

> A free, open-source tool that turns a spreadsheet of dated events into an interactive, multimedia timeline — for laying out a case chronology.

## When to use
You have assembled a set of dated events, sightings, posts, or evidence and need to see and communicate them in order. TimelineJS builds a scrollable, embeddable timeline with images, maps, tweets, and video attached to each event — ideal for reconstructing a missing person's last-known movements, mapping a subject's activity over time, or presenting a chronology to a team or family. It's an organizing/output tool, not a discovery tool: it renders what you feed it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Copy the Knight Lab Google Sheets template and fill one row per event (date/time, headline, text, media URL, optional location).
2. On https://timeline.knightlab.com/, paste the published Sheet link to generate the timeline, or export/host the underlying JSON for full control.
3. Review the interactive timeline; each slide can carry an image, map point, or embedded social post.
4. For sensitive work, self-host the JSON/JS or keep source data private rather than using a public Sheet + hosted embed.
5. Pivot: the chronology surfaces gaps and clusters that direct where to investigate next.

## Inputs → Outputs
- **In:** dated events with optional media/location (Google Sheet or JSON) — not a person-selector input
- **Out:** an interactive multimedia web timeline (shareable link / embed) — a work product, not a selector
- **Empty/negative result looks like:** a malformed Sheet (bad date format, missing headers) yields a broken or blank timeline — fix the sheet structure; it never "finds" anything on its own.

## Gotchas & OpSec
- Human-in-the-loop: none for rendering, but you author all content.
- OpSec: the authoring is passive/local; **publishing is the risk** — public Sheets and default hosted embeds are accessible to others. Self-host or keep private for case data.
- Requires clean date formatting; large timelines can get unwieldy — scope to the relevant window.

## Overlaps ("do both")
- Pairs with `[[storymap]]` (spatial narrative) and `[[timeline]]` — use TimelineJS for the chronological view and StoryMap for the geographic one on the same case.

## Trust & verifiability
`trust: trusted` — a mature, open-source tool from a respected university lab; the code is auditable and it introduces no third-party data, only rendering your own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | timeline-js3 |
| category | evidence-capture |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
