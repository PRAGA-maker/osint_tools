---
id: youngersibling
name: YoungerSibling
description: Use when you have a `username`, `email`, `domain`, `phone`, or `image` and want a quick combined recon sweep — returns username availability across 400+ sites, MX/DNS/IP data, EXIF metadata, and search results from one CLI.
url: https://github.com/aeticusdev/YoungerSibling
category: username
path:
- username
bestFor: 'Quick combined recon: username availability across 400+ platforms plus DNS/IP, email MX, phone, and EXIF lookups.'
selectorsIn:
- username
- email
- domain
- phone
- image
selectorsOut:
- social-profile
- ip-address
- metadata-exif
status: live
pricing: free
costNote: Free and open-source (MIT); `pip install youngersibling`. Some functions call third-party services that may rate-limit.
opsec: passive
opsecNote: Runs locally and queries public sources/site presence server-to-server, so it is not attributed to the subject. The username module probes 400+ sites for a handle — high request volume can trip rate limits; route through appropriate egress and avoid bursts against sensitive targets.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Small MIT-licensed solo project (v1.2, late 2024) with modest adoption; code is open and inspectable, but low star count means less community vetting — verify hits downstream.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- YoungerSibling
tags:
- username
- enrichment
- python
- exif
source: gh-topic-osint-resources
lastVerified: '2026-07-19'
enrichment: full
---

# YoungerSibling

> A single Python CLI that bundles the common first-pass recon moves — username availability across 400+ sites, DNS/IP/MX lookups, phone lookup, Google search, and EXIF extraction — into one tool for fast triage of a lead.

## When to use
You have a starting selector — a `username`/handle, an `email`, a `domain`, a `phone`, or an `image` with possible EXIF — and want to run the standard early checks quickly without switching between separate tools: is this handle taken on the major platforms, what infrastructure sits behind this domain/email, and does this image carry location/camera metadata. It is a convenience aggregator for the opening moves of an investigation.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install youngersibling` (or clone the repo).
2. Launch the CLI and pick a module: Username Lookup (400+ platforms), IP Lookup, Email/MX Lookup, Phone Lookup, EXIF extraction, Google Search, or Web OSINT.
3. Feed the relevant selector (e.g. a handle for username availability, an image path for EXIF).
4. Read results: found-vs-not-found per platform for usernames, records for DNS/MX/IP, and any GPS/camera fields from EXIF.
5. Re-verify positive hits in the platform itself or a dedicated tool, since automated presence checks produce occasional false positives/negatives.
6. Pivot: confirmed profiles feed social-network tools; EXIF GPS feeds geolocation; MX/IP feeds infrastructure analysis.

## Inputs → Outputs
- **In:** `username`, `email`, `domain`, `phone`, or `image`
- **Out:** `social-profile` (per-platform presence), `ip-address`/DNS/MX records, `metadata-exif` (image GPS/camera data)
- **Empty/negative result looks like:** "not found" across platforms (handle may still exist behind anti-bot checks), empty EXIF (many social images are stripped on upload), or a module erroring on a rate-limited upstream — none of these is proof of absence.

## Gotchas & OpSec
- Human-in-the-loop: none required, but expect some modules to hit third-party rate limits on heavy use.
- OpSec: **passive** — local execution querying public sources; nothing is sent to the subject. High-volume username checks can still be noisy; pace them.
- Vetting: it is a small solo project, so treat outputs as leads and confirm important hits in a maintained, better-known tool.

## Overlaps ("do both")
- Pairs with dedicated username-search tools (Sherlock, WhatsMyName, Maigret), EXIF readers, and DNS/MX lookups — YoungerSibling is a jack-of-all-trades wrapper; when a single dimension matters, the specialised tool is more thorough and better maintained.

## Trust & verifiability
`trust: community` — open-source and inspectable but lightly adopted; its checks reproduce what dedicated tools do, so cross-verify any consequential hit in a more established source before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | youngersibling |
| category | username |
| selectorsIn → selectorsOut | username, email, domain, phone, image → social-profile, ip-address, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
