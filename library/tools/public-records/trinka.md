---
id: trinka
name: Trinka
description: Use when you have two texts/documents and want authorship, plagiarism or consistency signals — returns grammar/style/plagiarism analysis to compare writing and check originality.
url: http://trinka.ai
category: public-records
path:
- public-records
bestFor: Grammar/consistency/plagiarism analysis of a document — usable for authorship-style comparison and originality checks on text tied to a subject.
selectorsIn:
- name
selectorsOut: []
status: live
pricing: freemium
costNote: Free tier with monthly limits (grammar/consistency and basic checks); plagiarism scans, larger volumes and advanced features are paid. A free account is required for most features.
opsec: passive
opsecNote: You upload/paste text into a third-party AI service, which may store it. Do not submit sensitive, confidential, or evidentiary documents you are not authorised to disclose — for those, use offline stylometry tooling. It does not touch any subject; the only exposure is your upload to Trinka's servers.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial AI writing-assistance product (Trinka.ai) aimed at academic authors; its grammar/plagiarism output is a heuristic aid, not a forensic-grade stylometry or authorship determination.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- trinka.ai
tags:
- Science
- text-analysis
- stylometry
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Trinka

> An AI writing-analysis service (grammar, consistency, citation and plagiarism checking for academic text) — in an OSINT context, a lightweight aid for comparing writing style and checking whether text is original or copied.

## When to use
You are working with text a subject wrote — a paper, statement, forum posts, a manifesto — and want quick signals: is this passage plagiarised/copied from somewhere (plagiarism check), and does its grammar/consistency profile resemble another sample (a rough authorship/stylometry aid). It is a **secondary utility**, not a forensic authorship tool; use it to generate leads, not conclusions.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://trinka.ai and create a free account.
2. Paste or upload the text (mind the free-tier size limits).
3. Run the grammar/consistency check to profile the writing; run the plagiarism check to see whether passages match published/online sources.
4. Compare two samples' error/style patterns manually to gauge whether they could share an author.
5. Pivot: a plagiarism match → the original source (and its author/site); a style resemblance → corroborate with dedicated stylometry tooling before drawing any conclusion.

## Inputs → Outputs
- **In:** text/document (optionally tied to a `name` you're profiling)
- **Out:** grammar/consistency profile and plagiarism/source matches — comparison signals, not an identity
- **Empty/negative result looks like:** clean grammar and no plagiarism matches — that neither confirms nor refutes authorship; it only means nothing was flagged.

## Gotchas & OpSec
- **Human-in-the-loop: account-login**, and text is sent to a third-party AI service that may retain it — never submit confidential/evidentiary material; prefer offline stylometry for sensitive work.
- Not forensic: grammar/plagiarism heuristics are not a defensible authorship determination.
- Plagiarism and advanced features are paywalled beyond the free tier.

## Overlaps ("do both")
- Complements dedicated stylometry tools (e.g. JStylo/authorship analyzers) — Trinka gives a fast plagiarism/consistency read online, while purpose-built stylometry does the rigorous authorship comparison offline.

## Trust & verifiability
`trust: community` — a commercial writing-assistant, useful as a quick lead generator; any authorship or originality signal it produces must be confirmed with proper stylometric methods and primary sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | trinka |
| category | public-records |
| selectorsIn → selectorsOut | name → — |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
