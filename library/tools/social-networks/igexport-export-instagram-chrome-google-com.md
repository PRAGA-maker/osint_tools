---
id: igexport-export-instagram-chrome-google-com
name: igexport / Followers Exporter (Instagram, Chrome)
description: Use when you have an Instagram `social-profile` and want its full follower/following list as a spreadsheet — returns username, name, image, and (detailed mode) email/phone.
url: https://chrome.google.com/webstore/detail/igexport-export-instagram/ehbjlcniiagahknoclpikfjgnnggkoac
category: social-networks
path:
- social-networks
bestFor: Exporting a target Instagram account's followers/following (with profile fields) to CSV/Excel for pivoting.
selectorsIn:
- social-profile
- username
selectorsOut:
- username
- name
- image
- email
- phone
- social-profile
status: live
pricing: freemium
costNote: Free tier exports basic fields (username, ID, name, profile-pic, verified). "Detailed mode" enrichment (public email, phone, bio, website) and very large exports are typically gated behind a paid upgrade.
opsec: active
opsecNote: The extension scrapes through YOUR logged-in Instagram session, so the requests come from your account and IP — Instagram can rate-limit, action-block, or ban the account for bulk follower pulls. Always use a burner/sock-puppet Instagram login and a clean browser, never your real identity. The vendor claims local-only processing, but that is unverified.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: browser-extension
trust: unverified
trustNote: Third-party Chrome extension (has appeared under names like "Followers Exporter") that requires Instagram access; it has broad permissions over your session and its local-only-processing claim is not independently verified. Treat as untrusted with a sock puppet.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
aliases:
- igexport
- Followers Exporter
- IG Exporter
tags:
- instagram
- Instagram Related Sites
- follower-export
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# igexport / Followers Exporter (Instagram, Chrome)

> A Chrome/Edge extension that dumps an Instagram account's followers or following list — with profile fields — to CSV/Excel via your own logged-in session.

## When to use
You have a subject's Instagram `social-profile` (public, or one your sock-puppet can view) and you want the *list* behind it: who follows them / who they follow, as structured rows you can filter, dedupe, and pivot on. Useful for building an `associate` map or spotting a subject's alternate accounts among their followers.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the extension from the Chrome Web Store into a clean browser profile.
2. Log in to Instagram with a **burner** account (never your real one).
3. Navigate to the target profile, open the extension, and choose Followers or Following.
4. Let it page through (respect its cooldown/rate-limit handling), then export to CSV/Excel.
5. Pivot: feed the exported `username`s into username-search tools; public `email`/`phone` (detailed mode) feed email/phone OSINT; profile-pic URLs feed reverse-image/face search.

## Inputs → Outputs
- **In:** `social-profile` / `username` of the Instagram account whose list you want
- **Out:** rows of `username`, numeric ID, `name`, profile-pic `image`, verified flag; detailed mode adds public `email`, `phone`, bio, website
- **Empty/negative result looks like:** an empty/partial export, a "rate limited" pause, or a private account you can't view — Instagram throttling or access limits, not necessarily a tool failure.

## Gotchas & OpSec
- Human-in-the-loop: you must be logged into Instagram (account-login) and babysit rate-limit cooldowns on big lists.
- OpSec: **active** — traffic originates from your account/IP; bulk scraping is a fast way to get an Instagram account action-blocked or banned. Sock puppet + clean browser, always.
- Trust: it's a third-party extension with access to your Instagram session; the "processed locally" claim is unverified. Assume it *could* exfiltrate; isolate it to a throwaway profile.

## Overlaps ("do both")
- Pairs with any reverse-image/face tool on the exported profile-pic URLs, and with username-search tools on the exported handles — this extension gets you the list; those resolve each row into a real person.

## Trust & verifiability
`trust: unverified` — an anonymous/renamed browser extension operating inside your authenticated Instagram session. It works, but the risk is on you: burner account, disposable browser profile, and don't feed it anything tied to your real identity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | igexport-export-instagram-chrome-google-com |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile, username → username, name, image, email, phone, social-profile |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | yes (account-login, rate-limit) |
