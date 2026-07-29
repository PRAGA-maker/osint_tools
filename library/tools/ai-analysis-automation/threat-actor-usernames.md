---
id: threat-actor-usernames
name: Threat Actor Usernames
description: Use when you have a `username`/alias and want to know if it's a known threat actor and where they operate — returns matching handles and the forums/platforms they use.
url: https://threatactorusernames.com/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Checking a handle against 3M+ scraped threat-actor usernames to see where an alias is active.
selectorsIn:
- username
selectorsOut:
- username
- social-profile
status: live
pricing: free
costNote: Free searchable database and API (by CTI Updates); no paywall noted.
opsec: passive
opsecNote: Searching queries the aggregated database, not the actor's accounts — you don't touch their profiles and nothing is disclosed. Data is scraped from forums/platforms, so treat matches as attribution leads, not confirmed identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community threat-intel project ("threat intel scraped") indexing ~2.8M distinct usernames across forums. Useful for cross-referencing handles; provenance per record varies, so verify at the source platform.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- whatsmyname
- intelx
- dehashed
aliases:
- threatactorusernames.com
- CTI Updates usernames
tags:
- username-search
- threat-intel
- cyber-forums
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Threat Actor Usernames

> A searchable index of 3M+ usernames scraped from cybercrime forums and platforms — check whether a handle belongs to a known threat actor and see where it appears.

## When to use
You have a `username`/alias (from a breach, a forum post, a chat, or another OSINT step) and want to know whether it maps to threat-actor activity and on which forums/platforms it operates. Complements general username-search tools by focusing specifically on the cybercrime/threat-actor ecosystem those tools usually don't cover.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://threatactorusernames.com/ and search the `username`/alias (or use the documented API for automation).
2. Read the matches: the distinct handle(s) and the forums/platforms where they're recorded as active.
3. Cross-check the forum listing directly at the source platform to confirm the account and its activity.
4. Correlate reused handles across platforms to build an actor profile.
5. Pivot: a confirmed handle feeds `[[whatsmyname]]` (broader platform enumeration) and breach tools `[[intelx]]` / `[[dehashed]]` for linked emails/data.

## Inputs → Outputs
- **In:** `username`/alias
- **Out:** matching threat-actor `username`s and the `social-profile`/forum locations where they operate
- **Empty/negative result looks like:** no matches — the handle isn't in the scraped cybercrime dataset (common for ordinary users; the DB is threat-actor-focused). Use general username tools instead.

## Gotchas & OpSec
- Scope is the threat-actor/cybercrime ecosystem — it won't help with ordinary-person username OSINT.
- Scraped data varies in freshness and provenance; a match is an attribution lead to verify at the source, not proof of identity.
- Same-handle ≠ same-person across platforms without corroboration; handles get reused and impersonated.

## Overlaps ("do both")
- Pairs with `[[whatsmyname]]` (enumerates a handle across hundreds of general platforms) and breach tools `[[intelx]]` / `[[dehashed]]`. Do both: this for threat-actor context, WhatsMyName for breadth, breach tools to tie the handle to emails/leaked data.

## Trust & verifiability
`trust: community` — a useful, large community-scraped index. Records are leads, not verdicts; confirm each match at the originating forum/platform before attributing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | threat-actor-usernames |
