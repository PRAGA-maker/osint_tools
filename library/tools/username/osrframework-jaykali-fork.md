---
id: osrframework-jaykali-fork
name: OSRFramework (jaykali fork)
description: Use when you have a `username`, `email`, `phone` or `domain` and want a multi-module CLI to enumerate accounts and registrations — returns `social-profile`, `email`, `domain` leads.
url: https://github.com/jaykali/osrframework
category: username
path:
- username
bestFor: Classic multi-utility OSINT suite (usufy/mailfy/searchfy/phonefy/domainfy) for username, email, name, phone and domain enumeration.
selectorsIn:
- username
- email
- domain
- phone
selectorsOut:
- social-profile
- email
- domain
status: degraded
pricing: free
costNote: Free and open source; install via pip/from source. No account. Note it is aging — several provider modules (notably mailfy and some usufy sites) are known to be partially broken.
opsec: active
opsecNote: usufy probes each target site directly to test a username (like Sherlock), and phonefy/domainfy hit third-party services — these touch platforms, not the subject. Run behind Tor/proxy for sensitive work. mailfy historically queried breach/registration services; treat those queries as logged.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Fork of the well-known i3visio OSRFramework; the original is largely unmaintained and bit-rotted, so expect broken modules — still useful where its providers remain live.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- osrframework
- usufy
- mailfy
- searchfy
tags:
- username
- email
- domain
- i3visio
source: gh-topic-osint-framework
lastVerified: '2026-07-10'
enrichment: full
---

# OSRFramework (jaykali fork)

> The classic i3visio OSINT suite — usufy, mailfy, searchfy, phonefy, domainfy — bundled as one CLI. Powerful in concept, but aging: run it, and expect some modules to be dead.

## When to use
You have a `username`, `email`, full `name`, `phone`, or `domain` and want to run several enumeration strategies from one tool rather than stitching together single-purpose scripts. usufy spreads a username across sites; searchfy hunts a full name; mailfy/phonefy/domainfy work emails, phones, and domains. Reach for it when you want breadth in one pass — but pair it with a live tool, because its providers have decayed.

## How to use it (`bestInteractionPattern`: cli)
1. Install from the fork: clone `github.com/jaykali/osrframework` (or `pip install osrframework`) and its dependencies.
2. Pick a module:
   - `usufy -n <username>` — username across sites → `social-profile` URLs
   - `searchfy -q "<full name>"` — name → profiles
   - `mailfy -m <email>` — email registration/leak checks
   - `phonefy -n <phone>` / `domainfy -n <domain>` — phone/domain leads
3. Run behind Tor/proxy for sensitive subjects.
4. Read results, discarding modules that error out (bit-rot is common).
5. Pivot: cross-check hits with `[[sherlock]]` / `[[namechk]]`; feed profiles to reverse-image/manual review.

## Inputs → Outputs
- **In:** `username`, `email`, `domain`, `phone`, or a full `name`
- **Out:** `social-profile` URLs (usufy/searchfy), `email`/registration signals (mailfy), `domain` leads (domainfy)
- **Empty/negative result looks like:** module errors, timeouts, or empty tables — often a dead provider rather than a true negative. Confirm with a currently-maintained tool before concluding "not found."

## Gotchas & OpSec
- Human-in-the-loop: none to run; you must sift live vs broken modules.
- OpSec: **active** — usufy/phonefy/domainfy touch third-party sites/services. Use Tor/proxy; assume queries are logged.
- **Staleness:** the framework is largely unmaintained (`status: degraded`). Never treat its silence as proof of absence.

## Overlaps ("do both")
- Pairs with `[[sherlock]]` and `[[namechk]]` — OSRFramework adds email/phone/domain angles; the others give fresher, better-maintained username coverage.

## Trust & verifiability
`trust: community` — a respected but aging open-source suite (fork of i3visio). Corroborate every result with a live source; assume some modules no longer work.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osrframework-jaykali-fork |
| category | username |
| selectorsIn → selectorsOut | username, email, domain, phone → social-profile, email, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
