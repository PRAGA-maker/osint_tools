---
id: username-checker-2
name: CheckUser.org Username Checker
description: Use when you have a username and want to see which social platforms it exists on — returns per-platform availability/existence across 70+ sites with direct profile links.
url: https://checkuser.org/
category: username
path:
- username
bestFor: Fast triage of one username across 70+ social platforms to find where a subject has accounts.
selectorsIn:
- username
selectorsOut:
- username
- social-profile
status: live
pricing: freemium
costNote: Free, no signup required for the core check.
opsec: passive
opsecNote: CheckUser queries each platform (or its own index) to test whether the handle exists; the target account is not notified, but the checks originate from CheckUser's infrastructure or your browser. Use a sock-puppet/VPN for sensitive handles, and verify hits manually rather than trusting the availability label alone.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A free web username-availability checker; convenient for breadth, but "available/taken" labels can be wrong for sites that soft-fail, so confirm the actual profile.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- CheckUser
- checkuser.org
- username availability checker
tags:
- username
- username-enumeration
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# CheckUser.org Username Checker

> A no-signup web checker that tests one handle across 70+ platforms at once — a quick way to see where a subject reused a username before you dig into each account.

## When to use
You have a `username` and want a fast, browser-based sweep of where it exists — Facebook, Twitter/X, Instagram, TikTok and 70+ more — without installing an enumerator like Sherlock/`[[sultan-username-search-tool-builder]]`. It's the low-friction first pass: run the handle, note the "taken" platforms (those are candidate accounts), then open and verify each one.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://checkuser.org/ in a sock-puppet browser.
2. Enter the `username` (min 3 characters, no spaces).
3. Read the per-platform grid: "taken/exists" flags candidate accounts, "available" suggests no account — each with a confidence label and a direct profile link.
4. Open the "taken" results to confirm the profile is really your subject (the label is a hint, not proof).
5. Pivot: each confirmed `social-profile` feeds the platform's own tools; consistent avatars/bios across platforms strengthen attribution.

## Inputs → Outputs
- **In:** a single `username`
- **Out:** per-platform existence/availability plus `social-profile` links to the "taken" accounts
- **Empty/negative result looks like:** everything shows "available" (handle unused anywhere) or a spread of soft-fails. Web checkers are prone to false "available" (site blocked the check) and false "taken" (soft-200 pages) — always open the links to verify.

## Gotchas & OpSec
- Availability labels are heuristic: platforms that rate-limit or soft-fail produce both false negatives and false positives — verify every hit by opening it.
- Same handle ≠ same person; corroborate with avatar, bio and content before attributing accounts to your subject.
- Passive toward the target; still VPN for sensitive handles.

## Overlaps ("do both")
- Pairs with `[[sultan-username-search-tool-builder]]` and Sherlock/WhatsMyName — the CLI enumerators cover different/more sites and let you validate; use the web checker for speed, the CLI for depth.
- Feeds `[[amazon-usernames]]` and other `site:` dorks to pull detail from a confirmed platform.

## Trust & verifiability
`trust: community` — a free convenience checker; good for breadth and speed, but its per-platform verdicts are not authoritative, so confirm each "taken" result against the live profile before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | username-checker-2 |
| category | username |
| selectorsIn → selectorsOut | username → username, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
