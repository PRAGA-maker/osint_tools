---
id: har2warc
name: har2warc
description: Use when you have a browser-captured HAR of a `domain` and want a preservable web archive — returns a standards-compliant WARC file of the captured traffic.
url: https://github.com/webrecorder/har2warc
category: archives-cache
path:
- archives-cache
bestFor: Converting a browser HAR capture into a WARC evidence archive for long-term preservation.
selectorsIn:
- domain
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free, open-source (Apache 2.0), install via `pip install har2warc`.
opsec: passive
opsecNote: A local, offline format converter — it processes a HAR file you already captured and makes no network requests to the target. All OpSec risk sits in how you captured the HAR (that browsing was the active step), not in the conversion.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: trusted
trustNote: Maintained by the Webrecorder project (the WARC/web-archiving ecosystem); a small but reliable, standards-aware utility.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- har2warc
tags:
- web-archiving
- warc
- evidence-preservation
- cli
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
relatedTools:
- replayweb
---

# har2warc

> A small Webrecorder utility that turns a browser's HAR capture into a proper WARC archive — the format-conversion step in preserving web evidence.

## When to use
You captured a target `domain`'s traffic as a HAR file (e.g. from browser DevTools while documenting a page) and need it in **WARC**, the archival standard used by the Wayback Machine and forensic web-archiving tools. Use har2warc to convert HAR → WARC so the capture can be indexed, replayed, and preserved as evidence rather than sitting as a fragile HAR. It's an infrastructure/preservation step, not a lookup — hence its low direct missing-persons relevance.

## How to use it (`bestInteractionPattern`: python-lib)
1. Capture the page's traffic to a HAR file (browser DevTools → Network → "Save all as HAR").
2. Install: `pip install har2warc`.
3. Convert on the CLI: `har2warc input.har output.warc.gz`
   - Or import it as a Python library to convert files/buffers programmatically.
4. Verify/replay the resulting WARC in a WARC viewer or ingest it into your archiving pipeline.
5. Pivot: the WARC becomes durable evidence and feeds replay tools; response headers/metadata (`metadata-exif`-style) inside it corroborate what the site served and when.

## Inputs → Outputs
- **In:** a HAR capture (of a `domain`/page you visited)
- **Out:** a `.warc.gz` archive preserving the requests/responses and their metadata
- **Empty/negative result looks like:** an error or empty WARC — usually a malformed/partial HAR; re-capture a complete HAR and retry.

## Gotchas & OpSec
- Fidelity is bounded by the HAR: anything the browser didn't record (streamed media, some binary responses) won't be in the WARC.
- It's stable but lightly maintained (few releases) — pin your version and validate output for critical evidence.
- OpSec: passive/offline; the sensitive part was capturing the HAR, which you should have done from a sock-puppet browser if the target site is monitored.

## Overlaps ("do both")
- Pairs with Wayback/web-archive tools and WARC players: har2warc produces the archive, those replay and cross-reference it. Capture with a proper archiving browser extension when you can, and use har2warc when all you have is a HAR.

## Trust & verifiability
`trust: trusted` — from the Webrecorder project, the reference ecosystem for WARC. It's a deterministic converter, so output is verifiable by replaying the WARC; the only limits come from the input HAR's completeness.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | har2warc |
