---
id: nadj-org-uk
name: NADJ Directory
description: Use when you have a `name`, business name or `address`/area and want to find a UK disc jockey's professional listing — returns `name`, `employer-org` (DJ business), `address`/area, `social-profile`.
url: https://www.nadj.org.uk/member-directory/#!directory/map/ord=rnd
category: public-records
path:
- public-records
bestFor: Locating a UK DJ via the National Association of Disc Jockeys member directory and marketplace.
selectorsIn:
- name
- employer-org
- address
selectorsOut:
- name
- employer-org
- address
- social-profile
status: live
pricing: free
costNote: Free to browse the public directory; listings are paid/DIY for members, but searching and viewing them costs nothing.
opsec: passive
opsecNote: Public member directory; browsing is passive and needs no login. Any contact you initiate through a listing is an active step — keep to reading unless you intend to engage.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Run by the National Association of Disc Jockeys (NADJ) CIC, a UK trade body; listings are member self-submitted, so treat business details as claimed, not verified.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- National Association of Disc Jockeys
- NADJ member directory
tags:
- professionlicensing
- Profession & Licensing Sites
- dj
- entertainment
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# NADJ Directory

> The National Association of Disc Jockeys' member directory and marketplace — a niche but useful way to tie a name or DJ business to a UK region and contact/social presence.

## When to use
You have a `name`, a DJ/entertainment business name, or an area, and think the subject works as a disc jockey in the UK. The directory maps members to their trading name, service area and often a website/social links — a targeted lead when a subject's livelihood is DJing (weddings, events, mobile disco), which many general people-searches miss.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.nadj.org.uk/member-directory/ (a map/list view of members).
2. Browse or filter by location/area, business name, or member name.
3. Open a listing: read the trading name, area covered, description, and any linked website/social profiles.
4. Use the business name + area as `employer-org`/`address` pivots and follow linked socials.
5. Pivot: run the DJ/business name through Companies House, general search, and social enumeration; reverse-image any listing photos.

## Inputs → Outputs
- **In:** `name`, DJ business `employer-org`, or `address`/area
- **Out:** `name`, `employer-org` (DJ trading name), `address`/service area, `social-profile` links
- **Empty/negative result looks like:** no matching member — the subject isn't an NADJ member (membership is optional), trades under a different name, or DJs outside the UK; absence doesn't rule out DJ work.

## Gotchas & OpSec
- Covers only NADJ members, a small slice of all UK DJs — many operate without joining.
- Listings are self-submitted marketing; treat business claims and areas as indicative.
- Service "area" is a coverage region, not a home address.

## Overlaps ("do both")
- Pairs with general search and Companies House — the directory confirms the DJ trade and region, those add the registered business/ownership and residential leads.

## Trust & verifiability
`trust: community` — a legitimate trade-body directory, but listings are member-supplied, so corroborate the business name, area and any identity claim against an independent source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nadj-org-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, address → name, employer-org, address, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
