---
id: fediverse-osint
name: Fediverse_OSINT
description: Use when you have a `username` and want to hunt for it across Mastodon/Fediverse instances — returns `social-profile` matches and which servers the handle exists on.
url: https://github.com/cyfinoid/fediverse_osint
category: social-networks
path:
- social-networks
- fediverse-mastodon
bestFor: Checking whether a username exists across known Fediverse (Mastodon/ActivityPub) servers.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free, open-source Python CLI; no account. Uses the open ActivityPub/WebFinger APIs of public instances.
opsec: active
opsecNote: It queries many Fediverse instances directly from your host — each instance admin can see your requests in their logs. Use a non-attributable IP if the target is sensitive; there is no central intermediary hiding you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source project by cyfinoid; inspectable code. Coverage is bounded by its known-instances list, so absence isn't proof.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- cyfinoid fediverse_osint
tags:
- fediverse
- mastodon
- activitypub
- username-enumeration
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# Fediverse_OSINT

> A Python CLI that hunts a username across the decentralised Fediverse — checks whether a domain federates, whether a handle exists on a given server, and searches known discoverable instances.

## When to use
You have a `username` and want to find the subject on Mastodon and other ActivityPub networks, which centralized username checkers usually miss. Because the Fediverse is spread across thousands of independent servers, a handle can live on any of them; this tool automates checking the known/discoverable set and confirming a `handle@server` exists.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo (`git clone https://github.com/cyfinoid/fediverse_osint`) and install requirements (`pip install -r requirements.txt`).
2. Run the script with a target username (and/or a domain to test federation), per the repo README.
3. It uses each instance's open API/WebFinger to check existence and hunts across its `nodes.json` list of known servers.
4. Read the output: which servers the handle exists on, with profile URLs.
5. Pivot: open each confirmed `social-profile`, read posts/bio for further selectors, and correlate with the same handle on centralized platforms.

## Inputs → Outputs
- **In:** `username` (and optionally a domain to test)
- **Out:** `social-profile` matches — `handle@server` accounts and their profile URLs
- **Empty/negative result looks like:** no hits — the handle isn't on any checked instance, or it lives on a server outside the tool's known list; Fediverse coverage is inherently partial, so this isn't proof of absence.

## Gotchas & OpSec
- Coverage is limited to the tool's known-instances list plus what it can discover — the Fediverse has far more servers, so negatives are weak.
- Queries hit instances directly from your IP; each admin can log you.
- The same person may use different handles on different instances — combine with handle variations.

## Overlaps ("do both")
- Pairs with general username enumerators ([[user-scanner]], Sherlock) and manual Mastodon search — those cover centralized sites; this covers the decentralized Fediverse they ignore.

## Trust & verifiability
`trust: community` — open-source and inspectable; results (existence on a server) are reliable where checked, but coverage is bounded, so treat a null result as "not found in the known set," not "doesn't exist."

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fediverse-osint |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
