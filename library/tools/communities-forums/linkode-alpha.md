---
id: linkode-alpha
name: Linkode(alpha)
description: Use when you already hold a Linkode paste link and want to read its contents — returns whatever the poster stored (possibly email, password, crypto-wallet); there is no public search.
url: https://linkode.org/
category: communities-forums
path:
- communities-forums
bestFor: Reading a specific Linkode code/text paste you were handed a link to; useful mainly as negative knowledge — you cannot discover pastes here.
selectorsIn: []
selectorsOut:
- email
- password
- crypto-wallet
status: live
pricing: free
costNote: Free, no account required.
opsec: passive
opsecNote: Viewing a paste is passive. Open the link in a puppet browser in case it is tracked, and preserve the contents (screenshot/copy) before you leave — pastes can be set read-only or expire.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An alpha-stage public code/text paste host supporting many languages; run by an unknown operator with no stated longevity guarantee.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- zbin
aliases:
- linkode.org
- Linkode
tags:
- pastebins
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# Linkode(alpha)

> An alpha-stage multi-language code/text paste host — somewhere a target might *drop* a snippet, not somewhere you can search for one.

## When to use
Only when an investigation has already surfaced a `linkode.org/...` link and you need to read what it holds. Like most modern paste hosts, Linkode offers no public index or search, so it is not a discovery tool — reach for it only to resolve a link you already have.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the full paste URL in a sock-puppet browser.
2. Read the paste (Linkode renders code with syntax highlighting; text is shown as-is).
3. Extract any selectors it leaks — `email`, `password`, `crypto-wallet`, API keys, usernames — into your case notes right away.
4. Pivot on the extracted selectors; the paste itself yields no further Linkode leads.

## Inputs → Outputs
- **In:** a complete Linkode paste link (a `url`, not a searchable selector).
- **Out:** the paste body — potentially `email`, `password`, `crypto-wallet`, or other leaked text/code.
- **Empty/negative result looks like:** a "not found"/expired page or an empty paste — nothing to extract and nothing else to query.

## Gotchas & OpSec
- **No search / no browse** — you cannot enumerate a person's pastes; discovery must come from elsewhere (a bio link, a chat, a breach).
- Alpha software: expect occasional downtime and no guarantee a paste persists.
- Read-only/expiring pastes may vanish; capture evidence on first view.

## Overlaps ("do both")
- Same view-only limitation as `[[zbin]]` — both resolve a link you already hold; neither lets you hunt for a target's content.

## Trust & verifiability
`trust: community` — an independently operated, alpha-stage paste service. The content it returns is only as trustworthy as whoever posted it; treat leaked selectors as leads to corroborate, not facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | linkode-alpha |
| category | communities-forums |
| selectorsIn → selectorsOut | — → email, password, crypto-wallet |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
