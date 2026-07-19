---
id: google-custom-search-engine
name: Google Custom Search Engine
description: Use when you want to build your own Google search scoped to a chosen set of sites/domains — a Programmable Search Engine you configure, then query with a `name`/`username`/`domain` to get focused web results.
url: https://cse.google.com/cse/
category: search-engines
path:
- search-engines
- search-tools
bestFor: Creating and running a curated Google Programmable Search Engine that searches only sites you pick (e.g. all major social platforms, or a country's news outlets).
selectorsIn:
- name
- username
- domain
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free to create and use Google Programmable Search Engines; a Google account is needed to build one (not to run a shared one).
opsec: passive
opsecNote: Passive toward targets — you run Google searches, touching no site of theirs. Building a CSE ties it to your Google account; querying is logged to your session. Use a research/sock-puppet Google account and clean browser for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Google product (Programmable Search Engine, formerly Custom Search Engine); Google runs the search, you control the source list.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- google-cse-instances-search-engine
aliases:
- Programmable Search Engine
- Google PSE
- CSE builder
tags:
- search-engine
- google-cse
- programmable-search
- search-tools
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# Google Custom Search Engine

> The builder for Google Programmable Search Engines — roll your own Google that only searches the sites you choose, cutting noise for repeatable OSINT queries.

## When to use
You want Google's index but restricted to a curated set of sources — every major social network, a country's newspapers, breach-paste sites, public-records portals — so a `name`/`username`/`domain` query returns focused results without general-web clutter. Build one CSE once and reuse it across cases, or run a pre-built community CSE.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://cse.google.com/cse/ and sign in with a (research) Google account.
2. Create a new engine; add the sites/domains to include (e.g. `facebook.com`, `linkedin.com/in/*`, `t.me/*`) — or set "search the entire web but emphasise these sites".
3. Save; use the public URL or embed. Run queries with standard Google operators (quotes, `-`, `site:` within the scope).
4. Read the output: ranked results limited to your configured sources. Pivot: follow hits to profiles/pages and feed selectors onward. Tune the source list as you learn what surfaces the target.

## Inputs → Outputs
- **In:** `name` / `username` / `domain` query (against your chosen sources)
- **Out:** focused web results — `social-profile`s, `domain`s, documents within scope
- **Empty/negative result looks like:** no hits may mean the term is genuinely absent *or* your source list is too narrow — widen the scope or run the query on plain Google before concluding nothing exists.

## Gotchas & OpSec
- Results are shaped entirely by your configured sites — a missing result can be a config gap, not real absence.
- Building/managing engines requires a Google login; running a shared public CSE does not.
- Human-in-the-loop: occasional CAPTCHA on heavy use. OpSec: passive toward the target; queries logged to your Google session.

## Overlaps ("do both")
- Do both with `[[google-cse-instances-search-engine]]` — that is a ready-made community CSE; this is how you build/customise your own for a specific investigation.

## Trust & verifiability
`trust: trusted` — first-party Google infrastructure; results are authentic Google hits, so verify each on its live page as normal.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-custom-search-engine |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, domain → social-profile, domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
