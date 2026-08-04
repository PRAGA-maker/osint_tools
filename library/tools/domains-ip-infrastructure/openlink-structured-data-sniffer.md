---
id: openlink-structured-data-sniffer
name: OpenLink Structured Data Sniffer
description: Use when you have a `domain`/page and want to extract the structured metadata embedded in it — returns schema.org Person/Organization data such as name, address, and social-profile links.
url: https://chromewebstore.google.com/detail/openlink-structured-data/egdaiaihbdoiibopledjahjaihbmjhdj
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Pulling embedded structured data (JSON-LD, RDFa, Microdata) — including schema.org Person/Organization fields — out of a live web page.
selectorsIn:
- domain
selectorsOut:
- name
- address
- social-profile
- employer-org
status: live
pricing: free
costNote: Free browser extension (Chrome Web Store, v3.4.x as of 2025); no account or payment required.
opsec: active
opsecNote: The extension parses whatever page you are currently viewing, so the target page is loaded live from your own browser/IP. Visit the target through a sock-puppet browser or proxy if the visit itself would be attributable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Published by OpenLink Software, a long-established data/semantic-web vendor; it only surfaces markup already present in the page, so there is no third-party data-quality risk beyond what the site publishes.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- OSDS
- OpenLink Structured Data Sniffer extension
tags:
- Domain/IP/Links
- Source Code Analyzes
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# OpenLink Structured Data Sniffer

> A browser extension that decodes the hidden structured metadata (JSON-LD, RDFa, Microdata, Turtle) a page embeds — often revealing schema.org author, organization, address and social links that don't appear in the visible text.

## When to use
You are on a target's website, profile, or article page and want the machine-readable data behind it. Modern sites embed schema.org markup — `Person`, `Organization`, `LocalBusiness`, `Article` — carrying names, postal addresses, phone numbers, `sameAs` social-profile URLs, author identities and org affiliations that the rendered page may not spell out. This surfaces those fields cleanly instead of hand-reading page source.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the extension from the Chrome Web Store (works in Chrome/Chromium/Edge).
2. Navigate to the target page (ideally in a sock-puppet browser profile).
3. When the page contains structured data the extension icon activates — click it.
4. Read the extracted property sheet: entity types and their fields (name, address, contactPoint, `sameAs` links, author/publisher orgs).
5. Pivot: `sameAs` URLs feed social-profile enumeration; an embedded postal address/phone feeds people-search; a publisher `Organization` feeds employer/company OSINT.

## Inputs → Outputs
- **In:** `domain` / a specific page URL (you visit it in-browser)
- **Out:** `name`, `address`, `social-profile` (`sameAs`), `employer-org`, plus any other schema.org fields present
- **Empty/negative result looks like:** the icon stays inactive / "no structured data found" — many small or hand-built pages carry no markup at all; absence means the site didn't embed it, not that the entity doesn't exist.

## Gotchas & OpSec
- **Active:** the page is fetched by your own browser. Route through a sock puppet/proxy if the visit is sensitive.
- It only reveals what the site author chose to embed — treat embedded data as the publisher's claim, not independently verified fact.
- Structured data can be templated/boilerplate (e.g. a CMS default org block) rather than specific to the page's subject; sanity-check before pivoting.

## Overlaps ("do both")
- Complements page-source/metadata inspectors and site-fingerprinters like [[w3techs]] — that one profiles the stack, this one extracts the semantic entity data (people, orgs, contacts) embedded in the content.

## Trust & verifiability
`trust: community` — reputable vendor (OpenLink Software) and it merely parses on-page markup, so reliability equals the site's own published data; verify extracted contacts against a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | openlink-structured-data-sniffer |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → name, address, social-profile, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | no |
