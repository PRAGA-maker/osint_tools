---
id: google-word-sniper
name: Google Word Sniper
description: Use when you want two terms to appear near each other in Google results and want the AROUND() proximity query built for you — returns a ready Google search string.
url: https://googlewordsniper.eu/
category: search-engines
path:
- search-engines
bestFor: Building Google AROUND(n) proximity queries without fumbling the exact syntax.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free web helper; no account.
opsec: passive
opsecNote: The helper only assembles a string and touches nobody. OpSec applies when you run the query on Google against your subject — do that from a clean/sock-puppet session, as it's a live search about the person.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A tiny single-purpose query builder; it adds no data of its own, so trust attaches to Google's results, and its only job is to format the (unofficial, sometimes flaky) AROUND() operator correctly.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- googlewordsniper.eu
tags:
- Tools for Google
- proximity-search
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# Google Word Sniper

> A one-trick helper that writes Google `AROUND(n)` proximity queries for you — forcing two terms to appear within N words of each other, which plain quotes can't do.

## When to use
You want results where two things co-occur *closely* — a person's first and last `name` split by a middle name or title, a `name` near an employer or city, a handle near a real name — rather than just anywhere on the page. Google's `AROUND(n)` operator does this but its syntax is finicky and undocumented; this tool formats it correctly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://googlewordsniper.eu/.
2. Enter the two terms and the proximity distance N (how many words apart, at most).
3. Copy the generated query, e.g. `"Jane" AROUND(3) "Roe"` or `"Jane Roe" AROUND(5) "Acme GmbH"`.
4. Paste it into Google (clean/sock-puppet session) and review the SERP for tight co-occurrences.
5. Tune N up (looser) or down (stricter) and re-run. Pivot: matching pages yield `social-profile`/`domain` leads tying the two terms together.

## Inputs → Outputs
- **In:** two terms (`name`/`username`/keyword) + a proximity distance
- **Out:** a copy-paste Google `AROUND(n)` query; when run, `social-profile`/`domain` results where the terms co-occur closely
- **Empty/negative result looks like:** the query always builds; "empty" is downstream — Google returns nothing, meaning the two terms don't co-occur that tightly on any indexed page. Loosen N or drop to a normal query before concluding no link exists.

## Gotchas & OpSec
- `AROUND()` is an unofficial Google operator; it works but can be inconsistent and may break without notice.
- It builds a query only — all coverage/ranking limits are Google's.
- Very small N with common words yields nothing; start looser.
- OpSec: building is passive; running the query is a live Google search about your subject — use a clean session.

## Overlaps ("do both")
- Complements `[[boolean-builder-thebalazs]]`: that builds `site:`/Boolean X-Ray strings, this adds the proximity dimension — combine them (X-Ray a site *and* require the two terms close together) for precise people-search.

## Trust & verifiability
`trust: community` — a minimal query formatter; verifiability rests entirely on the Google results the string returns, and the only risk it introduces is the flakiness of the `AROUND()` operator itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-word-sniper |
