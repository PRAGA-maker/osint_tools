---
id: quora
name: Quora
description: Use when you have a `name`/`username` and want a subject's Quora presence — returns social-profile, stated employer/education, interests, and their questions/answers as behavioral leads.
url: http://www.quora.com
category: communities-forums
path:
- communities-forums
bestFor: Finding a person's Quora profile and mining their answers for bio, employer/education, and interests.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- employer-org
status: live
pricing: free
opsec: passive
opsecNote: Reading public profiles/answers is passive, but Quora increasingly gates content behind a login wall and personalizes what it shows — use a sock-puppet account, never your real one, if you must log in. Following or upvoting is attributable; just read. What people volunteer in answers (locations, jobs, personal anecdotes) is often unguarded and revealing.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A mainstream Q&A platform; profile bios and answers are self-authored and unverified — good for leads, not proof.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Quora
- quora.com
tags:
- q-a-sites
- social-profile
- interests
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Quora

> A Q&A platform whose profiles and answers often over-share — a subject's Quora bio and the questions they ask/answer can leak employer, education, location, and personal interests.

## When to use
You have a `name`/`username` and want to check for a Quora presence. Profiles list a self-written bio, claimed employers/education ("credentials"), and topics followed; their answers frequently reveal profession, opinions, life details, and sometimes location through anecdotes. Useful for fleshing out interests and professional context, and the questions someone asks can itself be revealing (e.g. immigration, health, local specifics).

## How to use it (`bestInteractionPattern`: web-manual)
1. Search Quora for the subject's `name`/`username`, or use a site-scoped Google search (`site:quora.com "Name"`) to bypass some of the login wall.
2. Match a profile by name, photo, bio, or writing style.
3. Read the profile credentials and their answers/questions (`selectorsOut`); note any employer, school, city, or personal detail volunteered.
4. Pivot: the handle cross-checks on other platforms; stated employer/education feeds professional lookups; anecdotes give geographic/lifestyle leads.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** `social-profile` (Quora profile + handle), `employer-org` (stated credentials/education), interests and volunteered personal details
- **Empty/negative result looks like:** no matching profile, or a login wall blocking content — try Google site-search; absence means no reachable Quora presence, not that the person isn't online.

## Gotchas & OpSec
- Human-in-the-loop: Quora often forces a login to read fully (`account-login`); use a sock puppet.
- OpSec: passive to read; upvoting/following/messaging is attributable — don't.
- Self-reported and unverified: credentials and anecdotes can be embellished or false; treat as leads to corroborate.

## Overlaps ("do both")
- Pairs with Reddit and other forum/Q&A searches and with username-enumeration tools — people reuse handles and over-share across Q&A sites, so cross-run to build interests and professional context.

## Trust & verifiability
`trust: unverified` — a legitimate platform, but everything on a profile is self-authored. It's a rich source of leads (interests, employer, locale), all of which must be confirmed against harder sources before use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | quora |
| category | communities-forums |
| selectorsIn → selectorsOut | name, username → social-profile, employer-org |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
