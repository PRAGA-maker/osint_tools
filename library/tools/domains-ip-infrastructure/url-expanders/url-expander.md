---
id: url-expander
name: URL Expander
description: Use when you have an opaque shortened link (bit.ly, t.co, tinyurl, etc.) and want its true destination without clicking — returns the expanded `domain`/URL and the redirect chain.
url: https://urlex.org/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- url-expanders
bestFor: Safely revealing where a short link actually points before you visit it.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free web service, limited to ~100 lookups/day; no account.
opsec: passive
opsecNote: urlex.org fetches the redirect on your behalf, so the destination server sees urlex's request, not your IP — this is the safe way to resolve a suspicious link. Do not paste a one-time/tracking short link you don't want a third party to log and follow.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Long-running (since 2011) single-operator utility; reputable and SafeBrowsing-clean, but a third party you are trusting to fetch on your behalf.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- urlex-modified-url-expander
aliases:
- urlex.org
- Urlex
tags:
- url-expander
- link-safety
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# URL Expander

> A safe unshortener: paste a short link and see its real destination and redirect chain without your browser ever touching the target.

## When to use
Your subject posted, sent, or was sent a shortened link (bit.ly, t.co, tinyurl, goo.gl-style) and you need to know where it really goes — a profile, a scam site, a tracking pixel — before you (and your real IP) load it. Expanding first both protects you and reveals a real `domain` you can then investigate.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://urlex.org/.
2. Paste the shortened URL and submit.
3. Read the expanded destination and the full redirect chain (a short link often hops through several intermediaries).
4. Pivot: take the final `domain` into WHOIS / reputation (`[[url-void]]`) / reverse-IP tooling; note any tracking-parameter or intermediary that itself identifies a service.

## Inputs → Outputs
- **In:** a shortened URL (`domain`)
- **Out:** the expanded final URL/`domain` plus each redirect hop
- **Empty/negative result looks like:** an error or a link that resolves to itself — the shortener is dead, the target was removed, or the service is rate-limited (100/day cap).

## Gotchas & OpSec
- Passive for you — urlex does the fetching; that is the whole point for suspicious links.
- Some links serve different destinations based on IP/user-agent/one-time use, so what urlex sees may differ from what the intended victim saw.
- The daily cap (~100) limits bulk use; for volume, script an unshortener yourself.

## Overlaps ("do both")
- Pairs with `[[urlex-modified-url-expander]]` (same family) and hand the resolved domain to `[[url-void]]` for a reputation check.

## Trust & verifiability
`trust: unverified` — a long-lived, SafeBrowsing-clean utility, but you are trusting a third party to fetch and report the destination; for high-stakes links, confirm with a second unshortener or an isolated sandbox.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | url-expander |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
