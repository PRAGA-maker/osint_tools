---
id: namechk
name: Namechk
description: Use when you have a `username` (or `domain`) and want to see, in one screen, which platforms it is taken on — returns per-platform availability implying existing `social-profile`s.
url: https://namechk.com/
category: username
path:
- username
- username-search-engines
bestFor: Fast web-based check of a handle's availability across 90+ platforms and domain TLDs.
selectorsIn:
- username
- domain
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free to check usernames and domains; monetised via domain-registration and "brand" upsell links you can ignore.
opsec: passive
opsecNote: Namechk queries the platforms server-side and shows you availability — you never touch the target sites directly, and the subject is not notified. Namechk's own servers see the handles you submit; assume logged. Use a clean browser if the handle itself is sensitive.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running commercial username/domain checker; results are a quick triage signal, not proof of account ownership, and its "available/taken" logic can lag reality.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- namechk.com
tags:
- username
- availability
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Namechk

> A one-page web checker that flags a username as taken or free across 90+ social platforms and domain extensions — a fast triage before deeper enumeration.

## When to use
You have a `username` and want a quick, no-install visual of where it's already registered (a "taken" result implies a `social-profile` you can go read) or you're checking a `domain` a subject might own. It's the lightweight web counterpart to CLI enumerators — good when you can't run tooling, or as a second opinion alongside Sherlock.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://namechk.com/ and type the `username` (or a domain root).
2. Namechk shows a grid of platforms/TLDs marked available (free) or taken.
3. Treat every **taken** social platform as a lead — open that platform's `/username` URL directly to see if it's your subject.
4. Ignore the domain-registration upsells unless you're checking domain ownership.
5. Pivot: confirmed handles feed `[[sherlock]]` for wider coverage, reverse-image on profile pics, and manual review.

## Inputs → Outputs
- **In:** `username` or `domain` root
- **Out:** per-platform availability; "taken" ⇒ an existing `social-profile` to inspect; domain TLD availability
- **Empty/negative result looks like:** everything "available" — the handle is unused (or Namechk's check for those sites is stale). Availability logic can be wrong; verify the important ones by hand.

## Gotchas & OpSec
- Human-in-the-loop: expect **rate-limiting**/anti-bot friction on rapid repeat checks; space out queries.
- OpSec: **passive** — server-side checks, subject not contacted; Namechk logs your queries.
- "Taken" ≠ your subject owns it, and Namechk's platform list/accuracy drifts. Always open the actual profile URL to confirm.

## Overlaps ("do both")
- Pairs with `[[sherlock]]` and `[[osrframework-jaykali-fork]]` — Namechk is the quick web triage; the CLI tools go deeper and cover more sites.

## Trust & verifiability
`trust: community` — a convenient commercial triage tool, not an authority. Confirm any meaningful "taken" result on the live platform before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | namechk |
| category | username |
| selectorsIn → selectorsOut | username, domain → social-profile, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
