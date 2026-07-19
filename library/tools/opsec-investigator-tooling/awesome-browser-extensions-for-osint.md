---
id: awesome-browser-extensions-for-osint
name: Awesome Browser Extensions for OSINT
description: Use when you want a browser extension to speed up an investigation task and need a vetted list — returns categorized OSINT extensions with use-case notes.
url: https://github.com/osintambition/Awesome-Browser-Extensions-for-OSINT
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A curated, categorized catalog of browser extensions useful across OSINT tasks (image search, profile scraping, capture, OpSec).
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, open GitHub "awesome" list; the extensions it links are mostly free too.
opsec: passive
opsecNote: Reading the list is passive. Installing an extension is not neutral — extensions can read page content and phone home; vet each one's permissions and use a dedicated investigation browser profile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: A community-maintained GitHub list (osintambition); the curation is helpful but the linked extensions are third-party and must be vetted individually before install.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- social-media-osint-tools-collection
tags:
- browser-extension
- awesome-list
- catalog
source: gh-topic-osint-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Awesome Browser Extensions for OSINT

> A curated GitHub catalog of browser extensions that speed up investigations — image search, profile capture, metadata, and OpSec helpers — each with a note on what it's for.

## When to use
When a repetitive investigation task (reverse-image searching, capturing a profile, pulling links, checking metadata, managing sock-puppet sessions) could be done faster with a browser extension, use this list to find a vetted option instead of searching the extension stores blind. Especially handy when building out an investigation browser profile.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Open the list at https://github.com/osintambition/Awesome-Browser-Extensions-for-OSINT.
2. Scan the categories (image, social media, capture/archiving, metadata, productivity, privacy/OpSec) for your task.
3. Read the one-line use-case note for a candidate extension.
4. Before installing, review the extension's store listing and permissions — prefer open-source, low-permission options.
5. Install into a dedicated investigation browser profile (not your personal one), and disable when not needed.
6. Pivot: the chosen extension becomes part of your workflow; return to the list as new task needs arise.

## Inputs → Outputs
- **In:** an investigation task you want to accelerate (no data selector)
- **Out:** categorized, use-case-annotated pointers to OSINT browser extensions
- **Empty/negative result looks like:** no extension listed for your niche need, or a linked extension that's been removed from the store — awesome-lists lag, so confirm the extension still exists and is maintained before trusting it.

## Gotchas & OpSec
- Directory, not a tool: it recommends extensions; you must vet each one.
- Extensions are a real attack/leak surface — they can read every page you visit and exfiltrate data. Check permissions, prefer open-source, and isolate them in a dedicated profile.
- Some listed extensions may be abandoned or store-removed.

## Overlaps ("do both")
- Complements `[[social-media-osint-tools-collection]]` and other curated toolkits — this one focuses specifically on the browser-extension layer of an investigator's kit.

## Trust & verifiability
`trust: community` — a helpful community-curated list, but the trust decision rests on each individual extension; treat the list as a starting point and vet permissions/source before installing anything.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | awesome-browser-extensions-for-osint |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
