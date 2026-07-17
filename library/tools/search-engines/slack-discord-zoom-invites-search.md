---
id: slack-discord-zoom-invites-search
name: Slack/Discord/Zoom Invites Search
description: Use when you want to find public community invite links tied to a topic, org, or `username` — returns indexed Slack/Discord/Zoom invite pages to discover and join relevant communities.
url: https://cse.google.com/cse?cx=8e26eca532ec2cba3
category: search-engines
path:
- search-engines
bestFor: Discovering public Slack workspaces, Discord servers, and Zoom links via a targeted Google Custom Search.
selectorsIn:
- employer-org
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free Google Custom Search Engine (CSE); no account to search. Joining any community found is a separate, active step.
opsec: passive
opsecNote: The search itself is passive (a Google query) and doesn't touch any target. But ACTUALLY JOINING a found Slack/Discord/Zoom is active infiltration — it exposes your sock-puppet identity to that community and may alert admins/members. Decide deliberately before clicking an invite; never join from a personal account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A prebuilt Google CSE scoped to invite domains; results are real Google index hits, but invite links expire quickly so many will be dead.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- google-advanced-search
- disboard
aliases:
- Slack Discord Zoom invite search
tags:
- slack
- discord
- communities
- custom-search
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# Slack/Discord/Zoom Invites Search

> A prebuilt Google Custom Search Engine scoped to Slack/Discord/Zoom invite domains — a fast way to find public community invite links about a topic, organization, or handle.

## When to use
You want to find the online communities around a subject — a company's public Slack, a topic's Discord, a group tied to a `username` or `employer-org` — where members discuss, self-identify, and leave a trail. Public invite links are indexed by Google; this CSE narrows the search to invite domains so you can surface joinable communities relevant to your investigation without wading through generic results.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE at https://cse.google.com/cse?cx=8e26eca532ec2cba3.
2. Search a keyword, org name, project, or handle to find matching invite pages (Slack `*.slack.com` join links, Discord `discord.gg/…`, Zoom links).
3. Scan results for communities relevant to your subject; note the community name/topic even before joining.
4. Decide **deliberately** whether to join — that is an active step (see OpSec). If you do, use a prepared sock-puppet account only.
5. Pivot: a joined community can reveal member `username`s/`social-profile`s and self-disclosed details; observe first, engage minimally.

## Inputs → Outputs
- **In:** keyword / `employer-org` / `username` (topic to find communities for)
- **Out:** invite links and `social-profile` (communities and, once joined, their members)
- **Empty/negative result looks like:** few or dead links — invite links expire fast, so many indexed results 404 or say "invite invalid." A dead invite means the link aged out, not that the community is gone.

## Gotchas & OpSec
- Invite links are short-lived; expect a high proportion of expired/dead results — try several and search fresh terms.
- Searching is passive, but **joining is active infiltration**: it exposes your identity to the community and can alert admins. Never join from a personal account; consider legal/ethical limits before entering private-ish spaces.
- It's a general Google CSE, so results include noise — verify a link is really the community you want before acting.

## Overlaps ("do both")
- Pairs with `[[disboard]]` (Discord server directory) and `[[google-advanced-search]]` — the directory and hand-built dork queries surface communities this CSE misses, so run more than one discovery method.

## Trust & verifiability
`trust: community` — it's a scoped Google search returning real index hits; reliability is limited only by link expiry and index noise, so confirm each community directly before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | slack-discord-zoom-invites-search |
| category | search-engines |
| selectorsIn → selectorsOut | employer-org, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
