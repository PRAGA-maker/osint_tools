---
id: upwork
name: Upwork
description: Use when you have a `name`/`username` and want a freelancer's public profile — skills, work history, portfolio, location and rates — returns social-profile, employer-org and geolocation leads.
url: https://www.upwork.com
category: documents-metadata
path:
- documents-metadata
bestFor: Finding a subject's freelance profile — skills, portfolio, client history, and self-listed location — on the Upwork marketplace.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- employer-org
- geolocation
status: live
pricing: freemium
costNote: Free to browse many public freelancer profiles; full details, contact, and client-side features require a free account (and hiring is paid). No cost to view public profiles.
opsec: passive
opsecNote: Passive — browsing public freelancer profiles. Creating a client account to view more ties activity to you, and messaging/inviting a freelancer notifies them — avoid contact actions during research and use a sock-puppet account if you must sign in.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Profiles are self-authored by freelancers; skills, history, and location are self-reported (though Upwork verifies some work history and identity), so treat details as claimed until corroborated.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- upwork.com
tags:
- toddington
- freelance
- employment
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# Upwork

> The largest freelance marketplace — a subject's public Upwork profile can expose their skills, portfolio, client/work history, hourly rate, general location, and often a photo and first name.

## When to use
You have a `name` or `username` for someone who freelances and want their professional footprint: what services they offer, their portfolio (which may link personal sites/other work), their work history and reviews, and their self-listed location (usually city/country) and rates. Useful for employment/skills profiling, confirming a person does gig work, or pivoting from a handle to a fuller identity via portfolio links. Only public profile data is visible without an account.

## How to use it (`bestInteractionPattern`: web-manual)
1. Search a `name`/`username`/skill on https://www.upwork.com (browse logged-out where possible; sock-puppet if you sign in).
2. Open a freelancer profile: title, skills, overview, portfolio, employment/education, work history and reviews, hourly rate, and location.
3. Follow portfolio links (personal sites, other platforms).
4. Note the self-listed location and any real name/photo shown.
5. Pivot: portfolio links → domain/social tooling; general location → geolocation scoping; skills/history → corroborate employment on LinkedIn/`[[angellist]]`. Do not message/invite the freelancer (it alerts them).

## Inputs → Outputs
- **In:** a `name`, `username`, or skill
- **Out:** freelancer profile — skills, portfolio, work history/reviews (`social-profile`, `employer-org`), self-listed city/country (`geolocation`), rate, photo/first name
- **Empty/negative result looks like:** no profile or a private/limited one behind a login — the person isn't on Upwork under that identity or restricts visibility; a common name returns many candidates to disambiguate by portfolio/photo.

## Gotchas & OpSec
- Self-reported — location, availability, and history are claims (Upwork verifies some, not all); corroborate.
- Full profiles/contact often need a client account; use a sock-puppet and never send an invite/message during research.
- Freelancers may use a pseudonymous handle — link identity via portfolio, not name alone.

## Overlaps ("do both")
- Complements LinkedIn, `[[angellist]]`, and Fiverr/Freelancer profiles — Upwork is strong on gig-work history and portfolios; cross-reference the same handle/portfolio across platforms to confirm identity.

## Trust & verifiability
`trust: unverified` — self-authored profiles on a real marketplace; some verification exists, but treat skills/location/history as claimed until corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | upwork |
| category | documents-metadata |
| selectorsIn → selectorsOut | name, username → social-profile, employer-org, geolocation |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
