---
id: broken-link-checker
name: Broken Link Checker
description: Use when you have a `domain`/page and want to find which of its outbound links are dead — returns the broken links, exposing defunct sites and stale connections.
url: https://chrome.google.com/webstore/detail/broken-link-checker/nibppfobembgfmejpjaaeocbogeonhch
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Spotting dead outbound links on a page to find defunct related sites and datable link-rot.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free Chrome extension; no account.
opsec: passive
opsecNote: To test links the extension sends a request to each linked URL from your browser, so those third-party hosts see your IP. Passive toward your primary subject, but route through a VPN/sock-puppet if you don't want linked hosts logging you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: unverified
trustNote: A generic third-party Chrome extension; it does the mechanical job of checking link status but has no reputation as an investigative tool. Verify permissions before installing.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Chrome Broken Link Checker
tags:
- Domain/IP/Links
- Broken Links Checkers
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Broken Link Checker

> A Chrome extension that highlights the dead links on any page — useful for spotting defunct related sites and dating a page's link-rot.

## When to use
You are on a subject's page (personal site, org page, link hub) and want to know which outbound links are broken. Dead links flag sites that once existed — old profiles, shuttered businesses, moved resources — that you can then chase in an archive. It is a supporting tool: it tells you *what's gone*, not *who* anyone is.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the extension from the Chrome Web Store (review its permissions first).
2. Navigate to the page you want to audit (a subject's site, a link directory, an old bio page).
3. Run the checker — it requests each link and highlights broken (4xx/5xx/dead) ones directly on the page.
4. Note the dead URLs: each is a candidate for archive recovery.
5. Pivot: feed broken URLs into the Wayback Machine / a cache tool to recover the vanished content and any names, handles, or contact details it held.

## Inputs → Outputs
- **In:** `domain` (the page/site being audited)
- **Out:** `domain` (the broken/defunct linked hosts)
- **Empty/negative result looks like:** all links resolve — meaning no link-rot on this page, not that the site has no useful history (check archives regardless).

## Gotchas & OpSec
- Checking links sends live requests to every linked host from your IP; use a VPN/sock-puppet for sensitive audits.
- Being a generic extension, vet its Web Store permissions before installing — link-checkers can request broad host access.
- It confirms a link is dead, not why; the recovery step (archive lookup) is where the intelligence actually comes from.

## Overlaps ("do both")
- Pairs with a web-archive/cache tool — this finds the dead links, the archive tool resurrects what they pointed to.

## Trust & verifiability
`trust: unverified` — a commodity Chrome extension; the link-status result is mechanically checkable, but treat the extension itself with normal third-party caution.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | broken-link-checker |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
