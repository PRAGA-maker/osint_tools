---
id: unshorten-it
name: Unshorten.it
description: Use when you have a shortened/obfuscated link and want its true destination safely — expands it server-side and returns the destination `domain` plus a preview and safety rating.
url: https://unshorten.it/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Revealing where a bit.ly/t.co/short link actually goes without clicking it yourself.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free for interactive single-URL expansion; bulk/API access is paid.
opsec: passive
opsecNote: Unshorten.it fetches the link on its own servers, so the destination sees Unshorten.it's IP, not yours — this is the safe way to resolve a hostile/tracking short link. The destination is not directly touched by you, but assume the shortener's operator can see that the link was resolved.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running third-party unshortener; the destination and safety rating are reliable indicators but not a guarantee the target is safe.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
aliases:
- unshorten.it
- URL expander
tags:
- Domain/IP/Links
- URL unshorteners
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
---

# Unshorten.it

> A server-side URL expander — used in OSINT to see where a shortened or obfuscated link really points, and to preview it, without exposing your own IP to the destination.

## When to use
You have a shortened link (`bit.ly`, `t.co`, `tinyurl`, a tracking redirect) from a profile, message or post and need its real destination `domain` before deciding whether to visit. Also useful to strip a link down to its final URL for evidence and to read the safety/reputation signal.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://unshorten.it/.
2. Paste the short URL and submit.
3. Read: the full destination URL/`domain`, a page-title/screenshot preview, and a Web-of-Trust-style safety rating.
4. Pivot: take the destination domain into WHOIS/DNS tools; keep the resolved URL as evidence.

## Inputs → Outputs
- **In:** `domain` (a shortened URL)
- **Out:** destination `domain`/full URL, preview, safety rating
- **Empty/negative result looks like:** it can't resolve (dead short link, or a login/anti-bot wall on the destination) — treat as "unknown," not "safe."

## Gotchas & OpSec
- Some destinations cloak based on user-agent/geo, so the preview may differ from what a real browser would load.
- Multi-hop redirect chains matter for attribution — note every hop, not just the final URL.
- OpSec: this is the safe, passive way to resolve hostile links; never paste the short link into your own browser first.

## Overlaps ("do both")
- Pairs with WHOIS/DNS lookups and a sandboxed browser: this reveals the destination, those characterise and safely open it.

## Trust & verifiability
`trust: community` — a reputable long-standing service; the destination is accurate, but the safety rating is advisory, so still open unknown destinations in isolation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | unshorten-it |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
