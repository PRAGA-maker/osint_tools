---
id: project-whispers
name: Project Whispers (DDoSecrets)
description: Use when you have a `username`, handle, or keyword and want to search leaked far-right Discord chat logs for it — returns matching messages with author handles, timestamps, and server context.
url: https://whispers.ddosecrets.com/
category: public-records
path:
- public-records
bestFor: Full-text searching millions of leaked messages from neo-Nazi/QAnon/far-right Discord servers for a handle, phrase, or identifier.
selectorsIn:
- username
- name
selectorsOut:
- username
- social-profile
- associate
status: live
pricing: freemium
costNote: Free to search; DDoSecrets is a nonprofit transparency collective. Some bulk datasets are gated to journalists/researchers, but the Whispers search is publicly usable.
opsec: passive
opsecNote: You search DDoSecrets' hosted archive, not any live service, so subjects aren't alerted. Note DDoSecrets is a leak-transparency site and your queries are logged there; use a sock-puppet browser/VPN, and treat the underlying data as sensitive leaked material to handle carefully and legally.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Curated by DDoSecrets, an established transparency nonprofit; the archive is genuine leaked data widely used by journalists/researchers. As with any leak, verify identity claims — handles can be reused or spoofed within the logs.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- data-ddosecrets-search
- ddosecrets
aliases:
- Whispers DDoSecrets
- whispers.ddosecrets.com
tags:
- leaks
- discord
- extremism-research
- breach-data
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Project Whispers (DDoSecrets)

> DDoSecrets' searchable archive of ~9.8M leaked messages from neo-Nazi, QAnon and other far-right Discord servers — a full-text index of extremist chat logs for journalists and researchers.

## When to use
You are investigating far-right/extremist activity and have a `username`, display name, phrase, email, or other identifier that might appear in those communities' private Discord chats. Project Whispers lets you full-text search the leaked logs to surface a subject's messages, the servers they were active in, who they talked to, and when — turning a handle into a network and a timeline.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://whispers.ddosecrets.com/ (use a sock-puppet browser/VPN).
2. Search a handle, display name, distinctive phrase, or identifier.
3. Read matches: message text, author handle, timestamp, and the server/channel context.
4. Build the picture — cluster a handle's messages for behaviour/timeline, and note the other participants (`associate` links) and cross-posted identifiers.
5. Pivot: take handles/identifiers to username-search and social-profile tools; corroborate any real-name attribution with independent evidence before asserting it.

## Inputs → Outputs
- **In:** `username` / `name` / keyword / identifier.
- **Out:** matching messages with `username` (author handles), `social-profile`/server context, and `associate` links (co-participants).
- **Empty/negative result looks like:** no messages match — the identifier isn't in these particular leaked servers (it doesn't cover all of Discord), or the person used a different handle there.

## Gotchas & OpSec
- Human-in-the-loop: none for search, but responsible/lawful handling of leaked data is on you.
- OpSec: **passive** toward subjects (they aren't notified), but you're querying a leak-transparency site — use a VPN/sock puppet, and be mindful of the legal/ethical constraints on using breached data in your jurisdiction and case.
- Attribution caution: handles can be reused, shared, or impersonated inside the logs; a message under a name is not proof of a specific real person.
- Scope is limited to the specific leaked servers — absence is not exoneration.

## Overlaps ("do both")
- Pairs with `[[ddosecrets]]` / `[[data-ddosecrets-search]]` — the broader DDoSecrets library and search cover many other leaks beyond these Discord logs; run a handle across both to widen coverage.

## Trust & verifiability
`trust: community` — curated by the DDoSecrets nonprofit and heavily used by journalists, so the archive itself is credible. The caveat is internal: verify that a handle maps to your subject with corroborating evidence, since chat handles are easily reused or faked.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | project-whispers |
| category | public-records |
| selectorsIn → selectorsOut | username, name → username, social-profile, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
