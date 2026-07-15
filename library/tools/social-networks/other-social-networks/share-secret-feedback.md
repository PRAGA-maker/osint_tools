---
id: share-secret-feedback
name: Share Secret Feedback
description: Use when you have a Secreto `username`/profile link (often shared from a subject's Instagram/Snapchat bio) and want to view their public anonymous-feedback page — returns the target's Secreto `social-profile` page.
url: https://secreto.site/en/%3Cuser_id%3E
category: social-networks
path:
- social-networks
- other-social-networks
bestFor: Viewing a subject's public Secreto anonymous-feedback profile page, discovered from a link they shared on other social platforms.
selectorsIn:
- username
- social-profile
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free; viewing a public Secreto page needs no account. Sending or reading received messages requires the page owner's own login, which you will not have.
opsec: passive
opsecNote: Loading a public Secreto profile page is a standard, unauthenticated web request that does not notify the owner. Passive. Do NOT submit an anonymous message to their page as an investigator — that is active contact with the subject and can reveal your interest.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Secreto.site is a real, live anonymous-feedback platform. The value here is confirming a subject's presence and capturing their public page; the anonymous messages they receive are private and not visible to you.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Secreto
- secreto.site
tags:
- secreto
- anonymous-feedback
- other-social-networks
source: arf-seed
lastVerified: '2026-07-15'
enrichment: full
---

# Share Secret Feedback (Secreto)

> Secreto is an "anonymous message" link people post in their social bios — this entry is about finding and viewing a subject's public Secreto page, which confirms another account they own.

## When to use
While profiling a subject you find a Secreto link (`secreto.site/...`) in their Instagram/Snapchat/TikTok bio or a story. Secreto lets a person share a link to collect anonymous messages; the *link itself* is a pivot — it confirms an account the subject controls and adds a username to your map. You can view their public page; you cannot read the private messages they've received.

## How to use it (`bestInteractionPattern`: web-manual)
1. Take the Secreto link/username you found (replace the `<user_id>` placeholder in the URL with the actual handle, e.g. `https://secreto.site/en/theirname`).
2. Open it in a research/sock-puppet browser.
3. Confirm the public profile page loads — the display name and any public elements corroborate the subject's identity and username reuse.
4. Record the handle and cross-reference it against other platforms (username enumeration) — people reuse Secreto handles.
5. Pivot: feed the confirmed `username` into cross-platform username search; **do not** submit an anonymous message to the target.

## Inputs → Outputs
- **In:** a Secreto `username`/profile `social-profile` link
- **Out:** the subject's public Secreto `social-profile` page (existence + display name + reusable handle)
- **Empty/negative result looks like:** a 404/"page not found" means the handle is wrong or the page was removed; a loading page with no readable content is normal — the received messages are private and never shown to visitors.

## Gotchas & OpSec
- You **cannot** read the anonymous messages a person received — those are visible only to the logged-in owner.
- **Never** send an anonymous message to the target's page during an investigation; that is active contact and can tip them off.
- The stored URL uses a `<user_id>` placeholder — substitute the real handle before visiting.
- OpSec: **passive** when only viewing; sending anything flips it to active.

## Overlaps ("do both")
- Pairs with cross-platform username tools — a Secreto handle is a lead to run through username enumeration to surface the same person's other accounts.

## Trust & verifiability
`trust: unverified` — Secreto is a genuine live platform, but its investigative worth is narrow: it confirms an account exists and yields a reusable handle. It does not expose the private feedback, so treat it as a corroboration/pivot point, not a content source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | share-secret-feedback |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
