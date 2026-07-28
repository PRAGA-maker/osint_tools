---
id: gh-archive
name: GH Archive
description: Use when you have a GitHub `username` (or repo/org) and want their full historical public-event activity at scale — returns social-profile activity, associate and employer-org leads.
url: https://www.gharchive.org
category: archives-cache
path:
- archives-cache
bestFor: Querying the complete historical record of public GitHub events (pushes, PRs, comments) for a user or project.
selectorsIn:
- username
- domain
selectorsOut:
- social-profile
- associate
- employer-org
- email
status: live
pricing: free
costNote: Free. Hourly JSON archives are downloadable; the full dataset is also queryable via Google BigQuery (BigQuery's own usage costs apply for large queries).
opsec: passive
opsecNote: You query an archived dataset, not GitHub or the user, so activity is passive and invisible to the subject. Downloading archives or running BigQuery ties the work to your own infra/account, not the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: A long-standing, widely-used open dataset of GitHub's public event stream (the same events the GitHub API exposes), archived hourly. Data is GitHub's own public activity, so it's authoritative for what was public at capture time.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- github-search
- commits-by-a-particular-github-user
tags:
- github
- dataset
- archive
source: osintambition-social
lastVerified: '2026-07-28'
enrichment: full
---

# GH Archive

> An hourly archive of GitHub's entire public event stream since 2011 — lets you reconstruct a developer's full activity history and timing, including events GitHub's live UI no longer surfaces.

## When to use
You have a GitHub `username` (or a repo/org) and want more than the profile page shows: complete push/PR/issue/comment history, active hours (timezone inference), collaborators (`associate`), and commit emails that can reveal identity or `employer-org`. Especially useful when a subject deleted recent activity — the archive still holds what was public when captured.

## How to use it (`bestInteractionPattern`: cli / api)
1. Choose an access path: download hourly JSON.gz files from gharchive.org for a date range, or query the public dataset in Google BigQuery (`githubarchive`).
2. Filter events by `actor.login` (the username), repo, or org.
3. Analyse: event types and timestamps (activity pattern / timezone), repos touched (interests, employer projects), and commit author emails.
4. Extract identity leads — a commit email or a co-committer handle is a strong pivot.
5. Pivot: commit `email` → email/breach search; collaborators → network mapping; org repos → `employer-org`.

## Inputs → Outputs
- **In:** `username` (GitHub login), repo, or org, + a time range
- **Out:** `social-profile` activity history, `associate` (collaborators), `employer-org` (org repos), and commit `email`s
- **Empty/negative result looks like:** no events for the login in the window — the account may be new, inactive, private, or renamed (logins can change; historical events keep the old login). Absence isn't proof of no activity.

## Gotchas & OpSec
- Public events only — private repos and squashed/rewritten history aren't captured.
- Logins can be renamed; an old username in the archive may now point to a different or deleted account. Confirm identity via stable IDs/emails.
- Large BigQuery scans incur BigQuery costs; scope your date range.

## Overlaps ("do both")
- Pairs with live `[[github-search]]` and `[[commits-by-a-particular-github-user]]` for current-state confirmation — the archive gives history, live search gives what's public now.

## Trust & verifiability
`trust: trusted` — it mirrors GitHub's own public event API, archived faithfully. Reliable for what was public at capture time; verify that a login still maps to the same person before attributing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gh-archive |
| category | archives-cache |
| selectorsIn → selectorsOut | username, domain → social-profile, associate, employer-org, email |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
