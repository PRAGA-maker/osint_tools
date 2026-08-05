---
id: search-patterns
name: Search Patterns
description: Use when you have a `name`, topic or keyword and want to see the real questions and phrasings people search around it — returns Google/YouTube autosuggest clusters (a free AnswerThePublic alternative).
url: https://chromewebstore.google.com/detail/search-patterns/hjlahhonnlceifaecpjejlhhgjkipnbj
category: search-engines
path:
- search-engines
bestFor: Mining Google/YouTube autosuggest to surface the questions, comparisons and phrasings associated with a name or topic.
selectorsIn:
- name
selectorsOut: []
status: live
pricing: free
costNote: Free Chrome extension; no account. Developer states no data collection.
opsec: passive
opsecNote: It sends autosuggest queries to Google/YouTube for your keyword, so those providers see the term you researched (not the subject). Run it in a sock-puppet browser profile signed out of Google.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Small independent Chrome extension (a few hundred users, last updated Feb 2024); it merely surfaces public autosuggest data, so the risk is staleness/abandonment, not data quality.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Search Patterns extension
- AnswerThePublic alternative
tags:
- search-engine
- autosuggest
- keyword-research
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# Search Patterns

> A free browser extension that scrapes Google and YouTube autosuggest to reveal the questions, prepositions and comparisons people type around a term — an AnswerThePublic-style research aid.

## When to use
You have a `name`, alias, organisation, or topic and want to understand the public search conversation around it: what questions are being asked, what it's compared with, what phrasings recur. In an investigation it can surface unexpected associations, spellings, or public-interest angles tied to a subject's name — a lead-generation and framing tool, not a resolver.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Search Patterns" from the Chrome Web Store (link above) into a sock-puppet browser profile.
2. Enter your seed keyword (a `name`, alias, or topic).
3. The extension expands it via Google/YouTube autosuggest into clusters — questions (who/what/why…), prepositions, comparisons, and alphabetised variants.
4. Read the clusters for leads: recurring co-mentions, alternate spellings, or associated entities worth searching directly.

## Inputs → Outputs
- **In:** `name` / keyword / topic
- **Out:** autosuggest query clusters (leads/phrasings — no enum selector output)
- **Empty/negative result looks like:** a name with little search volume returns few or no suggestions; that means low public search interest, not that the person doesn't exist.

## Gotchas & OpSec
- Human-in-the-loop: none; it runs automatically once you enter a term.
- Autosuggest reflects aggregate public search behaviour and personalisation — sign out of Google and use a clean profile for cleaner, less biased results.
- It is a framing/ideation tool: expect search inspiration, not verified facts.

## Overlaps ("do both")
- Complements direct search-engine dorking: Search Patterns tells you *what phrasings to try*, then you run those queries in Google/Bing/Yandex for the actual results.

## Trust & verifiability
`trust: community` — a small third-party extension surfacing public autosuggest data; low data-quality risk, but confirm it's still maintained before relying on it, and always verify the leads it inspires in a real search.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-patterns |
| category | search-engines |
| selectorsIn → selectorsOut | name → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
