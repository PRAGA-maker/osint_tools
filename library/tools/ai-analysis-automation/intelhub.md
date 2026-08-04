---
id: intelhub
name: IntelHub
description: Use when you are investigating in-browser and have a `username`, `image`, url or block of text — a browser extension that runs Telegram profiling, reverse-image/EXIF, tech-recon and entity extraction, returning social-profiles, metadata-exif and extracted identifiers.
url: https://github.com/tomsec8/IntelHub
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: An all-in-one OSINT browser extension for on-the-page recon, metadata analysis and entity extraction.
selectorsIn:
- username
- image
- domain
selectorsOut:
- social-profile
- metadata-exif
- email
status: live
pricing: free
costNote: Free and open-source (MIT); available on the Chrome, Firefox and Edge stores.
opsec: active
opsecNote: Some features (Telegram profiling, website recon, archive/reverse-image lookups) fire live queries to third parties from your browser; others (EXIF, text extraction, local AI via LM Studio) run entirely locally. Use a dedicated research browser profile; the local-AI mode keeps analysis offline, but network features still expose your IP to the services queried.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Community project by tomsec8 (actively developed, v5.x); verify outputs against primary sources.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- intel hub extension
tags:
- browser-extension
- metadata
- entity-extraction
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# IntelHub

> A cross-browser OSINT extension that puts Telegram profiling, reverse-image/EXIF, website recon, entity extraction and (optional) local AI into the page you're already looking at.

## When to use
You're investigating in the browser and want quick, in-context tooling: profile a Telegram `username`, extract `metadata-exif` from an `image`, pull emails/phones/crypto addresses out of a `text` block, fingerprint a site's tech stack, or find archived versions — without switching to separate apps. Handy as an on-the-page multitool during manual review.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install from the Chrome Web Store / Firefox Add-ons / Edge Add-ons in a research browser profile.
2. (Optional) Set up LM Studio locally to enable the offline "Local OSINT Agent" for AI summaries with no data leaving your machine.
3. Open the target page/image/text and invoke the relevant panel: Telegram profiling, reverse-image + EXIF, tech recon, or text entity extraction.
4. Read the outputs — profiles, extracted identifiers, metadata reports, and an investigation graph you can build up.
5. Pivot: extracted `email`/`phone`/`social-profile` values feed dedicated selector tools; the graph organises what you've found.

## Inputs → Outputs
- **In:** `username` (Telegram), `image`, `domain`/url, or pasted text/files (PDF/DOCX/image).
- **Out:** `social-profile` data, `metadata-exif` (incl. GPS), extracted `email`/`phone`/crypto strings, tech-stack and archive results, and a visual investigation graph.
- **Empty/negative result looks like:** a panel returning nothing (no EXIF present, private Telegram profile, no archive) — absence of a signal, not proof.

## Gotchas & OpSec
- Mixed passive/active: know which panel makes network calls (Telegram/website/archive) vs. which is local (EXIF/text/local-AI) before using it on sensitive targets.
- Browser extensions have broad page access — keep it in an isolated research profile.
- Community-maintained: cross-check any actioned finding against a primary source.

## Overlaps ("do both")
- Overlaps standalone metadata/username tools; use IntelHub for fast in-browser triage, then a dedicated CLI like `[[e4gl30s1nt]]` or `[[slash]]` for deeper, scriptable username/breach work.

## Trust & verifiability
`trust: community` — an actively developed community extension; its convenience is the draw, but treat each automated result as a lead to confirm, and prefer the local-AI mode when you need to keep material offline.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | intelhub |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | username, image, domain → social-profile, metadata-exif, email |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | no |
