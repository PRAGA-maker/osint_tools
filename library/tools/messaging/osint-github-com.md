---
id: osint-github-com
name: OSINT (github.com)
description: Use when you have a Discord `username` or user/server ID and want a reference map of every pivot point — returns a methodology guide, not live data (pivots toward `social-profile`).
url: https://github.com/sinwindie/OSINT/blob/master/Discord/Discord%20OSINT%20Attack%20Surface.pdf
category: messaging
path:
- messaging
bestFor: A reference "attack surface" diagram of what can be enumerated from a Discord identity, used to plan a Discord investigation.
selectorsIn:
- username
- phone
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free, open-source reference material on GitHub (sinwindie/OSINT); no account needed to view.
opsec: passive
opsecNote: This is documentation, not a query tool — reading it touches only GitHub and leaks nothing about the target. OpSec risk lives in the techniques it describes (joining servers, DMing, ID enumeration), which are active and can alert the subject; apply sock-puppet discipline when you execute them.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: sinwindie's OSINT repo is a widely-referenced, well-starred community resource; it is a curated methodology guide, not a maintained data feed.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- sinwindie Discord OSINT Attack Surface
- Discord OSINT Attack Surface PDF
tags:
- discord
- Discord Related Sites
- methodology
- reference
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# OSINT (github.com)

> sinwindie's "Discord OSINT Attack Surface" — a one-page reference diagram of every selector and pivot you can work from a Discord identity. A planning map, not a lookup tool.

## When to use
You are investigating a subject known only by a Discord `username`, user ID, or server presence and need to know *what is even enumerable* and in what order. This PDF (part of the well-known sinwindie/OSINT collection) lays out the Discord attack surface — username → user ID, servers, join dates, linked accounts, avatar, message history, phone-verification signals — so you can plan which pivots to attempt. Use it to structure the investigation before reaching for live Discord OSINT tools.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the PDF at the GitHub URL (or browse the parent repo `github.com/sinwindie/OSINT` for the Discord folder and other platform guides).
2. Read the attack-surface map: it enumerates each Discord data point and how one leads to the next.
3. For each node relevant to your case (e.g. user ID → mutual servers → avatar), select a concrete live tool from this library's `messaging`/Discord entries to actually pull that data.
4. Execute those pivots with sock-puppet discipline (see OpSec).
5. Cross-reference: the repo also covers Email, Skype, Snapchat, Instagram, crypto, phone, and image analysis — jump to the matching folder for adjacent selectors.

## Inputs → Outputs
- **In:** a Discord `username`/user ID (or `phone` for verification checks) — as the subject you plan around
- **Out:** a structured pivot map that points toward `social-profile`, linked `username`s, avatars, and server membership; **no live data itself**
- **Empty/negative result looks like:** N/A — it is static reference material; the "miss" is when a described pivot yields nothing when you run it with a live tool.

## Gotchas & OpSec
- Human-in-the-loop: none to read it; the techniques it describes require your judgement and, often, a puppet Discord account.
- OpSec: reading is **passive**. The described actions — joining a target's server, DMing, ID lookups — are active and can alert the subject or admins. Never use a real account.
- It is a guide, not a guarantee; Discord's exposed surface changes as the platform tightens privacy, so treat older editions as directional.

## Overlaps ("do both")
- Pairs with the live Discord/messaging tools in this library — this maps *what* to pivot; those do the pulling. Also complements `[[google-to-search-profiles-on-twitter]]` when a Discord handle is reused elsewhere.

## Trust & verifiability
`trust: community` — a popular, respected community methodology resource, but it is curated guidance, not verified live data. Confirm each pivot with a primary source when you execute it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-github-com |
| category | messaging |
| selectorsIn → selectorsOut | username, phone → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
