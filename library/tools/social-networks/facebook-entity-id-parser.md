---
id: facebook-entity-id-parser
name: Facebook Entity Id Parser
description: Use when you have a Facebook profile/page `social-profile` (URL) and want its stable numeric entity ID — returns the numeric Facebook ID that survives vanity-URL and display-name changes.
url: https://osint.support/chrome-extensions/2019/09/08/facebook-entity-id-parser.html
category: social-networks
path:
- social-networks
bestFor: Extracting the durable numeric Facebook ID behind a profile/page so it can be tracked across renames.
selectorsIn:
- social-profile
selectorsOut:
- device-id
- social-profile
status: degraded
pricing: free
costNote: Free Chrome extension (downloadable zip). No account.
opsec: passive
opsecNote: The extension reads the Facebook page already loaded in YOUR browser and parses its numeric ID locally — it does not query Facebook about the target beyond your normal page view, so it's passive. BUT the developer warns the code is obfuscated (may trigger antivirus) and you assume risk installing third-party extensions; load it only in a sandboxed/sock-puppet browser profile, ideally not one logged into your real Facebook.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: community
trustNote: Community tooling from osint.support. Useful and long-standing, but the 2019 extension is obfuscated and unmaintained; Facebook DOM changes can break parsing.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- lookup-id-com
- sowsearch
aliases:
- Facebook Entity ID Parser
- FB ID grabber
tags:
- facebook
- chrome-extension
- entity-id
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# Facebook Entity Id Parser

> A Chrome extension that pulls the stable numeric Facebook ID out of a profile or page you're viewing — the identifier that doesn't change when someone renames their vanity URL.

## When to use
You have a Facebook `social-profile` (a profile or page, possibly with a custom vanity URL) and need its underlying numeric entity ID. That numeric ID is the durable anchor: it survives display-name and username changes, powers Facebook Graph-search-style URL tricks, and lets you re-find an account that has renamed itself or that you want to monitor reliably.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Download and load the extension into a sandboxed/sock-puppet Chrome profile (the site notes its obfuscated code may trip antivirus — install at your own risk).
2. Navigate to the target's Facebook profile or page.
3. Run the extension; it parses the page and returns the numeric entity ID.
4. Pivot: feed the numeric ID into Facebook URL/Graph techniques or an ID-lookup service like `[[lookup-id-com]]`, and use it to build search/monitoring URLs (e.g. via `[[sowsearch]]`).

## Inputs → Outputs
- **In:** `social-profile` (a Facebook profile/page you can open)
- **Out:** `device-id` (numeric Facebook entity ID), confirmed `social-profile`
- **Empty/negative result looks like:** no ID returned — Facebook changed its page structure and the parser can't find it, or the page didn't fully load; try an alternative like `[[lookup-id-com]]`.

## Gotchas & OpSec
- Human-in-the-loop: viewing many Facebook pages generally works best while **logged in**, so use an investigative account, not your real one.
- OpSec: **passive** parsing of an already-loaded page, but the extension itself is unmaintained/obfuscated — sandbox it and keep it away from your real identity.
- **Degraded:** a 2019 tool against an ever-changing Facebook DOM; expect occasional breakage.

## Overlaps ("do both")
- Pairs with `[[lookup-id-com]]` (web-based FB numeric-ID lookup — a no-install fallback) and `[[sowsearch]]` (builds Facebook search URLs from an ID) — get the ID here, act on it there.

## Trust & verifiability
`trust: community` — handy community tooling, but obfuscated and unmaintained. The numeric ID it returns is verifiable (cross-check with a second ID-lookup), which is the right habit before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facebook-entity-id-parser |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → device-id, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | yes (account-login) |
