---
id: robots-txt-search-engine
name: Robots.txt Search Engine
description: Use when you have a `domain` and want to find paths its robots.txt tries to hide from crawlers — returns disallowed/hidden directories worth probing, via a Google CSE.
url: https://cse.google.com/cse?cx=013991603413798772546:zu7epjqvunu
category: search-engines
path:
- search-engines
bestFor: Searching across sites' robots.txt files to surface "Disallow" paths (admin, staging, hidden directories) that hint at non-public site structure.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free hosted Google Programmable Search Engine; no account required.
opsec: passive
opsecNote: Querying the CSE runs on Google and does not touch the target site, so it's passive. If you then visit a discovered path directly, that request hits the target's server — use a sock-puppet IP for that step.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party-configured Google CSE scoped to robots.txt content; its index and scope are opaque and may drift, so treat null results as non-authoritative.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- robots.txt CSE
tags:
- google-cse
- recon
- web-infrastructure
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# Robots.txt Search Engine

> A hosted Google Programmable Search Engine that searches within sites' `robots.txt` files — a quick recon trick for finding the paths a site *asks* crawlers to avoid, which are often the interesting ones.

## When to use
You're profiling a `domain` and want hints about its non-public structure. A site's `robots.txt` lists `Disallow:` paths — admin panels, staging areas, upload folders, internal tools — that the owner would rather keep out of search results. Searching across robots.txt content can reveal these directory names and, sometimes, cross-site patterns worth probing for a target.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE: https://cse.google.com/cse?cx=013991603413798772546:zu7epjqvunu
2. Search for the target `domain`, or a keyword you expect in a Disallow path (e.g. `admin`, `staging`, `backup`, a product name).
3. Review results for the robots.txt entries and note interesting `Disallow` paths.
4. Cross-check by fetching the target's own `https://<domain>/robots.txt` directly (from a sock-puppet IP) to confirm current paths.
5. Pivot: discovered paths feed directory/endpoint probing and broader infrastructure mapping.

## Inputs → Outputs
- **In:** `domain` (or a keyword expected in robots.txt)
- **Out:** references to robots.txt files and their `Disallow` paths on the target/related `domain`s
- **Empty/negative result looks like:** no indexed robots.txt hits — the CSE may not cover the site, or the site has a trivial/blank robots.txt. Always confirm by fetching the live robots.txt directly.

## Gotchas & OpSec
- The CSE's scope/index is opaque and can drift; a miss here is not authoritative — read the live robots.txt yourself.
- `Disallow` reveals paths but does not grant access; probing them may be logged by the target and, depending on jurisdiction/authorisation, may cross legal lines.
- Google may present a CAPTCHA on repeated queries.

## Overlaps ("do both")
- Pairs with direct robots.txt fetching, directory-brute tools, and archive snapshots — this finds candidate hidden paths broadly, while those confirm and enumerate them on a specific target.

## Trust & verifiability
`trust: community` — a genuine Google search product configured by an unknown third party; the underlying index is reliable, but always verify a finding against the site's live robots.txt.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | robots-txt-search-engine |
| category | search-engines |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
