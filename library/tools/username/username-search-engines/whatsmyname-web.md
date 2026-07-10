---
id: whatsmyname-web
name: WhatsMyName (web)
description: Use when you have a `username` and want to find every site it exists on — returns direct profile links across hundreds of social, gaming, forum and professional sites.
url: https://whatsmyname.app/
category: username
path:
- username
- username-search-engines
bestFor: Fast, browser-based username enumeration across 600+ sites with direct links to the profiles that exist.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free, open-source project (Micah Hoffman / OSINT community); no account needed.
opsec: passive
opsecNote: Checks are executed from WhatsMyName's own infrastructure, so target sites see its servers rather than your IP — passive from your side. Still avoid entering anything but the handle, and note the site owner can see your queries.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The de-facto community-standard username enumerator; its site-detection list (wmn-data) is open, widely reviewed and continuously maintained, making it one of the most reliable enumerators available.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- whatsmyname-python
- gosearch
- instant-username
aliases:
- whatsmyname.app
- WMN
tags:
- username
- enumeration
- social-media
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# WhatsMyName (web)

> The browser version of the community-standard username enumerator — type a handle and get direct links to the hundreds of sites where that username exists.

## When to use
You have a `username` and want to map its footprint fast without installing anything. WhatsMyName checks the handle against a large, well-maintained list of sites (social, gaming, forums, dev, professional, adult, niche) and returns the ones where a profile exists. It's the go-to first move whenever a handle is your pivot point — the results become a to-do list of profiles to inspect.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://whatsmyname.app/ and enter the `username`.
2. Let it run; results populate as each site is checked, with direct profile links and category filters.
3. Open each hit and confirm it's your subject (same handle ≠ same person) via bio, photo, or cross-links.
4. For scripting, offline use, or larger runs, use the CLI/library `[[whatsmyname-python]]`.
5. Pivot: confirmed profiles yield names, photos, emails and associates; feed handle variants back through to catch near-matches.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` links across sites where the handle exists (with `username` confirmation)
- **Empty/negative result looks like:** few or no hits — the handle is unused, spelled differently, or the person uses different names per site; absence isn't proof of no presence.

## Gotchas & OpSec
- Same handle can belong to **different people** on different sites — verify each profile individually.
- Site checks can produce occasional false positives/negatives as sites change; the open wmn-data list is updated often, but corroborate important hits.
- OpSec: passive (checks run from WhatsMyName's infra), but the operator sees your queries.

## Overlaps ("do both")
- The web front-end to `[[whatsmyname-python]]`; pair with `[[gosearch]]` and `[[instant-username]]` to cover sites any single list misses. Different enumerators, different coverage — run more than one.

## Trust & verifiability
`trust: trusted` — an open, heavily-reviewed, actively-maintained community standard; still, treat each match as a lead to confirm on the actual platform, since a shared handle doesn't guarantee a shared owner.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whatsmyname-web |
| category | username |
| selectorsIn → selectorsOut | username → social-profile, username |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
