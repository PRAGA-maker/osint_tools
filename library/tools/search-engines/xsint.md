---
id: xsint
name: xsint
description: Use when you have a single `email`, `phone`, `username`, `ip-address`, or `address` and want to fan it out across ~60 services in one command — returns account presence, breach exposure, phone metadata, and geocoded addresses.
url: https://github.com/h1lw/xsint
category: search-engines
path:
- search-engines
bestFor: Quickly pivoting from a single identifier to account-presence hits, breach exposure, phone metadata, and geocoded addresses in one CLI run.
selectorsIn:
- email
- phone
- username
- ip-address
- address
selectorsOut:
- email
- phone
- social-profile
- geolocation
- address
- username
status: live
pricing: free
costNote: Free and open-source (GPL v3). Core modules need no keys; optional modules (HaveIBeenPwned, IntelX, GHunt/Google, GitFive/GitHub, a Telegram breach bot) require you to supply your own accounts or API keys.
opsec: active
opsecNote: Many modules hit third-party auth/recovery endpoints (e.g. Instagram recovery flow, Amazon/Snapchat presence checks) using the target's identifier, which those services can log and may surface to the account owner. xsint supports Tor/Burp proxying — route it through a sock-puppet IP and expect that some checks are intrusive rather than passive.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Open-source Python CLI by GitHub user h1lw (~120 commits, small star count, no tagged releases). Verify module behavior against a known control before relying on results.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- account-live-com
aliases:
- h1lw/xsint
tags:
- aggregator
- account-enumeration
- email-osint
- phone-osint
- username
- breach
- cli
- python
source: xsint
lastVerified: '2026-07-13'
enrichment: full
---

# xsint

> One command that takes an email, phone, username, IP, or address and searches dozens of services for whatever is public about it.

## When to use
You have exactly one selector — an `email`, `phone`, `username`, `ip-address`, or `address` — and want a fast first-pass map of where the subject exists online before committing to slower manual pivots. A single run tells you which of ~60 services the identifier is registered on, whether it appears in known breaches, what a phone's carrier/line-type/timezone are, and where an address geocodes to.

## How to use it (`bestInteractionPattern`: cli)
1. Install on Mac/Linux with Python 3.10+: `curl -fsSL https://raw.githubusercontent.com/h1lw/xsint/main/install.sh | bash`.
2. Run against a selector, optionally type-prefixed to skip auto-detection: `xsint someone@example.com`, `xsint phone:+15551234567`, `xsint user:janedoe`, `xsint addr:"221B Baker St London"`.
3. Read the per-module output: account-presence hits (Spotify, GitHub, Adobe, Pinterest, and ~60 more), masked recovery hints, breach names, phone metadata, and OSM coordinates.
4. Route through Tor/Burp for OPSEC, and add keys for the optional GHunt/GitFive/HIBP/IntelX/Telegram modules if you need those.
5. Pivot: confirmed accounts feed username- and email-specific enrichment; masked recovery hints feed `[[account-live-com]]` and phone-OSINT.

## Inputs → Outputs
- **In:** `email`, `phone`, `username`, `ip-address`, or `address`
- **Out:** `social-profile` / `username` presence, `email` and `phone` recovery hints, `geolocation`, `address`
- **Empty/negative result looks like:** a module reporting "not found" for every service, or a module silently skipped because its API key/login was not configured — absence here is weak evidence, not proof.

## Gotchas & OpSec
- Human-in-the-loop: optional modules will not run without your own accounts/API keys (Google session, GitHub PAT, HIBP, IntelX, Telegram) — the "0 hits" from an unconfigured module is a false negative.
- OpSec: this is **active**. Presence checks and recovery-flow probes touch third-party auth infrastructure with the target's identifier; some services log or alert on this. Proxy it and use throwaway accounts.
- New/small project — cross-check a couple of results against a known-good control before trusting the full sweep.

## Overlaps ("do both")
- Pairs with `[[account-live-com]]` — xsint's Instagram/recovery modules leak masked contacts the same way, but account.live.com is the authoritative first-party oracle for the Microsoft ecosystem specifically.

## Trust & verifiability
`trust: community` — open-source and inspectable, but maintained by a single author with no releases; treat results as leads to verify, not confirmed facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | xsint |
