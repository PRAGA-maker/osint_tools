---
id: find-my-facebook-id-2
name: Find My Facebook ID (CommentPicker)
description: Use when you have a Facebook profile/page/group URL or vanity name and want its stable numeric ID — returns the numeric Facebook ID for use in other lookups.
url: https://commentpicker.com/find-facebook-id.php
category: social-networks
path:
- social-networks
bestFor: Converting a Facebook vanity URL or username into the permanent numeric user/page/group ID.
selectorsIn:
- social-profile
- username
selectorsOut:
- social-profile
- document-id
status: live
pricing: free
costNote: Free, no login, no stated usage cap; ad-supported.
opsec: passive
opsecNote: You paste a public Facebook URL into CommentPicker's server, which resolves it via Facebook's public graph — the target is not notified. The operator logs the URL you submit; avoid pasting URLs that would reveal your active investigation focus if you are cautious, and use a VPN. It does not require you to log into Facebook.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: CommentPicker is a long-running giveaway/tools site; the ID it returns is verifiable against Facebook itself, so accuracy is easy to confirm even though the operator is a third party.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- CommentPicker Facebook ID finder
- Find Facebook ID
- facebook id lookup
tags:
- facebook
- id-lookup
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
relatedTools:
- commentpicker
- commentpicker-com
- commentpicker-com-2
- instagram-user-id
- youtube-channel-id
---

# Find My Facebook ID (CommentPicker)

> A one-field converter that turns a Facebook vanity URL or username into the account's permanent numeric ID — the key that stays constant even when the display name and vanity URL change.

## When to use
You have a Facebook `social-profile` URL (or a vanity `username` like `facebook.com/john.smith.123`) and need its underlying numeric ID. That numeric ID is the durable handle for a Facebook identity: it survives name changes and lets you build direct graph URLs, feed other Facebook-OSINT tools, and re-find a profile that has since renamed itself. Getting the ID is often the first step before deeper Facebook enumeration.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://commentpicker.com/find-facebook-id.php.
2. Paste the target's full Facebook profile, page or group URL into the input.
3. Submit — the tool resolves it and displays the numeric ID.
4. Copy the ID. Build direct URLs from it (e.g. `facebook.com/<id>`) or feed it to other Facebook lookup/graph tools.
5. Pivot: the numeric ID feeds Facebook photo/friends enumeration and lets you re-locate the profile after any future rename.

## Inputs → Outputs
- **In:** a Facebook profile/page/group URL, or a vanity `username`
- **Out:** the numeric Facebook `document-id` (the stable account ID), re-usable as a `social-profile` anchor
- **Empty/negative result looks like:** an error or blank when the URL is malformed, the account is deleted, or the profile is fully private/unresolvable. Re-check the URL form (must be a real facebook.com link) before concluding the account is gone.

## Gotchas & OpSec
- Works for profiles, pages and groups; make sure you pasted a canonical `facebook.com/...` URL, not a mobile/`m.` or share-tracking link.
- Passive — the target is not alerted — but CommentPicker logs the submitted URL and is ad-heavy; use a VPN and ignore sponsored buttons.
- Verify a surprising ID by opening `facebook.com/<id>` yourself; the number should load the same profile you started from.

## Overlaps ("do both")
- Pairs with `[[find-my-facebook-id-2]]`-adjacent lookupid.com-style tools as a cross-check — if two independent resolvers return the same numeric ID, you can trust it.
- Feeds Facebook photo/friend enumeration tools that require the numeric ID rather than the vanity name.

## Trust & verifiability
`trust: community` — a third-party utility, but its output is self-verifying: paste the returned ID back into `facebook.com/<id>` and confirm it loads the original profile, so accuracy does not depend on trusting the operator.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | find-my-facebook-id-2 |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile, username → social-profile, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
