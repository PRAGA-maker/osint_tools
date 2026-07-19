---
id: repos-timeline
name: Repos Timeline
description: Use when you have a GitHub `username` and want their activity over time — returns a chronological timeline of the user's repositories and forks as a pattern-of-life view.
url: https://repostimeline.nazifbara.com/
category: social-networks
path:
- social-networks
bestFor: Visualizing a GitHub user's repositories and forks on a timeline to see when and on what they were active.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free, browser-based; no account or payment. Reads GitHub's public API.
opsec: passive
opsecNote: You submit a public GitHub username to a third-party web app that queries GitHub's public API; the target is not notified. Nothing you couldn't see on the profile is revealed — it's just arranged on a timeline. Use a research browser profile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A small independent web tool (nazifbara.com) over GitHub's public API; the timeline is reproducible against the live profile, but it's a third-party visualizer, not an authoritative source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Repos Timeline
tags:
- Social Media
- Github
- pattern-of-life
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Repos Timeline

> Enter a GitHub username and get a chronological timeline of every repo they created and forked — a quick pattern-of-life read on a developer's activity.

## When to use
You've linked a subject to a GitHub `username` and want more than a repo list: when they were active, bursts and gaps in activity, and what technologies/projects they engaged with over time. The timeline surfaces active periods (a pattern-of-life / time-zone hint), the projects that mattered to them, and forks that reveal interests and collaborators. It's soft behavioural context built from public GitHub data — supporting signal, not identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://repostimeline.nazifbara.com/ and enter the target's GitHub username; click Generate.
2. Read the timeline: repositories and forks placed by date, showing active vs dormant periods.
3. Note the projects and the collaborators/upstreams behind notable forks.
4. Cross-check standout items against the live GitHub profile.
5. Pivot: active repos lead to commit metadata (emails, co-authors) and to the same handle on other platforms.

## Inputs → Outputs
- **In:** GitHub `username`
- **Out:** a dated timeline of repos/forks → linkable `social-profile`/`username` context and activity windows
- **Empty/negative result looks like:** an empty or sparse timeline — the user has few public repos, or the handle doesn't exist / is mistyped.

## Gotchas & OpSec
- Human-in-the-loop: none.
- Only public repos are visible; private activity and the contributions graph aren't fully represented.
- It's a visualizer — for hard data (commit emails, co-authors) go to the repos/commits themselves.

## Overlaps ("do both")
- Pairs with GitHub commit-metadata and cross-platform username tools — this frames *when* a user was active; those extract *who* (emails, collaborators) and *where else* the handle appears.

## Trust & verifiability
`trust: community` — a third-party visualizer over GitHub's public API; the timeline is checkable against the live profile but is convenience, not an authoritative record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | repos-timeline |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
