---
id: have-i-been-sold
name: Have I Been Sold?
description: Use when you have an `email` and want to check whether it appears in illegally-sold spam/marketing databases — but the original domain is dead, so treat this as unavailable.
url: https://haveibeensold.app/
category: email
path:
- email
bestFor: (Historically) checking whether an email address turned up in illegally-traded spam/marketing lists.
selectorsIn:
- email
selectorsOut:
- email
status: down
pricing: free
costNote: Was a free web check. The domain no longer resolves to the tool — as of this verification haveibeensold.app 301-redirects to an unrelated third-party gambling site, indicating the original service is defunct or the domain was dropped and re-registered.
opsec: passive
opsecNote: Do NOT visit the current URL — it redirects off-host to an unrelated commercial/gambling domain that could serve hostile content. There is no safe live endpoint to query; entering a target email would leak it to whoever now controls the domain.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: The service that this record describes is no longer reachable at its URL; the domain now points to unrelated content, so nothing here can be verified against a live tool.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- HaveIBeenSold
- haveibeensold.app
tags:
- Emails
source: cyb-detective
lastVerified: '2026-07-14'
enrichment: full
---

# Have I Been Sold?

> A now-defunct email-exposure checker: the domain redirects to an unrelated site, so this is documented as dead, not usable.

## When to use
Do not reach for this in a live investigation — it is recorded here so an agent recognizes the name and does not waste time. Historically the case was: you have an `email` and want a signal that it circulates in illegally-sold spam/marketing databases (a lighter, "am I on the spam lists" cousin of breach-checkers). That signal is no longer obtainable from this tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Recognize the status: `https://haveibeensold.app/` now issues a 301 redirect to an unrelated off-host domain — the original checker is gone.
2. Do not enter a target email anywhere on the redirected site; you cannot trust the party that now controls it.
3. Substitute a maintained tool: use `[[account-live-com]]` for Microsoft-account existence, or a breach/exposure checker for whether the address appears in known dumps, and treat those as the live path.

## Inputs → Outputs
- **In:** `email` (historically)
- **Out:** a yes/no-style "appears in sold spam lists" indicator (historically) — currently nothing usable
- **Empty/negative result looks like:** not applicable — there is no working endpoint; any content served at the old URL is from an unrelated site, not a result.

## Gotchas & OpSec
- The domain change is the whole story: a lapsed OSINT domain re-registered by a third party is a classic trap. Never submit a subject's selector to it.
- If a future revalidation shows the genuine service restored, flip `status` back to live and re-author from the real page — do not assume the historical behavior from this note.

## Overlaps ("do both")
- Superseded in practice by `[[account-live-com]]` and mainstream breach/exposure checkers, which are maintained and answer the "is this address real / exposed" question this tool used to gesture at.

## Trust & verifiability
`trust: unverified` — there is no live tool to verify; the URL resolves to unrelated content, so this record exists only to mark the tool as down.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | have-i-been-sold |
| category | email |
| selectorsIn → selectorsOut | email → email |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
