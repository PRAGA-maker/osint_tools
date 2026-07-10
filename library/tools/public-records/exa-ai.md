---
id: exa-ai
name: exa.ai
description: Use when you have a company `name` or website `domain` and want an AI-compiled dossier — people, funding, competitors, news — returns `employer-org`, `associate`, and web-source leads.
url: https://companyresearcher.exa.ai/
category: public-records
path:
- public-records
bestFor: AI/neural-search company research that assembles a profile (people, funding, news) from a company URL in seconds.
selectorsIn:
- employer-org
- domain
- name
selectorsOut:
- employer-org
- associate
- address
status: live
pricing: free
costNote: The Company Researcher demo is free to use (powered by Exa's neural search API; the underlying API is paid for developers). No account needed for the web demo.
opsec: passive
opsecNote: Passive — Exa searches the public web and synthesises a summary; the company/people are not notified. Your input query goes to Exa's servers (logged). Because output is AI-generated, treat every fact as a lead to verify, not confirmed data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Exa is a reputable neural-search company, but the Company Researcher output is LLM-synthesised from web sources and can hallucinate or conflate — always trace claims back to the cited source.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Exa Company Researcher
- exa.ai
tags:
- companysites
- Company Related Sites
- ai-search
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# exa.ai

> Exa's Company Researcher: paste a company URL and get an AI-assembled dossier — what it does, who runs it, funding, competitors, and recent news — stitched from a neural web search.

## When to use
You have a company `name` or website `domain` tied to your subject and want a fast orientation: the business's description, key people (`associate` leads), funding/investors, competitors, and recent coverage. Good as a rapid first pass to understand an `employer-org` before drilling into official registers — but because it's AI-generated, it's a lead generator, not a source of record.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://companyresearcher.exa.ai/ and enter the company's website URL (or name).
2. It runs a neural web search and returns a structured profile: overview, people, funding, competitors, news.
3. For every fact you care about, click through to the underlying web source to verify — the summary can be wrong or outdated.
4. Note named people/executives as `associate` pivots and any address as a lead.
5. Pivot: verify the entity in an official register (`[[companycheck-co-uk]]`, `[[info-clipper-com]]`, `[[dnb-co-uk]]`); run named people through people-search.

## Inputs → Outputs
- **In:** company `name` or website `domain`
- **Out:** AI-synthesised `employer-org` profile, key people (`associate`), funding/competitors, news, source links; sometimes an `address`
- **Empty/negative result looks like:** a thin or generic summary — the company has little web presence, or the URL was wrong. Watch for confident-but-false details (hallucination); absence of a citation is a red flag.

## Gotchas & OpSec
- Human-in-the-loop: none to run, but **you must verify** — LLM output can fabricate people, figures, or relationships.
- OpSec: **passive** — Exa searches the public web; your query is logged server-side.
- Not authoritative: treat it as a research accelerator, never as evidence.

## Overlaps ("do both")
- Pairs with `[[companycheck-co-uk]]` / `[[info-clipper-com]]` / `[[dnb-co-uk]]` — Exa gives fast context and names; the registers confirm the legal entity, directors, and filings.

## Trust & verifiability
`trust: unverified` — reputable vendor, but LLM-synthesised output. Trace every claim to its cited source and confirm entity facts against an official register.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | exa-ai |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, domain, name → employer-org, associate, address |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
