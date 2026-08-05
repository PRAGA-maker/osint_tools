---
id: github-danaxscully
name: DanaXScully onion_links (GitLab)
description: Use when you need vetted dark-web entry points and have a target service type — returns a maintained list of `.onion` addresses to reach from Tor.
url: https://gitlab.com/DanaXScully/onion_links
category: dark-web
path:
- dark-web
bestFor: A version-controlled, community-maintained directory of onion links as starting points for dark-web research.
selectorsIn: []
selectorsOut:
- domain
status: live
pricing: free
costNote: Free public GitLab repository; reading the list needs nothing. Visiting the linked services requires Tor.
opsec: active
opsecNote: Reading the repo is passive, but VISITING any listed .onion is active dark-web activity — use Tor Browser in a hardened/VM environment, never log in or transact, and assume many listed services are scams, honeypots, or law-enforcement-monitored. Treat links as leads, not endorsements.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A single-maintainer GitLab repo (created 2025, ~22 commits) curating onion links; being git-versioned makes changes auditable, but the linked sites are unvetted and volatile.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- the-hidden-wiki
- onion-search-engine
- onion-land
aliases:
- DanaXScully onion links
- onion_links gitlab
tags:
- darkweb
- onion-directory
- Dark Web Links
source: uk-osint
lastVerified: '2026-08-05'
enrichment: full
---

# DanaXScully onion_links (GitLab)

> A git-versioned list of `.onion` addresses — a more auditable starting index for dark-web research than the usual SEO listicles, though the destinations are still unvetted.

## When to use
You need entry points into Tor hidden services for a research task — marketplaces, forums, mirrors, search services — and want a curated list you can review by category. Because it's a GitLab repo, its edit history is visible, so you can see when a link was added or removed, unlike a static "top onion links" web page. Use it to find candidate services, then verify each one live.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://gitlab.com/DanaXScully/onion_links and read the README/list (this part is clearnet, passive).
2. Note the `.onion` addresses relevant to your task and the maintainer's notes/last-updated commits.
3. Switch to a hardened Tor setup (Tor Browser in a VM/Tails) and visit the addresses cautiously.
4. Verify each service is what it claims (many onions are dead, cloned, or scams); confirm via a Tor-capable `[[onion-search-engine]]` and cross-reference `[[the-hidden-wiki]]`.
5. STOP at observation — do not create accounts, log in, or transact.

## Inputs → Outputs
- **In:** none (a directory; you bring the need)
- **Out:** `.onion` `domain` addresses to investigate
- **Empty/negative result looks like:** links that fail to resolve in Tor (hidden services churn constantly) or lead to seized/placeholder pages. A dead onion is normal, not evidence of anything.

## Gotchas & OpSec
- **Active dark-web risk:** treat every listed service as potentially a scam, honeypot, or monitored site; browse read-only from an isolated environment.
- Onion addresses rot fast; expect a high dead-link rate and re-verify freshness against the commit history.
- The list is one maintainer's picks — not vetted or endorsed.

## Overlaps ("do both")
- Cross-check against `[[the-hidden-wiki]]` and live dark-web search via `[[onion-search-engine]]` / `[[onion-land]]` — a directory tells you where to look, but a search engine confirms what's currently up.

## Trust & verifiability
`trust: community` — an auditable but unvetted single-maintainer list; the git history lends transparency to the *list*, not legitimacy to the *sites*, so verify each service independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | github-danaxscully |
| category | dark-web |
| selectorsIn → selectorsOut |  → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
