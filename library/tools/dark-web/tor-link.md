---
id: tor-link
name: tor.link
description: Use when you have a `username`/`email`/keyword and want to find related Tor `.onion` sites via a clearnet darknet directory/search — returns dark-web `social-profile`/site leads.
url: https://tor.link/
category: dark-web
path:
- dark-web
bestFor: A clearnet-accessible darknet search engine and categorized directory of .onion markets, forums, and services.
selectorsIn:
- username
- email
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to browse and search; no account.
opsec: active
opsecNote: The index is browsable on the clearnet from tor.link, but acting on any result means opening a .onion address — do that only in Tor Browser on an isolated VM (Tails/Whonix). The directory lists many illicit markets/services; treat listings as untrusted and screen for legality before opening. Searching from your real IP/browser is attributable to tor.link and its ad partners; use sock-puppet egress.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: unverified
trustNote: An anonymous community-run darknet directory; link accuracy is not vetted and phishing clones of listed sites are common — cross-check onion addresses against trusted sources.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- tor.link darknet search
tags:
- darkweb
- Dark Web Links
- onion-directory
source: uk-osint
lastVerified: '2026-07-29'
enrichment: full
---

# tor.link

> A clearnet-accessible darknet search engine and categorized .onion directory — a starting index for locating dark-web markets, forums, and services tied to a subject.

## When to use
You need to check whether a `username`, `email`, handle, or keyword surfaces on Tor hidden services and want a clearnet index to find candidate .onion destinations without first knowing their addresses. tor.link groups entries into markets, vendors, forums, and directories, so it is a discovery layer before you pivot into Tor.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://tor.link/ on the clearnet (sock-puppet browser/egress) and use its search or category listings.
2. Query your `username`/`email`/keyword, or browse the relevant category (e.g. forums) for candidate onion sites.
3. Copy candidate `.onion` addresses — do NOT act on them yet.
4. Switch to Tor Browser on an isolated VM to actually visit and verify the sites, manually screening each for phishing clones and legality.
5. Pivot: a confirmed forum/marketplace presence feeds breach-data and username-correlation work.

## Inputs → Outputs
- **In:** `username` / `email` / keyword
- **Out:** candidate `.onion` links, categorized darknet `social-profile`/site leads
- **Empty/negative result looks like:** no indexed onion hits — meaning nothing in tor.link's (partial) index matches, not proof of no dark-web presence.

## Gotchas & OpSec
- **Untrusted listings:** the directory is unvetted and riddled with phishing mirrors of real onion sites; verify addresses against a second trusted index before trusting any.
- **Active** once you follow a link into Tor — never open listed onions in a normal browser or attributable environment.
- Legal risk: many listings are illicit; only access material appropriate to your authorized scope.

## Overlaps ("do both")
- Pairs with `[[onion-search-engine]]` and the osint.me dark-web link lists (`[[osint-me-1]]`) — cross-referencing multiple onion indexers is how you both widen coverage and catch phishing clones.

## Trust & verifiability
`trust: unverified` — anonymously operated, unvetted; useful purely as a discovery index, never as an authority on which onion address is genuine.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tor-link |
