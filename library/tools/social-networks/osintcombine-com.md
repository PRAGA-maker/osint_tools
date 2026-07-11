---
id: osintcombine-com
name: OSINT Combine (Free Tools & Guides)
description: Use when you need a vetted free OSINT tool or methodology guide (alt-tech search, TikTok/username checkers, maps, platform how-tos like Bluesky) — returns purpose-built browser tools and step-by-step guides, not a single lookup.
url: https://www.osintcombine.com/
category: social-networks
path:
- social-networks
bestFor: A hub of free, analyst-built OSINT micro-tools and platform how-to guides (incl. alt-tech and Bluesky).
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: freemium
costNote: The how-to guides and a suite of free browser tools are free with no login. Training courses and the flagship NexusXplore platform are paid/commercial.
opsec: passive
opsecNote: Reading guides and using the client-side free tools is passive. Some free tools redirect your query into the target platform's own search (e.g. TikTok/Google) — the same OpSec as searching that platform applies, so use a sock puppet where you'd normally use one.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Reputable Australian OSINT firm used by law enforcement, defense, and enterprise; its free tools and guides are professionally produced and well-regarded in the community.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- OSINT Combine
- osintcombine.com
tags:
- bluesky
- BlueSky / BSky Related Sites
- osint-tools
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# OSINT Combine (Free Tools & Guides)

> A professional OSINT firm's public toolbox — free, analyst-built browser tools (alt-tech search, username/TikTok checkers, an atlas of maps) plus step-by-step platform guides such as its Bluesky OSINT guide.

## When to use
You need either a purpose-built free tool for a specific platform (searching alt-tech networks like Gab/Rumble/BitChute, checking a `username`/hashtag on TikTok, browsing thematic maps/satellite imagery) or a vetted methodology for investigating a platform you don't know well (e.g. Bluesky). Reach for it to pick the right technique and tool for a `name`/`username` lead, then execute with the tool it provides.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.osintcombine.com/ → "Free Tools" for the micro-tools, or "How-to Guides" for methodology.
2. For a guide (e.g. Bluesky), read the workflow and apply it directly on the target platform.
3. For a free tool, enter your `name`/`username`/hashtag; results typically link back to the source platform or to a Google search.
4. Note that some tools just build and hand off a platform query, so on-platform OpSec applies.
5. Pivot: a found `social-profile` feeds username enumeration and face/photo tools; a guide points you to the platform's native search.

## Inputs → Outputs
- **In:** `username`, `name`, hashtag, or a "how do I investigate platform X" question
- **Out:** links to `social-profile`s on the target platform, or methodology/tool pointers (no raw personal data held by OSINT Combine)
- **Empty/negative result looks like:** a tool returning no matches (the handle isn't on that platform) or no guide for your exact niche — you still get adjacent methodology. It doesn't return facts about a person directly.

## Gotchas & OpSec
- Free vs paid: the guides and browser tools are free; NexusXplore and training are commercial — don't expect the paid platform's depth from the free tools.
- Hand-off tools: several tools just redirect into a platform's own search, so apply that platform's OpSec (sock puppet).
- Tools change: the free-tool lineup evolves; check what's currently offered.

## Overlaps ("do both")
- Pairs with dedicated enumerators like `[[blackbird]]` and with platform-native search — OSINT Combine's tools are handy for alt-tech/niche platforms those miss, and its guides tell you which tool to reach for.

## Trust & verifiability
`trust: trusted` — a well-regarded professional OSINT provider; its free tools and guides are reliable and analyst-built, though the free tools ultimately surface data from the underlying platforms, which you should still verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osintcombine-com |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
