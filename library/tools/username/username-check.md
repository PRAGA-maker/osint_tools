---
id: username-check
name: Username Check
description: Use when you have a `username` and want to see which sites/social platforms it is registered on — returns candidate `social-profile` links across many services.
url: http://www.usernamecheck.com
category: username
path:
- username
bestFor: A fast, no-login sweep of one handle across dozens of social and web platforms.
selectorsIn:
- username
selectorsOut:
- social-profile
- name
status: degraded
pricing: free
costNote: Free, no account required.
opsec: passive
opsecNote: The tool queries each platform on your behalf; the target is not notified. It does, however, make live requests to many sites — run it from a sock-puppet browser/IP rather than an attributable connection.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party availability checker; results can lag reality (false "available"/"taken") and the service has shown intermittent downtime — verify each hit manually.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- usernamecheck.com
tags:
- username
- enumeration
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# Username Check

> A classic bulk username-availability checker: type one handle, see the platforms where it is already taken — each "taken" is a candidate account to open and confirm.

## When to use
You have a `username` and want a quick, unauthenticated fan-out across many social/web platforms to find where that exact handle exists. It is a triage tool for the start of a username investigation. Reliability is uneven and the domain has shown downtime (`status: degraded`), so treat a non-response as a tool problem and fall back to a maintained alternative rather than concluding the handle is unused.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.usernamecheck.com and enter the target `username`.
2. Wait for the grid to populate — "taken/registered" markers indicate the handle exists on that site.
3. For each hit, open the platform's profile URL directly and confirm it is the same person (avatar, bio, activity) — availability checkers produce false positives/negatives.
4. Pivot: confirmed profiles feed name/photo extraction; the whole result set feeds a link-analysis of the subject's footprint.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` candidates across platforms, sometimes a public `name` from the confirmed profiles
- **Empty/negative result looks like:** all-clear/"available everywhere" or a stalled grid — with an aging checker this often means throttling or downtime, not genuine absence.

## Gotchas & OpSec
- Availability ≠ identity: a "taken" handle may belong to a different person; always open and confirm.
- Site lists on legacy checkers go stale — missing platforms are blind spots, not clearances.
- Prefer a maintained tool for authoritative sweeps and use this as a second opinion.

## Overlaps ("do both")
- Pairs with `[[whatsmyname]]` and Sherlock/Maigret-style tools — the maintained enumerators cover far more current platforms, while this offers a quick browser check with no install.

## Trust & verifiability
`trust: unverified` — an anonymous third-party checker with intermittent reliability; never attribute an account from its output alone, always verify on the platform itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | username-check |
| category | username |
| selectorsIn → selectorsOut | username → social-profile, name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
