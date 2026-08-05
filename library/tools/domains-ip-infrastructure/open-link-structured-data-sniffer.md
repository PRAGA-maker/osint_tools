---
id: open-link-structured-data-sniffer
name: OpenLink Structured Data Sniffer
description: Use when you have a `domain`/web page and want the machine-readable metadata embedded in it (schema.org, microdata, RDFa, JSON-LD, RSS) — surfaces hidden entities, authors and links.
url: https://chromewebstore.google.com/detail/openlink-structured-data-sniffer/egdaiaihbdoiibopledjahjaihbmjhdj
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Extracting the structured/semantic metadata baked into a webpage (author, org, contacts, related URLs) that isn't visible in the rendered text.
selectorsIn:
- domain
selectorsOut:
- name
- employer-org
- social-profile
status: live
pricing: free
costNote: Free open-source browser extension by OpenLink Software; no account.
opsec: passive
opsecNote: The extension parses the page you are already viewing — it makes no extra requests to the target beyond your normal page load, so it adds no footprint. Standard rule still applies: view the target page from a sock-puppet browser/IP, not your real identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: trusted
trustNote: Published and maintained by OpenLink Software, a known data/RDF vendor; it just reads and displays markup already present in the page, so what it shows is verifiable in the page source.
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
- OpenLink Structured Data Sniffer
tags:
- Domain/IP/Links
- Source Code Analyzes
- metadata-exif
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# OpenLink Structured Data Sniffer

> A browser extension that reads the structured data buried in a webpage — schema.org/JSON-LD, microdata, RDFa, POSH, RSS — and lays out the entities, authors, organisations and links that the rendered page doesn't show.

## When to use
You're viewing a subject's site, a company page, a blog post, or a profile and want the semantic metadata behind it: an article's declared `author`, an organisation's structured contact block, `sameAs` links to social profiles, embedded person/place entities, feed URLs. Pages routinely carry rich schema.org/JSON-LD markup that never appears on-screen; this extension pulls it out in one click.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install OpenLink Structured Data Sniffer from the Chrome Web Store (Chromium browsers).
2. Navigate to the target page in a sock-puppet browser.
3. Click the extension icon; it parses the current page's RDFa/microdata/JSON-LD/RSS and lists the extracted entities and properties.
4. Pivot: `author`/`Person` entities → `name`; `Organization` → `employer-org`; `sameAs` URLs → `social-profile`; feed/URLs → further pages to crawl.

## Inputs → Outputs
- **In:** `domain`/web page you are viewing
- **Out:** `name` (declared authors/persons), `employer-org` (organisation markup), `social-profile` (sameAs links), plus feed URLs and other embedded entities
- **Empty/negative result looks like:** the sniffer reports no structured data — the page carries no schema markup (common on hand-built or very old sites); fall back to reading raw HTML source and meta tags.

## Gotchas & OpSec
- It only surfaces markup the site author chose to embed; absence of data ≠ absence of the entity.
- Structured data can be stale or aspirational (copied templates, wrong author) — corroborate before trusting.
- Purely local parsing of an already-loaded page, so it adds no extra target footprint.

## Overlaps ("do both")
- Pairs with a general page-source/metadata viewer: this decodes the *semantic* layer (entities/relationships) while raw source gives you comments, scripts and hidden fields the schema omits.

## Trust & verifiability
`trust: trusted` — maintained by OpenLink Software and it only reflects markup already in the page, which you can confirm directly in view-source. The reliability of the *content* still depends on whoever authored the markup.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | open-link-structured-data-sniffer |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → name, employer-org, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
