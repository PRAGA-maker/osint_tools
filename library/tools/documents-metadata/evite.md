---
id: evite
name: Evite
description: Use when you have a `name` or an event and want a subject's party/event footprint — returns event details, host/guest `name`s, dates, and locations from public or shared Evite invitations.
url: https://www.evite.com
category: documents-metadata
path:
- documents-metadata
bestFor: Recovering event context (host, guests, date, venue) from a shared or indexed Evite invitation.
selectorsIn:
- name
selectorsOut:
- name
- associate
- address
status: live
pricing: free
costNote: Free to create/receive invitations; premium designs are paid. There is no public search — you reach content via a shared link or a search engine.
opsec: passive
opsecNote: Viewing a shared/public invite link is passive. Do NOT RSVP, comment, or sign in to an invitation you are investigating — that notifies the host and other guests and burns your access. Open links in a sock-puppet browser and never interact.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Evite is a legitimate, long-running invitation platform, but it is not a searchable OSINT database — its value is incidental, when an invite URL leaks or gets indexed.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Evite.com
tags:
- toddington
- curated-directory
- useful-websites-tools-documents
- events
source: toddington-resources
lastVerified: '2026-08-05'
enrichment: full
---

# Evite

> A mainstream digital-invitation platform — occasionally an OSINT windfall when a subject's event invite is shared publicly or indexed, exposing hosts, guests, dates, and venues.

## When to use
You are mapping a subject's social circle or timeline and a lead points to a party/event — a shared invitation link found in their posts, a Google-indexed public Evite, or an invite forwarded to you. Evite pages can reveal the host and guest `name`s (potential `associate`s), the event date, and the venue (`address`). It is not something you search directly; treat it as a place a useful document may live, reached via a link or a web search.

## How to use it (`bestInteractionPattern`: web-manual)
1. You will usually arrive via a shared Evite URL or a search hit (try `site:evite.com "<name>"` on Google), not by browsing evite.com.
2. Open the invitation link in a clean sock-puppet browser.
3. Read the public fields: event title, host, date/time, location, and any visible guest list or comments.
4. Do not sign in, RSVP, or comment — that would alert the host.
5. Pivot: guest `name`s become new `associate` selectors; the venue `address` and date anchor a timeline.

## Inputs → Outputs
- **In:** a `name` (via a targeted web search) or a shared invite link
- **Out:** event details, host/guest `name`s (`associate`), venue `address`
- **Empty/negative result looks like:** no indexed/shared invite for the subject (the common case — most invites are private) — Evite yields nothing unless a link is exposed.

## Gotchas & OpSec
- Human-in-the-loop: none to view a shared invite; interacting requires a login you should not use.
- OpSec: strictly view-only. RSVPs and comments are visible to the host and guests — never interact with a target's invitation.
- Coverage is incidental and sparse; do not expect systematic results. Absence means "not exposed," not "no such event."

## Overlaps ("do both")
- Pairs with general search-engine dorking and social-graph tools — those find the exposed Evite link; the invite then adds concrete guests, dates, and a venue to the graph.

## Trust & verifiability
`trust: unverified` — the platform is legitimate, but any single invite is user-created and could be stale or aspirational; corroborate names/venues before treating them as fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | evite |
| category | documents-metadata |
| selectorsIn → selectorsOut | name → name, associate, address |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
