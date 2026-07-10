---
id: quidam
name: Quidam
description: Use when you have an `email` or `username` and want to harvest the masked account-recovery hints that "forgot password" flows leak — returns partial recovery `email`/`phone` and account existence.
url: https://pypi.org/project/quidam/
category: username
path:
- username
bestFor: Automating the "forgot password" recovery-hint leak across multiple sites for one email/username.
selectorsIn:
- email
- username
selectorsOut:
- email
- phone
- social-profile
status: degraded
pricing: free
costNote: Free, open-source (GPLv3) Python package by megadose. No account or key needed.
opsec: active
opsecNote: Each check hits the target account's real password-recovery endpoint on the live site, so the provider may log the attempt and could email/SMS a security alert to the account owner. Run from a sock-puppet IP, and never advance past the hint-disclosure step into an actual reset.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: python-lib
trust: community
trustNote: Authored by megadose (also behind Holehe/GHunt); GPLv3 on GitHub. Last release 1.23 (May 2020), so site-specific selectors have likely rotted.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- account-live-com
- holehe
aliases:
- megadose/Quidam
tags:
- account-existence
- password-recovery
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Quidam

> A Python tool that scripts the "forgot password" flow across sites to scrape the masked recovery hints (partial email/phone) those flows reveal.

## When to use
You have an `email` or `username` and want to confirm which services it is registered on AND capture the partial recovery contacts they expose during account recovery — e.g. a masked secondary `j****@gmail.com` or `+** *** ** 89`. Those masks are pivot leads toward a second address or phone number for the same person.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install: `pip install quidam` (Python 3). Source: https://github.com/megadose/Quidam.
2. Run it against the target `email`/`username` per the repo's README/CLI usage.
3. Read the output per site:
   - EXISTS + hint: the tool reports the account is registered and prints the masked recovery `email`/`phone`.
   - Not found: the address isn't registered on that site.
4. STOP at the hint. Do not trigger or complete an actual password reset — that alerts the owner.
5. Pivot: masked hints feed phone/email OSINT; confirmed registrations feed `[[holehe]]` and per-service tools.

## Inputs → Outputs
- **In:** `email` or `username`
- **Out:** per-site account-exists boolean, masked recovery `email`/`phone` hints
- **Empty/negative result looks like:** every site returns "no account" or errors — treat as unregistered on those sites, not as proof the person has no accounts. Because the tool is from 2020, blanket failures often mean the site changed its recovery flow, not that the account is absent.

## Gotchas & OpSec
- Human-in-the-loop: many recovery flows now gate on CAPTCHA, which the old scripted requests cannot solve — expect breakage.
- OpSec: **active**. You are querying each provider about the target's address; proceeding to a real reset sends a security notification to the owner. Use a sock-puppet IP.
- Staleness: last release 2020. Verify each module still works before trusting a negative.

## Overlaps ("do both")
- Pairs with `[[account-live-com]]` — that is the manual Microsoft-specific version of the same existence-oracle trick; Quidam automates the pattern across more sites.
- Pairs with `[[holehe]]` — Holehe checks registration silently via signup/reset without leaking masks; Quidam additionally surfaces the masked recovery contacts.

## Trust & verifiability
`trust: community` — reputable author (megadose) and open source, but unmaintained since 2020; treat site coverage as partially rotted and re-verify before relying on results.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | quidam |
| category | username |
| selectorsIn → selectorsOut | email, username → email, phone, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | python-lib |
| opsec | active |
| human-in-loop | yes (captcha) |
