---
id: dorkgpt
name: DorkGPT
description: Use when you have a target `domain`/`name` and a research goal and want a ready-made Google dork query — returns AI-generated advanced search operators to paste into Google.
url: https://www.dorkgpt.com/
category: search-engines
path:
- search-engines
bestFor: Turning a plain-English investigative goal into a working Google dork (advanced-operator query).
selectorsIn:
- domain
- name
selectorsOut: []
status: live
pricing: free
costNote: Free web tool; generation runs in-browser with no account needed.
opsec: passive
opsecNote: Generating a dork is passive — you only send your natural-language prompt to DorkGPT, which returns query text; nothing touches the target. The subsequent Google search is where the real (still passive) query happens. Avoid pasting sensitive real names into the generator if you don't want them logged by the third-party service.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent AI helper that composes Google search-operator strings; it doesn't access any data itself, so the only risk is a poorly-formed or over-broad query — always sanity-check the output.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Dork GPT
- dorkgpt.com
tags:
- google-dorks-tools
- ai
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# DorkGPT

> An AI helper that writes Google dorks for you: describe what you're hunting for in plain English, get back a query full of `site:`, `filetype:`, `intitle:` operators to paste into Google.

## When to use
You know *what* you want to find — exposed documents on a domain, a person's profile across a site, config files, login pages — but don't want to hand-craft the advanced-operator syntax. Reach for DorkGPT to draft the query, then run it in a real search engine. It generates search strings only; it does not itself search, index, or return results, so treat it as a query-authoring aid, not a data source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.dorkgpt.com/.
2. Describe your goal in natural language, e.g. "find PDF resumes mentioning ACME Corp" or "login pages on example.com".
3. Read the generated dork — a Google query using operators like `site:`, `filetype:`, `inurl:`, `intitle:`, `"exact phrase"`.
4. **Sanity-check it** (operators can be wrong or too broad), then paste it into Google (or another engine) and run the search.
5. Pivot: the results — documents, profiles, subdomains — feed the rest of your workflow; refine the prompt and regenerate if the dork misses.

## Inputs → Outputs
- **In:** a plain-English goal, optionally scoped to a `domain` or `name`
- **Out:** a Google dork query string (advanced search operators) — no results, just the query
- **Empty/negative result looks like:** a vague or generic dork that returns nothing useful in Google; tighten your prompt (add the site, filetype, exact phrases) and regenerate.

## Gotchas & OpSec
- It outputs a *query*, not answers — you still run the search yourself.
- AI-generated dorks can be malformed or overly broad; verify the operators before trusting the results.
- OpSec: passive; but your prompt (which may contain a target name) is sent to a third-party service — keep it generic if that matters.

## Overlaps ("do both")
- Pairs with any curated Google-dork cheat-sheet or dork database: use those for known high-value patterns and DorkGPT for bespoke, one-off queries. Feed its output into whichever search engine you're using.

## Trust & verifiability
`trust: community` — an independent AI tool that only composes query text; it accesses no data, so verification means checking the dork's syntax and the Google results it produces, not the tool's own "findings".

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dorkgpt |
| category | search-engines |
| selectorsIn → selectorsOut | domain, name →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
