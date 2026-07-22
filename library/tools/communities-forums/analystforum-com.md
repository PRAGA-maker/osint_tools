---
id: analystforum-com
name: AnalystForum
description: Use when you have a `username` and want to trace a finance/CFA-candidate's forum footprint — returns `social-profile`, reused `username` and disclosed career/location detail.
url: https://www.analystforum.com/
category: communities-forums
path:
- communities-forums
bestFor: Tracing a finance professional's or CFA/FRM candidate's posts, handle reuse and volunteered career details.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
- employer-org
status: live
pricing: free
costNote: Free to read; a free account is needed to post or view some member fields.
opsec: passive
opsecNote: Reading and Google-dorking public threads is passive. Registering or messaging a member is active and visible — sock puppet only if you must interact.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running community for CFA/finance-exam candidates; posts are user self-report, valuable mainly for handle reuse and volunteered career/location detail.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Analyst Forum
- analystforum.com
tags:
- forums
- finance
- cfa
source: uk-osint
lastVerified: '2026-07-22'
enrichment: full
---

# AnalystForum

> The main online community for CFA/FRM candidates and finance professionals — a targeted place to trace someone in the investment/finance world by their handle.

## When to use
You have a `username` (or `name`) and reason to think the subject works in finance, investment or is pursuing the CFA/FRM. Members discuss exams, careers, employers, cities and compensation, frequently volunteering current or target employers, locations and study timelines. Best for confirming a finance career claim, recovering a reused handle, or geolocating/dating a subject via their study/job posts.

## How to use it (`bestInteractionPattern`: web-manual)
1. Use the forum search, or Google-dork it: `site:analystforum.com "<username>"`.
2. Open the member profile (join date, post count) and post history.
3. Read posts for volunteered detail — employer, city, exam level/year, university, comp discussion.
4. Pivot: a reused `username` feeds cross-platform enumeration; an `employer-org` feeds LinkedIn/company checks; exam-year posts date the subject's activity.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** `social-profile` (profile + posts), reused `username`, `employer-org` and location/timeline disclosures
- **Empty/negative result looks like:** no profile or dork hits — the handle isn't used here (likely unless the subject is in finance); some fields may be hidden without a login.

## Gotchas & OpSec
- Niche to finance/CFA — expect nothing for unrelated subjects.
- Self-reported career claims; corroborate via LinkedIn/company records.
- Passive to read; posting/DMing is attributable — sock puppet only.

## Overlaps ("do both")
- Pairs with LinkedIn, Companies House and cross-platform username tools — the forum reveals the handle and volunteered detail; those confirm the employer/role behind it.

## Trust & verifiability
`trust: community` — a legitimate, established finance community; content is user self-report, so treat claims as leads to corroborate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | analystforum-com |
| category | communities-forums |
| selectorsIn → selectorsOut | username, name → social-profile, username, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
