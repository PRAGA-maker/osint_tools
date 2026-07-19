---
id: xing
name: XING
description: Use when you have a `name` or `employer-org` in the German-speaking market and want their professional profile — returns employment history, job title and connections (`social-profile`).
url: https://www.xing.com/
category: public-records
path:
- public-records
- employee-profiles-and-resumes
bestFor: Professional background research on people and companies in the DACH region (Germany, Austria, Switzerland), where XING rivals LinkedIn.
selectorsIn:
- name
- employer-org
selectorsOut:
- social-profile
- employer-org
- name
status: live
pricing: freemium
costNote: Free account lets you search and view basic profiles; a paid Premium tier unlocks deeper search filters and full visitor/contact features.
opsec: active
opsecNote: XING shows members "who viewed your profile", so a logged-in view can expose your account to the target. Always use a sock-puppet XING account, and prefer public/logged-out or cached views for read-only checks. Never view from an attributable personal account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Long-established DACH professional network (owned by New Work SE). Profiles are self-reported by members, so employment claims are unverified, but the platform itself is authentic and widely used.
missingPersonsRelevance: medium
coverage:
- de
- at
- ch
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- xing.com
- New Work XING
tags:
- professional
- employee-profiles
- dach
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# XING

> The German-speaking world's home-grown professional network — the DACH-region counterpart to LinkedIn for tying a `name` to an employer, job title and career history.

## When to use
You have a `name` (or an `employer-org` whose staff you are mapping) with a Germany/Austria/Switzerland connection and want current job title, employment history, education and professional connections. In the DACH market XING often has coverage LinkedIn lacks, so it is a first-stop for confirming a subject's occupation, employer and locale, and for enumerating colleagues as potential `associate` leads.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log into a **sock-puppet** XING account (a free account is enough for basic search).
2. Use the people search for the target `name`; filter by company, location or industry to disambiguate.
3. Open the best-matching profile and read job title, employment/education timeline, and public "contacts".
4. Cross-check details (employer, city, prior roles) against other sources — profiles are self-reported.
5. Pivot: a confirmed `employer-org` feeds company-registry and email-pattern tools; named colleagues feed associate mapping; a profile photo feeds face/image search.

## Inputs → Outputs
- **In:** `name` (optionally + `employer-org` or location to disambiguate)
- **Out:** `social-profile` (XING profile URL), `employer-org` and job title, employment/education history, connection names
- **Empty/negative result looks like:** no matching member, or only a stub profile with no employer — common for people outside DACH or those who never joined XING. Absence here says nothing about LinkedIn or other networks.

## Gotchas & OpSec
- Human-in-the-loop: an account login is required to search; use a burner, never a real identity.
- OpSec: **active** — logged-in profile views can appear in the target's "who viewed me" list. Keep to a sock puppet and lean on logged-out/cached views where possible.
- Free accounts see limited detail on some profiles; do not read a thin free-tier view as the person's full record.

## Overlaps ("do both")
- Pairs with a LinkedIn-style search because XING and LinkedIn have complementary DACH coverage — one frequently has a subject the other misses.

## Trust & verifiability
`trust: community` — the platform is authentic and mainstream, but profile content is self-declared; verify employment claims against company registries or the employer directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | xing |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → social-profile, employer-org, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
