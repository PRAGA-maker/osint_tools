---
id: fedifinder
name: Fedifinder
description: Use when you want to map a Twitter/X account's contacts to their Mastodon/Fediverse handles — but the tool is now offline (Twitter API lockdown killed it); historically returned social-profile handles from a Twitter following list.
url: https://fedifinder.glitch.me/
category: social-networks
path:
- social-networks
- fediverse-mastodon
bestFor: (Historic) Discovering the Fediverse/Mastodon handles that a Twitter account's follows had posted in their bios/tweets.
selectorsIn:
- social-profile
selectorsOut:
- social-profile
status: down
pricing: free
costNote: Was a free tool hosted on Glitch. Now offline — the page returns HTTP 410 Gone, and its Twitter-OAuth mechanism broke when X restricted/priced its API in 2023. Documented so you don't chase a dead endpoint.
opsec: active
opsecNote: When it worked, it required Twitter OAuth (delegating access to your Twitter account) and scanned the public bios/tweets of accounts you followed. That OAuth grant tied the activity to your Twitter identity — a reason to have used a sock-puppet account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A popular community tool during the 2022–2023 Twitter-to-Mastodon migration, but hosted on Glitch and now gone (410). Its OAuth model is obsolete given X's API changes.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: true
relatedTools:
- khendrikse-netlify-app
- bskythreadreader
- mastovue
aliases:
- fedifinder.glitch.me
tags:
- mastodon
- fediverse
- migration
source: arf-seed
lastVerified: '2026-07-15'
enrichment: full
---

# Fedifinder

> A migration-era tool that scraped Mastodon handles out of the bios/tweets of the people a Twitter account followed — now **offline** (410 Gone), a casualty of X's API lockdown.

## When to use
Historically: to bulk-discover which of a Twitter account's follows had announced a Fediverse handle, exporting them as a CSV to re-follow on Mastodon. **It no longer works** — the Glitch page is gone and the Twitter-OAuth path is dead. This entry exists so you recognise it as defunct and pivot to still-working methods for the same goal.

## How to use it (`bestInteractionPattern`: web-manual)
Historic procedure (no longer functional):
1. Visit fedifinder.glitch.me and authorise via Twitter OAuth.
2. It scanned the bios/tweets of your follows for `@user@instance` patterns.
3. It output a CSV of discovered Fediverse handles to import into Mastodon.

Today, to achieve the same thing:
- Parse a **Twitter/X data export** (or a following list) yourself for `@user@instance` / instance-domain strings.
- Once you have a handle, resolve its account with the Mastodon lookup API (see `[[khendrikse-netlify-app]]`).

## Inputs → Outputs
- **In:** `social-profile` (a Twitter/X account's following list)
- **Out:** `social-profile` (matched Mastodon/Fediverse handles)
- **Empty/negative result looks like:** **always fails now** (410 / broken OAuth). Even historically, it only found handles that people had put in bios/tweets — silent movers were missed.

## Gotchas & OpSec
- **Defunct:** the endpoint is gone and depends on a Twitter-OAuth flow that X's API changes broke.
- The method only ever surfaced *self-declared* Fediverse handles.
- OpSec: it required delegating Twitter access — historically a sock-puppet-account job.

## Overlaps ("do both")
- Pairs with the Mastodon account-ID lookup (`[[khendrikse-netlify-app]]`) to resolve any handle you do find.
- For live discovery, parse Twitter/X exports manually or use a current fediverse-handle finder instead.

## Trust & verifiability
`trust: unverified` — a legitimate but now-dead community tool; recorded as **down** so investigators don't waste time on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fedifinder |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
