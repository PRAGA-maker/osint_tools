---
id: meetup
name: Meetup
description: Use when a subject's hobbies/interests are known — find the groups and in-person events they attend, plus public member profiles and RSVP histories.
url: https://www.meetup.com/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Tying a person to recurring real-world events, interest groups, and a local community via public RSVPs and member profiles.
input: Topics, location, group/member preferences
output: Group listings, event calendars, member profiles, RSVP/attendee lists
selectorsIn: [name, username, geolocation, image]
selectorsOut: [name, username, image, geolocation, social-profile, associate]
status: live
pricing: freemium
costNote: Free to browse groups, events and many member profiles; some groups charge dues and organizing costs money. No payment needed for OSINT reading.
opsec: passive
opsecNote: Viewing public groups, events and member profiles is passive but often requires a logged-in account; RSVP'ing or joining a group exposes your account to organizers and other members.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Meetup is a large, real event-organizing platform widely used in OSINT for event/attendee discovery; entry reasoned from known functionality, not re-verified.
missingPersonsRelevance: high
coverage: [global]
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags: [events, groups, social, community]
source: arf-seed
lastVerified: ''
enrichment: full
---

# Meetup

> Interest-based event and group platform — turns a subject's hobbies into a list of physical places, recurring events, and the people they show up with.

## When to use
You have a `name`/`username` and some idea of the subject's interests or city (`geolocation`) and want to find the real-world groups and events they attend, photos from those events, or co-attendees (`associate`s). Especially valuable for a missing person with known hobbies (hiking, gaming, language exchange, support groups) — past RSVPs and event photos can place them at a date/location.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign in (a sock-puppet account is recommended; some content is gated behind login).
2. Search the location and topic, or search a `username` directly. Open candidate groups.
3. On a group, review past/upcoming events, the member list, and event photo albums; open a member profile to see display name, photo, intro text, joined-groups, and sometimes RSVP history.
4. Pivot: a reused `username` → cross-platform username search; an event date/place → timeline; co-attendees → `associate` enumeration; profile `image` → reverse-image search.

## Inputs → Outputs
- **In:** `name`, `username`, `geolocation`, profile `image`
- **Out:** `name`/`username`, profile `image`, `geolocation` (group city, event venue), `social-profile`, `associate` (co-members/attendees)
- **Empty/negative result looks like:** no member match, or a profile that joined groups but never RSVP'd — presence in a group is weaker evidence than an actual event RSVP.

## Gotchas & OpSec
- Human-in-the-loop: account login generally required to see member lists and full profiles.
- OpSec: passive while reading, but joining a group or RSVP'ing notifies organizers/members. Use a sock puppet and do not RSVP unless you accept the exposure.
- Members can hide RSVP visibility; attendee lists may be partial.

## Overlaps ("do both")
- Pairs with username-pivot tools to confirm the same person across platforms, and with event/photo geolocation for timeline building.

## Trust & verifiability
`trust: community` — established platform with a documented public surface and (historically) an API; this entry is reasoned from known behavior, not freshly verified.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | meetup |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, username, geolocation, image → name, username, image, geolocation, social-profile, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
