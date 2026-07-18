---
id: return-youtube-comment-username
name: Return YouTube Comment Username
description: Use when you are reading YouTube comments and want the legacy `username` behind an @handle — a browser extension that restores the old display name alongside the handle.
url: https://chromewebstore.google.com/detail/return-youtube-comment-us/kamibelompadnaekbellinmgbphoidmj
category: social-networks
path:
- social-networks
bestFor: Showing a commenter's old-style username next to their @handle throughout the YouTube comments UI.
selectorsIn:
- username
selectorsOut:
- username
- social-profile
status: live
pricing: free
costNote: Free open-source Chrome/Chromium extension; no account or payment.
opsec: passive
opsecNote: The extension only re-renders data YouTube already serves in the page — it makes no extra request to the target and sends no signal to the commenter. Standard passive browsing; still view YouTube in a sock-puppet/logged-out browser if the collection is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Open-source extension (dev yakisova41) with ~30k users and a 4.3 rating; it manipulates the page client-side. Vet the source before installing on an investigative machine, as with any extension.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Return YouTube Comment Username extension
tags:
- Social Media
- YouTube
- browser-extension
- username-resolution
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# Return YouTube Comment Username

> A browser extension that puts the old-style YouTube username back next to each @handle in the comments — recovering a second selector YouTube's handle migration hid.

## When to use
You are examining a YouTube video's comments and want more than the @handle to work with. Since YouTube's handle rollout, comment authors show only `@handle`; this extension surfaces the legacy display username alongside it, giving you a second identifier per commenter to pivot on. Handy when a handle is generic but the display name is distinctive, or vice-versa, and you are mapping a community of commenters.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the extension from the Chrome Web Store (works in Chrome/Chromium/Edge) on your investigation browser profile.
2. In its options, choose a display format — username only, `@handle (Username)`, or `Username (@handle)`.
3. Open any YouTube video and scroll the comments; author lines now render both the handle and the restored username.
4. Collect both selectors per commenter of interest.
5. Pivot: run each `username`/handle through cross-platform account checkers and open the channel (`social-profile`) for further detail.

## Inputs → Outputs
- **In:** `username` (the @handle you see in comments; the extension augments it in place)
- **Out:** `username` (restored legacy display name) + `social-profile` (channel link) shown together
- **Empty/negative result looks like:** the comment shows only the @handle with no added name — happens when the account never had a legacy username or YouTube doesn't expose it for that author; not every commenter resolves.

## Gotchas & OpSec
- Client-side only: it re-labels what YouTube already sends, so it cannot recover data the page doesn't contain.
- It is a third-party extension — install it on a sandboxed/investigation profile and review the open-source code before trusting it on a sensitive machine.
- Passive; no request reaches the commenter.

## Overlaps ("do both")
- Feeds the username/account-enumeration tools in the [[social-networks]] and [[username]] sets — this recovers the extra handle-plus-name pair, those spread each identifier across other platforms.

## Trust & verifiability
`trust: community` — a popular open-source extension, but unvetted third-party code running in your browser. Confirm any resolved username by opening the actual channel before attributing it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | return-youtube-comment-username |
| category | social-networks |
| selectorsIn → selectorsOut | username → username, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
