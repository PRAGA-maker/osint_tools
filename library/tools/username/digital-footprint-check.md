---
id: digital-footprint-check
name: Digital Footprint Check
description: Use when you have a `username` (or `email`) and want to see which of 500+ platforms it exists on — returns direct `social-profile` links where the handle is registered.
url: https://www.digitalfootprintcheck.com/free-checker.html
category: username
path:
- username
bestFor: Client-side username/email enumeration across 500+ sites using the WhatsMyName dataset.
selectorsIn:
- username
- email
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Completely free; no account. Checks run client-side in your browser.
opsec: passive
opsecNote: The tool states checking is client-side ("zero data sent to our servers"), but your browser still makes requests to each of the 500+ platforms to test the handle — those platforms see your IP. Run from a sock-puppet browser/VPN if you don't want target sites logging the check. It does not notify the account owner.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A front-end over the open-source WhatsMyName database (the community-standard username-enumeration dataset). Results are only as current as WhatsMyName's rules; false positives/negatives occur.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- digitalfootprintcheck.com
- WhatsMyName web checker
tags:
- username-check
- username-enumeration
source: awesome-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Digital Footprint Check

> A browser-based username enumerator built on the WhatsMyName dataset — paste a handle and it returns direct links to every one of 500+ platforms where that username is registered.

## When to use
You have a `username` (or `email`) and want to map where the subject exists online in one pass — social, professional, coding/tech, and creative platforms. This is a classic first move in username OSINT: one handle often reuses across sites, so enumeration builds the account graph you then investigate individually.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.digitalfootprintcheck.com/free-checker.html.
2. Enter the username (or email) and run the check — processing happens in your browser against 500+ platforms.
3. Review the results, grouped by category (Social Media, Professional, Coding/Tech, Creative); it lists only sites where the handle actually exists.
4. Open each hit to confirm it's the same person (avatars, bio, linked accounts) — same handle ≠ same human.
5. Pivot: confirmed profiles feed per-platform OSINT, and cross-linked handles expand the search.

## Inputs → Outputs
- **In:** `username` (or `email`)
- **Out:** direct `social-profile` links on platforms where the handle is registered
- **Empty/negative result looks like:** few or no hits — the handle is uncommon, the person uses different handles per site, or WhatsMyName's rules missed it. Absence on a platform is not proof; verify manually for key sites.

## Gotchas & OpSec
- Same-handle ≠ same-person: common usernames collide across unrelated people — always confirm identity per profile.
- Accuracy depends on the WhatsMyName ruleset; expect occasional false positives (site matched a "not found" page) and false negatives.
- "Client-side" means no central logging by this tool, but the 500+ target sites still see your requests — use a sock-puppet/VPN for sensitive work.

## Overlaps ("do both")
- Overlaps with Sherlock, Maigret and the WhatsMyName CLI (same underlying dataset) — this is the no-install web version; run a CLI tool too for scripting and to cross-check misses.

## Trust & verifiability
`trust: community` — a community front-end over the open WhatsMyName database; reliable as a lead generator but each hit must be manually verified as the same individual.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | digital-footprint-check |
| category | username |
| selectorsIn → selectorsOut | username, email → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
