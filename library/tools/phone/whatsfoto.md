---
id: whatsfoto
name: whatsfoto
description: Use when you have one or more `phone` numbers and want their WhatsApp profile photos in bulk — returns downloaded profile `image`s (zipped).
url: https://github.com/zoutepopcorn/whatsfoto
category: phone
path:
- phone
bestFor: Bulk-downloading WhatsApp profile pictures for a list of phone numbers via a Chrome extension.
selectorsIn:
- phone
selectorsOut:
- image
status: live
pricing: free
costNote: Free and open source (MIT). No cost, but requires a logged-in WhatsApp Web session on your own WhatsApp account.
opsec: active
opsecNote: It drives YOUR logged-in web.whatsapp.com session to look up each number, so the checks are tied to your WhatsApp account and phone. Numbers you query may end up as contacts/known to WhatsApp. Use a dedicated sock-puppet WhatsApp account and number, never your real one, and remember that querying can be visible in your account's activity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: community
trustNote: Small open-source (MIT) Chrome extension by zoutepopcorn; inspect the source before loading it, since it runs inside your authenticated WhatsApp session.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
aliases:
- whats foto
tags:
- whatsapp
- profile-photo
source: osintambition-social
lastVerified: '2026-07-17'
enrichment: full
---

# whatsfoto

> A Chrome extension that harvests WhatsApp profile photos for a list of numbers — a bulk version of "does this number have WhatsApp, and what's the picture?"

## When to use
You have one or more `phone` numbers and want the WhatsApp profile `image` for each — to confirm a number is on WhatsApp, to grab a face for reverse-image search, or to compare a photo against a known subject. It shines when you have many numbers to check at once rather than eyeballing them one by one in the app.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Clone/download the repo from GitHub and load the folder as an unpacked extension in Chrome (enable Developer mode → "Load unpacked").
2. Open and log in to https://web.whatsapp.com (ideally on a sock-puppet WhatsApp account, not your personal one).
3. Feed the extension your numbers in CSV form (e.g. `31600000000`; leading `06…` is auto-converted to `316…` — mind the country-code formatting for your target region).
4. Run it; it fetches each number's current profile photo and packages the results into a downloadable zip.
5. Pivot: run recovered `image`s through reverse-image / face-search tools; a returned photo also confirms the number is active on WhatsApp.

## Inputs → Outputs
- **In:** `phone` number(s), CSV
- **Out:** WhatsApp profile `image`(s), zipped
- **Empty/negative result looks like:** no image for a number — either the number isn't on WhatsApp, or the user has set profile-photo privacy so only their contacts can see it (a blank/placeholder). Absence is not proof the number is unused.

## Gotchas & OpSec
- **Active** and account-bound: it operates through your logged-in WhatsApp session, so activity is attributable to that account and number. Always use a dedicated burner account/number.
- Privacy settings and the country-code format are the two big failure modes — many users hide their photo from non-contacts, and mis-formatted numbers silently return nothing.
- It's an unpacked extension running inside your authenticated WhatsApp: read the (small, JS) source first; don't load code you haven't reviewed into a session that holds your account.

## Overlaps ("do both")
- Do both with a manual WhatsApp check and with reverse-image search: whatsfoto gets the photo at scale, reverse-image search then tells you where else that face/photo appears. Pair with other `phone`-to-identity tools to corroborate the number's owner.

## Trust & verifiability
`trust: community` — small MIT-licensed open-source project; the code is inspectable, but because it runs inside your WhatsApp session the trust burden is on you to review it before use. The photo it returns is authoritative (straight from WhatsApp), subject to the target's privacy settings.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whatsfoto |
| category | phone |
| selectorsIn → selectorsOut | phone → image |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | yes (account-login) |
