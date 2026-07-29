---
id: osint-me-3
name: OSINT Me – Dark Web Investigations Resources
description: Use when you're starting a dark-web investigation and need a vetted resource list — returns curated tools, methods, and safety guidance for Tor/onion research.
url: https://www.osintme.com/index.php/2022/02/12/darkweb-osint-investigations-resources-for-2022/
category: dark-web
path:
- dark-web
bestFor: A curated reading list of dark-web OSINT tools, onion search engines, and investigative methodology.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free blog article on osintme.com; no account.
opsec: passive
opsecNote: Reading the guide is passive. The dark-web activity it describes is not — follow its safety guidance (isolated VM, Tor, no logins tying to your identity) before touching any onion resource it links.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Published on osintme.com, an established OSINT practitioner blog. A curated 2022 resource roundup — solid as a starting map, but dark-web links rot fast, so verify each before use.
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
- ahmia
- dark-search
- tor-project
- osint-list-of-public-sex-offenders-registers-osintme-com
- osint-me-1
- osint-me-2
- osintme-com
aliases:
- osintme darkweb resources
- OSINT Me dark web guide
tags:
- dark-web
- methodology
- reference
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# OSINT Me – Dark Web Investigations Resources

> A practitioner's curated roundup of dark-web OSINT — the search engines, tools, and safety practices to start Tor/onion research without going in blind.

## When to use
When an investigation extends onto the dark web and you need an orientation: which onion search engines and indexes to use, what tools help monitor marketplaces/forums, and — critically — how to do it safely. Use it as a vetted starting map before you spin up a Tor environment, rather than trawling for links yourself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read the article at the URL for its curated lists and methodology.
2. Note the recommended safety setup (isolated/throwaway VM, Tor Browser, no identity-linking logins) and implement it first.
3. Pick the relevant resources — onion search engines, monitoring tools, reference indexes — and verify each is still live (dark-web links die quickly).
4. Proceed with collection using proper evidence-capture and OpSec discipline.
5. Pivot: onion search engines it names (e.g. `[[ahmia]]`) become your actual query tools; findings feed clearnet corroboration.

## Inputs → Outputs
- **In:** none (a curated reference article)
- **Out:** vetted lists of dark-web tools, onion search engines, and safety/methodology guidance
- **Empty/negative result looks like:** many linked onion resources are dead — expected for a 2022 roundup; use the surviving ones and a current onion search engine to find replacements.

## Gotchas & OpSec
- It's a 2022 snapshot; dark-web resources are especially prone to link rot and takedowns. Treat the list as a starting point, not a current index.
- **Safety first:** never touch onion links from your normal machine/identity. Follow the isolation/Tor guidance before clicking anything.
- Dark-web content can be illegal or harmful; stay within legal scope and your authorisation.

## Overlaps ("do both")
- Pairs with live onion search engines `[[ahmia]]` and `[[dark-search]]` and the `[[tor-project]]` browser — this guide tells you *how and what*; those are the tools you actually run.

## Trust & verifiability
`trust: community` — a reputable practitioner blog's curated guide. Reliable as orientation and method; verify every linked resource's current status and legality before use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-me-3 |
