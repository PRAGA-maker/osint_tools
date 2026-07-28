---
id: autoregex
name: AutoRegex
description: Use when you need a regex from a plain-English description (or to explain one) to extract selectors — emails, phones, wallet addresses — from text; an AI regex helper to verify, not trust.
url: https://www.autoregex.xyz/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Turning a verbal description into a regular expression (and back) for extracting patterns from scraped text.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free tier with limited conversions; paid plan for more usage. Account may be required beyond a few tries.
opsec: passive
opsecNote: You send your description (and any example text) to a third-party AI service — do NOT paste real sensitive data or actual case content as examples. Use generic placeholders; the risk is data exposure to the service, not to a target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: An AI-generated-regex service; output is frequently imperfect (it can miss edge cases or produce subtly wrong patterns), so always test the regex on real samples before relying on it.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- autoregex.xyz
tags:
- regex
- text-extraction
- ai
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# AutoRegex

> An AI helper that turns "match every email/phone/BTC address in this text" into a regular expression — and explains regexes back in English. Handy for extraction work, but its output must be tested, not trusted.

## When to use
You're extracting selectors from a pile of scraped/dumped text — emails, phone numbers, IPs, crypto-wallet addresses, IDs — and want a regex fast without hand-crafting it, or you've found a regex and want it explained. AutoRegex generates a pattern from a plain-English description (and translates a pattern into words). It speeds up building the extraction step of a pipeline; because AI regexes are often subtly wrong, you use it to draft, then verify.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.autoregex.xyz/.
2. Describe what to match in plain English (use **generic** examples, never real sensitive data).
3. Get the generated regex; or paste a regex to have it explained.
4. **Test it on real sample text** — check for false positives/negatives and edge cases (the tool's own docs note it errs, e.g. on wallet-address prefixes).
5. Pivot: drop the vetted regex into `grep`/`ripgrep`/your scraper to extract selectors, then run those through the matching OSINT tools.

## Inputs → Outputs
- **In:** a plain-English description of a pattern (no person selector)
- **Out:** a regular expression to extract that pattern (which you then test and apply)
- **Empty/negative result looks like:** a regex that over- or under-matches on your samples — expected; refine the description or fix the pattern by hand.

## Gotchas & OpSec
- OpSec: your prompt/examples go to a third-party AI — use placeholder data, never real case content.
- Accuracy: AI regexes are commonly imperfect; **always** validate against real data before trusting extraction results.
- For anything security-sensitive (validation you rely on), treat the output as a draft to review, not a finished pattern.

## Overlaps ("do both")
- Feeds text-search/extraction tools like `[[agent-ransack]]` and `grep`/`ripgrep` — AutoRegex drafts the pattern, those apply it across your document set once you've verified it.

## Trust & verifiability
`trust: unverified` — an AI generator whose output needs testing every time; verifiability comes from running the regex on known samples, not from the tool's confidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | autoregex |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
