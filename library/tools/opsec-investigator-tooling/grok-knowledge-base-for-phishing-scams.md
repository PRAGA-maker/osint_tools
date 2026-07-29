---
id: grok-knowledge-base-for-phishing-scams
name: GROK Knowledge Base For Phishing Scams
description: Use when you need a plain-English reference cataloguing scam, hoax, and phishing types to classify a lure or brief a subject — returns definitional/reference material, not lookup data.
url: https://grok.lsu.edu/article.aspx?articleid=16680
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Identifying and naming the category of a phishing/scam message so an investigator or victim knows what they are dealing with.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free public knowledge-base article from Louisiana State University's GROK IT support wiki; no login.
opsec: passive
opsecNote: Reading a static university reference article. It touches no target infrastructure and leaks nothing — safe to browse directly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by Louisiana State University IT (GROK knowledge base); institutional, non-commercial reference.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- LSU GROK phishing article
- GROK scam knowledge base
tags:
- opsec
- phishing
- reference
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# GROK Knowledge Base For Phishing Scams

> A static LSU IT reference page listing and defining common scam, fraud, hoax, and phishing types — a classification aid, not an investigative tool.

## When to use
You have a suspicious message, lure, or fraud pattern and want to name and understand its category (advance-fee, credential-harvesting, tech-support, romance scam, hoax chain, etc.). Useful for orienting a victim during a doxxing/fraud response or teaching yourself the taxonomy before analysing a phishing artifact. It returns knowledge, not data about a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the article at the URL.
2. Read the enumerated scam/phishing categories and their descriptions.
3. Match the message you are examining to the closest described type to understand its mechanics and typical goal.
4. Follow-up: once the scam type is identified, pivot the actual investigation to the message's real selectors — sender `email`, links (`domain`), or `crypto-wallet` — with dedicated analysis tools.

## Inputs → Outputs
- **In:** none (reference material; you bring context in your head)
- **Out:** definitions and category names for scam/phishing types
- **Empty/negative result looks like:** the taxonomy simply may not name a novel scam variant — treat absence as "not catalogued," not "not a scam."

## Gotchas & OpSec
- This is educational reference content, not a live scanner or database — it will not analyse a URL or message for you.
- University KB articles can go stale; cross-check terminology against current FTC/anti-phishing guidance.
- No OpSec exposure: passive reading of a public page.

## Overlaps ("do both")
- Use as the definitional layer alongside operational phishing analysis (header inspection, URL/domain reputation, sender-email OSINT) — this names the threat; those tools investigate the specific artifact.

## Trust & verifiability
`trust: trusted` — hosted by Louisiana State University's official GROK IT knowledge base, an institutional non-commercial source with no data-quality incentive to distort.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | grok-knowledge-base-for-phishing-scams |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
