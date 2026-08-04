---
id: gptzero
name: GPTZero
description: Use when you have a suspect body of text and want to judge whether it was AI-generated — returns an AI-probability score with sentence-level highlighting.
url: https://gptzero.me/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Screening a document, message or "witness" narrative for signs it was written by an LLM rather than a person.
input: Text (minimum ~250 characters recommended)
output: Overall AI probability score, perplexity/burstiness analysis, and highlighted AI-generated sentences
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free to paste and scan; scans over ~10,000 characters need a free account, and bulk/API and higher limits are paid.
opsec: active
opsecNote: Submitted text is sent to GPTZero's servers and may be retained — never paste sensitive operational, victim or source material; sanitise or excerpt first.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A widely used commercial AI-text detector; scores are probabilistic and produce both false positives and false negatives, so treat any single verdict as a signal, not proof.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- gptzero.me
tags:
- ai-detection
- content-analysis
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# GPTZero

> An AI-text detector: paste a passage and get a probability that it was machine-generated, with the suspect sentences highlighted.

## When to use
You have a block of text whose authenticity matters — a tip, a "witness statement", a profile bio, a threatening message, a document purporting to be human-written — and you want a signal on whether it was produced by an LLM. GPTZero scores the text and flags which sentences look AI-generated, helping you weight how much to trust the content and its supposed author.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://gptzero.me/ and paste the text (aim for ~250+ characters; very short samples are unreliable).
2. Run the scan and read the overall AI-probability score plus the per-sentence highlighting and perplexity/burstiness notes.
3. For passages over ~10,000 characters, sign in with a free account; for repeated/bulk checks use the paid API.
4. Treat the verdict as one data point — corroborate with writing-style consistency, metadata, and provenance before concluding.

## Inputs → Outputs
- **In:** free text (not a structured selector)
- **Out:** AI-probability score, highlighted AI-suspect sentences, perplexity/burstiness readout
- **Empty/negative result looks like:** a mid-range score on short or heavily edited text — inconclusive; detectors struggle with paraphrased or human-edited AI output and can wrongly flag non-native or formulaic human writing.

## Gotchas & OpSec
- Human-in-the-loop: only for large texts (free account) or API bulk use.
- OpSec: **active** — text leaves your machine and is processed/stored by a third party; never submit sensitive case, victim or source material. Sanitise or use an excerpt.
- Reliability: probabilistic, with documented false positives (especially on ESL or formulaic prose) and false negatives on edited AI text — never use as sole proof of authorship.

## Overlaps ("do both")
- Pairs with other AI-detection and content-analysis tools because detectors disagree; agreement across independent detectors is a stronger signal than any one score.

## Trust & verifiability
`trust: community` — a popular commercial detector whose method is only partly disclosed and whose scores are inherently probabilistic; verifiability comes from corroboration, not from the score alone.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
