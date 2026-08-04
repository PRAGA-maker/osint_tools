---
id: eventbrite-canada
name: Eventbrite (Canada)
description: Use when you have a `name`/organisation and want their public events — returns organiser identity, venue/`address`, dates and attendee/associate signals.
url: https://www.eventbrite.ca
category: documents-metadata
path:
- documents-metadata
bestFor: Finding a person's or group's public events and the organiser, venue, date and audience details attached to them.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- geolocation
- associate
- employer-org
status: live
pricing: free
costNote: Free to browse and search public events; buying a ticket costs money and is not needed for OSINT.
opsec: passive
opsecNote: You browse public event listings; the organiser is not notified. Do NOT register/buy a ticket for a subject's event — that is contact, may expose your identity to the organiser, and could tip them off.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A legitimate global events platform (Canadian storefront); event details are organiser-supplied, so names, venues and times are claims to corroborate, and past events may be delisted.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Eventbrite Canada
- eventbrite.ca
tags:
- toddington
- curated-directory
- events
source: toddington-resources
lastVerified: '2026-08-04'
enrichment: full
---

# Eventbrite (Canada)

> Eventbrite's Canadian storefront — public event pages that can tie a `name` or organisation to a real place and time, plus the organiser and audience around it.

## When to use
Your subject may organise, host or attend events — talks, classes, community meetups, fundraisers, conventions. Eventbrite event pages expose the organiser's name/brand, the venue (a concrete `address`/`geolocation`), the date/time (placing someone somewhere on a day), a description, and sometimes a public attendee or "who's going" signal. Searching a `name`/org here can confirm activity, location and associates, and can anticipate where a person will physically be.

## How to use it (`bestInteractionPattern`: web-manual)
1. Search Eventbrite.ca (and a site-scoped web search: `site:eventbrite.ca "name"`) for the subject, their org, or an associated topic/venue.
2. Open matching events; record organiser name, venue address, date/time, and any public attendee/host details.
3. Capture the page (screenshot + timestamp) before the event is delisted; note co-organisers/attendees as `associate` leads.
4. Pivot: feed organiser/venue into maps and business registries, and named people into people/social search; a future event date/venue is an actionable location lead.

## Inputs → Outputs
- **In:** `name` / `employer-org` (or topic/venue)
- **Out:** organiser `name`/`employer-org`, venue `geolocation`/`address`, dates, `associate` signals from hosts/attendees
- **Empty/negative result looks like:** no events, or only a generic org page — many events are private, unlisted, or removed after they pass; absence isn't proof of no activity.

## Gotchas & OpSec
- Human-in-the-loop: none to browse; never register/buy a ticket for a subject's event (that is contact).
- OpSec: passive — viewing a public listing is invisible to the organiser.
- Currency: past events are often delisted, so capture promptly; details are self-published and may be inaccurate.

## Overlaps ("do both")
- Pairs with Meetup and other event platforms and with social search because a person may promote the same event across several, and attendee/organiser names resolve into identities elsewhere.

## Trust & verifiability
`trust: community` — a real platform hosting self-published events; strong for concrete place/time leads, but organiser-supplied details should be corroborated and captured before they disappear.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
