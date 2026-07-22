---
id: reddit-onions
name: r/onions (Reddit)
description: Use when you have a dark-web keyword, service name, or `crypto-wallet` and want community reports on current .onion sites and their status — returns onion `domain` leads and scam warnings.
url: https://www.reddit.com/r/onions/
category: dark-web
path:
- dark-web
- general-info
bestFor: Crowd-sourced discovery and vetting of .onion services — which are live, which are scams, which just moved.
selectorsIn:
- domain
- username
selectorsOut:
- domain
- social-profile
status: live
pricing: free
costNote: Free to read; a Reddit account (optional, sock-puppet) is only needed to post or search while logged in.
opsec: passive
opsecNote: Reading the subreddit on the clearnet is passive. Do NOT open .onion links mentioned here in a normal browser — use Tor Browser. Posting or commenting is attributable to your Reddit account, so use a sock puppet and never reveal case details.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Anonymous community reports; links are user-submitted and frequently include scams, phishing mirrors, and dead onions — verify everything independently.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- reddit
- reddit-darknet
- reddit-deep-web
- r-opendirectories
aliases:
- r/onions
- reddit onions
tags:
- dark-web
- Tor
- reddit
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# r/onions (Reddit)

> The Reddit hub for the .onion ecosystem — a crowd-sourced, clearnet-readable feed of which dark-web services exist, moved, or turned out to be scams.

## When to use
You're investigating something on the dark web and need current, human-vetted signal about .onion services: whether a market/forum is live, its new address after a move, or whether a link is a known phishing clone. Reachable on the clearnet, it's a low-risk way to orient before entering Tor. In a missing-persons/trafficking context it can surface which onion venues are active and where community discussion points.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.reddit.com/r/onions/ in a normal browser (reading is clearnet).
2. Search the subreddit for the service name, keyword, or `domain` of interest; sort by New for current status.
3. Read reports on whether a site is up, its verified address, and scam/phishing warnings.
4. Take any onion `domain` you decide to visit into **Tor Browser only** — never open it on the clearnet.
5. Pivot: a verified onion address feeds `[[iaca-dark-web-investigation-support]]` search engines; usernames/wallets mentioned feed further tracing.

## Inputs → Outputs
- **In:** dark-web keyword, service name, `domain`, or `username`
- **Out:** onion `domain` leads, operational-status reports, scam/phishing warnings, related `social-profile` handles
- **Empty/negative result looks like:** no recent posts on your target — common, since coverage is sporadic and community-driven. Absence of discussion is not evidence a service is gone.

## Gotchas & OpSec
- Links are anonymous and unvetted: phishing mirrors and scam addresses are routinely posted. Treat every onion link as suspect until independently confirmed.
- OpSec: read on clearnet, but open onions only in Tor. Posting/commenting ties to your Reddit identity — use a sock puppet and disclose nothing.
- Some threads discuss illegal content/markets; follow legal and organizational dark-web handling policy.

## Overlaps ("do both")
- Pairs with `[[iaca-dark-web-investigation-support]]` (onion search engines/directories) and other `reddit-darknet`/`reddit-deep-web` communities — cross-check a claimed address across sources before trusting it.

## Trust & verifiability
`trust: unverified` — anonymous crowd reports; useful as leads and early warning, but every address and status claim must be verified independently before you rely on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reddit-onions |
| category | dark-web |
