---
id: ukwa
name: UK Web Archive
description: Use when you have a UK `domain`/website that has changed or vanished and want an archived copy — returns historical snapshots of UK web pages back to 2013.
url: https://www.webarchive.org.uk/
category: archives-cache
path:
- archives-cache
bestFor: Retrieving archived versions of UK-based websites (half a billion+ pages) not always well covered by the global Wayback Machine.
selectorsIn:
- domain
selectorsOut:
- domain
status: degraded
pricing: free
costNote: Free public archive run by the British Library and UK legal-deposit partners; no account. Some services remain limited following the 2023 British Library cyber incident.
opsec: passive
opsecNote: You query the archive, not the target's live server, so the site owner sees nothing. The archive operator logs the lookup, not the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the British Library and UK legal-deposit libraries; an authoritative institutional archive, though service availability has been degraded since the 2023 incident.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- wayback-machine
tags:
- Archives
- web-archive
- uk
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# UK Web Archive

> The British Library's archive of the UK web — half a billion-plus pages captured since 2013, often preserving UK sites and pages the global Wayback Machine missed.

## When to use
A UK website, business page, forum, blog, or profile relevant to your case has changed or gone offline, and the global Wayback Machine has thin or no coverage. UKWA captures the `.uk` web under legal deposit, so it can hold snapshots of British sites — recovering a deleted address, phone number, staff list, or bio — that other archives lack.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.webarchive.org.uk/.
2. Search by URL to find captures of a specific UK site, or use title/keyword browse where full-text search is available.
3. Open a snapshot and pick a capture date close to when the content was live.
4. Read the archived page for the details later removed; save/screenshot with the capture date as provenance.
5. If UKWA's search is unavailable (see gotchas), try the same URL on the Wayback Machine as a fallback.
6. Pivot: recovered selectors (old `phone`, `address`, names) → people-search and address tools.

## Inputs → Outputs
- **In:** a UK site URL / `domain`
- **Out:** archived historical snapshots of that page (from 2013 onward)
- **Empty/negative result looks like:** no capture for the URL, or a service/search error — coverage is selective and, since the 2023 British Library cyber-attack, some UKWA functions have been offline or degraded. Absence isn't proof the page never existed; check the Wayback Machine too.

## Gotchas & OpSec
- Degraded service: the October 2023 British Library ransomware incident took several UKWA services offline; full-text search and some access have been limited/restored piecemeal, so expect intermittent functionality.
- UK-focused: strongest for `.uk` and UK-hosted sites; use the global Wayback Machine for everything else.
- OpSec: passive — you hit the archive, not the target.

## Overlaps ("do both")
- Pairs with `[[wayback-machine]]` — always check both, since UKWA and the Internet Archive capture overlapping but non-identical sets of UK pages.

## Trust & verifiability
`trust: trusted` — an authoritative British Library / legal-deposit archive; snapshots carry capture timestamps you should cite, with the caveat that current service availability is degraded post-incident.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ukwa |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
