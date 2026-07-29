---
id: export-chrome-history
name: Export Chrome History
description: Use when you have supervised access to a subject's Chrome and want their browsing/bookmark history as data — returns visited URLs, titles, and timestamps as CSV/JSON.
url: https://chrome.google.com/webstore/detail/export-historybookmarks-t/dcoegfodcnjofhjfbhegcgjgapeichlf
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Exporting Chrome browsing history and bookmarks to CSV/JSON for archiving or investigation on a machine you control.
selectorsIn: []
selectorsOut:
- domain
- social-profile
status: live
pricing: freemium
costNote: Free Chrome extension from the Chrome Web Store; no account needed. (Web Store listings can be delisted — confirm it is still available before relying on it.)
opsec: passive
opsecNote: Runs entirely locally against the browser profile it is installed in — no data leaves the machine and no remote target is contacted. The sensitivity is legal/consent, not network: only run it on a device and profile you are authorised to examine. On someone else's machine, installing an extension is a visible, logged action.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: A third-party Chrome extension, not a first-party Google tool. Verify the current listing and reviews before installing; a history-reading extension has broad access to sensitive local data.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- hindsight
aliases:
- Export History/Bookmarks to CSV/JSON
tags:
- browser-artifacts
- history
- forensics
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Export Chrome History

> A Chrome extension that dumps the browser's history and bookmarks to CSV/JSON — a quick way to turn a subject's local browsing record into analysable data.

## When to use
When you have lawful, supervised access to a machine/profile and want the Chrome history and bookmarks as structured data: visited `domain`s, page titles, and timestamps you can sort, filter, and correlate. Useful for a light, on-the-spot examination of "other people's computers" (the author's stated use case) or for archiving your own browsing. For a full forensic acquisition, prefer a dedicated forensics tool.

## How to use it (`bestInteractionPattern`: browser-extension)
1. In the target Chrome profile, install the extension from the Web Store listing.
2. Open the extension and choose an export: history and/or bookmarks, in CSV or JSON.
3. Save the file; each history row has URL, title, and visit timestamp.
4. Analyse: sort by frequency/recency, grep for logins, webmail, social platforms, or a subject's known handles.
5. Pivot: exported `domain`s and `social-profile` URLs feed profile-enumeration and infrastructure tools; the timeline corroborates activity windows.

## Inputs → Outputs
- **In:** none (reads the local browser profile it runs in)
- **Out:** CSV/JSON of visited `domain`s/URLs, titles, timestamps, bookmarks → candidate `social-profile` links
- **Empty/negative result looks like:** an empty export — the profile has no/cleared history, or you're in a fresh/guest profile; confirm you're in the right Chrome profile.

## Gotchas & OpSec
- **Consent/legal gate:** browsing history is highly sensitive. Only run on a device and profile you are authorised to examine; document your authority.
- It reads live browser data, not a forensic image — it does not preserve deleted entries or provide chain-of-custody. For evidentiary work, image the profile and use a forensic parser instead.
- Third-party extension with deep access to local data — vet the current listing/reviews and prefer a known-good version.

## Overlaps ("do both")
- Pairs with `[[hindsight]]` — Hindsight forensically parses Chrome/Chromium profile artifacts (history, cache, downloads) from a copied profile with proper rigor. Use this extension for a fast live pull, Hindsight for a defensible forensic analysis.

## Trust & verifiability
`trust: community` — a functional third-party utility, not first-party. Output is directly verifiable (real URLs/timestamps), but confirm the extension is still listed and reputable before installing, given its access to sensitive data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | export-chrome-history |
