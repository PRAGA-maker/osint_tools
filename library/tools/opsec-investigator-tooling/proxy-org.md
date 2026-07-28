---
id: proxy-org
name: Proxy.org
description: Use when you need a fresh web proxy to view a target's content from a non-attributable address — an investigator OpSec directory, not a lookup on a subject.
url: http://proxy.org
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A continuously-updated directory of thousands of public web proxies for disposable, low-attribution browsing.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free directory; the listed proxies are third-party and free to use.
opsec: active
opsecNote: Public proxies are run by unknown operators who can log, inject, or alter everything you route through them — never send credentials, logins, or sensitive case data over one. Treat them as burner viewing paths only; for real anonymity use Tor or a vetted VPN, not a random public proxy.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Proxy.org itself is a stable directory, but the proxies it lists are untrusted third parties of unknown provenance.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- proxy.org
tags:
- toddington
- curated-directory
- proxy-servers-online-privacy-security-tools
- opsec
source: toddington-resources
lastVerified: '2026-07-28'
enrichment: full
---

# Proxy.org

> A large, frequently-updated index of public web proxies — a quick way to grab a throwaway browsing path, with the heavy caveat that every listed proxy is run by a stranger.

## When to use
You want to load a target's page, profile, or a geo-restricted site from an address that isn't yours, and you don't have (or don't want to burn) a dedicated VPN/Tor circuit for it. Proxy.org lists thousands of public web proxies you can pick from. This protects the investigator's origin for passive viewing; it returns no data about any subject. It is a convenience/low-attribution tool, not a real anonymity solution.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://proxy.org and browse the directory (it advertises tens of thousands of tracked proxies, refreshed every ~10 minutes).
2. Pick a proxy — ideally one supporting HTTPS and in a region that fits your need.
3. Use that proxy to open the target URL (through the proxy's own web form, or by configuring it in a disposable browser profile).
4. View the target content; rotate to a different proxy if one is slow, dead, or blocked.
5. Discard — don't reuse the same public proxy for anything that could correlate your activity.

## Inputs → Outputs
- **In:** none (you choose a proxy; you supply nothing about a target)
- **Out:** a working third-party web proxy / low-attribution viewing path (not a harvested selector)
- **Empty/negative result looks like:** a chosen proxy times out, throws certificate warnings, or is itself blocked by the target — normal for public proxies; pick another.

## Gotchas & OpSec
- OpSec: **active/high-risk** — public proxy operators see your traffic in the clear and can log or tamper with it. Never authenticate, log in, or transmit sensitive data through one.
- For genuine anonymity or anything evidentiary, use Tor or a reputable VPN; a random public proxy is disposable viewing only.
- Many listed proxies are dead or malicious at any given time; expect to try several.

## Overlaps ("do both")
- Use alongside Tor and VPN tooling in this category: Proxy.org is the quick-and-dirty option, while Tor/VPN provide the real anonymity for higher-stakes browsing.

## Trust & verifiability
`trust: unverified` — the directory is stable and long-running, but it is only a listing; the proxies themselves are unvetted third parties. Trust the index, not the endpoints.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | proxy-org |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
