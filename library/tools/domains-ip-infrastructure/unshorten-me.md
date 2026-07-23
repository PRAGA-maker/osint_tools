---
id: unshorten-me
name: Unshorten.me
description: Use when you have a shortened link (bit.ly, t.co, goo.gl, tinyurl, etc.) and want to see its real destination without clicking it — returns the expanded `domain`/URL.
url: https://unshorten.me/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Safely revealing where a shortened URL points before you visit it.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free for interactive/manual use; a free-tier API (with an optional API key for higher limits) is available for automation.
opsec: passive
opsecNote: Unshorten.me resolves the redirect server-side, so the destination's server sees Unshorten.me's IP, not yours — a safer way to preview a hostile/tracking link than clicking it. The shortener operator can still see that the link was resolved.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Long-standing free URL-expansion service; reliable for common shorteners, but it's a third party — verify sensitive destinations with a second expander.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- unshorten.me
tags:
- Domain/IP/Links
- URL unshorteners
- redirect
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Unshorten.me

> Server-side URL expander: paste a shortened link and see its true destination without exposing your own browser/IP to it.

## When to use
You have a shortened or obfuscated link — from a message, a social profile, a phishing sample, a QR code — and need to know where it actually leads before visiting. Because Unshorten.me follows the redirect chain on its own servers, you learn the real `domain` and full URL without clicking through and leaking your IP/user-agent to a tracking or malicious endpoint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://unshorten.me.
2. Paste the shortened URL (bit.ly, t.co, goo.gl, ow.ly, tinyurl, fb.me, etc.) and submit.
3. Read the result: the final destination URL, the redirect chain, and often a safety/preview note.
4. For batch/automated use, call the free `/api` endpoint (add an API key for higher rate limits).
5. Pivot: the revealed `domain` feeds WHOIS/hosting lookups and reputation checks; if it's another shortener, expand again.

## Inputs → Outputs
- **In:** a shortened `domain`/URL
- **Out:** the expanded final URL and `domain`, plus the intermediate redirect chain
- **Empty/negative result looks like:** an error or an unchanged URL — the link was dead, not a supported shortener, or already a direct link; try a second expander before concluding.

## Gotchas & OpSec
- Some links cloak based on user-agent/geo, so a server-side expander may see a different destination than a real victim would — treat the result as indicative.
- Don't rely on a single expander for a security-sensitive link; cross-check with another.
- OpSec: passive and protective — resolving here avoids exposing your IP to the destination, but the shortener operator still logs the resolution.

## Overlaps ("do both")
- Pairs with WHOIS/hosting tools in this category — Unshorten.me reveals the destination `domain`, which those tools then attribute to a host, owner and infrastructure.

## Trust & verifiability
`trust: unverified` — a long-running, widely-used free service that reliably expands common shorteners; because it's a third party interpreting redirects, confirm any high-stakes destination with a second tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | unshorten-me |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
