---
id: codepen
name: CodePen
description: Use when you have a `username` or developer name and want their front-end work — search CodePen for a person's pens/profile, or use it as a scratchpad to prototype scraping/parsing snippets.
url: https://codepen.io/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Finding a developer's CodePen profile/pens, or prototyping HTML/JS parsing snippets.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: freemium
costNote: Free to browse, search and create public pens; PRO (private pens, assets) is paid but not needed for OSINT lookups.
opsec: passive
opsecNote: Browsing and searching are passive. If you create pens while logged in, they're public by default and tied to your account — use a puppet account and never paste case data or private code into a public pen.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A well-known, established front-end code-sharing community; profiles and pens are genuine user content.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- codepen.io
tags:
- code-sharing
- developer-osint
- prototyping
source: osint4all
lastVerified: '2026-08-04'
enrichment: full
---

# CodePen

> A front-end code playground and community — searchable for a developer's profile and public "pens," and usable as a quick sandbox to prototype parsing/scraping snippets.

## When to use
Two OSINT uses: (1) your subject is technical and reuses a handle — search CodePen for that `username`/`name` to find their profile, linked sites and coding activity, another node in a username graph; (2) you need to quickly test an HTML/JS snippet (a regex, a fetch, a DOM parse) without setting up a local environment.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://codepen.io/.
2. To profile-hunt: use search for a `username` or name, or try `codepen.io/<username>` directly; review their pens, bio and outbound links (personal site, GitHub, social).
3. To prototype: create a pen (use a puppet account if logged in) and test your HTML/CSS/JS snippet live.
4. Note any external profiles/links a subject exposes on their CodePen bio.
5. Pivot: feed a confirmed handle into cross-platform username search; feed linked domains/socials into their respective tools.

## Inputs → Outputs
- **In:** `username` / `name` (for profile search) — or code (for prototyping)
- **Out:** CodePen `social-profile` + reused `username`, bio links; or a working code snippet
- **Empty/negative result looks like:** no profile/pens for the handle — meaning the subject isn't on CodePen under that name, not that the handle is unused elsewhere.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** for search; if you sign in to create pens, everything public defaults to your account — use a puppet and never paste sensitive data.
- Handle collisions are common; confirm a profile is your subject via corroborating links before relying on it.

## Overlaps ("do both")
- Pair with cross-platform username tools and GitHub search — CodePen is one more site in a handle graph; developers often link CodePen↔GitHub↔personal site.

## Trust & verifiability
`trust: trusted` — a reputable, long-running developer community; profile content is real user data, though identity attribution across sites still needs corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | codepen |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
