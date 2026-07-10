---
id: skype
name: Skype
description: Use when an old lead references a Skype username/account — returns little live intelligence; Skype was retired in May 2025, so treat it as historical and pivot to Teams/other traces.
url: https://www.skype.com/en/
category: social-networks
path:
- social-networks
bestFor: Recognising that a Skype handle is a legacy artifact and knowing where the identity may have migrated (Microsoft Teams) or what historical traces remain.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: down
pricing: free
costNote: The consumer service was retired 5 May 2025 (subscriptions end May 2026); there is no live directory to query.
opsec: passive
opsecNote: There is no live Skype search to run. Historically, third-party "Skype resolvers" that mapped usernames to IPs were abusive and unreliable — do not use them. Any legitimate lookup now goes through Microsoft/Teams under normal account rules.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Microsoft retired consumer Skype on 5 May 2025, migrating users to Teams Free; the platform is no longer a live investigative surface, so this entry is a redirect and historical note.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- account-live-com
aliases:
- skype.com
- Skype ID
tags:
- toddington
- curated-directory
- social-media
- defunct
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# Skype

> Microsoft's retired (May 2025) consumer VoIP/chat service — kept here so an agent treats a Skype handle as a *legacy* identifier and knows the identity likely migrated to Teams.

## When to use
You encounter a Skype `username` or a "find me on Skype: <id>" reference in someone's older profiles, business cards, or archived pages. Microsoft retired consumer Skype on 5 May 2025 and moved accounts to Teams Free, so there is no live Skype directory to search. The value of the handle is now historical: it may match a Microsoft account, a reused username elsewhere, or archived content.

## How to use it (`bestInteractionPattern`: web-manual)
1. Treat the Skype ID as a legacy `username` — do not expect a live Skype search.
2. Because a Skype ID is a Microsoft identity, check whether the associated email is a live Microsoft account with `[[account-live-com]]`; the same handle may now surface in Teams.
3. Reuse the username across other platforms with a username enumerator — people commonly carried the same handle elsewhere.
4. Search archives/cached pages for the Skype ID to recover context (linked name, email, org).
5. Avoid third-party "Skype resolver" sites — historically abusive, inaccurate, and now moot.

## Inputs → Outputs
- **In:** `name` or `username` (legacy Skype ID)
- **Out:** at most a `social-profile` link via reuse of the handle elsewhere or a migrated Microsoft/Teams identity; nothing from Skype itself
- **Empty/negative result looks like:** no live Skype presence (expected) — pursue the handle on other platforms rather than concluding the person is untraceable.

## Gotchas & OpSec
- Consumer Skype is **retired** — any tool claiming live Skype lookups is stale or abusive.
- Don't touch "Skype resolver" IP-grabber services; they're unreliable and dubious.
- OpSec: passive; route any Microsoft-identity check through legitimate flows only.

## Overlaps ("do both")
- Pairs with `[[account-live-com]]` — a Skype ID is a Microsoft identity, so test the linked email for a live Microsoft account and pivot into the Microsoft/Teams ecosystem.

## Trust & verifiability
`trust: unverified` — the platform is retired; the handle is only a historical selector, so any finding must be confirmed on a still-live surface.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | skype |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
