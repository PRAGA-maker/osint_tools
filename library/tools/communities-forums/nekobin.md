---
id: nekobin
name: Nekobin
description: Use when you have a paste `domain`/URL on nekobin and want to read the shared text — a lightweight pastebin that hosts snippets, logs and dumps at short URLs.
url: https://nekobin.com/
category: communities-forums
path:
- communities-forums
bestFor: Reading text/code/log snippets shared as nekobin pastes referenced elsewhere.
selectorsIn:
- domain
selectorsOut:
- email
- ip-address
- crypto-wallet
status: live
pricing: free
costNote: Free, open-source (Hastebin-style) paste host; no account to read or create pastes.
opsec: passive
opsecNote: Opening a paste URL is passive — nekobin sees your IP fetching it, the subject does not. Do NOT paste your own investigation notes/selectors here; pastes are public to anyone with the URL and are not private storage.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Small open-source pastebin run by an individual (Dan); it hosts user content with no vetting, so treat pasted material as unverified.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- nekobin.com
tags:
- pastebins
- paste
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# Nekobin

> A minimal Hastebin-style pastebin — you'll meet it when a link, chat log or forum post points at a `nekobin.com/<id>` paste you need to read.

## When to use
You've found a reference to a nekobin paste (in a chat export, a forum thread, a config, a breach discussion) and need to read what was shared there before it's deleted. Nekobin is a plain text/code paste host with no search of its own, so it's not a discovery tool — its value is reading a *specific* paste tied to your subject, and harvesting any selectors (emails, IPs, wallets, credentials) that appear in the text.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the paste URL directly, e.g. `https://nekobin.com/<id>` (append `/raw` or use the "raw" link for plain text).
2. Read the content; copy it out promptly, since pastes can be removed or expire.
3. Run the raw text through an extractor like `[[datasurgeon]]` to pull every `email`/`ip-address`/`crypto-wallet`/hash out of it.
4. There is no on-site search — to *find* nekobin pastes about a subject, dork externally: `site:nekobin.com <selector>` in a search engine, or search where the link was shared.
5. Pivot: extracted selectors feed account-existence, breach-lookup and chain-explorer tools.

## Inputs → Outputs
- **In:** a specific nekobin paste `domain`/URL
- **Out:** the pasted text, and any `email` / `ip-address` / `crypto-wallet` / credentials contained in it
- **Empty/negative result looks like:** a "paste not found"/expired page — the content is gone; check web-archive tools for a cached copy.

## Gotchas & OpSec
- No native search or index — you must arrive with the URL or find it via an external search engine.
- Content is user-submitted and unvetted; anything in a paste is a *claim*, not confirmed fact.
- Pastes are ephemeral; snapshot important ones (e.g. via `[[archive-is]]`) immediately.
- Never use it to stash your own selectors — public URLs, no privacy.

## Overlaps ("do both")
- Pairs with `[[datasurgeon]]` to structure a paste's text into selectors, and with `[[archive-is]]` to preserve a paste before it expires. Treat it like any other pastebin surfaced in a `pastebins` sweep.

## Trust & verifiability
`trust: community` — a small individually-run open-source paste host. It faithfully returns whatever was pasted, but performs no moderation or verification, so the *content* is unverified user data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nekobin |
| category | communities-forums |
| selectorsIn → selectorsOut | domain → email, ip-address, crypto-wallet |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
