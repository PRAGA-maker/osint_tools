---
id: github
name: GitHub
description: Use when you have a `username`/`name`/`email` and want a developer's code, contacts and network — returns profile, repos, commit `email`s and `associate`s.
url: https://github.com
category: documents-metadata
path:
- documents-metadata
bestFor: Pivoting a developer identity into commit emails, real names, projects, and collaborators.
selectorsIn:
- username
- name
- email
selectorsOut:
- email
- name
- associate
- social-profile
status: live
pricing: freemium
costNote: Free to browse and search public code and profiles; paid plans are only for private hosting, not for OSINT reading.
opsec: passive
opsecNote: Passive reading of public data — but starring, following, or opening issues is logged and visible to the target. Search and read while logged out (or from a puppet account); never interact from an attributable account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Microsoft-owned platform; the data (commits, profiles) is authoritative, though profile display names and bios are user-supplied.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- github-gist
aliases:
- github.com
tags:
- toddington
- curated-directory
- useful-websites-tools-documents
- code-hosting
source: toddington-resources
lastVerified: '2026-07-28'
enrichment: full
---

# GitHub

> The world's largest public code host — and a rich OSINT source: a developer's real name, contact `email`s, projects, timezone, and collaborators are often all recoverable from public activity.

## When to use
You have a developer's `username` (or `name`/`email`) and want to expand it: GitHub links a handle to repos, an org, a bio, a location, and — critically — the `email` addresses baked into public commit history, plus the network of people they collaborate with.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the profile at `github.com/<username>`; note real name, bio, location, company, linked website, and pinned repos.
2. Search: use `in:name`, `in:login`, `in:email` in user search, or global code search for a `name`/`email`/keyword.
3. Extract commit emails: browse a repo's commits, or query the API `https://api.github.com/users/<username>/events/public` and commit patches — author emails are frequently the person's real address.
4. Map `associate`s: followers/following, org members, and frequent co-committers/PR reviewers.
5. Pivot: commit `email`s feed breach/email-OSINT; the linked website/handle feeds cross-platform username enumeration.

## Inputs → Outputs
- **In:** `username`, `name`, or `email`
- **Out:** profile (`name`, location, company), commit `email`s, projects, and collaborator `associate`s / `social-profile` links
- **Empty/negative result looks like:** a bare profile with no repos/activity, or "user not found" — the handle may be unused, renamed, or reserved.

## Gotchas & OpSec
- Any *interaction* (star, follow, issue) notifies/exposes you — read only, logged out or via puppet.
- Users can set a `noreply` GitHub email to hide their real address; older commits often predate that and still leak it.
- Display name and bio are self-supplied and can be fake; commit emails and timestamps are harder to fake and more reliable.
- Commit timestamps reveal a working-hours pattern → approximate timezone/`geolocation`.

## Overlaps ("do both")
- Pairs with [[github-gist]] and username-enumeration tools — GitHub gives the core identity and commit emails, gists reveal ad-hoc code/notes, and enumeration spreads the handle across other platforms.

## Trust & verifiability
`trust: trusted` — first-party platform; commit metadata is authoritative (hard to forge convincingly), while free-text profile fields should be corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | github |
| category | documents-metadata |
| selectorsIn → selectorsOut | username, name, email → email, name, associate, social-profile |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
