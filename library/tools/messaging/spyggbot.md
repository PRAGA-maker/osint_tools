---
id: spyggbot
name: SpyGGbot
description: Use when you have an NFT/crypto wallet address and want to track its holdings, ownership and floor prices via Telegram — returns crypto-wallet activity and ownership links.
url: https://telegram.me/SpyGGbot
category: messaging
path:
- messaging
bestFor: Tracking NFT wallet holdings, ownership and floor prices from within Telegram.
selectorsIn:
- crypto-wallet
selectorsOut:
- crypto-wallet
status: live
pricing: free
costNote: Free Telegram bot for NFT/wallet tracking; some tracking bots gate alerts/extras behind credits.
opsec: passive
opsecNote: You query on-chain/marketplace data that is already public; the wallet owner is not notified. You must, however, message the bot from a Telegram account, which exposes your querying account to the bot operator — use a burner Telegram identity for research.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: An anonymous Telegram bot (bio pitches NFT wallet/floor-price/ownership tracking); provenance and continuity of the handle are unverifiable, so treat outputs as leads and confirm on a block explorer or marketplace directly.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
aliases:
- SpyGG bot
- SpyGGbot NFT tracker
tags:
- telegram
- crypto
- nft
- wallet-tracking
source: awesome-osint
lastVerified: '2026-07-16'
enrichment: full
relatedTools:
- avtogram-bot
- datxpert
- discord-sensor
- getchatlist
- getsendgifts
- instabot
- leak-osint
- oksearch
- pimeyes
- searchforchats
- unamer
---

# SpyGGbot

> A Telegram bot for NFT/crypto wallet intelligence — track a wallet's holdings, ownership, and NFT floor prices without leaving the app.

## When to use
You have a crypto wallet address (or NFT of interest) linked to a subject and want a quick read on what it holds, its NFT ownership, and current floor prices. Blockchain activity is public and immutable, so a wallet can corroborate a subject's crypto footprint, connect them to marketplaces, or reveal linked wallets. Missing-persons relevance is low and situational — reach for this only when a case genuinely involves crypto/NFT assets, and treat every result as a lead to confirm on a primary block explorer.

## How to use it (`bestInteractionPattern`: web-manual)
1. From a **burner** Telegram account, open https://telegram.me/SpyGGbot and press Start.
2. Send the wallet address (or follow the bot's prompt to track a wallet/collection).
3. Read the response: holdings, ownership, and floor-price data the bot surfaces from marketplaces/chain.
4. Pivot: take any wallet address or collection returned to a full block explorer (Etherscan and equivalents) and marketplace pages to verify and expand.

## Inputs → Outputs
- **In:** `crypto-wallet` (a wallet address / NFT reference)
- **Out:** `crypto-wallet` holdings, ownership links, and floor-price context
- **Empty/negative result looks like:** no holdings / "nothing found" — meaning the wallet is empty of tracked assets or outside the bot's coverage, not that the address is invalid; confirm on-chain.

## Gotchas & OpSec
- Human-in-the-loop: requires a Telegram account to message the bot (account-login).
- OpSec: the on-chain data itself is public and querying it is passive, but the bot operator sees your Telegram account — use a research persona.
- The @SpyGGbot handle currently presents as an NFT/wallet tracker; older OSINT lists may have referenced a different tool under this name. Verify you're using the current bot and confirm data on primary sources.

## Overlaps ("do both")
- For anything load-bearing, corroborate with a first-party block explorer rather than trusting the bot's summary; pair with dedicated crypto-address OSINT tools for deeper tracing.

## Trust & verifiability
`trust: unverified` — an anonymous Telegram bot with no accountability. Because the underlying blockchain data is public, you can and should independently verify every claim on a primary explorer or marketplace.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | spyggbot |
| category | messaging |
| selectorsIn → selectorsOut | crypto-wallet → crypto-wallet |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
