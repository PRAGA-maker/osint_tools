---
id: cupidcr4wl
name: Cupidcr4wl
description: Use when you have a `username` or `phone` and want to check whether the subject appears on dating, hookup, fetish, cam, and adult platforms — returns social-profile hits.
url: https://github.com/OSINTI4L/cupidcr4wl
category: username
path:
- username
bestFor: Checking a handle or phone number against adult/dating/escort platforms the mainstream username tools skip.
selectorsIn:
- username
- phone
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free and open-source. No account or API key required.
opsec: active
opsecNote: The tool queries adult/dating/escort sites directly from your host, so those platforms see your IP. Use a VPN/sock-puppet network. Handle findings with extreme care — adult-platform presence is sensitive, potentially embarrassing data; only pursue it with a legitimate investigative purpose and never expose a subject gratuitously.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source tool by OSINTI4L; results are unverified account matches you must confirm, and adult-site checkers are especially prone to false positives.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
aliases:
- cupidcr4wl
- cc.py
tags:
- username-check
- dating-sites
- adult-platforms
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Cupidcr4wl

> A CLI username/phone crawler aimed squarely at dating, hookup, fetish, cam, and escort sites — the corner of the web general enumerators ignore.

## When to use
You have a `username` or `phone` and need to know whether the subject has a presence on adult-content, dating, or escort platforms — a lead that can matter in missing-persons, trafficking, or welfare cases where a person's alternate life is the thread to pull. Use it to complement mainstream username tools, which deliberately skip this category.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `https://github.com/OSINTI4L/cupidcr4wl` and install requirements (`requests`, `rich`; Python 3.6+).
2. By username: `python3 cc.py -u handle` (comma-separate for several). By phone: `python3 cc.py -p 15551234567`.
3. List supported sites with the tool's list flag; use debug mode to sanity-check accuracy before trusting a run.
4. Read output: it flags platforms where a match was found and can export an HTML report.
5. Verify each hit by opening the profile; then pivot a confirmed handle/photo into reverse-image and cross-platform checks.

## Inputs → Outputs
- **In:** `username`, `phone`
- **Out:** `social-profile` (adult/dating/escort platform hits)
- **Empty/negative result looks like:** no flagged platforms — the identifier wasn't matched. Given how often these sites change, treat a null result as inconclusive, not exculpatory.

## Gotchas & OpSec
- False positives are common on adult sites that serve generic pages; confirm visually.
- OpSec: **active** and **sensitive** — you touch adult platforms directly. VPN/sock-puppet strongly advised, and be disciplined about not over-collecting or exposing embarrassing data.
- Legal/ethical: only run with a clear, lawful investigative basis.

## Overlaps ("do both")
- Pairs with `[[nexfil]]` — NExfil covers mainstream platforms, Cupidcr4wl covers the adult/dating layer NExfil omits, so run both for full username coverage.

## Trust & verifiability
`trust: community` — open source and inspectable, but automated adult-site matching is noisy; every hit is a lead to verify, never a conclusion.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cupidcr4wl |
| category | username |
| selectorsIn → selectorsOut | username, phone → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
