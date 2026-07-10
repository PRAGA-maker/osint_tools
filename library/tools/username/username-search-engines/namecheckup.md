---
id: namecheckup
name: NameCheckup
description: Use when you have a `username` and want to see which platforms and domains it is taken on — returns a per-platform available/taken map that reveals where accounts exist.
url: https://namecheckup.com/
category: username
path:
- username
- username-search-engines
bestFor: Fast side-by-side check of a username across many social platforms and domain extensions to find where the handle is already registered.
selectorsIn:
- username
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Completely free; no account required and it states it does not collect personal data on search.
opsec: passive
opsecNote: Checks run through NameCheckup's servers, not from your IP against each platform, and the target is not notified. Still treat the handle as sensitive and work from a research context.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party availability checker built for brand/handle registration. Reliable as a quick "taken vs free" signal, but confirm each "taken" by visiting the actual profile.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- socialscan
aliases:
- namecheckup.com
tags:
- username
- handle-check
- account-existence
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# NameCheckup

> A username/domain availability checker, read backwards for OSINT: "taken" means an account exists there — a fast map of where a handle is in use.

## When to use
You have a candidate `username` and want a quick, no-install overview of which platforms and domains it is registered on. It's marketed for people picking a brand handle, but for investigation the signal you care about is the *red/taken* results — each one is a live account to go inspect. Good as a fast first pass before running heavier tools.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://namecheckup.com/ and enter the `username`.
2. Read the color-coded grid: green = available (no account), red = taken (account exists), grey = invalid for that platform's rules.
3. Focus on the **red/taken** platforms (Instagram, TikTok, X, YouTube, etc.) and the matching domains (.com/.net/.io).
4. Visit each taken profile to confirm it's your subject (handles get reused by different people).
5. Pivot: confirmed accounts feed platform-specific tools; a registered `domain` feeds WHOIS/domain OSINT.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` existence map across platforms + `domain` availability
- **Empty/negative result looks like:** everything green (nothing registered). That can mean the handle is genuinely unused, or that the subject uses variants — try adding/removing separators, numbers, or common suffixes.

## Gotchas & OpSec
- "Taken" ≠ "your subject" — the same handle on different platforms can belong to different people; always verify by visiting.
- Platform list is fixed; it won't cover niche sites.
- Availability logic can lag platform changes — spot-check surprising results.
- OpSec: passive; checks are server-side and the subject isn't notified.

## Overlaps ("do both")
- Pairs with `[[socialscan]]` — NameCheckup is a zero-install web grid across major platforms and domains; socialscan gives endpoint-accurate CLI checks with fewer false positives. Use NameCheckup to triage, socialscan to confirm.

## Trust & verifiability
`trust: unverified` — a third-party availability tool. Its "taken/free" signal is a reliable starting point, but every "taken" must be confirmed by opening the actual profile before you attribute it to your subject.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | namecheckup |
</content>
