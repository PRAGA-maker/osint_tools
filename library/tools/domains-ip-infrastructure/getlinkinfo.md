---
id: getlinkinfo
name: GetLinkInfo
description: Use when you have a shortened or suspicious URL and want to see where it really leads without clicking it — returns the expanded destination, page title/description, and a safety check.
url: http://www.getlinkinfo.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Safely expanding a short/obfuscated link to reveal its true destination, page metadata, and outbound links.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free web tool; no account. Paste a link and it resolves it server-side.
opsec: passive
opsecNote: GetLinkInfo fetches the link from ITS server, not yours — so your IP and browser never touch the destination, which is the whole point for a suspicious URL. The trade-off: you disclose the URL to GetLinkInfo. Don't submit links that themselves contain private tokens/session IDs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A simple, long-standing URL-expander service; it reports the destination and a Google Safe Browsing check, but it is a third-party convenience tool, not an authoritative scanner.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- unshorten-link
- urlscan-io
aliases:
- GetLinkInfo
- getlinkinfo.com
tags:
- url-expander
- unshortener
- link-safety
source: sinwindie-osint
lastVerified: '2026-07-29'
enrichment: full
---

# GetLinkInfo

> A server-side URL expander: paste a short or sketchy link and it tells you the real destination, the page's title/description, its outbound links, and a Safe Browsing verdict — without you ever clicking it.

## When to use
You have a shortened (`bit.ly`, `t.co`, etc.) or otherwise obfuscated URL — from a profile bio, a message, a dark-web listing — and need to know where it goes before exposing your machine to it. GetLinkInfo resolves the chain on its own server and reports the final `domain`, so you can triage a link safely and decide whether it's worth a hardened visit. Good first step for any untrusted link.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.getlinkinfo.com/.
2. Paste the short/suspicious URL and submit.
3. Read the report: the expanded final URL/`domain`, page title and starting description, external links on the page, and the Google Safe Browsing safety check.
4. Decide: benign → note the destination; suspicious → inspect further in a sandbox (e.g. `[[urlscan-io]]`) rather than a real browser.
5. Pivot: the revealed `domain` feeds your normal domain/infra OSINT.

## Inputs → Outputs
- **In:** a URL (`domain`), typically shortened/obfuscated
- **Out:** expanded destination `domain`, page title/description, outbound links, Safe Browsing verdict
- **Empty/negative result looks like:** the expander can't resolve it (dead link, login wall, or an unsupported shortener) — try `[[unshorten-link]]` or a full sandbox fetch.

## Gotchas & OpSec
- **You disclose the URL to GetLinkInfo** — fine for public short links, not for URLs carrying private tokens/session IDs.
- Safe Browsing check is a signal, not a guarantee — a "clean" verdict doesn't make a link safe to interact with.
- OpSec: **passive** and protective — your IP never hits the destination.

## Overlaps ("do both")
- Pairs with `[[urlscan-io]]` and `[[unshorten-link]]` — GetLinkInfo is the quick "where does this go + is it flagged" check; urlscan.io does a deeper sandboxed capture (screenshot, requests, indicators) when a link looks worth investigating.

## Trust & verifiability
`trust: community` — a straightforward, established convenience tool; the expanded URL is verifiable, but treat its safety verdict as one input, not a clearance.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | getlinkinfo |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
