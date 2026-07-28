---
id: eventbrite-united-states
name: Eventbrite (United States)
description: Use when you have a `name`, `username`, or an event/organizer and want to find events a subject organized or attended — returns organizer profiles, locations, dates and associates.
url: https://www.eventbrite.com
category: documents-metadata
path:
- documents-metadata
bestFor: Searching public events, organizer profiles and attendee-facing pages to place a person at an event or surface who runs one.
selectorsIn:
- name
- username
selectorsOut:
- name
- geolocation
- social-profile
- associate
status: live
pricing: free
costNote: Browsing and searching public events is free; ticket purchase (not needed for OSINT) costs money.
opsec: passive
opsecNote: Searching public event pages is passive and doesn't touch the subject. Registering/buying a ticket, messaging an organizer, or RSVPing is active and may expose your identity — use a sock puppet and stop at public browsing unless you have reason to go further.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: First-party public event platform; the events are real listings, but organizer-supplied details are self-reported and unverified.
missingPersonsRelevance: low
coverage:
- global
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- Eventbrite
- eventbrite.com
tags:
- toddington
- curated-directory
- useful-websites-tools-documents
- events
source: toddington-resources
lastVerified: '2026-07-28'
enrichment: full
---

# Eventbrite (United States)

> A public events platform whose organizer pages and listings can place a subject at a time and place — or reveal who runs a group they're tied to.

## When to use
You have a subject's `name` or `username`, or the name of an event/group they're connected to, and you want to find events they organized, spoke at, or that their community runs. Organizer profiles, public event pages (with venue, date, and description), and "hosted by" links can corroborate a location at a date, surface an `employer-org`/community affiliation, or reveal co-organizers as `associate` leads.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.eventbrite.com and use the search bar; filter by location and date, or open an organizer's profile URL directly.
2. Search the subject's name/handle, an org name, or a known event title.
3. Read results:
   - **Organizer profile** — past/upcoming events, bio, links, sometimes social handles.
   - **Event page** — venue `geolocation`, date/time, description, and the hosting organizer.
4. Pivot: a venue+date corroborates presence; an organizer's other events and co-hosts extend the network; linked social handles feed username/social-profile tools.

## Inputs → Outputs
- **In:** `name`, `username`, event/organizer name
- **Out:** organizer `social-profile`, event `geolocation`/dates, `name`s and `associate` (co-organizers/hosts)
- **Empty/negative result looks like:** no matching organizer or events — the person may use a different platform (Meetup, Facebook Events) or private/unlisted events; absence isn't proof of no activity.

## Gotchas & OpSec
- Organizer-supplied info is self-reported — treat names/bios as leads to verify.
- Stay passive: browsing public pages is safe; buying a ticket, RSVPing, or messaging an organizer is active and can expose you — use a sock puppet if you must.
- Many events are private/unlisted and won't appear in search.

## Overlaps ("do both")
- Do both with Meetup and Facebook Events searches — communities split across platforms, so an absence on Eventbrite is often a presence on one of the others.

## Trust & verifiability
`trust: unverified` — a real first-party platform, but organizer and event details are self-reported. The existence of a listing is reliable; the claims inside it need corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | eventbrite-united-states |
| category | documents-metadata |
| selectorsIn → selectorsOut | name, username → name, geolocation, social-profile, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
