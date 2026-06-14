---
id: slack
name: Slack
description: Use when you want guidance/links for finding people and emails across public Slack workspaces — points to Slack-OSINT resources rather than running a query.
url: https://bloopbase.keybase.pub/SLACK/index.html
category: email
path:
- email
bestFor: A curated reference page of Slack-related OSINT links/techniques for pivoting from a person to public Slack workspaces.
selectorsIn:
- username
- email
- name
selectorsOut:
- social-profile
- username
status: unknown
pricing: free
costNote: Static page hosted on Keybase public storage; no paid component.
opsec: passive
opsecNote: Reading the reference page is passive. Acting on it (joining/searching a Slack workspace) may require login and can expose your presence to admins.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A static page on an individual's Keybase public folder (bloopbase.keybase.pub); author and currency are unknown, and Keybase-hosted pages are frequently stale or offline.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- email
- slack
source: osint4all
lastVerified: ''
enrichment: full
---

# Slack

> A Keybase-hosted reference page pointing to techniques/links for OSINT across public Slack workspaces.

## When to use
You have a `username`, `email`, or `name` and want to check whether the person is active in public/community Slack workspaces (open-source projects, professional communities). This page is a pointer to methods and links, not a live search engine.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://bloopbase.keybase.pub/SLACK/index.html (Keybase public storage — may be slow or offline).
2. Read the linked resources/techniques for enumerating public Slack communities and searching members.
3. Apply a method: e.g. search public Slack directories or community sites for the target's `email`/`username`.
4. Pivot: a matched workspace member profile yields a `username`/`social-profile` and timezone/activity clues to feed into username and people searches.

## Inputs → Outputs
- **In:** `username`, `email`, or `name`
- **Out:** `social-profile` / `username` leads on public Slack workspaces (via the techniques it references)
- **Empty/negative result looks like:** the page is unreachable, or the linked methods return no workspace membership for the identifier.

## Gotchas & OpSec
- This is a static link page, not a tool; its links may rot. Verify each before relying on it.
- Human-in-the-loop: actually searching a Slack workspace usually requires joining/login, which can reveal you to workspace admins — use a sock-puppet account.

## Overlaps ("do both")
- Pairs with username-search tools; Slack membership is one of many platforms to enumerate from a single handle.

## Trust & verifiability
`trust: unverified` — individual's Keybase public page of unknown authorship and uncertain availability; treat as a starting-point reference only.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | slack |
| category | email |
| selectorsIn → selectorsOut | username, email, name → social-profile, username |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
