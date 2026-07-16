---
id: intel-sw-com
name: Intel-SW.com
description: Use when you have a `name` or `employer-org` and want to find someone's Facebook profile and mutual connections via advanced Graph-style operators — returns social-profile, image and associate links.
url: http://www.intel-sw.com/blog/facebook-search
category: social-networks
path:
- social-networks
bestFor: Advanced Facebook people-search (by mutual friends / employer) from a free Chrome extension.
selectorsIn:
- name
- username
- employer-org
selectorsOut:
- social-profile
- image
- associate
status: live
pricing: free
costNote: The Facebook Search Chrome extension is offered free; Intelligence Software markets it to recruiters as a sourcing aid.
opsec: active
opsecNote: The extension drives queries through your own logged-in Facebook session, so every search runs as YOU and is attributable to that account. Use a sock-puppet Facebook profile and a clean browser profile; never run it from an account tied to your real identity or the investigation.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: unverified
trustNote: Third-party recruitment vendor (Intelligence Software), not affiliated with Meta; it re-packages Facebook Graph-style search operators, so result quality depends on Facebook's current surface.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
relatedTools:
- search-linkedin-intelligence-recruitment-software
aliases:
- Intel-SW Facebook Search
- Intelligence Software Facebook Search
tags:
- facebook
- social-media
- people-search
source: metaosint
lastVerified: '2026-07-16'
enrichment: full
---

# Intel-SW.com

> A free Chrome extension that layers ~260 advanced search operators over Facebook to find people and map mutual connections — pitched at recruiters, useful for OSINT people-finding.

## When to use
You have a `name`, a Facebook `username`, or an `employer-org` and want to locate a subject's Facebook presence or find who connects two known people. It shines when the subject hides their workplace: by pivoting on mutual friends and shared connections you can infer a person's network and surface a profile that a plain Facebook search misses.

## How to use it (`bestInteractionPattern`: browser-extension)
1. From Intel-SW.com's Facebook Search page, install the Chrome extension into a clean, sock-puppet browser profile.
2. Log that browser into a **sock-puppet Facebook account** — the extension issues searches through your active session.
3. Build a query with the extension's operators: search by name/keywords, by people who work (or worked) at a company, or by "friends of X" / "mutual friends of X and Y" to map associates.
4. Read the results as Facebook profile cards: profile URL (`social-profile`), profile `image`, and the connecting friends (`associate`).
5. Pivot: a confirmed profile feeds face-search and username tools; a list of mutual friends feeds the next round of association mapping.

## Inputs → Outputs
- **In:** `name`, `username`, or `employer-org` (plus optional known associates to pivot on)
- **Out:** `social-profile` (Facebook profile URLs), `image` (profile photos), `associate` (mutual/shared friends)
- **Empty/negative result looks like:** no profile cards returned, or only generic pages/groups — meaning Facebook's Graph surface didn't match your operators, not proof the person has no account.

## Gotchas & OpSec
- Human-in-the-loop: you must be logged into Facebook for the extension to work — always use a sock puppet, never a real or investigation-linked account.
- OpSec: **active** — every query is attributable to the logged-in account and counts against Facebook's rate/anti-automation limits; aggressive use can get the sock puppet flagged or throttled.
- Facebook periodically shrinks its Graph-search surface, so some operators degrade over time; treat non-results as "surface changed," not "confirmed absent."

## Overlaps ("do both")
- Pairs with [[search-linkedin-intelligence-recruitment-software]] — the same vendor's LinkedIn sourcing angle covers professional identity while this covers the personal/social graph, so run both to triangulate employer and network.

## Trust & verifiability
`trust: unverified` — it is a third-party recruitment vendor re-packaging Facebook's own search, not an official Meta product; the underlying data is Facebook's, but coverage and operator behaviour shift with Facebook's platform changes.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | intel-sw-com |
| category | social-networks |
| selectorsIn → selectorsOut | name, username, employer-org → social-profile, image, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | yes (account-login) |
