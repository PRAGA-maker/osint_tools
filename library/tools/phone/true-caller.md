---
id: true-caller
name: True Caller
description: Use when you have a `phone` number and want a crowd-sourced caller-ID name, carrier/location hints and spam reputation — returns name, address (region) and social-profile leads.
url: https://www.truecaller.com/
category: phone
path:
- phone
bestFor: Attaching a crowd-sourced name and spam reputation to an unknown phone number.
selectorsIn:
- phone
selectorsOut:
- name
- address
- social-profile
status: live
pricing: freemium
costNote: Free tier requires creating/using a Truecaller account and gives limited lookups; unlimited/detailed search and the "who searched me" data sit behind Truecaller Premium.
opsec: active
opsecNote: Truecaller ties a lookup to YOUR account, and its "who viewed my number" feature can surface that a search happened — so a query is not fully anonymous. Use a dedicated sock-puppet Truecaller account/number, never your real one, and be aware that installing the app uploads your contact book by default (do NOT do this from a real device).
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Large, established caller-ID service, but names are crowd-sourced from users' address books — often an outdated nickname, a business tag, or how one contact saved the number, not a verified legal name.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
aliases:
- Truecaller
tags:
- phone
- caller-id
- reverse-phone
source: arf-seed
lastVerified: '2026-07-14'
enrichment: full
---

# True Caller

> The big crowd-sourced caller-ID database: turn an unknown `phone` number into a likely name and a spam-reputation signal — with real OpSec caveats about attribution and your contact book.

## When to use
You have a `phone` number and need a first-pass identity: a probable owner name, a region/carrier hint, and whether the number is flagged as spam/scam. Best as an early reverse-phone step to get a name to pivot on — corroborate before trusting, because the name is whatever other users saved the number as.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.truecaller.com/ and sign in with a **sock-puppet** Truecaller account (never your real number/identity).
2. Use the web search box to look up the target `phone` in full international format (+country code).
3. Read the result: crowd-sourced `name`/label, region/carrier, and spam/scam tags with report counts.
4. Treat the name as a lead — cross-check against a second reverse-phone source and any `social-profile` the number links to.
5. Pivot: a returned name feeds people-search; a region hint narrows geolocation; spam tags help triage whether the number is personal or a business/robocaller.

## Inputs → Outputs
- **In:** `phone`
- **Out:** crowd-sourced `name`/label, region/carrier `address` hint, spam reputation, occasional `social-profile` link
- **Empty/negative result looks like:** "no name available" / only a location or spam count — the number isn't in enough users' address books, not proof it's unassigned.

## Gotchas & OpSec
- Human-in-the-loop: an account/login is required; free lookups are capped, deeper detail is Premium.
- OpSec (active): lookups tie to your account and can be surfaced to the number's owner ("who searched me"). Use a throwaway account.
- NEVER install the mobile app on a real device — it uploads your contact book, exposing your own network.
- Crowd-sourced names are frequently wrong/outdated — always corroborate.

## Overlaps ("do both")
- Pairs with other reverse-phone lookups (carrier/HLR and social-based) — Truecaller's crowd names and a records-based lookup catch different numbers; run both and reconcile.

## Trust & verifiability
`trust: community` — a large, real service, but the identity data is user-contributed and unverified; a Truecaller name is a strong lead, never a confirmed legal identity.
