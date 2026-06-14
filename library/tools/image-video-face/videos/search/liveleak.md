---
id: liveleak
name: LiveLeak
description: Use when chasing older user-uploaded incident/event video — but note LiveLeak shut down in 2021; treat as a defunct/archive-only lead.
url: https://www.liveleak.com/
category: image-video-face
path:
- image-video-face
- videos
- search
bestFor: Historically, a user-submitted shock/incident video platform; now defunct (succeeded by ItemFix).
input: ''
output: ''
selectorsIn:
- name
- geolocation
selectorsOut:
- image
- geolocation
status: down
pricing: free
costNote: Was free; site is no longer operating.
opsec: passive
opsecNote: Site is offline; any remaining content lives in web archives (Wayback Machine) and on the successor ItemFix. Searching archives is passive/read-only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: LiveLeak was a real, widely-known incident-video site that closed in May 2021 and redirected to ItemFix. Listing retained for historical/archive value only.
missingPersonsRelevance: low
coverage: [global]
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- ItemFix (successor)
tags:
- video
- defunct
source: arf-seed
lastVerified: ''
enrichment: full
---

# LiveLeak

> A former user-uploaded incident/event video site that shut down in May 2021 — now reachable only through web archives and its successor, ItemFix.

## When to use
Only when a historical lead points at a video that was hosted on LiveLeak (e.g. a cited URL in an old report, an event captured on camera around a person's last-known location). The live site is gone, so this is an archive-recovery task, not a live search. For current event/incident video, go straight to ItemFix or general video search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Do not expect https://www.liveleak.com/ to load — it is defunct.
2. Recover specific old content via the Wayback Machine (search the original LiveLeak URL) or check the successor site ItemFix.
3. From any recovered video, read background detail for `geolocation` and visible `image` frames of people/vehicles.
4. Pivot: an extracted frame goes to reverse-image/face search; a confirmed location feeds a geographic canvass.

## Inputs → Outputs
- **In:** `name`, `geolocation` (as an archive/keyword lead)
- **Out:** archived `image` frames, `geolocation` context — only when the specific item was archived.
- **Empty/negative result looks like:** dead links and no archive capture — common, since the platform is gone.

## Gotchas & OpSec
- The platform is offline; treat any "live" expectation as a false lead.
- Archived shock content can be graphic; handle accordingly.
- OpSec: passive — you are reading archives, not uploading anything.

## Overlaps ("do both")
- Use general/archived video search and ItemFix for current incident video; LiveLeak itself is recovery-only.

## Trust & verifiability
`trust: community` — genuine but defunct service; retained for historical archive lookups only, hence low MP relevance.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | liveleak |
| category | image-video-face |
| selectorsIn → selectorsOut | name, geolocation → image, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
