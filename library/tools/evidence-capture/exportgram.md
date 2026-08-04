---
id: exportgram
name: Exportgram
description: Use when you have an Instagram post/`social-profile` and want its comments as structured data — returns commenter `username`s, timestamps, likes and text as Excel/CSV/JSON.
url: https://exportgram.net/
category: evidence-capture
path:
- evidence-capture
bestFor: Bulk-exporting an Instagram post's comments (usernames, dates, text) into a spreadsheet for analysis and evidence.
selectorsIn:
- social-profile
selectorsOut:
- username
- social-profile
status: live
pricing: freemium
costNote: Free tier exports up to ~50 comments instantly with no account; a paid plan unlocks comment replies, larger exports and more formats.
opsec: passive
opsecNote: You paste a public post URL/data into a third-party web app that fetches the public comments; the target is not notified, but the export is processed on Exportgram's servers, so only use it on public content and keep the exported file in your evidence store.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party Instagram scraping utility; results depend on Instagram's current public access and can break or lag when Instagram changes, so timestamp and screenshot alongside the export.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- exportgram.net
- ExportGram
tags:
- instagram
- comments
- export
source: osintambition-social
lastVerified: '2026-08-04'
enrichment: full
---

# Exportgram

> A web utility that turns an Instagram post's comment thread into a spreadsheet — every commenter's `username`, timestamp, like count and text as Excel/CSV/JSON, for analysis and preservation.

## When to use
You are working a public Instagram post (a suspect's, a victim's, an event's) and need its comments as structured data rather than an endless scroll — to enumerate who is engaging (`username` → `social-profile`), spot associates, build a timeline, or preserve the thread as evidence before it is deleted. Exportgram bulk-extracts the comments into a file you can filter and cite.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://exportgram.net/ and provide the target public post (per the site's input method).
2. Run the export; the free tier returns up to ~50 comments instantly (paid plans go further and include replies).
3. Download as CSV/Excel/JSON and review commenter usernames, dates, likes and text.
4. Preserve properly: also screenshot the live thread and record the capture time — a scrape alone is weaker evidence than scrape + screenshot + timestamp.
5. Pivot: feed commenter `username`s into profile-search and cross-platform username tools to identify associates.

## Inputs → Outputs
- **In:** an Instagram post/`social-profile` (public)
- **Out:** commenter `username`s + their `social-profile`s, comment text, timestamps, like counts (spreadsheet/JSON)
- **Empty/negative result looks like:** no export or a truncated one — the post is private, deleted, or Instagram has changed access; a partial free-tier cap is expected, not an error.

## Gotchas & OpSec
- Human-in-the-loop: none, but capping at ~50 on free means large threads need the paid tier or repeated pulls.
- OpSec: passive — the account owner is not alerted; still restrict use to public content and treat the third-party processing accordingly.
- Evidence integrity: a scrape can be edited; pair it with a screenshot/archive and note capture time so it holds up as evidence.

## Overlaps ("do both")
- Pairs with username-search and profile tools because the export yields commenter handles that those tools resolve into identities and other-platform presence.

## Trust & verifiability
`trust: community` — a third-party scraper dependent on Instagram's shifting public access; verify the export against the live thread and preserve corroborating captures.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
