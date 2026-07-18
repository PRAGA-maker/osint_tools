---
id: ezr-osint-sidebar
name: EZR OSINT Sidebar
description: Use when you're viewing a web page/`image` and want in-browser metadata, EXIF, hashes, and reverse-search links — returns `metadata-exif`, SHA-256 hashes, and pivot links plus screenshots.
url: https://chromewebstore.google.com/detail/ezr-osint-sidebar/joagbbgciboooipadijeaoidjjigdmof
category: evidence-capture
path:
- evidence-capture
- web-browsing
bestFor: A browser sidebar that extracts metadata/EXIF, hashes evidence, and generates reverse-search pivots while you browse.
selectorsIn:
- image
- ip-address
- email
selectorsOut:
- metadata-exif
- image
status: live
pricing: free
costNote: Free Chrome/Chromium extension installed from the Chrome Web Store; no account required.
opsec: passive
opsecNote: Passive by design — it processes content already on the page in your browser and builds reverse-search links (which you choose whether to click). Some enrichment (reverse image, IP lookups) reaches third parties when you trigger it, so treat those clicks as outbound and use a sock-puppet session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: A community-published investigator extension on the Chrome Web Store; useful convenience tooling, but unofficial and unaudited — verify what it extracts.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- hunchly
- exif-tool
aliases:
- EZR Sidebar
tags:
- evidence-capture
- browser-extension
- metadata
- exif
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# EZR OSINT Sidebar

> A browser sidebar that turns the page you're on into leads — pulling metadata/EXIF, hashing content, capturing screenshots, and generating reverse-search links without leaving the tab.

## When to use
During hands-on web review, when you want investigator utilities docked next to the page instead of copy-pasting into separate tools: extract an `image`'s `metadata-exif`, compute SHA-256 hashes to preserve evidence integrity, screenshot for documentation, and one-click into reverse-image / IP / email lookups. Best as a workflow accelerator layered over your normal browsing, not as a standalone data source.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "EZR OSINT Sidebar" from the Chrome Web Store (Chrome/Edge/Brave/other Chromium browsers).
2. Open the sidebar while on a page of interest.
3. Point it at content — an image, an IP, an email, page text — to pull metadata/EXIF, compute a SHA-256 hash, or capture a screenshot.
4. Use the generated reverse-search / lookup links to pivot the extracted selector into other services.
5. Save the hash + screenshot to your case notes for a documented chain of evidence.

## Inputs → Outputs
- **In:** `image` (for EXIF), `ip-address`, `email`, or on-page content.
- **Out:** `metadata-exif`, SHA-256 hashes, screenshots, and reverse-search/lookup pivot links.
- **Empty/negative result looks like:** an image stripped of EXIF (many social platforms remove it) returns no metadata — absence of EXIF is normal, not a tool failure.

## Gotchas & OpSec
- EXIF often stripped: social networks and messaging apps remove metadata on upload, so expect empty EXIF on most reshared images.
- Convenience wrapper: it aggregates and links to other services rather than owning any dataset — the pivots go to third parties when clicked.
- Unofficial: a community extension; confirm critical extractions (hashes, EXIF) with a dedicated tool for evidentiary work.
- OpSec: local extraction is passive, but clicking its enrichment links makes outbound requests — do so from a sock-puppet session.

## Overlaps ("do both")
- Pairs with `[[hunchly]]` (thorough capture/case management) and `[[exif-tool]]` (authoritative metadata extraction) — this is the quick in-browser first pass, those are the rigorous follow-ups.

## Trust & verifiability
`trust: community` — an unofficial investigator extension; it's convenient but unaudited, so verify hashes and metadata with an established tool before relying on them as evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ezr-osint-sidebar |
| category | evidence-capture |
| selectorsIn → selectorsOut | image, ip-address, email → metadata-exif, image |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
