---
id: iaca-dark-web-investigation-support
name: IACA Dark Web Investigation Support
description: Use when you have a `username`, `name`, `crypto-wallet`, or keyword and want vetted Tor search engines and marketplace directories to run it against — returns dark-web `social-profile` / listing leads.
url: https://iaca-darkweb-tools.com/
category: dark-web
path:
- dark-web
bestFor: A free, curated launchpad of dark-web search engines, marketplace directories, and reference material for Tor-based investigation.
selectorsIn:
- username
- name
- crypto-wallet
- email
selectorsOut:
- social-profile
- crypto-wallet
- document-id
status: live
pricing: free
costNote: Explicitly free; provided by the International Anti Crime Academy (IACA). No account or payment.
opsec: passive
opsecNote: The portal itself does not log or store queries, but the linked resources must be reached over Tor. Run everything through the Tor Browser (never your clearnet identity), and never paste sensitive operational indicators into shared third-party dark-web search boxes.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: Maintained since 2013 by IACA (Netherlands), an OSINT/SOCMINT training body; it is a curated link hub, so quality depends on the third-party engines it points to.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- IACA dark web tools
- iaca-darkweb-tools.com
tags:
- dark-web
- Tor
- curated-directory
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# IACA Dark Web Investigation Support

> A free, curated hub of Tor search engines, marketplace directories, and reference material — the safe on-ramp before you touch any onion service.

## When to use
You need to check whether a `username`, alias, `email`, `crypto-wallet`, or keyword surfaces on the dark web — leaked-data forums, marketplaces, or onion social media — and you want a vetted, single starting page rather than hunting for working onion search engines yourself. In a missing-persons context this helps trace an alias that has gone dark on the clearnet, or check trafficking/marketplace chatter tied to a subject's identifiers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://iaca-darkweb-tools.com/ in a normal browser to read the catalogue and its usage manual first.
2. Launch the **Tor Browser** separately. Do not open onion links in a clearnet browser.
3. Pick a category from the hub: Dark Web Search engines, Marketplaces directory, Dark Web Social Media, Pastebin collections, or the Dictionary/reference material.
4. Run your selector (alias/username, wallet, keyword) inside the chosen Tor search engine. Manually review results — dark-web indexes are noisy and full of stale/scam links.
5. Pivot: a hit feeds `crypto-wallet` chain analysis, a leaked-credential lookup, or corroboration of an alias found on the clearnet.

## Inputs → Outputs
- **In:** `username` / `name` / `email` / `crypto-wallet` / keyword
- **Out:** dark-web `social-profile` / forum handles, marketplace listings, `crypto-wallet` mentions, leaked-`document-id` references
- **Empty/negative result looks like:** most onion search engines return sparse or no results even for real targets — dark-web indexing is incomplete, so treat a blank as "not indexed," never as proof of absence.

## Gotchas & OpSec
- Human-in-the-loop: results demand manual review; dark-web search engines surface phishing, scam mirrors, and dead onions constantly.
- OpSec: **only** access linked resources over Tor. The hub says it does not log queries, but the third-party engines it links may. Never enter a live case's sensitive indicators into a shared search box.
- Legal/safety: many linked destinations host illegal content. Follow your jurisdiction's rules and your organisation's dark-web handling policy.

## Overlaps ("do both")
- Pairs with clearnet breach/paste search and `crypto-wallet` tracing tools — the dark-web hits found here are strongest when corroborated against clearnet identifiers.

## Trust & verifiability
`trust: community` — a long-running curated link hub from a training academy, not an authoritative dataset. It is only as reliable as the external onion engines it aggregates, so verify every lead independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | iaca-dark-web-investigation-support |
| category | dark-web |
