---
id: discord-com-2
name: discord.com
description: Use when you have a `username` on Discord and need to know what data Discord retains and how law-enforcement/legal process can obtain it — returns process knowledge, not lookups.
url: https://discord.com/safety/360043712132-how-we-investigate
category: messaging
path:
- messaging
bestFor: Understanding what account/message data Discord holds and the legal channel to request it.
selectorsIn:
- username
selectorsOut: []
status: live
pricing: free
costNote: Free public policy/reference page.
opsec: passive
opsecNote: Reading a public policy page reveals nothing about your subject. Purely a reference — no query touches the target.
humanInLoop: true
humanInLoopReason:
- legal-gate
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Discord Trust & Safety documentation; authoritative on Discord's own retention and disclosure practices.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Discord How We Investigate
- Discord Trust and Safety
tags:
- discord
- Discord Related Sites
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# discord.com

> Discord's official "How we investigate" Trust & Safety page — a reference that spells out what Discord retains, how it acts on reports, and the legal process (subpoena, court order, emergency disclosure request) needed to obtain user data.

## When to use
This is a **reference, not a lookup**. Reach for it when a subject's trail runs into Discord and you need to know what is actually obtainable — before drafting a preservation request, an emergency-disclosure request in a life-at-risk missing-persons case, or advising a family/LE contact on next steps. It tells you what Discord *can* hand over and through which channel, so you don't burn time trying to scrape what only legal process can get.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://discord.com/safety/360043712132-how-we-investigate and read the disclosure and emergency-request sections.
2. Note the distinction between what a user exposes publicly (scrape-able) versus account/IP/message data (requires legal process).
3. For an at-risk case, follow the page's links to Discord's request portal / emergency-disclosure path and route it through the appropriate law-enforcement channel.
4. Pivot: use it to set expectations, then combine public-surface findings (`[[support-discord-com-2]]`, server scraping) with a properly filed request.

## Inputs → Outputs
- **In:** context of a `username`/case you are working (used to decide what to request)
- **Out:** procedural knowledge — retention scope, disclosure thresholds, request routes (no data records)
- **Empty/negative result looks like:** N/A — it's documentation; the "failure" mode is misreading what's obtainable without process.

## Gotchas & OpSec
- Human-in-the-loop / **legal-gate**: the data this page describes is only released to verified law enforcement via subpoena, court order, or emergency request — not to investigators directly. Do not represent yourself as LE.
- OpSec: **passive** — reading policy pages is invisible to the subject.
- Policy pages change; re-verify the current request process before relying on specifics.

## Overlaps ("do both")
- Pairs with `[[support-discord-com-2]]` — that surfaces what a user already exposed publicly; this defines the legal route to everything that isn't public.

## Trust & verifiability
`trust: trusted` — first-party Discord Trust & Safety documentation; authoritative for its own platform's practices.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | discord-com-2 |
| category | messaging |
| selectorsIn → selectorsOut | username → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (legal-gate) |
