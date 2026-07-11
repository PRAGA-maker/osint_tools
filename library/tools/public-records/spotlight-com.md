---
id: spotlight-com
name: Spotlight (Contacts & Performers)
description: Use when you have a `name` for someone in the UK entertainment industry and want to find their professional profile or the agents/services around them — returns performer/service listings with location and representation.
url: https://www.spotlight.com/contacts
category: public-records
path:
- public-records
bestFor: Locating UK performers, their agents/representation, and industry service providers by name or location.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- name
- address
- employer-org
- image
- physical-description
status: live
pricing: freemium
costNote: Browsing the Contacts directory of agents/services is free. Full performer profiles (with photos, physical stats, showreels, agent) live in the Spotlight members' directory, parts of which are gated behind an industry membership/login used by casting professionals.
opsec: passive
opsecNote: Public browsing is passive — subjects are not notified. Deeper casting features require an industry account; using one ties the lookup to that identity, so use a sock-puppet professional account if discretion matters.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Spotlight is the long-established, authoritative UK casting directory (since 1927); performer listings are self-submitted and verified for industry use, so identity/representation data is reliable though self-reported physical stats may be dated.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- Spotlight.com
- Spotlight Contacts
- Spotlight casting directory
tags:
- professionlicensing
- Profession & Licensing Sites
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Spotlight (Contacts & Performers)

> The UK's canonical casting directory — an "industry address book" that links a performer's name to their photo, physical description, agent, and location, plus a searchable directory of industry services.

## When to use
You have a `name` for a UK actor, dancer, presenter or other performer, or for an industry service (agent, casting director, photographer), and you want a professional profile: representation, business location, and — for performers — headshots and self-reported physical stats. Genuinely useful in a missing-person or identity workup when the subject has an entertainment background, because a performer profile bundles a photo, physical description, and an agent who can be contacted.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.spotlight.com/contacts for the industry services directory, or the main Spotlight performer search for actors/performers.
2. Search by `name`, or filter by `address`/location, specialism, or professional membership.
3. Read results: for services, a listing with contact details sortable by distance or alphabetically; for performers, a profile page with `image` headshots, `physical-description` (height, eye/hair colour), credits, and the agent/`employer-org` representing them.
4. Note that full performer profiles may require an industry login; the Contacts services directory is open.
5. Pivot: an agent/`employer-org` gives a real contact route to the subject; a headshot feeds face-search; a physical description corroborates other records.

## Inputs → Outputs
- **In:** `name`, `address`/location, or `employer-org` (agency)
- **Out:** professional `name`, `image` (headshots), `physical-description`, representing agent `employer-org`, business `address`/area
- **Empty/negative result looks like:** no matching performer/service — common if the subject isn't (or is no longer) an active industry member; absence is not proof they never performed.

## Gotchas & OpSec
- Human-in-the-loop: deeper performer/casting features are behind an industry membership login; the open Contacts directory covers services/agents only.
- Data caveat: performer physical stats and photos are self-submitted and can be years out of date.
- OpSec: passive; browsing does not alert the subject. Use a sock-puppet industry account if you need the gated casting features discreetly.

## Overlaps ("do both")
- Pairs with face-search and image tools — Spotlight yields a verified headshot and physical description you can push into reverse-image/face search to find the same person elsewhere.

## Trust & verifiability
`trust: trusted` — the authoritative UK casting directory; representation and identity data are reliable for industry use, with the usual caveat that self-reported stats age.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | spotlight-com |
| category | public-records |
| selectorsIn → selectorsOut | name → address, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
