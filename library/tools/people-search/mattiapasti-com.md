---
id: mattiapasti-com
name: mattiapasti.com
description: Use when you have a `name` (first + last) and want to sweep many social platforms for matching profiles at once — returns social-profile, username.
url: https://sfinder.mattiapasti.com/
category: people-search
path:
- people-search
bestFor: One-shot cross-platform social-profile search from a person's first and last name.
selectorsIn:
- name
selectorsOut:
- social-profile
- username
status: live
pricing: freemium
costNote: Free tier ("Continua con il limite free") runs searches with a per-session cap; a premium login raises the search limit. No payment needed to start.
opsec: passive
opsecNote: Server-side aggregator — queries run from the tool's infrastructure, not your browser, so the platforms see the tool's requests, not yours, and the subject is not notified. Still run from a sock-puppet session; the operator can log what you search.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: unverified
trustNote: A single-developer OSINT project (Mattia Pasti) with no transparency on data sources or freshness; results are best-effort name matches that need manual confirmation.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Social Finder
- sfinder
tags:
- peoplesearch
- People Search Sites
- social-search
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# mattiapasti.com

> "Social Finder" — a free, name-driven aggregator that fans a first/last name out across many social platforms in one query.

## When to use
You have a subject's `name` (first + last) and want a fast, broad sweep for candidate social-media profiles before you commit to platform-by-platform manual searching. Best as an early net-widening step: it surfaces handles/usernames to then verify by hand.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://sfinder.mattiapasti.com/ (interface is Italian: Nome = first name, Cognome = last name).
2. Enter the `name` and choose "Continua con il limite free" for a free search, or log in for the premium (higher-limit) tier.
3. Run the search and read the results list — candidate profiles flagged valid/invalid across the platforms it checks.
4. Manually open and confirm each hit; a common name will return many false positives.
5. Pivot: take confirmed `username`s/handles into direct profile OSINT and username-enumeration tools.

## Inputs → Outputs
- **In:** `name` (first + last)
- **Out:** `social-profile`, `username` (candidate matches across platforms)
- **Empty/negative result looks like:** "Nessun risultato" / no results displayed — meaning no name match on the platforms it queried, not that the person has no accounts.

## Gotchas & OpSec
- Human-in-the-loop: free tier is rate/limit-capped per session; heavy use needs the premium login.
- Matches are on name string alone — expect noise for common names; verify every hit manually.
- No source/freshness transparency; treat output as leads only.
- OpSec: passive (server-side queries), but the operator sees your searches — use a throwaway session.

## Overlaps ("do both")
- Pairs with [[whatsmyname]] / username-enumeration tools: this finds candidates by *name*, those confirm a *handle* exists across sites — run both and cross-reference.

## Trust & verifiability
`trust: unverified` — an independent single-developer tool with no sourcing transparency; useful for breadth, but every result must be manually confirmed on the source platform.
