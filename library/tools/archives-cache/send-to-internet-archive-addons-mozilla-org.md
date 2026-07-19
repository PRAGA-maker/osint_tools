---
id: send-to-internet-archive-addons-mozilla-org
name: Send to Internet Archive (Firefox add-on)
description: Use when you have a live page/URL you want preserved as evidence — one click sends it to the Wayback Machine, returning a timestamped archive URL (document-id).
url: https://addons.mozilla.org/en-US/firefox/addon/send-to-internet-archive/
category: archives-cache
path:
- archives-cache
bestFor: One-click preservation of the page you're viewing (or a right-clicked link) into the Internet Archive before it changes or is deleted.
selectorsIn:
- domain
selectorsOut:
- document-id
status: degraded
pricing: free
costNote: Free open-source Firefox add-on; no account. Relies on the free Internet Archive Save Page Now service.
opsec: active
opsecNote: Saving a page makes the Internet Archive FETCH the live URL — that fetch comes from Archive's IP (not yours) but can appear in the target site's logs, and the archived copy becomes public. Don't archive a page if a fetch or a public permanent copy would tip off the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Community-built add-on that simply calls the Internet Archive; the archiving itself is done by the trusted Archive, but the extension is dated (last updated 2019) and may need compatibility checking.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- web-archive-org
- archive-org
aliases:
- Send to Internet Archive Firefox extension
tags:
- archive
- Archive & Cached Related Sites
source: uk-osint
lastVerified: '2026-07-19'
enrichment: full
---

# Send to Internet Archive (Firefox add-on)

> A toolbar-button shortcut for "Save Page Now" — capture the page you're on into the Wayback Machine in one click, so volatile evidence is preserved with a timestamp.

## When to use
You're viewing a live page — a social profile, a listing, a news article, a company page — that could be edited or deleted, and you want a timestamped, citable copy before it vanishes. This add-on pushes the current tab (or a right-clicked link) to the Internet Archive without breaking your browsing flow, which is faster than manually visiting web.archive.org/save for each page during active research.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Send to Internet Archive" from Firefox Add-ons (verify it works with your Firefox version — it's dated).
2. On a page you want to preserve, click the toolbar button; it opens a background tab that submits the URL to archive.org while keeping focus on your page.
3. Or right-click a link and choose the archive option to save that target URL.
4. Record the resulting Wayback `document-id`/archive URL in your case notes as evidence.
5. Pivot: the permanent snapshot backs your report; later, browse the same URL on `[[web-archive-org]]` to compare captures over time.

## Inputs → Outputs
- **In:** the current page URL / a `domain`+path (or right-clicked link)
- **Out:** a timestamped Internet Archive snapshot → `document-id` / archive URL
- **Empty/negative result looks like:** the save fails or no snapshot URL appears — the target blocks archiving (robots/anti-bot), the page needs login, or the add-on is broken on your Firefox version; fall back to manual Save Page Now or `[[archive-today]]`.

## Gotchas & OpSec
- Human-in-the-loop: none, but confirm the snapshot actually saved (dated add-on may misbehave).
- OpSec: **active** — archiving triggers a live fetch of the target (from Archive's IP) and creates a public permanent copy; don't archive if either would alert the subject or expose the investigation.
- Login-gated or JS-heavy pages often archive incompletely; check the snapshot captured what you needed.

## Overlaps ("do both")
- Pairs with `[[web-archive-org]]` and `[[archive-org]]` — this add-on is the fast "save now" trigger, while web.archive.org is where you browse and compare the historical captures it creates.

## Trust & verifiability
`trust: community` — the extension is a thin, dated community wrapper, but the archiving and timestamp come from the trusted Internet Archive; the snapshot itself is authoritative even though the add-on may need a compatibility check.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | send-to-internet-archive-addons-mozilla-org |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | no |
