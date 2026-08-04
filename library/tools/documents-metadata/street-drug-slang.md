---
id: street-drug-slang
name: DEA Drug Slang Terms & Code Words
description: Use when you have intercepted text/chat and want to decode street-drug slang and code words — returns the DEA's reference mapping of slang terms to specific drugs.
url: https://ndews.umd.edu/sites/ndews.umd.edu/files/dea-drug-slang-terms-and-code-words-july2018.pdf
category: documents-metadata
path:
- documents-metadata
bestFor: A DEA intelligence reference for translating drug slang/code words found in messages, listings, or forum posts.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free public PDF hosted by the University of Maryland's NDEWS; no account, just download and read.
opsec: passive
opsecNote: A static reference document you download and consult offline — it queries nothing about any subject and leaks nothing. Purely a lookup aid.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Authored by the U.S. Drug Enforcement Administration and rehosted by an academic institution (NDEWS/University of Maryland); authoritative but a 2018 snapshot — slang evolves fast.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- global-terrorism-database
- start-consortium-for-the-study-of-terrorism-and-responses-to-terrorism
aliases:
- DEA drug slang
- drug code words reference
tags:
- reference
- drug-slang
- dea
source: toddington-resources
lastVerified: '2026-08-04'
enrichment: full
---

# DEA Drug Slang Terms & Code Words

> The DEA's intelligence reference (July 2018) mapping hundreds of street-slang terms and code words to the specific drugs they denote — a decoder for drug-related language in messages and listings.

## When to use
You've come across text — chat logs, marketplace listings, forum posts, social captions — peppered with terms that may be drug code words, and you need to know what they actually mean. This DEA document is the standard reference for translating slang to substance, which helps interpret a subject's communications, gauge the nature of a marketplace listing, or corroborate a drug-related lead. It's a lookup reference, not a search tool; you bring the term, it gives the meaning.

## How to use it (`bestInteractionPattern`: web-manual)
1. Download the PDF from the URL (hosted by NDEWS / University of Maryland).
2. Search within the document (Ctrl-F) for the slang term you encountered.
3. Read the mapped drug(s); many terms are ambiguous and map to several substances — note all candidates.
4. Corroborate against context and a *current* slang source, since language shifts since 2018.
5. Apply the decoded meaning to interpret the surrounding communication.

## Inputs → Outputs
- **In:** a slang term/code word (no OSINT selector — you supply the text)
- **Out:** the drug(s) the term denotes (reference knowledge, no selector)
- **Empty/negative result looks like:** term not listed — it may be newer than 2018, regional, or not drug-related; check a current, community-maintained slang source before drawing conclusions.

## Gotchas & OpSec
- Human-in-the-loop: it's a manual lookup/interpretation aid (`manual-review`); meaning depends on context you supply.
- Dated (2018) and US-centric: drug slang turns over quickly and varies by region, so treat mappings as strong leads, not certainties.
- Many terms are polysemous (also everyday words) — beware false positives.

## Overlaps ("do both")
- Pairs with current community slang references and marketplace/forum tools: this gives the authoritative baseline, while up-to-date sources catch newer coinages — do both when decoding recent communications.

## Trust & verifiability
`trust: trusted` — an official DEA intelligence product rehosted by an academic institution; authoritative for what it covers, with the sole caveat that it's a 2018 snapshot of fast-moving language.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | street-drug-slang |
| category | documents-metadata |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
