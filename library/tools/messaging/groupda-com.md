---
id: groupda-com
name: GroupDA
description: Use when you have a topic/place/keyword and want to find public WhatsApp & Telegram groups a subject might be in — returns group invite links (`social-profile`/community) filterable by category, country and language.
url: https://groupda.com/add/
category: messaging
path:
- messaging
bestFor: Discovering public WhatsApp/Telegram group invite links by category, country, language or keyword.
selectorsIn:
- username
- geolocation
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to browse and search the directory; no account needed to view listings.
opsec: passive
opsecNote: Browsing the directory is passive. Actually JOINING a group via an invite link is active and exposes your account/number to that group — never join with a personal WhatsApp/Telegram account; use a dedicated sock-puppet number/handle, and remember members can see who joined.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A community-submitted, user-generated group directory; listings are unvetted, may be stale, spammy, or bait. Verify a group is real before acting on it.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- groupda
aliases:
- groupda.com
- Group DA
tags:
- whatsapp
- WhatsApp
- telegram
- group-directory
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# GroupDA

> A public directory of user-submitted WhatsApp and Telegram group invite links — searchable by category, country, language and keyword to find communities tied to a topic, place, or interest.

## When to use
You're trying to find where a subject congregates online, or to map communities around a `geolocation`, interest, employer or event. GroupDA lists public WhatsApp/Telegram group invite links you can filter by category (dating, gaming, jobs, business…), by country (190+), and by language, or search by keyword. It's a lead-generation directory, not a reverse-lookup: you won't map a `phone` number to its groups here, but you can discover groups a person of interest might frequent.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://groupda.com and use the search box or the category/country/language filters (the `/add/` page is for submitting groups; the browse/search sections are for finding them).
2. Enter a keyword tied to your subject — a town, employer, hobby, event, or handle.
3. Review the returned group listings (title, description, category, invite link).
4. Assess each link's relevance and legitimacy from the metadata before touching it.
5. Pivot: a relevant group can be monitored from a sock-puppet account; group names/admins feed further social OSINT.

## Inputs → Outputs
- **In:** keyword / topic / place (`geolocation`), or a handle (`username`)
- **Out:** public WhatsApp/Telegram group invite links (`social-profile`/community pointers) with category/country/language metadata
- **Empty/negative result looks like:** no listings match your keyword — the directory only holds groups people chose to submit, so absence here says nothing about whether such groups exist privately.

## Gotchas & OpSec
- Joining is the risky step: an invite link puts your account into a group where members and admins can see you — sock-puppet only, never personal.
- Listings are unvetted UGC: expect stale/dead links, spam, and honeypots. Verify before engaging.
- This finds groups, not people; use it to locate communities to observe, then investigate members with other tools.

## Overlaps ("do both")
- Pairs with Telegram-search and WhatsApp OSINT tools — GroupDA surfaces the public entry points; dedicated tools help enumerate members and history once you're observing.

## Trust & verifiability
`trust: unverified` — a community-submitted directory with no vetting; treat every listing as an unconfirmed lead and validate the group's authenticity before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | groupda-com |
| category | messaging |
| selectorsIn → selectorsOut | username, geolocation → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
