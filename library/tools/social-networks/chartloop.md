---
id: chartloop
name: Chartloop
description: Use when you have an `employer-org` and want to reconstruct its reporting structure from LinkedIn into an org chart — returns `associate`, `employer-org`, `social-profile` (colleagues and hierarchy). NOTE: hosted app appears offline.
url: https://buildorgchart.herokuapp.com/
category: social-networks
path:
- social-networks
bestFor: Building a LinkedIn-derived organizational chart of a company to map colleagues, reporting lines, and associates around a target.
selectorsIn:
- employer-org
- name
selectorsOut:
- associate
- employer-org
- social-profile
status: down
pricing: free
costNote: Was a free hosted web app; the Heroku deployment now returns HTTP 404 (Heroku retired its free dyno tier in Nov 2022), so the tool appears offline.
opsec: active
opsecNote: Building an org chart means viewing many LinkedIn profiles, which LinkedIn records as profile views the target's colleagues can see. If a working instance is found, drive it only from a sock-puppet LinkedIn account with "private mode" browsing enabled; never use an attributable account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Community-built third-party tool that scrapes/organizes LinkedIn data; not affiliated with LinkedIn and its hosted endpoint is currently unreachable.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
aliases:
- Build Org Chart
- buildorgchart
tags:
- linkedin
- org-chart
- social-networks
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Chartloop

> A LinkedIn org-chart builder that maps a company's people and reporting lines — but the hosted Heroku app is currently down (HTTP 404).

## When to use
You have an `employer-org` (a target's workplace) and want to map the colleagues, reporting structure, and associates around them from LinkedIn data — a strong lead source for who a person knows and works with. In practice, verify the hosted app is live first: as of this writing the endpoint 404s.

## How to use it (`bestInteractionPattern`: web-manual)
1. Attempt to open https://buildorgchart.herokuapp.com/ — if it returns "No such app"/404, the deployment is offline (Heroku free tier retirement) and you should fall back to an alternative.
2. If a working instance exists: connect/authenticate the sock-puppet LinkedIn account it requires.
3. Enter the target `employer-org`; the tool pulls employees and arranges them into a reporting-hierarchy chart.
4. Read the chart for `associate` names, roles, and profile links around the target.
5. Pivot: feed discovered colleague `social-profile`s and names into username/people searches; use the hierarchy to identify likely close contacts.

## Inputs → Outputs
- **In:** `employer-org` (company), optionally a `name` to center the chart
- **Out:** `associate` (colleagues), `employer-org` structure, `social-profile` links (LinkedIn)
- **Empty/negative result looks like:** a 404/"No such app" page (the app is down), or — if live — an empty chart when the company has too few indexed employees.

## Gotchas & OpSec
- **Currently down:** the herokuapp endpoint returns 404; treat this skill as a pointer to the technique, and substitute a maintained alternative until/unless the app returns.
- Active toward the graph: pulling profiles registers LinkedIn profile views; always use a sock puppet with private-mode browsing.
- Scraping LinkedIn may violate its ToS and risk account bans.

## Overlaps ("do both")
- Pairs with a maintained LinkedIn OSINT toolkit (e.g. a local scraper that batch-collects employees and renders a D3 org chart) — use that when Chartloop's hosted app is unavailable. Also pairs with `[[thats-them]]` to enrich named colleagues.

## Trust & verifiability
`trust: community` — a third-party LinkedIn tool, not affiliated with LinkedIn. Its hosted instance is presently unreachable, so any output must come from a verified live deployment and be corroborated against the actual LinkedIn profiles.
