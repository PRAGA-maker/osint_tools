---
id: osintgeek-tools
name: OSINTgeek Tools
description: Use when you have a `username`, `email`, `image` or `domain` and want a curated launchpad of vetted lookup tools (with a DACH/German focus) — returns links out to `social-profile` and other research services.
url: https://osintgeek.de/tools
category: search-engines
path:
- search-engines
bestFor: A curated, category-organised toolbox of free investigation tools, strong on German/Austrian/Swiss (DACH) sources.
selectorsIn:
- username
- email
- image
- domain
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: The tool links and search dashboards are free to use; the operator also sells an optional PDF guide via Stripe, but nothing on the toolbox itself is paywalled.
opsec: passive
opsecNote: The catalogue page itself is passive — browsing it reveals nothing about your target. OpSec risk lives in the third-party tools it links out to; assess each destination (some touch the target's infrastructure) before running it, and use a sock-puppet browser for anything active.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Maintained by OSINTgeek (osintgeek.de), an established German-language OSINT educator; a curated directory rather than a data source, so trust is in the curation, not in any single linked tool.
missingPersonsRelevance: medium
coverage:
- global
- eu
auth: none
api: false
localInstall: false
registration: false
aliases:
- OSINTgeek Toolbox
- osintgeek.de/tools
tags:
- tool-collection
- dashboards
- dach
source: ultimate-osint
lastVerified: '2026-07-21'
enrichment: full
---

# OSINTgeek Tools

> A German-maintained, category-organised toolbox that routes a selector (username, email, image, domain) to the right free lookup service, with unusually good DACH-region coverage.

## When to use
You are early in a case, holding a `username`, `email`, `image`, or `domain`, and want a curated menu of working tools rather than a blank search box — especially when the subject has a **German, Austrian, or Swiss** footprint, where OSINTgeek's people-research and identity sections point at regional databases most English-language lists miss.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://osintgeek.de/tools in a sock-puppet browser.
2. Pick the category that matches what you hold: Search Engines & Dorks, People Research, Email & Identity, Images & Media, or Infrastructure & Security.
3. Some category cards embed a live input box (paste a username or email and it builds the query); others are plain link-outs. Use the box to launch, or click through to the external tool.
4. Read the destination tool's result there — this page only routes you; the actual `social-profile` / breach / domain data comes from the linked service.
5. Pivot: feed a confirmed username onward to username-enumeration tooling, or an email to a dedicated existence oracle like `[[account-live-com]]`.

## Inputs → Outputs
- **In:** `username`, `email`, `image`, or `domain`
- **Out:** links to services returning `social-profile` and related identity/infrastructure data (not the data itself)
- **Empty/negative result looks like:** the category has no tool for your selector, or a linked tool has gone dead — treat OSINTgeek as a directory whose entries can rot, and verify the destination loads.

## Gotchas & OpSec
- This is a **meta-resource**: it holds no database of its own, so its usefulness equals the usefulness of whatever it links to.
- German-language UI; the category labels are self-explanatory, but use a translator for the guidance text.
- OpSec is inherited from the linked tool, not the catalogue — an image reverse-search or a domain WHOIS behaves very differently from a passive username check.
- The optional paid PDF guide is an upsell; ignore it, the tools are free.

## Overlaps ("do both")
- Pairs with broad tool aggregators — OSINTgeek is smaller but DACH-aware, so run it alongside a general OSINT framework when the subject is Central European.

## Trust & verifiability
`trust: community` — a reputable, actively maintained German OSINT educator's curated list; reliable as a launchpad, but each linked tool must be trust-assessed on its own merits.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osintgeek-tools |
| category | search-engines |
| selectorsIn → selectorsOut | username, email, image, domain → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
