---
id: osint-belarus
name: OSINT Беларусь (Telegram)
description: Use when you want a curated, Russian-language feed of OSINT tools and regional monitoring links for Belarus/Eastern Europe — a resource channel, no personal selectors out.
url: https://t.me/s/osintby
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Following a Russian-language Telegram channel that curates OSINT tools and Belarus/EE monitoring resources.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free public Telegram channel; readable in-browser via the /s/ web preview without a Telegram account.
opsec: passive
opsecNote: Reading the public web preview (t.me/s/osintby) is passive and requires no login. If you join via a Telegram client to see full history or the discussion chat, use a sock-puppet Telegram account — joining exposes your account to the channel/admins.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent, admin-curated channel (Russian-language). Useful for leads and tool discovery, but curation is opinionated and unvetted — verify any tool or claim independently.
missingPersonsRelevance: low
coverage:
- by
- ru
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- osintby
- OSINT Belarus Telegram
tags:
- other-resources
- telegram-channel
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# OSINT Беларусь (Telegram)

> A Russian-language Telegram channel that curates OSINT tools and Belarus/Eastern-Europe monitoring resources — a discovery feed, not a lookup service.

## When to use
Your investigation touches Belarus, Russia, or the wider region and you want a running, community-curated stream of relevant OSINT tools (breach search, domain/URL analysis, video verification, threat-actor tracking) framed for that context. Treat it as a source of *leads and tools*, not as a data source you query with a selector.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://t.me/s/osintby in a browser — the `/s/` path renders the public post history without a Telegram account.
2. Scroll or search the feed for the topic/tool you need; posts include descriptions and direct links.
3. Follow a linked tool out to its own site and evaluate it there before using it.
4. (Optional) Join via a sock-puppet Telegram client to read the companion discussion chat and full archive.
5. Pivot: a linked tool → add it to your workflow after independent verification; a regional lead → your primary research on that entity.

## Inputs → Outputs
- **In:** none (browse/read); topic keywords at most
- **Out:** curated tool links and regional monitoring resources (no personal selectors)
- **Empty/negative result looks like:** the topic simply isn't covered in recent posts — this channel's scope is regional/tooling, so many people-search questions won't be addressed here at all.

## Gotchas & OpSec
- Russian-language content; use translation if needed and don't lose nuance in machine translation of tool descriptions.
- Curation is unvetted — a link appearing here is not an endorsement of safety or accuracy. Verify every tool independently before running it.
- Passive to read via `/s/`; joining with a real account exposes you to the channel — use a sock puppet.

## Overlaps ("do both")
- Complements broader curated lists (e.g. awesome-osint directories) with a regional, frequently-updated Eastern-Europe lens.

## Trust & verifiability
`trust: community` — a single admin's curation. Good for discovery and regional awareness; treat every surfaced tool/claim as unverified until you check it yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-belarus |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | (browse) → (resource feed) |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
