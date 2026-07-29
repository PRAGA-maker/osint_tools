---
id: justdeleteme
name: JustDeleteMe
description: Use when you have a service/platform name and want the direct account-deletion URL and difficulty rating — returns deletion links, notes, and an easy/medium/hard/impossible rating per service.
url: http://justdelete.me
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: A reference directory of direct account-deletion links and difficulty ratings for hundreds of web services — used for privacy hygiene and to understand deletion friction on a platform.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (community-maintained on GitHub); browser extension available. No account.
opsec: passive
opsecNote: A static reference directory — you look up a service, you don't query any target. Reading it discloses nothing about a subject. The linked deletion pages, of course, only apply to accounts you control.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running open-source community project (contributions via GitHub); reliable as a curated pointer list, though individual links can drift as services change their flows.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- accountkiller
- backgroundchecks-org
aliases:
- justdelete.me
- Just Delete Me
tags:
- privacy-and-encryption-tools
- account-deletion
- opsec-reference
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# JustDeleteMe

> A crowd-maintained directory of direct account-deletion links, colour-coded by how hard each service makes it to leave — a privacy-hygiene and dark-pattern reference.

## When to use
Two situations. (1) **Investigator OpSec / cleanup:** you're tearing down sock-puppet or personal accounts and want the fastest deletion route for each service, plus a heads-up on which ones are "hard" or "impossible" to leave. (2) **Understanding a platform:** knowing a service is rated "impossible" to delete explains why a subject's old profile still lingers. It is a static reference, not a lookup that takes a person's selectors.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://justdelete.me (redirects to the maintained mirror) or install the browser extension.
2. Browse the alphabetical list or search for the service name.
3. Read the entry: the **direct deletion URL**, any procedural notes (e.g. "must email support"), and the difficulty colour — Easy / Medium / Hard / Impossible.
4. Follow the link to delete an account you control; use the difficulty rating to plan (Hard/Impossible entries need support tickets or can't be removed).
5. Pivot: for services not listed, check `[[accountkiller]]`; for the inverse task (finding which services an email is registered on), use account-enumeration tools, not this.

## Inputs → Outputs
- **In:** none (a service name you look up in the directory).
- **Out:** none per-subject — deletion URLs, notes, and difficulty ratings per service.
- **Empty/negative result looks like:** the service isn't in the directory — it's a gap in coverage, not a statement that the account can't be deleted; check a sibling directory.

## Gotchas & OpSec
- Human-in-the-loop: none for the directory itself.
- OpSec: **passive** — a reference you read; it queries nothing about any target and only helps delete accounts you own.
- Links rot: services change or hide deletion flows, so an entry can be out of date — treat the URL as a strong starting point, not a guarantee.
- Not an enumeration tool: it tells you *how to delete* a known service, not *whether a person has an account* anywhere.

## Overlaps ("do both")
- Overlaps with `[[accountkiller]]` — a parallel account-deletion directory with different coverage; check both when a service is missing or the flow has changed.

## Trust & verifiability
`trust: community` — an open-source, crowd-sourced list. Dependable as curated guidance, but verify each deletion link at the source since platforms move their flows frequently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | justdeleteme |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
