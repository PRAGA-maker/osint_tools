---
id: khoji-onrender-com
name: Khoji (Snapchat Bitmoji Viewer)
description: Use when you have a Snapchat `username` and want to confirm the account and see its Bitmoji avatar — returns the account's Bitmoji image and existence signal.
url: https://khoji.onrender.com/
category: social-networks
path:
- social-networks
bestFor: Confirming a Snapchat account exists and pulling its Bitmoji avatar image for a given username.
selectorsIn:
- username
selectorsOut:
- image
- social-profile
status: degraded
pricing: free
costNote: Free hobby tool hosted on Render's free tier; no account or payment. Free-tier hosting means cold starts and occasional downtime.
opsec: passive
opsecNote: It queries Snapchat's public Bitmoji endpoint, not the user directly, so the target is not notified. Run from a research context; a returned Bitmoji only confirms account existence, not identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source hobby tool (by developer Ashar, inspired by Micah Hoffman's Backmoji). It surfaces public Snapchat Bitmoji data; reliability depends on both free hosting and Snapchat's endpoint.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- epieos
- quick-cache-and-archive-search
aliases:
- Khoji
- Bitmoji viewer
- Backmoji-style tool
tags:
- snapchat
- Snapchat
- bitmoji
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Khoji (Snapchat Bitmoji Viewer)

> A Bitmoji lookup for Snapchat: enter a username, get back the account's Bitmoji avatar — a quick, quiet way to confirm the account exists.

## When to use
You have a candidate Snapchat `username` and want to (a) confirm an account actually exists under it and (b) see its Bitmoji avatar, which can corroborate identity (matching a known avatar) or give you a visual to compare. Because Snapchat itself exposes little publicly, a Bitmoji-existence check like this is one of the few passive signals available for a Snapchat handle.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://khoji.onrender.com/ (allow for a slow first load — free hosting cold-starts).
2. Enter the Snapchat `username`.
3. Read the result: if a Bitmoji avatar returns, the account exists and you have its avatar `image`; if nothing returns, no public Bitmoji is associated.
4. Compare the avatar against known images/other accounts of the subject.
5. Pivot: a confirmed handle feeds broader username/account searches (e.g. `[[epieos]]` from an associated email/phone); the avatar feeds visual comparison.

## Inputs → Outputs
- **In:** `username` (Snapchat)
- **Out:** `image` (Bitmoji avatar), `social-profile` existence signal
- **Empty/negative result looks like:** no Bitmoji returned / error. This can mean the account doesn't exist, has no Bitmoji set, or (commonly) the free host is asleep or Snapchat's endpoint changed — retry before concluding the account is absent.

## Gotchas & OpSec
- **Status degraded:** free Render hosting sleeps between uses (slow/failed first loads) and the tool depends on Snapchat's undocumented endpoint, which can break it.
- A Bitmoji confirms account *existence*, not who owns it — avatars are not unique identity proof.
- Not every account has a Bitmoji; absence of an avatar ≠ absence of an account.
- OpSec: passive; queries a public endpoint, not the user.

## Overlaps ("do both")
- Pairs with `[[epieos]]` and account-existence checks — Khoji confirms the Snapchat handle side, Epieos maps an email/phone to accounts; together they cross-confirm a subject's identity across platforms.

## Trust & verifiability
`trust: community` — an open-source hobby project surfacing genuine public Bitmoji data. Treat a returned avatar as an existence signal to corroborate, and expect intermittent availability given its free hosting and reliance on Snapchat's endpoint.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | khoji-onrender-com |
</content>
