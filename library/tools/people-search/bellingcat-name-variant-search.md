---
id: bellingcat-name-variant-search
name: Bellingcat Name Variant Search
description: Use when you have a `name` and want every plausible spelling, transliteration, and nickname to search across — returns an expanded set of `name` variants with pre-built search links.
url: https://bellingcat.github.io/name-variant-search/
category: people-search
path:
- people-search
bestFor: Generating alternate spellings, transliterations, and nicknames of a person's name so no variant is missed.
selectorsIn:
- name
selectorsOut:
- name
- social-profile
status: live
pricing: free
costNote: Free, open-source Bellingcat tool; runs entirely in the browser, no account or key.
opsec: passive
opsecNote: Generating variants is passive and local — nothing is sent to the target. The pre-built DuckDuckGo/Facebook search links, however, are ordinary searches; run them from a sock-puppet browser if you don't want them tied to you, and remember that clicking through to a target's profile can be active.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built and maintained by Bellingcat, a well-known open-source investigations organisation; source is public on GitHub.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- alternate-spelling-finder
- forebears
aliases:
- Bellingcat name variant tool
- name-variant-search
tags:
- bellingcat-toolkit
- people
- name-variants
source: bellingcat-toolkit
lastVerified: '2026-07-10'
enrichment: full
---

# Bellingcat Name Variant Search

> A browser tool that explodes one name into all its plausible spellings, transliterations, and nicknames so a search never misses the subject under an alternate form.

## When to use
You have a `name` — especially one that transliterates from another alphabet (Cyrillic, Arabic, Chinese) or has common nickname/diminutive forms — and you are about to search social media or the open web. Before searching, run the name here to get the full spread of variants so a profile registered as "Yevgeny" isn't missed when you only searched "Evgenii", or "Bill" when you searched "William".

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://bellingcat.github.io/name-variant-search/ in a browser.
2. Type the subject's `name` and press enter.
3. The tool lists generated variants — alternate spellings, transliterations, and nicknames. Tick the checkboxes to keep the variants worth pursuing and add your own suggestions to widen the net.
4. Use the built-in per-variant links to search DuckDuckGo and Facebook, or copy the variants into other people-search and username tools.
5. Pivot: feed the confirmed variants into `[[whatsmyname-web]]`, `[[peekyou]]`, or any social-network search to catch profiles filed under a different spelling.

## Inputs → Outputs
- **In:** `name`
- **Out:** an expanded list of `name` variants, plus ready-made search links that can surface a `social-profile`
- **Empty/negative result looks like:** for a very plain single-locale name the tool may return few or no new variants — that just means the input was already canonical, not that the search failed.

## Gotchas & OpSec
- Human-in-the-loop: none for generation; you decide which variants are worth chasing.
- OpSec: variant generation is passive and runs in your browser. The follow-on searches are normal web searches — use a sock puppet if attribution matters, and treat clicking into a live profile as potentially active.
- It suggests plausible variants, not verified aliases; confirm any variant against real records before treating it as the subject's actual name.

## Overlaps ("do both")
- Pairs with `[[alternate-spelling-finder]]` — both widen a name; cross-check their variant lists since each uses different heuristics.
- Feed variants into `[[forebears]]` to gauge which spellings are common in the subject's likely country of origin.

## Trust & verifiability
`trust: trusted` — produced and maintained by Bellingcat with public source code; it generates candidate variants deterministically and leaks nothing about your query.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bellingcat-name-variant-search |
| category | people-search |
| selectorsIn → selectorsOut | name → name, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
