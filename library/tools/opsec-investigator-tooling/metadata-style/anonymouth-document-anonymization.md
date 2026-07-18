---
id: anonymouth-document-anonymization
name: Anonymouth (Document Anonymization)
description: Use when you must publish/send writing without it being linked to you by style — analyzes a document's stylometric fingerprint and guides edits to reduce authorship attribution.
url: https://github.com/psal/anonymouth
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- metadata-style
bestFor: Reducing the risk that your own writing style de-anonymizes you, by surfacing the linguistic features that give you away and suggesting changes.
selectorsIn:
- document-id
selectorsOut:
- document-id
status: degraded
pricing: free
costNote: Free and open-source (Java); runs locally. Unmaintained since ~2017 but still runnable with a compatible Java/JRE.
opsec: passive
opsecNote: This is a defensive OpSec tool for the INVESTIGATOR, not a lookup on a target. It runs entirely offline — your draft never leaves your machine, which is the whole point. Do not run it on someone else's text hoping to identify them; it de-styles your own writing, it doesn't attribute others'.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: desktop-app
trust: community
trustNote: Built by Drexel's Privacy, Security and Automation Lab (PSAL) as the applied counterpart to their JStylo stylometry research; academically grounded but old and no longer maintained.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Anonymouth
- psal/anonymouth
tags:
- opsec
- stylometry
- anonymization
- arf-seed
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Anonymouth (Document Anonymization)

> A stylometric anonymization aid — it analyzes the linguistic fingerprint of your own writing and shows which features (word choice, sentence structure, function-word rates) could de-anonymize you, then guides edits to blur them.

## When to use
This is protective tradecraft for the researcher, not a way to identify a subject. When you must release a report, tip, or message that could be linked back to you by *how you write* (stylometry can attribute anonymous text to a known author with unnerving accuracy), Anonymouth measures your document against sample corpora and flags the stylistic tells to change. Use it before publishing sensitive OSINT findings anonymously, or advising a source on the same. It does not attribute other people's writing — that's the offensive flip side (JStylo) and out of scope here.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Get a compatible Java runtime (the project is old — a legacy JRE may be needed), then clone/build from https://github.com/psal/anonymouth.
2. Launch the desktop app and load: your document to anonymize, a set of your own known writing samples, and a corpus of other authors' writing.
3. Run the analysis — it computes stylometric features (function words, word/sentence length distributions, punctuation, vocabulary richness) and shows which most identify you.
4. Edit iteratively following its feedback, re-analyzing until your document's fingerprint no longer stands out.
5. Manually review every suggested change — automated rewrites can distort meaning; you own the final text.
6. Result: a rewritten `document-id` whose style is harder to attribute to you.

## Inputs → Outputs
- **In:** your draft plus known-author and background corpora (`document-id`s)
- **Out:** a stylometric feature analysis and a guided, restyled `document-id`
- **Empty/negative result looks like:** it can't meaningfully anonymize very short texts, and it won't run cleanly on modern-only Java without the right runtime — a failure to launch is an environment problem, not "your text is safe."

## Gotchas & OpSec
- **Unmaintained (~2017)** and Java-version sensitive — expect setup friction; a Rust/successor or manual stylometry may be more practical.
- It reduces, never eliminates, attribution risk — combine with the obvious: strip metadata, don't reuse handles, vary vocabulary deliberately.
- Human-in-the-loop: you must judge whether edits preserve meaning.
- Defensive only — running it on a target's text does not identify them.

## Overlaps ("do both")
- Complements metadata-stripping tools (this handles *style*, they handle *file metadata*) — do both before publishing anonymously, since either channel alone can unmask you.

## Trust & verifiability
`trust: community` — a research-lab tool grounded in published stylometry work; credible in principle but old and unmaintained, so treat it as one layer of anonymization to verify manually, not a guarantee.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | anonymouth-document-anonymization |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | document-id → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | yes (manual-review) |
