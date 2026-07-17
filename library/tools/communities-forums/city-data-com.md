---
id: city-data-com
name: city-data.com
description: Use when you have a `username` or a place and want forum posts and member profiles tied to it — returns social-profile, username and local-knowledge leads.
url: http://www.city-data.com/forum/
category: communities-forums
path:
- communities-forums
bestFor: Searching a huge US-centric relocation/local-discussion forum (2M+ members) for a handle's posts/profile or for local knowledge about a specific city.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free to read and search; registration (free) is required to see some member content and to post.
opsec: passive
opsecNote: Reading and searching is passive. Do not register and message a subject during an investigation — that would be active contact. Use a research browser and sock-puppet account if you must register to view gated content.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: User-generated forum content; posts are self-reported and unverified, and a handle here may or may not be the same person as elsewhere.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- City-Data Forum
- city-data.com
tags:
- forums
- local
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# city-data.com

> One of the largest US local/relocation forums — search it for a handle's posts and profile, or for granular local knowledge about a city.

## When to use
Two use cases. (1) You have a `username` and want to see if it posts on City-Data — profiles, post history and photos can reveal location, interests and other handles. (2) You're investigating a specific US city/neighborhood and want ground-level local knowledge (crime, streets, businesses, "who would know X") from long-running local threads. Both are lead-generation, not proof.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.city-data.com/forum/.
2. Search the `username` (or use a Google `site:city-data.com "handle"` query for better recall) to find posts and the member profile.
3. Or navigate to the state → city subforum and read/search local threads for the place of interest.
4. Read profiles for stated location, join date, post count, member photos, and linked handles.
5. Pivot: a reused handle feeds username-enumeration tools; location clues in posts feed geolocation; local-thread contacts can be community sources.

## Inputs → Outputs
- **In:** `username` (or a place/city to research)
- **Out:** member `social-profile`/post history, reused `username` leads, and local-knowledge context
- **Empty/negative result looks like:** no member/posts for the handle — they don't use City-Data (or use a different handle); absence isn't meaningful.

## Gotchas & OpSec
- Some member content is only visible to registered users — use a sock-puppet account if needed.
- Forum posts are self-reported and can be years old; corroborate any location/identity claim.
- Same handle ≠ same person across sites; confirm before attributing.

## Overlaps ("do both")
- Pairs with username-enumeration and Google dorking — dorking often surfaces City-Data posts faster; enumeration confirms the handle is reused elsewhere.

## Trust & verifiability
`trust: unverified` — user-generated forum content; treat posts and profiles as leads to verify, not facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | city-data-com |
| category | communities-forums |
| selectorsIn → selectorsOut | username → social-profile, username |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
