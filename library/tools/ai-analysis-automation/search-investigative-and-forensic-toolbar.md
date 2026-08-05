---
id: search-investigative-and-forensic-toolbar
name: SEARCH Investigative and Forensic Toolbar
description: Use when you want one-click access to a vetted set of OSINT/forensic lookups — returns a launcher menu into tools for `name`, `phone`, `ip-address`, and `email`.
url: https://chromewebstore.google.com/detail/search-investigative-and/idgjbdfnngdcenpahfalcamfmcjdfbcj
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: A curated browser launcher consolidating dozens of investigative and forensic web tools in one drop-down.
selectorsIn:
- name
- phone
- ip-address
- email
selectorsOut:
- social-profile
- address
status: live
pricing: free
costNote: Free Chrome extension from SEARCH Group, Inc. No account or payment; requires no sensitive permissions.
opsec: passive
opsecNote: The toolbar is just a menu of links — installing and opening it leaks nothing. OpSec depends on the destination tool you click; some (people-search, background checks) are active/attributable, so evaluate each before running it against a target from a sock-puppet profile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: trusted
trustNote: Published by SEARCH Group, Inc. (the National Consortium for Justice Information and Statistics), a US non-profit that trains investigators; a reputable curator, though the linked third-party tools vary in quality.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- awesome-recon-tools
- awesome-screenshot-extension-chrome
aliases:
- SEARCH Toolbar
- SEARCH Investigative and Forensic Toolbar
tags:
- investigator-toolkit
- browser-extension
- launcher
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# SEARCH Investigative and Forensic Toolbar

> A browser drop-down curated by a justice-information non-profit — one click to dozens of investigative and forensic lookups, so you're not hunting for the right site each time.

## When to use
You want a fast, organized launcher for the common lookups an investigation cycles through — reverse phone, IP address lookup, email header tracing, background/people search, curated OSINT lists — without maintaining your own bookmark pile. It doesn't run queries itself; it's a categorized menu that opens the right tool for whichever selector you have in hand.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "SEARCH Investigative and Forensic Toolbar" from the Chrome Web Store in your investigation profile.
2. Click the toolbar icon to open the categorized drop-down (OSINT, phone, IP, email-header, background-check resources, etc.).
3. Pick the tool matching your current selector (`name`/`phone`/`ip-address`/`email`) — it opens that resource in a tab.
4. Run the lookup there; return to the menu for the next step. Evaluate each destination's OpSec before pointing it at a target.

## Inputs → Outputs
- **In:** `name` / `phone` / `ip-address` / `email` (whatever the destination tool consumes)
- **Out:** routes you to tools that return `social-profile`, `address`, IP/email intel — the toolbar itself returns links, the tools return data
- **Empty/negative result looks like:** a linked tool that's dead or has changed — curated lists age, so verify the destination still works and consider `[[awesome-recon-tools]]` for a broader, community-updated menu.

## Gotchas & OpSec
- It's a launcher, not a data source — quality/OpSec live in the tools it links; some (people-search) are active and attributable.
- Requires no sensitive permissions, which is reassuring for a browser extension.
- Destinations skew US-centric; pair with region-appropriate tools for other countries.

## Overlaps ("do both")
- Complements `[[awesome-recon-tools]]` (a broader curated menu) and evidence-capture add-ons like `[[awesome-screenshot-extension-chrome]]` — use the toolbar to reach a tool fast, then capture what you find.

## Trust & verifiability
`trust: trusted` — curated by a reputable justice-information non-profit and permission-light; the toolbar is trustworthy, but each linked third-party tool still needs its own verification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-investigative-and-forensic-toolbar |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | name, phone, ip-address, email → social-profile, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
