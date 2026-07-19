---
id: time-travel-for-web-chromewebstore-google-com
name: Time Travel for the Web (Memento)
description: Use when you have a `domain`/page URL and want a past version — returns the nearest archived snapshot across many web archives via the Memento protocol.
url: https://chromewebstore.google.com/detail/time-travel-for-web/ogckpcboinbcohhilmofkalobpkolkib
category: archives-cache
path:
- archives-cache
bestFor: Finding the archived version of a web page nearest a chosen date across multiple web archives at once.
selectorsIn:
- domain
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free browser extension; no account. Queries the Memento Time Travel aggregator (LANL/Old Dominion research project).
opsec: passive
opsecNote: You query public web-archive aggregators for a URL and date; the site's current owner is not notified. Passive research — the extension sees the URLs you look up, so use a research browser profile for sensitive targets.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: trusted
trustNote: Implements the Memento protocol (RFC 7089) via the academic Time Travel aggregator; results are real snapshots from established web archives, so provenance is verifiable.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- Memento Time Travel
- Time Travel for Web
tags:
- archive
- Archive & Cached Related Sites
- web-archive
source: uk-osint
lastVerified: '2026-07-19'
enrichment: full
---

# Time Travel for the Web (Memento)

> A browser extension that finds the archived version of any page nearest a date you pick — polling many web archives at once via the Memento protocol.

## When to use
You have a page or `domain` that has changed or vanished — a deleted profile, an edited bio, a removed listing — and you want to see it as it was near a specific date. Rather than checking the Wayback Machine alone, Memento's Time Travel aggregator queries many archives simultaneously (Internet Archive, Archive.today, national libraries, and more) and returns the closest snapshot. For an investigation this recovers deleted contact details, past addresses, prior claims, and the state of a site at a key moment.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Time Travel for the Web" from the Chrome Web Store.
2. On a page (or by entering a URL), invoke the extension and pick a target date/time.
3. It queries the Memento aggregator across archives and takes you to the nearest captured snapshot.
4. Compare snapshots over time to see what changed and when; note the archiving source for each.
5. Pivot: recovered details (old emails, addresses, names) feed the relevant people/email/domain tools; the snapshot URL is citable evidence.

## Inputs → Outputs
- **In:** a page URL / `domain` + a target date
- **Out:** the nearest archived snapshot (a citable `document-id`/memento) from whichever archive holds it
- **Empty/negative result looks like:** no memento near the date — the page was never archived (common for obscure/private pages) or only exists outside the queried date range.

## Gotchas & OpSec
- Human-in-the-loop: none beyond installing the extension.
- Aggregates archives but isn't exhaustive — if it misses, also check the Wayback Machine and Archive.today directly.
- Snapshots capture a moment; the same URL can differ wildly across dates, so pick the date that matters.

## Overlaps ("do both")
- Pairs with the Wayback Machine and Archive.today — this aggregates across many archives by date; those give the deepest single-archive coverage and on-demand captures.

## Trust & verifiability
`trust: trusted` — built on the standardized Memento protocol and an academic aggregator; snapshots come from established archives with verifiable provenance.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | time-travel-for-web-chromewebstore-google-com |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
