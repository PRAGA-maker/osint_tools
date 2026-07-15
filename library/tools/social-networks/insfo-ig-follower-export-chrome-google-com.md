---
id: insfo-ig-follower-export-chrome-google-com
name: InsFo IG Follower Export (Chrome extension)
description: Use when you have an Instagram `username` and want to export and map their followers/following/commenters as an associate graph — returns social-profile, associate, username.
url: https://chromewebstore.google.com/detail/insfo-ig-follower-export/bckleejkdhlponanidmjfjdigpahlado
category: social-networks
path:
- social-networks
bestFor: Bulk-exporting an Instagram account's follower/following/commenter/tag lists to CSV for associate-network analysis.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
- username
status: live
pricing: free
costNote: Free Chrome extension (data exported to CSV/Excel); some analytics features may be gated behind an upgrade.
opsec: active
opsecNote: The extension scrapes Instagram through YOUR logged-in session, so requests come from your account and IP and can trigger Instagram rate-limits, action blocks or bans. Use a dedicated sock-puppet Instagram account and a clean browser profile — never your real account. Scraping is against Instagram's ToS.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: browser-extension
trust: unverified
trustNote: Third-party Chrome extension (~10k users, ~4.3★); publisher offers several similar scrapers. It runs inside your Instagram session, so it has access to your account context — vet the privacy policy and use only a throwaway account.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
invitationOnly: false
aliases:
- insfo ig follower export
- InsFo Instagram export
tags:
- instagram
- Instagram Related Sites
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# InsFo IG Follower Export (Chrome extension)

> A browser extension that dumps an Instagram account's followers, following, commenters and tagged users to a spreadsheet — turning a single `username` into a mappable associate network.

## When to use
You have a target Instagram `username` and want their social graph as data: who follows them, who they follow, who comments, who they tag. That list of connections is a rich `associate` source for identifying family, friends and links between accounts — often the fastest way to expand from one profile to a person's real-world circle.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "InsFo IG Follower Export" from the Chrome Web Store.
2. Log Chrome into a **sock-puppet** Instagram account (never your real one).
3. Navigate to the target profile and open the extension.
4. Choose what to export (followers / following / comments / tags / locations) and export to CSV/Excel.
5. Analyse the CSV: cross-reference follower and following lists for mutuals, cluster by shared connections, and flag distinctive handles.
6. Pivot: distinctive `username`s feed username-enumeration and `[[social-search-engine]]`; named/real-name accounts feed people-search.

## Inputs → Outputs
- **In:** `username` (the target Instagram account, which must be public or one your sock puppet can view)
- **Out:** CSV of `social-profile`/`associate` handles (followers, following, commenters, tagged), each a new `username`
- **Empty/negative result looks like:** an empty/partial export or an error — usually a private account, an Instagram rate-limit/action-block, or the extension being throttled; a truncated list is not the full network.

## Gotchas & OpSec
- OpSec: **active and risky** — it scrapes via your logged-in session; Instagram may rate-limit, action-block or ban the account used. Always use a disposable account and pace exports.
- Private targets: you only get what your logged-in account can already see.
- Trust: a third-party extension with access to your Instagram session — treat it as untrusted, isolate it in a dedicated browser profile, and review its data-handling before use.
- Scraping violates Instagram's Terms of Service; understand the legal/ethical context of your engagement.

## Overlaps ("do both")
- Pairs with `[[social-search-engine]]` — export the follower graph here, then resolve the interesting handles across other networks with a broad aggregator.

## Trust & verifiability
`trust: unverified` — a popular but third-party Chrome extension; it is real and functioning (confirmed listed, ~10k users), but it runs inside your account context and its data handling is not independently audited, so use a sock puppet and verify exported handles on-platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | insfo-ig-follower-export-chrome-google-com |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, associate, username |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | yes (account-login, rate-limit) |
