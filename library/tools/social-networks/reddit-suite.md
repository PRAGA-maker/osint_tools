---
id: reddit-suite
name: Reddit Suite
description: Use when you have a Reddit `social-profile`/username and want a browser layer that speeds investigation — inline user tagging, history navigation, and account context on hover.
url: https://chromewebstore.google.com/detail/reddit-enhancement-suite/kbmfpngjjgdllneeigpgjifpgocmfgmb
category: social-networks
path:
- social-networks
bestFor: Enhancing manual Reddit investigation with user tagging, navigation, and inline context.
selectorsIn:
- social-profile
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free, open-source browser extension (Reddit Enhancement Suite / RES); no account or payment.
opsec: passive
opsecNote: RES only augments how you view public Reddit in your own browser — it does not interact with the target. Passive, but you should still browse Reddit logged out or via a sock-puppet account to avoid tying your real account to the investigation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: A long-standing, widely-used open-source Reddit extension (RES); it enhances the interface only and surfaces no non-public data.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Reddit Enhancement Suite
- RES
tags:
- reddit
- browser-extension
source: awesome-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Reddit Suite

> Reddit Enhancement Suite (RES): a browser extension that turns manual Reddit investigation into a faster workflow — tag users, navigate their history, and see account context inline.

## When to use
You are working a Reddit `social-profile`/username by hand and want the interface to work for you: privately tag and annotate accounts (e.g. "same person as X"), expand a user's post/comment history without page-hopping, hover for account age/karma context, and keep long threads navigable. It adds no new data source — it makes the public data you already have far quicker to comb.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install Reddit Enhancement Suite from the Chrome Web Store (also available for Firefox) into a sock-puppet browser profile.
2. Browse to the target's Reddit profile or a thread, ideally logged out or on a burner account.
3. Use RES features: tag the account with a private note, use "never-ending reddit" and keyboard nav to review history, and read the inline account info on hover.
4. Pivot: patterns you spot (recurring subreddits, timezones from post times, shared handles) feed username enumeration (`[[username-generation-guide]]`) and cross-platform profile finding (`[[social-profiles-finder]]`).

## Inputs → Outputs
- **In:** a Reddit `social-profile`/username (viewed in-browser)
- **Out:** an enhanced view of that public profile — tags, full history, inline context (`social-profile` enrichment)
- **Empty/negative result looks like:** nothing new appears because the account is deleted/suspended or has no public activity — RES can't reveal what Reddit doesn't publicly show.

## Gotchas & OpSec
- It's a UI enhancer, not a data source — it won't deanonymize anyone or surface hidden data.
- Runs in your browser; keep it in a dedicated investigation profile so your tags and history stay separate from personal use.

## Overlaps ("do both")
- Pairs with `[[social-profiles-finder]]` and `[[username-generation-guide]]`: RES helps you extract signals from Reddit activity, which those tools then pivot into cross-platform identity leads.

## Trust & verifiability
`trust: community` — a mature, popular open-source extension that only re-renders public Reddit; nothing it shows requires trust beyond Reddit's own public data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reddit-suite |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
