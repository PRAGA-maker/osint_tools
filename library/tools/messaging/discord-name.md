---
id: discord-name
name: Discord.name
description: Use when you have a Discord `social-profile`/user ID and want to resolve it to a username and username history — but the service has been shut down by Discord, so returns nothing today.
url: https://discord.name/
category: messaging
path:
- messaging
bestFor: Historically, resolving a Discord snowflake user ID to current username and past username history.
selectorsIn:
- social-profile
- username
selectorsOut:
- username
- social-profile
status: down
pricing: free
costNote: Was a free, solo-maintained utility; no longer operational after Discord enforcement action, so there is no cost because there is no service.
opsec: passive
opsecNote: Moot while offline. When it ran it queried a third-party mirror of Discord data, so lookups did not touch the target's own account or notify them — but you were trusting an unofficial operator with the IDs you searched.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Solo-operated unofficial Discord data utility with no transparency about data sourcing; Discord itself deemed it a policy violation and forced it offline.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- discord.name
- Discord Name lookup
tags:
- discord
- id-lookup
- username-history
source: osintambition-social
lastVerified: '2026-07-15'
enrichment: full
---

# Discord.name

> A now-defunct utility that once resolved a Discord user ID to that account's username and name-change history — shut down by Discord for policy violations.

## When to use
Do not reach for this today: as of the last check the site serves only a shutdown notice. It is documented here so that when you see it recommended in an older OSINT list you know not to waste time. Historically the case was: you have a Discord snowflake `social-profile` (the long numeric user ID) and want to learn the current `username` plus any prior usernames the account used.

## How to use it (`bestInteractionPattern`: web-manual)
1. The site (https://discord.name/) is offline as a lookup tool — it now displays only an announcement that the maintainer shut it down after Discord cited automated data-collection and API-usage violations.
2. There is no input field to submit an ID; the historical flow (paste a user ID → get username history) no longer functions.
3. Pivot instead: for a live Discord ID→profile pivot, resolve the snowflake via Discord's own API or a maintained lookup, and pivot usernames through `[[discord-com-2]]` and general username tooling.

## Inputs → Outputs
- **In:** (historically) `social-profile` = Discord user ID / `username`
- **Out:** (historically) `username`, past username history, `social-profile`
- **Empty/negative result looks like:** every request now returns the shutdown notice rather than data — treat any "result" as noise, not a hit.

## Gotchas & OpSec
- Human-in-the-loop: none — but also no working function.
- OpSec: moot while offline. Note the broader lesson: unofficial Discord scrapers are routinely taken down, so any that reappear under a new domain are unstable and untrustworthy with the IDs you feed them.
- Do not cite historical username data from mirrors as current; Discord usernames and the ID→name mapping change.

## Overlaps ("do both")
- Pairs with `[[discord-com-2]]` — that covers live, first-party Discord investigation routes, which is what you need now that this mirror is dead.

## Trust & verifiability
`trust: unverified` — it was an opaque solo-run scraper with no sourcing transparency, and Discord classified it as a violating utility and forced it offline; nothing it output can be re-verified now.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | discord-name |
| category | messaging |
| selectorsIn → selectorsOut | social-profile, username → username, social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
