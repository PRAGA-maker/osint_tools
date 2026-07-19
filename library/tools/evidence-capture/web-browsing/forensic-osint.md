---
id: forensic-osint
name: Forensic OSINT
description: Use when you have a live web page (`social-profile`, `domain`) and want a court-defensible capture — returns a timestamped, hashed, digitally signed evidence record.
url: https://www.forensicosint.com/
category: evidence-capture
path:
- evidence-capture
- web-browsing
bestFor: Capturing web pages (including expanded comments, media and source) as forensically sound, timestamped, signed evidence.
selectorsIn:
- social-profile
- domain
selectorsOut:
- metadata-exif
- document-id
status: live
pricing: freemium
costNote: Free Chrome extension (Essential tier) covers signed full-page capture; advanced features (Subject Dossier, advanced OCR search, video continuity) require a paid ELITE plan. A free account/login is required even for the free tier.
opsec: passive
opsecNote: You capture pages your own browser loads — it does not probe or notify the target. But it runs in YOUR authenticated browser: capturing a logged-in view can embed your own identity/session in the evidence, so capture from a sock-puppet browser profile, not your real accounts.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: community
trustNote: A purpose-built commercial evidence tool used by investigators; the free tier is genuine, and captures include hashing/signing for chain-of-custody, though it is a vendor product rather than an open standard.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: true
registration: true
relatedTools:
- forensicosint-com
- forensic-osint-kb-guides
aliases:
- forensicosint.com
- Forensic OSINT extension
tags:
- evidence-capture
- web-archiving
- chain-of-custody
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# Forensic OSINT

> A Chrome extension that captures a live web page as court-defensible evidence — full page with expanded comments and media, timestamped, hashed and digitally signed for chain-of-custody.

## When to use
You've found something on a live page — a `social-profile`, a post, a listing on a `domain` — that matters to a case and needs to be preserved *before it's edited or deleted*, in a form that stands up to disclosure. Ordinary screenshots are trivially disputed; Forensic OSINT produces a signed, timestamped PDF/record with a hash of every artifact, capturing dynamic content (expanded comments, lazy-loaded images, video) and the page source, so the capture demonstrates integrity.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the free "Forensic OSINT" Chrome extension and create/log into a free account (required even for the Essential tier).
2. In a **sock-puppet browser profile**, navigate to the target page and let it fully render (scroll to expand comments/media if needed).
3. Trigger the extension to capture — it walks the page, expands dynamic content, and records HTML, media, timestamps and hashes.
4. Export the signed, timestamped PDF report and the capture package; file it with the case metadata (`document-id`).
5. Pivot: the preserved page is now stable evidence — annotate it and reference the hash/timestamp in your report; the underlying content still feeds normal OSINT follow-up.

## Inputs → Outputs
- **In:** a live URL — `social-profile`, post, or `domain` page
- **Out:** a digitally signed, timestamped evidence record with hashes and capture `metadata-exif`; a case `document-id` for organization
- **Empty/negative result looks like:** capture fails or is incomplete on heavily script-gated / login-walled pages, or the free tier blocks an advanced feature (Subject Dossier, OCR search) behind ELITE — the capture itself works, the gated analytics don't.

## Gotchas & OpSec
- Human-in-the-loop: account login is required; advanced analysis is paywalled (Essential tier still gives you signed capture).
- Capture reflects YOUR browser state — a logged-in session can leak your identity into the evidence; always capture from a clean sock-puppet profile.
- Dynamic/infinite-scroll pages need manual expansion before capture to be complete.
- OpSec: passive toward the target (no probing), but the capture is only as clean as the browser it runs in.

## Overlaps ("do both")
- Pairs with `[[forensicosint-com]]` (same vendor) and general archiving — use a public archive (Wayback/archive.today) for an independent third-party timestamp alongside the signed local capture, so integrity rests on two sources.

## Trust & verifiability
`trust: community` — a specialist vendor tool widely used by investigators; its hashing/signing gives verifiable integrity for a capture, but it is a commercial product, so pair it with an independent archive for corroboration where stakes are high.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | forensic-osint |
| category | evidence-capture |
| selectorsIn → selectorsOut | social-profile, domain → metadata-exif, document-id |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | yes (account-login) |
