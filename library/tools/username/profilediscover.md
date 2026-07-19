---
id: profilediscover
name: ProfileDiscover
description: Use when you have a `username` and want the social-media accounts using it across many platforms — returns a report of candidate `social-profile`s found on 400+ networks.
url: https://profilediscover.com/
category: username
path:
- username
bestFor: Fast enumeration of where a single username appears across social networks and communities.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: live
pricing: freemium
costNote: A free report is generated in seconds; deeper/expanded results may be gated or upsold, as is common for hosted username-search sites. The free pass is enough to triage which platforms to check.
opsec: passive
opsecNote: The lookup runs on ProfileDiscover's servers against public data — the target isn't contacted or notified, so it's passive. But you're disclosing the username of interest to a third-party site; use a sock-puppet context and don't submit sensitive selectors you wouldn't share.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A hosted commercial username-search service; results are automated guesses to verify by hand, and coverage/accuracy aren't independently audited. Listed on Michael Bazzell's IntelTechniques tools.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- profilediscover.com
- Profile Discover
tags:
- username
- account-enumeration
source: inteltechniques-tools
lastVerified: '2026-07-19'
enrichment: full
---

# ProfileDiscover

> A hosted username-to-profiles search — enter a handle, get candidate accounts across 400+ networks to check.

## When to use
You have a `username` (from an email prefix, a known handle, a leaked login, another profile) and want to know where else that same handle is used — Facebook, LinkedIn, Instagram, X, TikTok, gaming and community sites. It's a fast first sweep to see which platforms are worth a manual look, before you run a more auditable enumerator.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://profilediscover.com/ and enter the `username`.
2. Run the free report; read the list of platforms where the handle appears to exist.
3. **Manually open and verify each hit** — hosted checkers produce false positives (the account exists but belongs to someone else) and false negatives (missed due to blocking).
4. Confirm identity by cross-matching avatar, bio, real name, and linked accounts across the hits.
5. Pivot: a confirmed profile yields a `name`, other usernames, `associate`s, and posts; feed those into the wider people/social workflow.

## Inputs → Outputs
- **In:** `username`
- **Out:** candidate `social-profile`s / `username` matches across many platforms
- **Empty/negative result looks like:** few or no hits doesn't prove the handle is unused — hosted checkers miss platforms behind logins/anti-bot, and unique handles simply may not be widespread. Cross-run a second tool before concluding absence.

## Gotchas & OpSec
- Human-in-the-loop: none in the tool, but manual verification of every hit is mandatory — treat output as leads, not confirmations.
- You disclose the target username to a third-party site; use a sock puppet and avoid submitting sensitive selectors.
- Coverage and accuracy are unaudited; a hosted "found on 400+ networks" claim is a starting point, not proof.

## Overlaps ("do both")
- Pairs with `[[whatsmyname]]` and Sherlock-style enumerators — ProfileDiscover is a quick hosted sweep; the open-source checkers are auditable and configurable, and running both catches platforms either one misses.

## Trust & verifiability
`trust: community` — a commercial hosted checker with unaudited coverage; every result must be manually opened and identity-confirmed before it counts as a finding.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | profilediscover |
| category | username |
| selectorsIn → selectorsOut | username → social-profile, username |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
