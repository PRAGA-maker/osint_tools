---
id: forensic-osint-full-page-screen-capture
name: Forensic OSINT Full Page Screen Capture
description: Use when you need to preserve a web page or social profile as defensible evidence — captures full-page screenshots with metadata (URL, timestamp, hash) for chain-of-custody.
url: https://chromewebstore.google.com/detail/forensic-osint-full-page/jojaomahhndmeienhjihojidkddkahcn
category: evidence-capture
path:
- evidence-capture
bestFor: Capturing full-page, metadata-stamped screenshots of web pages and profiles as forensically defensible evidence.
selectorsIn:
- social-profile
- domain
selectorsOut:
- metadata
- image
status: live
pricing: freemium
costNote: Free tier captures full pages; advanced/forensic features (hashing, bulk, exports) are paid.
opsec: active
opsecNote: Capture happens in your live browser session against the page you are viewing — if you are logged in or viewing a profile, that visit is a normal page load the site can see. The extension itself does not contact the target beyond your own browsing.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: trusted
trustNote: Listed in Trace Labs awesome-osint and force-installed into Brave by the Trace Labs OSINT VM; a recognized investigator evidence-capture tool.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Forensic OSINT
tags:
- evidence
- screenshot
- capture
- browser-extension
source: tracelabs-repos
lastVerified: ''
enrichment: full
---

# Forensic OSINT Full Page Screen Capture

> A Chrome/Brave extension that captures the page you're viewing as a full-length screenshot stamped with capture metadata (URL, timestamp, and — in paid tiers — a content hash), so the evidence holds up later.

## When to use
The moment you find something that matters — a missing person's `social-profile`, a post, a listing, a page on a `domain` — and it could be deleted or edited. Use it to freeze that page as defensible evidence with a verifiable capture time and source URL, instead of an ad-hoc screenshot that's easy to challenge. Essential for Trace Labs–style missing-persons work where findings are submitted to law enforcement.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the extension from the Chrome Web Store (already force-installed in the Trace Labs Brave VM).
2. Navigate your browser to the page you want to preserve and let it fully load (scroll content/lazy-load images as needed).
3. Trigger the extension to capture the **full** page (not just the viewport); it records the URL and timestamp alongside the image.
4. Save/export the capture into your case file. Pivot: log the `metadata` (URL + time) in your evidence index; the captured `image` becomes the citation for any claim you make from that page.

## Inputs → Outputs
- **In:** `social-profile` / `domain` (whatever page is open in your browser)
- **Out:** `image` (full-page screenshot) + `metadata` (source URL, capture timestamp, optional hash)
- **Empty/negative result looks like:** a clipped/partial capture (page didn't fully load) or a blank capture on heavily script-gated content — re-scroll/reload and recapture.

## Gotchas & OpSec
- Human-in-the-loop: forensic features (hashing, bulk capture, structured export) sit behind the paid tier; free tier still does full-page screenshots.
- The capture reflects *your* session — if you're logged into a sock account, that login state may show in the screenshot; scrub it before sharing.
- OpSec: **active** in the sense that you must actually visit the page in your browser, which the target site can log like any visit. Use a sock browser profile/VPN; the extension adds no extra outbound contact with the target.
- Capture pages promptly — the whole value is preserving content that may vanish.

## Overlaps ("do both")
- Pairs with archival services (Wayback Machine / archive.today): the extension gives *you* a controlled, metadata-rich local copy; public archives give an independent third-party timestamp. Doing both strengthens evidentiary weight.

## Trust & verifiability
`trust: trusted` — endorsed by Trace Labs (awesome-osint) and bundled into their investigator VM. Captures include source URL and timestamp; paid tiers add hashing for integrity verification, which is what makes the output defensible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | forensic-osint-full-page-screen-capture |
| category | evidence-capture |
| selectorsIn → selectorsOut | social-profile, domain → image, metadata |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | yes |
