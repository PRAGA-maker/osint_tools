---
id: now-gg
name: now.gg
description: Use when you need to run a mobile messaging/social app (WhatsApp, Telegram, TikTok, etc.) in a disposable cloud Android instance — OpSec infrastructure for investigating apps without installing them on your own device.
url: https://now.gg/
category: messaging
path:
- messaging
bestFor: Running mobile-only OSINT/messaging apps in a browser-based cloud Android device, isolated from your real phone.
selectorsIn: []
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free browser-based cloud Android sessions (ad-supported / time-limited); paid tiers remove limits and add persistence.
opsec: active
opsecNote: This is OpSec *infrastructure* — a throwaway Android in the cloud so you don't install a target's messaging app on your own device or leak your real IMEI/number. Use a sock-puppet account and number inside it; remember the app you run may still notify the target (e.g. WhatsApp "last seen", contact adds). Content lives on now.gg's servers, so treat sessions as non-private.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A legitimate cloud-Android/gaming service (from the makers of BlueStacks); reliable as an emulator, but a third party that sees whatever you do in the session — not for sensitive credentials.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- now gg
- nowgg cloud android
tags:
- messengerapps
- Messenger Apps
- opsec
- emulator
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# now.gg

> A browser-based cloud Android device — run mobile-only messaging and social apps in a disposable instance, so you investigate them without touching your real phone.

## When to use
Much OSINT-relevant activity lives in mobile-only apps (WhatsApp, Telegram, TikTok, Signal, dating apps). Installing those on your own device risks leaking your number/IMEI, contaminating your contacts, or tying the activity to you. now.gg gives you a throwaway Android in the browser to run such an app from a clean environment — ideal for driving app-based lookups behind a sock puppet. It's tooling/infrastructure, not a lookup itself; the `social-profile` output is whatever the app you run surfaces.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://now.gg/ and launch a cloud Android session (register if needed).
2. Install the target app inside the cloud device from its app store.
3. Sign in with a **sock-puppet account and burner number** (see `[[giffgaff-com]]` for UK SIMs) — never your real identity.
4. Perform the app-based check (e.g. add a number to see a WhatsApp profile photo/last-seen) mindful that the app may notify the target.
5. Pivot: profile photos → reverse-image; discovered handles/contacts → cross-platform checks. Discard the session afterwards.

## Inputs → Outputs
- **In:** none directly (you provision an Android; the app inside does the lookups)
- **Out:** whatever the run app exposes — e.g. a `social-profile`, profile photo, or presence signal
- **Empty/negative result looks like:** N/A for the emulator itself; "no result" comes from the app you run, not now.gg.

## Gotchas & OpSec
- Not private: the session runs on now.gg's servers — never enter real credentials or sensitive data you can't afford a third party to hold.
- The app you run can still alert the target (contact adds, read receipts, "last seen") — sock-puppet discipline applies inside the emulator.
- Free sessions are time-limited/ad-supported and non-persistent; expect to redo setup.

## Overlaps ("do both")
- Pairs with `[[giffgaff-com]]` (burner number to register apps) and local emulators (Genymotion/Android Studio) — local gives full privacy/control, now.gg gives zero-install convenience.

## Trust & verifiability
`trust: community` — a legitimate cloud-Android service; dependable as an emulator, but a third party with visibility into your session, so keep sensitive material out and use it purely as disposable investigative infrastructure.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | now-gg |
| category | messaging |
| selectorsIn → selectorsOut |  → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
