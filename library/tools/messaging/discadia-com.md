---
id: discadia-com
name: discadia.com
description: Use when you have a community `name`/keyword or `username` and want to find the public Discord server(s) tied to it — returns `social-profile` (Discord server listings and invite links).
url: https://discadia.com/
category: messaging
path:
- messaging
bestFor: Discovering public Discord servers by name, keyword, or tag when you suspect a target runs or frequents a community.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free public directory; no account or payment needed to search or browse listings.
opsec: passive
opsecNote: Searching the directory is passive and does not touch the target — you are only querying Discadia's own index. Joining any server you find via its invite is active and exposes your Discord account; use a sock-puppet Discord account and clean browser session before joining.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party community-run Discord directory; listings are self-submitted by server owners, so presence is not authoritative and absence proves nothing.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Discadia
- Discadia Discord server list
tags:
- discord
- Discord Related Sites
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# discadia.com

> A searchable public directory of Discord servers (200+ added daily) — use it to find the community a name/keyword or handle points to, not to search individual users.

## When to use
You have a community `name`, a distinctive keyword, or a `username`/handle a target uses, and you want to locate the public Discord server(s) associated with it. Useful when a subject references "our Discord" or a group name and you need the actual invite/landing page to see who runs it and what it covers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://discadia.com/ in a sock-puppet browser session.
2. Enter a server `name`, keyword, or tag (e.g. gaming, roleplay, a town name, a fandom) in the search/filter bar; or append `?q=<term>` to the URL.
3. Read the results — each hit is a public Discord server listing with description, tags, member count, and a join/invite link.
4. Pivot: open a promising listing to read its public description and owner info; if you must go inside, join the server with a sock-puppet Discord account to enumerate members/channels. Feed Discord handles into `[[discord-lookup]]`-style tooling or username searches.

## Inputs → Outputs
- **In:** `name` (community/server name), keyword/tag, or `username`
- **Out:** `social-profile` — Discord server listings, descriptions, tags, member counts, invite links
- **Empty/negative result looks like:** no matching listings, or only generic servers unrelated to your term. Absence means the server was never submitted to Discadia — many private/target servers are not listed — so this is not proof a community doesn't exist.

## Gotchas & OpSec
- Listings are owner-submitted; a directory hit is not verification the target runs that server.
- Searching is passive; **joining** any server is active and can be seen by admins/bots — always use a sock puppet and never join with an attributable account.
- Server invites in old listings expire; a dead invite doesn't mean the server is gone.

## Overlaps ("do both")
- Pairs with `[[disboard-org]]` and other Discord directories — each indexes a different (owner-submitted) subset, so run the same query on both to catch servers one misses.

## Trust & verifiability
`trust: community` — Discadia is a third-party, self-submission directory. It is a discovery aid, not an authoritative source; corroborate any server-to-target link with independent evidence.
