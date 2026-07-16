---
id: responsesource-com
name: ResponseSource Journalist Profiles
description: Use when you have a `name` and want to confirm a UK journalist's outlet, beat and role — returns employer-org, social-profile, name.
url: https://profiles.responsesource.com/search
category: public-records
path:
- public-records
bestFor: Confirming which publication a UK-focused journalist writes for, their beat and freelance/staff status.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- social-profile
- name
status: live
pricing: freemium
costNote: Browsing public journalist profiles is free; the full media-contact database and enquiry/outreach service are paid B2B products, and some contact fields require a login.
opsec: passive
opsecNote: Searching public journalist profiles is passive. Do not use the outreach/enquiry side against a subject — that would email real journalists and expose your interest. Read-only profile browsing leaks nothing.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial UK media-contacts platform; profile data is self-reported by journalists and curated, so verify beats/outlets against published bylines.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- responsesource.com
- ResponseSource profiles
tags:
- professionlicensing
- Profession & Licensing Sites
- journalists
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
---

# ResponseSource Journalist Profiles

> A searchable directory of UK-focused journalists and media contacts — confirm who someone writes for and what they cover.

## When to use
You have a `name` (or an `employer-org`/outlet) and want to establish whether the person is a working journalist, which publication(s) they write for, their beat, and whether they are staff or freelance. Useful for verifying a claimed media role, attributing a byline, or mapping which reporters cover a given outlet or topic.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the ResponseSource profiles search.
2. Enter the subject's `name`, or filter by keyword/category/role (staff, freelance, private) and outlet.
3. Read the results:
   - A profile shows the journalist's name, outlet(s) (`employer-org`), role/beat, and often linked accounts or a bio (`social-profile`).
   - Select a profile to view detail — some contact fields prompt you to log in.
4. Pivot: the outlet feeds masthead/byline searches; linked handles feed username enumeration and social lookups.

## Inputs → Outputs
- **In:** `name` or `employer-org` (outlet)
- **Out:** `employer-org` (publication), `social-profile` (linked accounts/bio), `name` (professional spelling), plus role/beat
- **Empty/negative result looks like:** no profile — meaning the person isn't in this UK-leaning media database (they may be an overseas journalist, unlisted, or not in media). Not proof they aren't a reporter.

## Gotchas & OpSec
- **Login gate:** basic profiles are browseable, but full contact details and the enquiry/outreach service sit behind a paid account — do not treat missing detail as "no data."
- UK-centric; weak for non-UK media.
- Profiles are self-reported — confirm the beat/outlet against actual recent bylines before relying on it.
- OpSec: read-only browsing is passive; never fire the journalist-enquiry side at or about your subject.

## Overlaps ("do both")
- Pairs with Muck Rack-style journalist databases and plain byline searches — ResponseSource skews UK, the others broaden coverage and surface actual published work.

## Trust & verifiability
`trust: community` — a curated commercial directory with self-reported entries; corroborate outlet and beat against live bylines.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | responsesource-com |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, social-profile, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
