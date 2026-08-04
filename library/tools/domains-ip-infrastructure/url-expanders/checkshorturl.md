---
id: checkshorturl
name: CheckShortURL
description: Use when you have a shortened `domain`/link and want its real destination without clicking — returns the expanded URL, page title/preview and reputation flags.
url: https://checkshorturl.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- url-expanders
bestFor: Safely expanding a bit.ly/tinyurl/etc. short link to reveal its true destination before you (or your real IP) touch it.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free, capped at ~120 requests/day; no account required.
opsec: passive
opsecNote: CheckShortURL's server resolves the link, so YOUR IP/browser never hits the destination — important when a short link could be an IP-logger (e.g. Grabify) or malware. Note the destination server sees CheckShortURL's request, not you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A free link-expander that also aggregates third-party reputation (WOT, SiteAdvisor, Norton, Sucuri); the expansion is reliable, the reputation flags are advisory and only as current as those sources.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- checkshorturl.com
tags:
- url-expander
- link-safety
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# CheckShortURL

> A link-expander that resolves a shortened URL server-side to reveal its real destination — so you can see where a `bit.ly`/`tinyurl`/`youtu.be` link goes without your own IP clicking it.

## When to use
Someone (a target, a tip, a suspicious message) has given you a shortened link and you need its true destination before engaging. Clicking directly risks landing on an IP-logger that captures your IP (e.g. `[[grabify]]`) or on malware. CheckShortURL expands the link on its own servers and shows the destination plus a preview and reputation flags — a safe first look that keeps your identity off the target link.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://checkshorturl.com/ and paste the shortened URL.
2. Read the expanded destination URL, page title/description, and any screenshot/preview.
3. Check the aggregated reputation flags (WOT, SiteAdvisor, Norton, Sucuri, etc.) for phishing/malware warnings.
4. Pivot: take the real destination `domain` into WHOIS/DNS and reputation tools; if it looks like an IP-logger, do NOT click it from any attributable browser.

## Inputs → Outputs
- **In:** a shortened `domain`/URL
- **Out:** the expanded destination `domain`/URL, page title/preview, third-party reputation flags
- **Empty/negative result looks like:** the shortener isn't supported, the link is dead/expired, or you hit the ~120/day cap — try another expander or an offline `curl -I` from a sandbox.

## Gotchas & OpSec
- Human-in-the-loop: none; daily request cap applies.
- OpSec: passive for *you* — CheckShortURL fetches the link, so your IP stays off the destination; but the destination server does see CheckShortURL's fetch, and single-use logger links may still record that hit.
- Freshness: reputation flags come from external services and can lag; absence of a warning is not a guarantee of safety.

## Overlaps ("do both")
- Pairs with other URL-expanders and with `[[grabify]]` awareness because a link that expands to a known logger domain is itself the finding — expand first, attribute never.

## Trust & verifiability
`trust: community` — a dependable expander; the destination it returns is verifiable (it's the real redirect target), while the bundled reputation scores are advisory and worth cross-checking.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
