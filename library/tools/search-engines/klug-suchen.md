---
id: klug-suchen
name: Klug Suchen
description: Use when you have a German-language `name`, term, or topic and want a curated directory of German specialty search engines and databases to run it against — returns links to topical German search resources.
url: https://www.klug-suchen.de/
category: search-engines
path:
- search-engines
bestFor: Finding the right German specialty search engine or database for a topic before you search a German subject.
selectorsIn:
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free directory; no account or payment.
opsec: passive
opsecNote: Browsing the directory itself is passive and reveals nothing about your target. OpSec depends on the downstream engine you pick from it — treat each linked search on its own terms.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-standing German search-portal/directory ("Ihr Weg zur richtigen Information"); it is a curated index of other engines, not a data source itself.
missingPersonsRelevance: medium
coverage:
- de
aliases:
- klug-suchen.de
- Klug Suchen Suchmaschinen-Verzeichnis
tags:
- toddington
- curated-directory
- specialty-search
- germany
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Klug Suchen

> A German-language directory of specialty search engines and databases — a jumping-off point for finding the right German source, sorted by topic.

## When to use
Your subject or question is German-speaking (a person, company, publication, or record likely to sit in a German database) and you don't know which German search engine or catalogue to use. Klug Suchen organises German specialty search engines by subject — news, science, people, business, regional — so you can pick a topical engine rather than defaulting to a general web search that under-indexes German sources.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.klug-suchen.de/.
2. Browse the topical categories (or use the site search) to find a specialty German engine relevant to your lead.
3. Follow the link to that engine and run your actual query (`name`, term) there.
4. Pivot: the specialty engine is where the real result lives — Klug Suchen just routes you to it. Note the engine so you can return to it directly.

## Inputs → Outputs
- **In:** a topic/`name` you want to research in German-language sources.
- **Out:** links to relevant German specialty search engines/databases (the directory), which then yield `social-profile`s, records, or documents.
- **Empty/negative result looks like:** no category fits your topic — the directory is finite and German-centric; fall back to a general engine plus site-specific searches.

## Gotchas & OpSec
- It is a directory, not a search engine: it returns *engines to use*, not answers. Expect a second hop.
- German-focused; not useful for non-German subjects. Some linked engines may be stale — verify the target site is live before relying on it.
- Passive at the directory level; assess OpSec per downstream engine you choose.

## Overlaps ("do both")
- Use alongside general web search and country-specific people-search — the directory surfaces German niche sources those miss.

## Trust & verifiability
`trust: community` — a curated third-party index of other engines. It points you at sources; the trustworthiness of any result depends on the engine you land on, not on Klug Suchen.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | klug-suchen |
| category | search-engines |
| selectorsIn → selectorsOut | name → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
