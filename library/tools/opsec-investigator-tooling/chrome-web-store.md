---
id: chrome-web-store
name: Chrome Web Store
description: Use when you want to find or vet a browser extension for an OSINT task — Google's official catalog of Chrome/Chromium extensions, searchable with ratings and publisher info.
url: https://chromewebstore.google.com/category/extensions
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Finding, comparing, and vetting Chrome/Chromium browser extensions (including OSINT add-ons) before installing.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free official Google catalog; a Google account is only needed to leave reviews, not to browse or install.
opsec: passive
opsecNote: Browsing the store touches only Google, not any subject. The real OPSEC concern is downstream: extensions can read every page you visit, so install investigative add-ons only in a dedicated research browser profile, not the one tied to your identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Google's first-party extension marketplace; the store itself is authoritative, though individual third-party extensions listed on it vary wildly in trust and must be vetted one by one.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Chrome Web Store
- Chrome extensions store
tags:
- add-ons-apps-extensions
- browser-extensions
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# Chrome Web Store

> Google's official catalog of Chrome/Chromium extensions — where you discover, compare, and vet the browser add-ons that power a lot of hands-on OSINT.

## When to use
You need a browser extension for a task — RSS detection, reverse-image lookups, metadata viewers, link expanders, archive savers — and want to find candidates, check their ratings/user counts/publisher, and read reviews before trusting one with access to your browsing. Also the canonical place to confirm an extension referenced elsewhere is genuine and still published.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the store and search a capability keyword (e.g. "reverse image", "EXIF", "wayback").
2. Compare listings by user count, rating, last-updated date, and publisher identity.
3. Open a candidate's page; read the permissions it requests and recent reviews.
4. Vet: prefer extensions with many users, recent updates, and a credible publisher; be wary of ones demanding broad permissions.
5. Install into a **dedicated research browser profile**, then use the extension for the actual task.

## Inputs → Outputs
- **In:** none (a capability keyword you're shopping for)
- **Out:** matching extensions with ratings, permissions, publisher, and reviews
- **Empty/negative result looks like:** no relevant extension, or only low-rated/abandoned ones — the capability may not exist as an extension, or use a web tool instead.

## Gotchas & OpSec
- The store is trusted; the extensions on it are not automatically — each is third-party code with page-level access. Vet permissions and publisher.
- Install investigative add-ons in an isolated profile so they can't read your identity-linked browsing.
- Chrome/Chromium only; Firefox has its own AMO catalog.

## Overlaps ("do both")
- The delivery mechanism for extension-based tools in this library (e.g. [[rss-subscription-extension-chrome]]) — find and vet them here, then follow the tool's own file for usage.

## Trust & verifiability
`trust: trusted` — first-party Google marketplace; authoritative for whether an extension exists and who publishes it, but you still judge each extension's own trustworthiness individually.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | chrome-web-store |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | (none) → (none) |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
