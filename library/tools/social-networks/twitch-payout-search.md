---
id: twitch-payout-search
name: Twitch Payout Search
description: Use when you have a Twitch `username` (or streamer `name`) and want to check their subscription earnings from the Oct-2021 Twitch leak — returns a payout figure that corroborates the account and its scale.
url: https://sizeof.cat/project/twitch-payout-search/
category: social-networks
path:
- social-networks
bestFor: Looking up a top-10k Twitch streamer's Aug 2019–Sep 2021 subscription earnings from the leaked payout data.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free, browser-only tool; no account or payment. All data is processed client-side.
opsec: passive
opsecNote: The search runs entirely in your browser against a local copy of the leaked dataset — nothing is uploaded and no query hits Twitch, so the subject gets no signal. Note the data itself is a stolen leak; handling it may carry legal/ethical constraints depending on your jurisdiction and purpose.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Hobby project by sizeof(cat) built on the Oct-2021 Twitch breach; figures match the widely-circulated leak but are not officially confirmed by Twitch.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Twitch leak payout lookup
- sizeof cat twitch payouts
tags:
- social-networks
- financial
- data-breach
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- ransomware-darknet-websites
---

# Twitch Payout Search

> Browser-side search over the leaked Twitch creator-payout report: how much did a given streamer earn from subs between Aug 2019 and Sep 2021?

## When to use
You have a Twitch `username` or streamer `name` and want a financial-scale signal on them — confirmation that the handle appears in the top-10k earners of the October 2021 Twitch breach, plus the leaked cumulative subscription payout. Useful for corroborating that a Twitch identity is real, active, and monetised at a known scale.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://sizeof.cat/project/twitch-payout-search/ in a browser.
2. Type the streamer's Twitch `username` (or display `name`) into the search box.
3. Read the result: a matching row shows the channel and its total leaked subscription payout for the ~two-year window. The dataset is limited to the top ~10,000 earners.
4. Pivot: a confirmed handle feeds a live Twitch profile check via `[[check-channel-badges]]` or general username enumeration; the earnings figure is context, not an identity in itself.

## Inputs → Outputs
- **In:** `username` or `name` (Twitch streamer)
- **Out:** `social-profile` corroboration + leaked subscription payout amount
- **Empty/negative result looks like:** no matching row — the streamer either earned outside the top-10k, streamed under a different handle, or is not in the leak. Absence is not proof they never streamed.

## Gotchas & OpSec
- Only the top ~10,000 earners are included; smaller channels never appear.
- Figures are subscription payouts only for a fixed 2019–2021 window — not lifetime, not total (excludes bits, ads, sponsorships).
- The underlying data is a stolen leak. It runs locally so it is passive, but consider the legal/ethical footing of using breach data for your investigation.

## Overlaps ("do both")
- Pairs with `[[check-channel-badges]]` — that inspects a live Twitch channel's current state, while this adds a historical earnings dimension from the leak.

## Trust & verifiability
`trust: community` — an independent project built on the widely-mirrored Twitch breach; the numbers are consistent with the leak but never officially confirmed, so treat them as approximate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitch-payout-search |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
