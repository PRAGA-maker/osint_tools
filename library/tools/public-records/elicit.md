---
id: elicit
name: Elicit
description: Use when you have a `name` or research question and want AI-assisted discovery of relevant academic papers and their authors — returns paper lists with summaries, surfacing author affiliations and collaborators.
url: https://elicit.org/
category: public-records
path:
- public-records
bestFor: AI-assisted literature discovery to find and summarize papers by or about a subject/topic.
selectorsIn:
- name
selectorsOut:
- name
- associate
- employer-org
status: live
pricing: freemium
costNote: Free tier gives a monthly quota of searches/summaries; heavier use needs a paid plan, but the free allowance covers most investigative lookups.
opsec: passive
opsecNote: Queries hit Elicit's servers (an AI service over a papers corpus), not the subject — nothing is disclosed to them. Avoid typing sensitive case detail into the prompt; keep queries to public topics/names.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A well-known AI research assistant built on a large academic corpus (Semantic Scholar-scale); paper metadata is reliable, but AI-generated summaries can misstate and should be checked against the source.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- elicit.org
- Elicit AI research assistant
tags:
- Science
- academic
- ai-research
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Elicit

> An AI research assistant over ~175M papers — ask a question or a name and get relevant papers, summarized, with the authors and affiliations that anchor an academic identity.

## When to use
Your subject is a researcher/academic, or you need to understand a body of work tied to them, and you have a `name` or topic. Elicit's natural-language search finds and summarizes relevant papers faster than keyword databases, surfacing who published what, with whom, and where. Use it to map a subject's scholarly output and collaborators, or to get oriented in a technical field relevant to a case.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://elicit.org/ and register (free tier).
2. Enter a question or the subject's `name` + field.
3. Review the returned papers and AI summaries; open the actual papers for author lists and affiliations.
4. Note co-authors and institutions.
5. Pivot: co-authors become `associate` leads; affiliations become `employer-org`; author names feed ORCID/Scholar and institutional directories.

## Inputs → Outputs
- **In:** a `name` or research question
- **Out:** ranked papers + summaries → author `name`s, co-author `associate`s, institutional `employer-org`
- **Empty/negative result looks like:** thin or off-topic results — the subject may not be a published researcher, or the query needs sharpening; verify against a direct scholar search before concluding.

## Gotchas & OpSec
- AI summaries can hallucinate or over-generalize — always open the underlying paper to confirm a claim or an authorship.
- Free-tier quota limits searches/summaries per period.
- Registration required (use a research email/account).
- OpSec: passive; don't paste sensitive case detail into prompts.

## Overlaps ("do both")
- Pairs with [[connectedpapers]], Google Scholar, and ORCID — Elicit does natural-language discovery and summary, while those map citation networks and confirm author identity.

## Trust & verifiability
`trust: trusted` — a reputable AI research tool over a large, real corpus; the paper metadata is reliable, but treat the AI-written summaries as leads to verify at the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | elicit |
| category | public-records |
| selectorsIn → selectorsOut | name → name, associate, employer-org |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
