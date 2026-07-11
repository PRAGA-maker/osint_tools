---
id: fb-sleep-stats
name: Fb-sleep-stats
description: Use when you already have a Facebook contact and want to infer their sleep/activity schedule by logging online/offline status over time — returns a `geolocation`/time-zone-adjacent daily-routine pattern. Largely non-functional since Facebook blocked automated access.
url: https://github.com/sqren/fb-sleep-stats
category: social-networks
path:
- social-networks
bestFor: Demonstrating (historically) how Facebook Messenger online-status leaks a contact's sleep pattern.
selectorsIn:
- username
- social-profile
selectorsOut:
- geolocation
status: down
pricing: free
costNote: Free open-source Node.js script (MIT). No cost, but it requires your own logged-in Facebook session cookies to poll the chat presence API.
opsec: active
opsecNote: This is ACTIVE and intrusive. It logs into Facebook with YOUR credentials and repeatedly polls the presence of a specific person, building a covert surveillance log of when they sleep. It violates Facebook's Terms of Service (the author states Facebook contacted him to say so), risks your account being banned, and can constitute stalking. Only consider with explicit legal authorisation and a burner account; for most work, do not run it.
humanInLoop: true
humanInLoopReason:
- account-login
- legal-gate
bestInteractionPattern: cli
trust: community
trustNote: Open-source proof-of-concept by developer "sqren" on GitHub, written as a privacy demonstration. It is real code but effectively deprecated because Facebook blocked the automated presence access it relies on.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
relatedTools:
- facebook-com
aliases:
- fb sleep stats
- sqren/fb-sleep-stats
tags:
- facebook
- presence-tracking
- deprecated
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Fb-sleep-stats

> A privacy proof-of-concept that logs a Facebook contact's Messenger online/offline status around the clock and charts it into their sleep schedule — mostly historical, since Facebook now blocks the automated access it depends on.

## When to use
Almost never, in practice. Conceptually: you have a Facebook contact (a `social-profile`/`username`) whose Messenger presence is visible to you, and you want to infer their daily routine and rough time zone from when their "active now" indicator flips on and off. The technique illustrates a real leak, but the tool itself is effectively **down** — Facebook told the author automated access breaches their ToS and has since restricted the presence endpoints, so expect it not to run as-is.

## How to use it (`bestInteractionPattern`: cli)
1. Clone https://github.com/sqren/fb-sleep-stats and install its Node.js dependencies.
2. Supply your own Facebook session credentials/cookies (user id, cookies, app id) — the script authenticates as *you*.
3. Point it at a target contact and leave it polling their online/offline status over days.
4. It records presence transitions and renders a chart approximating the person's sleep window.
5. Reality check: current Facebook defences mean the polling typically fails or returns nothing; treat this entry as documentation of a technique, not a working tool.

## Inputs → Outputs
- **In:** `username`/`social-profile` of a Facebook contact whose presence you can see (plus your own logged-in session)
- **Out:** a `geolocation`/time-zone-adjacent inference — a daily activity/sleep pattern
- **Empty/negative result looks like:** authentication errors, empty presence data, or a flat chart — the expected outcome now, because the presence access is blocked.

## Gotchas & OpSec
- Human-in-the-loop: requires your own Facebook **account login**, and carries a hard **legal gate** — running it is covert surveillance of an individual.
- OpSec: **active and high-risk** — you log in with real credentials, repeatedly poll one person, and violate Facebook ToS; account bans and legal/stalking exposure are real. Never run against a person without documented authorisation, and only ever from a burner identity you accept losing.
- The tool is deprecated; do not rely on it and do not present its inference as reliable evidence.

## Overlaps ("do both")
- Related to `[[facebook-com]]` — Facebook itself is the passive, safer starting point (profile, friends, public posts). fb-sleep-stats is the intrusive, largely-defunct presence-tracking extreme of the same platform.

## Trust & verifiability
`trust: community` — a legitimate open-source demonstration of a genuine privacy weakness, but no longer a dependable tool. Its value today is educational (showing what presence indicators leak), not operational.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fb-sleep-stats |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login, legal-gate) |
