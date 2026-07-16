---
id: user-search
name: User Search
description: Use when you have a `username` and want to find matching accounts across social networks, plus reverse email/phone leads — returns candidate `social-profile`s and `name` hints to verify.
url: http://www.usersearch.org
category: username
path:
- username
bestFor: Searching one username across many social/dating/forum platforms from a single site.
selectorsIn:
- username
- email
selectorsOut:
- social-profile
- name
status: live
pricing: freemium
costNote: Username lookups across many networks are free. Deeper features — reverse email/phone lookups and some aggregated results — are gated behind paid credits/registration.
opsec: passive
opsecNote: usersearch.org runs the checks server-side against public profiles, so the target's platforms don't see your IP for the enumeration itself. Nothing is sent to the subject. Opening a returned profile does expose your browser to that site — use a sock puppet for follow-through.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing community username/identity search aggregator. It reports candidate matches, not confirmed identities — same username across sites is a lead, not proof of the same person.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- whatsmyname-app
- user-name-search-intel-techniques
- namechk
- username-search
- usersearch-org
aliases:
- usersearch.org
- UserSearch
tags:
- username-check
- account-enumeration
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# User Search

> A username-and-identity search aggregator: enter a handle and it checks it across social networks, dating sites, and forums, with optional (paid) reverse email/phone lookups.

## When to use
You have a `username` (or an `email` to reverse) and want a quick, broad sweep of where that handle exists — including dating and niche platforms that pure code-based checkers often skip. Good early in an identity workup to gather candidate `social-profile`s and any display `name`s attached, which you then manually confirm belong to the same person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.usersearch.org.
2. Enter the target `username` (or use the reverse email/phone option, which may require credits).
3. Run the search; it returns candidate profiles across the platforms it covers.
4. Manually open and vet each hit — confirm photos, bio, and activity tie to your subject before accepting it.
5. Pivot: confirmed profiles feed cross-platform correlation and people-search; corroborate coverage with `[[whatsmyname-app]]` and `[[user-name-search-intel-techniques]]`.

## Inputs → Outputs
- **In:** `username` (or `email` for reverse lookup)
- **Out:** candidate `social-profile`s across many sites, plus `name` leads
- **Empty/negative result looks like:** few or no matches — the handle isn't registered on covered platforms, or is spelled differently. Not proof of no online presence; try variants and other checkers.

## Gotchas & OpSec
- Human-in-the-loop: **manual review** — matches are candidates; a shared username does not prove a shared identity. Verify each.
- OpSec: the enumeration is server-side (passive to platforms), but opening results exposes your browser to those sites — follow through from a sock puppet.
- The deepest features (reverse email/phone) are paywalled; budget or fall back to free alternatives.

## Overlaps ("do both")
- Pairs with `[[whatsmyname-app]]`, `[[user-name-search-intel-techniques]]`, and `[[namechk]]` — each covers a different set of sites (usersearch is notably strong on dating/forum coverage). Run several and merge; no single checker is complete.

## Trust & verifiability
`trust: community` — a useful aggregator whose results are leads, not conclusions. Confirm every candidate profile on the platform itself, and treat username matches as correlation to be verified, not identity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | user-search |
| category | username |
| selectorsIn → selectorsOut | username, email → social-profile, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
