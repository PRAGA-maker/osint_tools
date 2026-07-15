---
id: ig-exporter-chrome-google-com
name: IG Exporter / Exporter for Followers (Chrome extension)
description: Use when you have an Instagram `username` and want to export their followers/following (with bio, email and website) to CSV for associate-network analysis — returns associate, social-profile, email.
url: https://chromewebstore.google.com/detail/ig-exporter/nmnhoiehpdfllknopjkhjgoddkpnmfpa
category: social-networks
path:
- social-networks
bestFor: Bulk-exporting an Instagram account's follower/following lists (up to ~50k, with bio/email/website in detailed mode) to a spreadsheet for network mapping.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
- username
- email
status: live
pricing: freemium
costNote: Free Chrome extension with fast and detailed export modes (detailed adds bio/email/website); higher-volume/detailed exports may be gated by a paid upgrade.
opsec: active
opsecNote: The extension scrapes Instagram through YOUR logged-in session, so requests come from your account and IP and can trigger rate-limits, action-blocks or bans — the developer explicitly warns against using your primary account. Use a dedicated sock-puppet Instagram account and a clean browser profile, and pace exports.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: browser-extension
trust: unverified
trustNote: Popular third-party Chrome extension (~500k users, ~4.2★, updated 2025) but its Web Store listing declares it collects personally identifiable and payment information; it runs inside your Instagram session — vet the privacy policy and use only a throwaway account.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
invitationOnly: false
aliases:
- IG Exporter
- Exporter for Followers
tags:
- instagram
- Instagram Related Sites
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# IG Exporter / Exporter for Followers (Chrome extension)

> A browser extension that exports an Instagram account's followers and following — with bio, email and website in detailed mode — to CSV, turning a single `username` into a spreadsheet of the subject's network.

## When to use
You have a target Instagram `username` and want their follower/following graph as structured data for associate analysis, including any public bio/email/website fields the detailed export captures. Ideal for mapping a subject's real-world circle, finding mutuals between accounts, or harvesting contact fields exposed in bios.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "IG Exporter / Exporter for Followers" from the Chrome Web Store.
2. Log Chrome into a **sock-puppet** Instagram account (never your primary — the developer warns of blocks).
3. Open the target profile, launch the extension, and choose fast (handles only) or detailed (adds bio/email/website) export, up to ~50k followers.
4. Export to CSV/Excel and analyse: cross-reference follower vs following for mutuals, cluster by shared connections, extract emails from bios.
5. Pivot: harvested `email`s feed email-OSINT; distinctive handles feed `[[social-search-engine]]`; mutuals become `associate` leads.

## Inputs → Outputs
- **In:** `username` (public target, or one your sock puppet can view)
- **Out:** CSV of `social-profile`/`associate` handles (followers, following), plus `email`/website/bio in detailed mode — each row a new `username`
- **Empty/negative result looks like:** an empty/partial export or an action-block error — usually a private account, an Instagram rate-limit, or the extension being throttled; a truncated list is not the full network.

## Gotchas & OpSec
- OpSec: **active and risky** — scrapes via your logged-in session; Instagram may rate-limit or ban the account used. Always use a disposable account and pace exports.
- The listing declares collection of PII and payment info — treat the extension as untrusted; isolate it in a dedicated browser profile.
- Private targets yield only what your logged-in account can already see.
- Scraping breaches Instagram's Terms of Service — understand your engagement's legal/ethical context.

## Overlaps ("do both")
- Near-duplicate capability to `[[insfo-ig-follower-export-chrome-google-com]]` — if one is throttled or delisted, the other is a drop-in alternative; results should broadly agree, so use them to cross-check each other.

## Trust & verifiability
`trust: unverified` — a popular but third-party Chrome extension that runs inside your account context and self-declares PII/payment data collection; it is real and functioning, but use a sock puppet and verify exported handles/emails on-platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ig-exporter-chrome-google-com |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, associate, username, email |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | yes (account-login, rate-limit) |
