---
id: support-discord-com
name: support.discord.com
description: Use when you're resolving a Discord `username` and need to understand the 2023 unique-username vs display-name system — returns reference knowledge for interpreting handles.
url: https://support.discord.com/hc/en-us/articles/12620128861463-New-Usernames-Display-Names
category: messaging
path:
- messaging
bestFor: Understanding Discord's unique-username / display-name model so you interpret and search handles correctly.
selectorsIn:
- username
selectorsOut: []
status: live
pricing: free
costNote: Free official Discord help article.
opsec: passive
opsecNote: Reading a help article is invisible to any subject. Pure reference.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Discord support documentation; authoritative on how Discord's username system works.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Discord New Usernames Display Names
tags:
- discord
- Discord Related Sites
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
relatedTools:
- discord-com
- discord-com-2
- support-discord-com-2
---

# support.discord.com

> Discord's official explainer for the 2023 username overhaul — the reference that tells you how the new unique @username differs from the mutable display name and the old `name#1234` discriminator, so you don't misread or mis-search a Discord handle.

## When to use
This is a **reference, not a lookup**. When your case involves a Discord `username`, you need to know which part is stable and searchable: Discord replaced the old discriminator system (`Name#1234`) with unique, lowercase @usernames plus freely-changeable display names. Misunderstanding this leads to dead-end searches — e.g. treating a display name as a unique handle. This page sets you straight before you pivot to actual Discord OSINT.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read https://support.discord.com/hc/en-us/articles/12620128861463-New-Usernames-Display-Names.
2. Note the distinction: the **unique @username** is the durable, one-per-account identifier; the **display name** is cosmetic and changeable; old `#1234` discriminators are retired.
3. When you have a handle, determine which type it is and search accordingly.
4. Pivot: use the unique username as your search anchor across Discord servers, ID-lookup bots, and cross-platform handle checks.

## Inputs → Outputs
- **In:** a Discord `username`/display name you're trying to interpret
- **Out:** the conceptual model needed to search correctly (no data records)
- **Empty/negative result looks like:** N/A — it's documentation; the failure mode is searching a mutable display name as if it were unique.

## Gotchas & OpSec
- Display names are not unique and change freely — never treat one as a stable identifier.
- OpSec: **passive** — reading help pages reveals nothing about the subject.
- Discord's system can evolve again; re-check the current article if handles behave unexpectedly.

## Overlaps ("do both")
- Pairs with `[[knowlesys-com-2]]`-style ID techniques and `[[discord-com-2]]` — this explains what a handle *is*, those explain what data sits behind it and how to obtain it.

## Trust & verifiability
`trust: trusted` — first-party Discord documentation; authoritative on its own username model.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | support-discord-com |
| category | messaging |
| selectorsIn → selectorsOut | username → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
