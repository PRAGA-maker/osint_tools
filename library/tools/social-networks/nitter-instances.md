---
id: nitter-instances
name: Nitter Instances
description: Use when you have a Twitter/X `username` and want to read a profile/tweets anonymously via a Nitter mirror — this page returns a live list of working Nitter instances (which yield `social-profile` content).
url: https://xnaas.github.io/nitter-instances/
category: social-networks
path:
- social-networks
bestFor: Finding a currently-working Nitter instance to view Twitter/X profiles and tweets without an account or JavaScript.
selectorsIn:
- username
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free. The list and Nitter itself are free; no account needed.
opsec: passive
opsecNote: The strength here is OpSec: viewing a target's X profile through a Nitter mirror avoids logging into X and prevents X from tying the view to your account. Use a fresh/sock-puppet browser session anyway. Note that a public instance operator can see your requests — pick reputable instances.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-maintained uptime list for Nitter, the open-source X front-end. Since X's 2023 API crackdown most instances are unstable or dead, so this list's value is finding the few that still work at any moment.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Nitter instance list
- xnaas nitter-instances
tags:
- nitter
- twitter
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# Nitter Instances

> A live uptime list of Nitter mirrors — the open-source, login-free front-end for Twitter/X — so you can find one that still works and read a profile anonymously.

## When to use
You want to view a Twitter/X `username`'s profile or tweets without logging into X (for OpSec, or because X now walls much content behind login). Nitter renders X profiles without JavaScript or an account, but public instances are frequently rate-limited or down. This page tracks which instances are currently up, so you can find a working one fast.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://xnaas.github.io/nitter-instances/ and look for instances marked healthy/online.
2. Take a working instance's base URL and append the target handle (e.g. `https://<instance>/username`).
3. Read the profile and tweets; try RSS or search paths the instance supports.
4. If an instance fails or rate-limits, fall back to the next healthy one from the list.
5. Pivot: captured tweets/handles feed archiving (`[[wayback-machine]]`), avatars feed reverse-image, and handles feed username OSINT.

## Inputs → Outputs
- **In:** Twitter/X `username` (applied to a chosen instance)
- **Out:** the tools to reach a `social-profile` — profile, tweets, media — via a working mirror
- **Empty/negative result looks like:** all instances red/dead, or an instance loads but returns errors/empty timelines — increasingly common since X's API changes. If nothing works, the content may only be reachable logged-in on X itself.

## Gotchas & OpSec
- Volatile: instance health changes hour to hour; expect to try several. Many are permanently dead post-2023.
- Instance operators see your traffic — prefer reputable ones and a clean session.
- Coverage/features vary per instance (some lack search or media).

## Overlaps ("do both")
- Pairs with `[[wayback-machine]]`/archive tools and direct X viewing — Nitter gives anonymous live-ish reads when it works, while archives recover deleted/old tweets Nitter can't show.

## Trust & verifiability
`trust: community` — a volunteer-maintained status list; it accurately reflects instance uptime, but the underlying Nitter ecosystem is degraded, so treat availability as best-effort.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nitter-instances |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
