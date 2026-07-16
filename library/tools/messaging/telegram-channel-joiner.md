---
id: telegram-channel-joiner
name: Telegram Channel Joiner
description: Use when you have a list of Telegram channel `username`s/links and want to bulk-join them from a sock-puppet account for monitoring — returns membership/access to those channels' content.
url: https://github.com/spmedia/Telegram-Channel-Joiner
category: messaging
path:
- messaging
bestFor: Automating a sock-puppet Telegram account into many channels/groups (rate-limit-safe) to set up bulk monitoring.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free and open-source (GitHub). Requires your own Telegram API credentials (free from my.telegram.org) and a Telegram account.
opsec: active
opsecNote: This joins channels using a real Telegram account, which becomes visible in each channel's member list and to admins. Use a dedicated sock-puppet account and number, never your own. The tool's built-in 300–600s random delay between joins is essential to avoid Telegram flood-bans — do not remove it.
humanInLoop: true
humanInLoopReason:
- account-login
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Community OSINT/CTI utility by a known practitioner (spmedia); uses the official Pyrogram library, so risk is account-ban, not malware — but review the code before running.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: true
aliases:
- Telegram Channel Joiner
- spmedia channel joiner
tags:
- telegram
- monitoring
- sock-puppet
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- crypto-scam-and-crypto-phishing-url-threat-intel-feed
- phishingseclists
- threat-actor-usernames-scrape
---

# Telegram Channel Joiner

> A Pyrogram script that bulk-joins a sock-puppet Telegram account into a list of channels/groups, throttled to survive rate limits — infrastructure for Telegram monitoring, not a lookup.

## When to use
You are building Telegram CTI/OSINT coverage and have a list of channel `username`s or invite links you want a monitoring account to be inside — e.g. channels connected to a subject, a topic, or a region. Rather than joining hundreds by hand (and getting flood-banned), this joins them slowly and unattended so you wake up with an account inside them all, ready to read.

## How to use it (`bestInteractionPattern`: cli)
1. Create a dedicated sock-puppet Telegram account (separate number).
2. Get API `id`/`hash` from https://my.telegram.org and install `pyrogram` + `tgcrypto`.
3. Clone https://github.com/spmedia/Telegram-Channel-Joiner, add your credentials and a text list of channel usernames/links.
4. Run the script and leave it — it joins with a random 300–600s gap between each to avoid bans (free accounts cap at 500 channels, Premium 1000).
5. Pivot: once inside, read/search the channels manually or with a Telegram scraper (e.g. `[[telegram-search]]`-class tools) to extract members, messages, and media tied to your target.

## Inputs → Outputs
- **In:** a list of Telegram channel `username`s / invite links
- **Out:** your sock-puppet account's membership in those channels — i.e. `social-profile` access to their content and member lists
- **Empty/negative result looks like:** joins fail or the account gets a flood-wait/ban — usually from too-fast joining or a flagged number. A private channel needs a valid invite; a wrong username silently skips.

## Gotchas & OpSec
- **Active and attributable:** the joining account is visible to channel admins — sock-puppet only, never a real identity.
- Aggressive joining triggers Telegram flood-bans; keep the built-in delays.
- It sets up access; it does not itself extract data — pair with a scraper.

## Overlaps ("do both")
- Pairs with Telegram search/scraper tools (e.g. Telegram search engines and message scrapers) — this gets your account *into* channels; those pull the intelligence *out*.

## Trust & verifiability
`trust: community` — an open-source utility from a known OSINT practitioner using the official Pyrogram API. Read the code first; the main risk is account banning, not the tool itself.
