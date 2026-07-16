---
id: facebook-email-reverse-lookup
name: Facebook Email Reverse Lookup (technique)
description: Use when you have an `email` and want to find the linked Facebook account — a technique using login/recovery and search, now heavily limited by privacy settings — returns a social-profile and name.
url: https://osint.support/chrome-extensions/2019/09/01/facebook-email-reverse-lookup.html
category: social-networks
path:
- social-networks
bestFor: Attempting to resolve an email address to a Facebook profile via the search bar and password-recovery flow — works only when the account allows lookup by email.
selectorsIn:
- email
selectorsOut:
- social-profile
- name
status: degraded
pricing: free
costNote: Free technique/guide; no tool to buy. The referenced 2019 Chrome extension approach is largely obsolete after Facebook removed bulk email search.
opsec: active
opsecNote: The password-recovery path touches Facebook's auth system for the target's email and, if pushed past the lookup step, can send a security alert to the account owner. Do the lookup only, from a sock-puppet Facebook account on a clean browser; never advance an actual reset.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Community technique documented on osint.support (2019); Facebook has since closed most email-based discovery, so success is now the exception, gated by the target's privacy settings.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
aliases:
- Facebook email lookup
- FB reverse email
tags:
- facebook
- email
- reverse-lookup
- technique
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- facebook-entity-id-parser
- facebook-friends-list-generator
- facebook-profile-id-grabber
- linkedin-email-reverse-lookup
- osint-and-socmint-tooling
---

# Facebook Email Reverse Lookup (technique)

> A technique (not a live tool) for turning an email into a Facebook profile — via the search bar and the password-recovery flow. Once easy, now heavily curtailed by Facebook's privacy changes.

## When to use
You have an `email` and want to know whether it's tied to a Facebook account, and if so, whose. This used to be a reliable email→profile pivot; Facebook has since restricted it, so today it works only when the target left "Who can look you up using your email" open, or when the recovery flow leaks a masked name/photo. Try it as one option among several, expecting it to fail more often than it succeeds.

## How to use it (`bestInteractionPattern`: web-manual)
1. From a sock-puppet Facebook account, paste the `email` into Facebook's search bar — if the owner allows email lookup, the profile may appear.
2. Alternatively, start the **password-recovery** flow at facebook.com with the email: if an account exists and lookup is permitted, Facebook may show a masked name and/or profile photo tied to it.
3. **Stop at the lookup** — do not request or enter a reset code, which alerts the owner.
4. Record any revealed name/photo (`name`, `social-profile`) and confirm via the profile.
5. Pivot: a confirmed profile feeds full Facebook OSINT (`[[facebook-matrix-2]]`); a masked name narrows other searches.

## Inputs → Outputs
- **In:** `email`
- **Out:** `social-profile` (linked Facebook account, if discoverable), `name` (possibly masked in recovery)
- **Empty/negative result looks like:** no account shown / "no search results" — usually because the owner disabled email lookup, NOT proof the email has no Facebook account. Treat negatives as inconclusive.

## Gotchas & OpSec
- **Largely obsolete:** the old bulk/extension methods are dead; success now depends entirely on the target's privacy settings.
- **Active:** the recovery path touches Facebook's auth for the target's email — never advance past the lookup, and use a puppet account.
- Masked hints are partial; treat revealed characters as leads.

## Overlaps ("do both")
- Pairs with `[[account-live-com]]`-style existence checks and email-OSINT tools like `[[buster]]` — cross-check whether the email is tied to other platforms; several weak signals together beat one uncertain Facebook lookup.

## Trust & verifiability
`trust: community` — a documented but now-degraded technique; any hit must be confirmed on the actual profile, and negatives should not be trusted as absence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facebook-email-reverse-lookup |
| category | social-networks |
| selectorsIn → selectorsOut | email → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
