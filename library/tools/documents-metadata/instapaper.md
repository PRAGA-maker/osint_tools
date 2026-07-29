---
id: instapaper
name: Instapaper
description: Use when you have a target `domain`/URL and want to capture its readable text for offline review and evidence-keeping — returns a saved, de-cluttered copy of the page.
url: https://www.instapaper.com
category: documents-metadata
path:
- documents-metadata
bestFor: Saving a stripped-to-text, dated copy of an article or profile page so evidence survives if the original is edited or deleted.
selectorsIn:
- domain
selectorsOut: []
status: live
pricing: freemium
costNote: Free tier saves unlimited articles and offers full-text search; the paid "Premium" tier ($3/mo) adds unlimited highlights, notes, text-to-speech and full-text archive search. Free tier is sufficient for evidence capture.
opsec: passive
opsecNote: When you save a URL, Instapaper's servers fetch that page from their own infrastructure — so the request to the target site comes from Instapaper, not you, which is a mild upside. The downside is Instapaper (and its account tied to your email) now holds a record of every page you save; use a dedicated research account, not a personal one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Long-running commercial read-later service (originally by Marco Arment, later Pinterest/Instant Paper Inc.); reputable as a utility but it is a third-party host of whatever you save, not an evidentiary chain-of-custody tool.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- pocket
- hunchly
aliases:
- Instapaper read later
tags:
- toddington
- curated-directory
- useful-websites-tools-documents
- read-later
- evidence-capture
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# Instapaper

> A read-later bookmarking service, repurposed as a lightweight way to snapshot the *text* of a page before it changes or vanishes.

## When to use
You have a URL (article, blog post, forum thread, profile bio) that is relevant to an investigation and you want a dated, de-cluttered text copy preserved outside the source site — in case the author edits or deletes it. Instapaper reformats the page to reader-view text and stores it under your account. It is a capture/workflow utility, not a person-finder, and it strips most layout/images, so for a faithful visual record prefer a full-page archiver.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create a dedicated research account at https://www.instapaper.com (use a sock-puppet email).
2. Save a page one of three ways: paste the URL into the "Add" box on the web app, use the browser "Save to Instapaper" bookmarklet/extension, or email the URL to your personal Instapaper submit address.
3. Instapaper fetches and stores a reader-view copy; open it under **Home** to confirm the text captured cleanly.
4. Export/print the saved article to PDF for your case file, and note the save date (that timestamp is your "seen on" evidence).
5. Pivot: for pixel-accurate, tamper-evident capture of the same URL, run it through `[[hunchly]]` or a web-archive tool in parallel.

## Inputs → Outputs
- **In:** `domain`/URL of the page to preserve.
- **Out:** a saved, searchable reader-view text copy (no new selectors — this is preservation, not enrichment).
- **Empty/negative result looks like:** a paywalled, JS-heavy, or login-gated page saves as an empty/garbled article — that's a signal to switch to a screenshot/archive tool.

## Gotchas & OpSec
- Human-in-the-loop: requires account login; saving is manual per URL.
- OpSec: **passive** toward the target (Instapaper's servers do the fetch), but every save is logged to your account — keep it a throwaway research identity.
- Not chain-of-custody grade: Instapaper can reflow/truncate content and stores no cryptographic hash. For anything that may become evidence, pair it with a proper archiver.
- Text-only: images, layout, and dynamic content are dropped.

## Overlaps ("do both")
- Pairs with `[[hunchly]]` — Hunchly captures a forensic, hashed full-page record while you browse; Instapaper is the quick, free text snapshot. Use Instapaper for volume, Hunchly for evidentiary weight.
- Overlaps with `[[pocket]]` as an interchangeable read-later capture service.

## Trust & verifiability
`trust: unverified` — a reputable, long-lived commercial service, but it is a third-party host reformatting your saved pages, not an authoritative or tamper-evident record. Treat saved copies as convenience, not proof.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | instapaper |
| category | documents-metadata |
| selectorsIn → selectorsOut | domain → — |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
