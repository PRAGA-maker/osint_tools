---
id: inleo-io
name: InLeo (inleo.io)
description: Use when you have a `username` or `name` and want to find and read someone's posts on the Hive-blockchain social network InLeo — returns their profile and on-chain, undeletable post history.
url: https://inleo.io/threads/v2
category: social-networks
path:
- social-networks
bestFor: Finding a subject's InLeo/Hive profile and mining their on-chain (permanent, uncensorable) microblog and long-form posts.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
- crypto-wallet
status: live
pricing: free
costNote: Free to browse and read; an account (a Hive keychain/wallet) is only needed to post or earn tokens.
opsec: passive
opsecNote: Reading public posts is passive and does not notify the author. Because content lives on the Hive blockchain it is public and permanent — you can read it without an account, and even "deleted" posts often remain retrievable on-chain.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: InLeo is a real, active Hive-based social platform; content is user-generated and self-asserted, but the blockchain backing means posts are timestamped and hard to alter or erase.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- InLeo
- LeoFinance
- inleo.io
tags:
- gsocialmedia
- General Social Media Sites
- hive-blockchain
- web3-social
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# InLeo (inleo.io)

> A Hive-blockchain social network (X-like threads + long-form): find a subject's profile and read their on-chain post history, which is timestamped and effectively permanent.

## When to use
You have a `username` or `name` and think the subject is active in crypto/Web3 social circles. InLeo (formerly LeoFinance) runs on the Hive blockchain, so a matched profile gives you a `social-profile`, their posts and threads, and a link to their on-chain `crypto-wallet`/account (the Hive username is the wallet). The blockchain backing is the OSINT payoff: posts are timestamped and hard to delete, so scrubbed content is often still retrievable.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://inleo.io/ (or the threads feed at /threads/v2). No login is needed to read.
2. Search the `username`/`name`, or go directly to `inleo.io/@<username>` if you have a handle.
3. Read the profile: threads, long-form posts, comments, and the Hive account name (which is also the on-chain wallet identifier).
4. For deeper/immutable history, cross-check the same Hive username on other Hive front-ends (e.g. hive.blog, peakd.com) and on a Hive block explorer — the underlying account is shared across all of them.
5. Pivot: the Hive username feeds cross-front-end and blockchain-explorer lookups; reused handle feeds general username search; wallet activity feeds crypto-tracing.

## Inputs → Outputs
- **In:** `username` / `name`
- **Out:** `social-profile`, posts/threads, `name`/bio, Hive account = `crypto-wallet` identifier
- **Empty/negative result looks like:** no matching handle/profile — meaning no InLeo/Hive account under that name, not that the person is absent from all social media.

## Gotchas & OpSec
- Human-in-the-loop: none to read; posting/earning needs a Hive key.
- OpSec: passive; on-chain content is public and permanent, which cuts both ways — great for recovering deleted posts, but also means your own posting there would be permanent.
- The same Hive account appears on multiple front-ends; don't treat inleo.io as the only place its content lives.

## Overlaps ("do both")
- Pairs with other Hive front-ends (hive.blog, peakd) and Hive block explorers — they share the account, so each surfaces content or history the others render differently.

## Trust & verifiability
`trust: community` — a genuine, active platform; posts are self-asserted like any social media, but blockchain timestamping makes authorship and timing unusually verifiable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | inleo-io |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name, crypto-wallet |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
