---
id: twiangulate-analyzing-the-connections-between-friends-and-followers
name: 'Twiangulate: analyzing the connections between friends and followers'
description: Use when you have two or more Twitter/X `username`s and want to find their mutual friends/followers and shared network — returns associate, social-profile. Likely degraded by X API lockdown.
url: http://twiangulate.com/search/
category: social-networks
path:
- social-networks
bestFor: Finding mutual connections and overlapping networks between Twitter/X accounts.
selectorsIn:
- username
selectorsOut:
- associate
- social-profile
status: degraded
pricing: freemium
costNote: Free to use; some analyses gated behind sign-in. No payment, but functionality now depends on X API access.
opsec: active
opsecNote: Requires "Sign in with Twitter", which authorises the app against YOUR X account and ties queries to it — not anonymous. Use a sock-puppet X account, never your real one, and revoke the app's access afterward.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running third-party network-analysis site (since 2009); genuine, but wholly dependent on Twitter/X API access, which has been heavily restricted — treat current functionality as unreliable until confirmed live.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: false
aliases:
- Twiangulate
tags:
- twitter
- network-analysis
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# Twiangulate

> A veteran Twitter/X network-analysis tool that finds the mutual friends and followers linking two accounts — powerful for mapping relationships, but at the mercy of X's locked-down API.

## When to use
You have two (or more) Twitter/X `username`s — say a subject and a suspected associate — and want to know who they both follow or who follows both, i.e. the overlap that reveals a shared social circle (`associate`). Also useful to characterise a single account's network. Reach for it when relationship-mapping on X matters — but verify it still returns data first, given API restrictions.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://twiangulate.com/search/ in a sock-puppet browser.
2. Sign in with a **throwaway** X account when prompted (the tool needs API authorisation).
3. Enter two handles to compare; run the mutual-friends / mutual-followers analysis (or a single-account network view).
4. Read the overlap list — accounts common to both — as candidate `associate`s and `social-profile` leads.
5. If it errors, returns nothing, or refuses to authorise (the likely degraded state under X API limits), fall back to manual following/followers review or another network tool.
6. Pivot: shared connections feed relationship mapping and further per-account OSINT.

## Inputs → Outputs
- **In:** two or more `username`s (Twitter/X handles)
- **Out:** `associate` (mutual friends/followers), `social-profile` (the overlapping accounts)
- **Empty/negative result looks like:** empty overlap, an API/error message, or a failed sign-in — increasingly likely due to X API restrictions rather than a genuine "no shared connections".

## Gotchas & OpSec
- Degraded risk: built on the Twitter/X API, which is now heavily rate-limited/paywalled — confirm it actually returns data before relying on it.
- OpSec (active): requires OAuth to an X account; use a sock puppet and revoke access after.
- Private/protected accounts won't expose their connections.

## Overlaps ("do both")
- Pairs with manual followers/following review and other X network-mapping tools — cross-check any overlap, since API gaps can make Twiangulate's list incomplete.

## Trust & verifiability
`trust: community` — an established, genuine tool, but its output is only as complete as the X API currently allows; treat gaps as tool/API limitations, not confirmed absence of a connection.
