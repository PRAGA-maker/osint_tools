---
id: secjuice-com-3
name: secjuice.com
description: Use when you're about to investigate a subject on LinkedIn and want a methodology walkthrough — returns techniques for finding and reading `social-profile`s, not a lookup itself.
url: https://www.secjuice.com/linkedin-osint-part-1/
category: social-networks
path:
- social-networks
bestFor: Learning a structured LinkedIn OSINT workflow (finding profiles, reading them safely) before you start.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free community infosec publication; no account.
opsec: passive
opsecNote: Reading the article is passive. It also teaches how to view LinkedIn profiles WITHOUT tipping off the target (private mode, Google cache) — apply those before browsing, since LinkedIn shows "who viewed your profile".
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Secjuice is a respected volunteer-run infosec publication; articles are practitioner-written but not formally peer-reviewed, so verify specific techniques still work.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Secjuice LinkedIn OSINT
tags:
- linkedin
- LinkedIn & Similar Sites
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# secjuice.com

> A practitioner walkthrough of LinkedIn OSINT (Part 1 of a series) — how to find a subject's profile, read it without alerting them, and turn what's there into leads.

## When to use
This is a **methodology reference, not a lookup**. Read it before working a subject on LinkedIn so you know the moves: locating a profile via Google when LinkedIn's own search is stingy, viewing it in a way that doesn't trigger "someone viewed your profile", and mining employment/education/connection data. It's the OpSec-and-technique layer around tools like `[[linkedprospect]]`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read https://www.secjuice.com/linkedin-osint-part-1/ for the workflow and OpSec cautions.
2. Apply the profile-discovery method (Google `site:linkedin.com/in "Name" "Company"`) to find your subject.
3. Use the privacy-preserving viewing techniques it describes (private mode / cached views / a sock account) before opening the profile.
4. Pivot: harvest current employer, history, and connections; feed handles/name variants into cross-platform checks.

## Inputs → Outputs
- **In:** the `name`/`username` you intend to research on LinkedIn
- **Out:** techniques → LinkedIn `social-profile`s and the employment/associate detail on them
- **Empty/negative result looks like:** N/A — it's a guide; the failure mode is browsing LinkedIn logged into your real account and alerting the subject.

## Gotchas & OpSec
- OpSec: **passive** to read, but the whole point is safe *active* viewing — follow its anti-alert steps or use a sock LinkedIn account.
- Written at a point in time; LinkedIn changes its privacy controls, so re-test that a described technique still works.
- Part 1 of a series — pair with the follow-ups for deeper technique.

## Overlaps ("do both")
- Pairs with `[[linkedprospect]]` (builds the Boolean search) and `[[osintteam-blog-2]]` (tool listicle) — this supplies the disciplined workflow around them.

## Trust & verifiability
`trust: community` — a well-regarded volunteer infosec outlet; the guidance is sound but practitioner-authored, so confirm current-day applicability before relying on any single step.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | secjuice-com-3 |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
