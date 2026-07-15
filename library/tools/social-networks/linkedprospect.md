---
id: linkedprospect
name: LinkedProspect
description: Use when you have a target's role or `employer-org` and want a ready-made LinkedIn Boolean query to surface matching profiles — returns a copy-paste search string leading to `social-profile`.
url: https://linkedprospect.com/linkedin-boolean-search-tool/
category: social-networks
path:
- social-networks
bestFor: Generating a correct LinkedIn Boolean search string from job-title, company, and keyword filters.
selectorsIn:
- name
- employer-org
selectorsOut:
- social-profile
- employer-org
status: live
pricing: freemium
costNote: The Boolean-string builder is free and needs no login. It is a lead-magnet for LinkedProspect's paid LinkedIn outreach/automation SaaS (free trial, then subscription) — but you never need to buy anything to use the generator.
opsec: passive
opsecNote: The generator runs in your browser and touches only LinkedProspect — nothing about the target leaves your machine until you paste the string into LinkedIn. The actual search then runs inside your logged-in LinkedIn session; visiting profiles can appear in "Who viewed your profile", so run it from a sock LinkedIn account if you need to stay covert.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: LinkedProspect is a third-party sales-outreach vendor; the free Boolean builder is a simple, transparent utility that only concatenates operators — no data is collected about the person you search.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- LinkedProspect Boolean Search Tool
- LinkedIn Boolean search builder
tags:
- linkedin
- boolean-search
source: osint4all
lastVerified: '2026-07-15'
enrichment: full
---

# LinkedProspect

> A free form that turns plain filters — job titles, companies, keywords, each with include/exclude — into a valid LinkedIn Boolean search string you paste straight into LinkedIn.

## When to use
You know something about *where* or *what* your subject does — a role, an `employer-org`, a keyword they'd list — but LinkedIn's native search keeps returning noise. Hand-writing Boolean (`("VP Sales" OR "Head of Sales") AND "Acme" NOT recruiter`) is error-prone; this builds it correctly so you can pinpoint the one profile among namesakes.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://linkedprospect.com/linkedin-boolean-search-tool/ (no login required).
2. Fill the six fields — job titles/keywords to **include** and **exclude**, company names to **include** and **exclude**, general keywords to **include** and **exclude** — separating multiple terms with commas.
3. Copy the generated Boolean string.
4. Paste it into the LinkedIn search bar (ideally from a sock account) and run it.
5. Pivot: matching `social-profile`s confirm current `employer-org`, title, and location; from there jump to people-search or email-permutation tools.

## Inputs → Outputs
- **In:** `name`/keywords + `employer-org` (as include/exclude term lists)
- **Out:** a Boolean query string → LinkedIn `social-profile` results and confirmed `employer-org`
- **Empty/negative result looks like:** the builder always returns a string; a *LinkedIn* search that returns nothing means your filters are too tight or the person isn't on LinkedIn under those terms — loosen the excludes and drop the company constraint.

## Gotchas & OpSec
- The tool only writes the query — the search itself, and any rate-limiting or "commercial use limit" LinkedIn imposes, happens in your account. Use a sock LinkedIn login for covert work.
- LinkedIn periodically deprecates Boolean operators (it dropped some for non-Recruiter accounts); if a string underperforms, simplify it.
- OpSec: **passive** at the generation step; **becomes active** the moment you view profiles in LinkedIn (the subject may see the visit).

## Overlaps ("do both")
- Pairs with `[[x-com-3]]` and other LinkedIn-technique notes — the Boolean string finds the profile; curated tip threads tell you what else to pull from it.

## Trust & verifiability
`trust: community` — a vendor freebie, not first-party LinkedIn tooling, but the builder is trivial and transparent (it just assembles operators), so there's little to distrust. Always confirm the surfaced profile is actually your subject.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | linkedprospect |
| category | social-networks |
| selectorsIn → selectorsOut | name, employer-org → social-profile, employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
