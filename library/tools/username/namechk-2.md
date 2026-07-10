---
id: namechk-2
name: Namechk (ha71 CLI)
description: Use when an old workflow references this bash username checker — returns little now; it's archived and broken, so use a maintained enumerator instead.
url: https://github.com/ha71/namechk
category: username
path:
- username
bestFor: Historical reference only — a bash CLI that once checked a username across 100+ sites; superseded by Sherlock/Maigret/WhatsMyName.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: down
pricing: free
costNote: Free and open-source, but archived (Nov 2022) and, per its own README, no longer working properly.
opsec: passive
opsecNote: When it worked, checks were made from your host against target sites (passive toward the subject). Not a live concern now — do not waste effort running it against current sites.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: The maintainer archived the repo on 29 Nov 2022 and the README explicitly recommends Sherlock, Maigret or WhatsMyName instead — treat this entry as a redirect, not a live tool.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- whatsmyname-python
- gosearch
aliases:
- ha71/namechk
tags:
- username
- open-source
- cli
- deprecated
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Namechk (ha71 CLI)

> An archived bash username-enumeration script — retained only so an agent recognises the name is dead and jumps straight to a maintained enumerator.

## When to use
You find `ha71/namechk` cited in an older OSINT list for checking a `username` across 100+ sites. It no longer works: the repository was archived in November 2022 and its README states plainly that the tool is broken and to use Sherlock, Maigret or WhatsMyName instead. Use this entry to confirm the dead end and switch tools.

## How to use it (`bestInteractionPattern`: cli)
1. Recognise it's deprecated — don't sink time into fixing site signatures that rotted years ago.
2. For the same goal (does this handle exist across many sites), run `[[whatsmyname-python]]` or `[[gosearch]]`, which are maintained and cover far more sites accurately.
3. If you must inspect the historical logic, the repo is read-only on GitHub.
4. Pivot: feed confirmed handles from a modern enumerator into per-site profile checks.

## Inputs → Outputs
- **In:** `username`
- **Out:** intended `social-profile`/`username` presence across sites — but results are unreliable/broken now
- **Empty/negative result looks like:** false "not found"/errors due to outdated site checks; do not trust either outcome.

## Gotchas & OpSec
- **Archived and broken** — its own authors redirect you elsewhere.
- Username enumerators go stale fast as sites change; always prefer a maintained one.
- OpSec: passive when run, but there's no reason to run it.

## Overlaps ("do both")
- Fully superseded by `[[whatsmyname-python]]` and `[[gosearch]]` — use those; this exists only as a pointer.

## Trust & verifiability
`trust: unverified` — deprecated project on read-only status; nothing it returns should be relied upon. Enumerate with a current tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | namechk-2 |
| category | username |
| selectorsIn → selectorsOut | username → social-profile, username |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
</content>
