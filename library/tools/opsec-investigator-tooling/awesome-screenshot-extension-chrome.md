---
id: awesome-screenshot-extension-chrome
name: Awesome Screenshot Extension (Chrome)
description: Use when you have a live web page (a `social-profile`, listing, or post) and want a defensible capture of it — returns an annotated full-page screenshot for your case file.
url: https://chromewebstore.google.com/detail/awesome-screenshot-screen/nlipoenfbbikpbjkfpfillcgkoblgpmj
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Capturing and annotating full-page screenshots of web evidence before it changes or is deleted.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free tier covers screenshot capture and annotation; screen recording and cloud/team features are a paid upsell you don't need for evidence capture.
opsec: passive
opsecNote: Capturing renders the page you're already viewing — it does not notify the site owner or subject. The privacy risk is outbound: do NOT use the cloud-upload/share feature for sensitive captures; save locally. Capture from a sock-puppet session so the visit itself isn't attributable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: unverified
trustNote: A widely-used third-party Chrome extension; it can read page content it captures, so treat it like any extension with broad page access and avoid its cloud features for sensitive work.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- fireshot
- screenshot-full-page-screen-capture
- lightshot-screen-capture-add-on
aliases:
- Awesome Screenshot
- Awesome Screenshot & Screen Recorder
tags:
- toddington
- curated-directory
- add-ons-apps-extensions
- evidence-capture
source: toddington-resources
lastVerified: '2026-08-05'
enrichment: full
---

# Awesome Screenshot Extension (Chrome)

> A one-click full-page screenshot and annotation tool — for freezing web evidence (a profile, post, or listing) exactly as it looked, before it's edited or taken down.

## When to use
You've found something that matters — a `social-profile`, a classified ad, a forum post, a cached page — and it could disappear or be edited. Capture it now. Full-page capture preserves the whole scroll, and annotation lets you ring the relevant detail (a handle, a timestamp, a phone number) for your report. This is investigator hygiene, not a discovery tool: it takes no selector in and produces evidence, not new leads.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Awesome Screenshot" from the Chrome Web Store in your investigation browser profile.
2. Navigate (from a sock-puppet session) to the page you need to preserve.
3. Click the extension → choose **Capture entire page** (not just the visible area) so the full scroll is recorded.
4. Annotate: highlight/box/arrow the key detail; add the URL and capture date/time in the image itself for provenance.
5. **Save to your local disk** — avoid the cloud/share option for anything sensitive. File it in your case folder alongside the source URL and timestamp.

## Inputs → Outputs
- **In:** a live web page you're viewing (no personal selector)
- **Out:** an annotated image artifact for the case file (evidence, not a new selector)
- **Empty/negative result looks like:** capture fails on pages that block extension access (some banking/DRM pages) or infinite-scroll feeds truncate — fall back to a print-to-PDF or a dedicated archiving tool.

## Gotchas & OpSec
- For evidentiary weight, capture the URL and clock in-frame and keep the original file; a screenshot alone is weaker than an archived page with a hash.
- The extension can read the content of pages it captures — don't grant it on your everyday profile; use a dedicated investigation profile.
- Don't push sensitive captures to its cloud; keep them local.

## Overlaps ("do both")
- Interchangeable with `[[fireshot]]`, `[[screenshot-full-page-screen-capture]]`, and `[[lightshot-screen-capture-add-on]]` — pick one. For stronger provenance than a screenshot, also archive the page with a timestamped web-archive tool.

## Trust & verifiability
`trust: unverified` — a popular but third-party extension with broad page access; the captures are only as trustworthy as your documentation of where and when they were taken, so record provenance yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | awesome-screenshot-extension-chrome |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
