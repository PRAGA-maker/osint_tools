---
id: pew-research-center
name: Pew Research Center
description: Use when you have a demographic/behavioural research question and want authoritative US survey microdata and reports — returns downloadable datasets and statistics, not individual-person records.
url: https://www.pewresearch.org/internet/datasets
category: public-records
path:
- public-records
bestFor: Context and base rates on how US populations behave online and offline (social media, dating apps, privacy attitudes).
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free; a free account (email login) is required to download the raw datasets, though reports are readable without one.
opsec: passive
opsecNote: Reading reports is fully passive. Downloading datasets requires registering a free account, which ties your email to the request — use a research/sock-puppet email if you don't want it linked to you.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Pew Research Center is a well-established non-partisan US fact tank; its survey methodology and microdata are widely cited in academia and journalism.
missingPersonsRelevance: low
coverage:
- us
auth: account
api: false
localInstall: false
registration: true
aliases:
- Pew Internet
- pewinternet.org
- Pew Research datasets
tags:
- data-and-statistics
- research
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Pew Research Center

> A non-partisan US research archive of survey microdata and reports — the place to get base rates and context, not to look up a specific person.

## When to use
You need to *contextualise* a finding rather than identify an individual: how common is a behaviour, how a demographic uses a platform, or what typical privacy attitudes are. Reach for this when building an assessment ("what fraction of US adults in this age band use dating apps / TikTok / VPNs") or when you need methodologically sound numbers to frame an investigation. It is a public-records/statistics resource, so it will never return an individual's address or phone — treat it as background intelligence.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.pewresearch.org/internet/datasets (or the broader site search) and browse by topic — social media, online dating, privacy, AI, science.
2. Read the published report for the headline findings and methodology; this needs no login.
3. To analyse the raw data yourself, click a dataset and **log in or create a free account**, then download the case-level microdata (typically SPSS/CSV) plus its codebook.
4. Load the microdata in your stats tool to derive custom base rates.
5. Pivot: use the base rate to weight or sanity-check leads from person-level tools — e.g. deciding how significant a platform hit really is.

## Inputs → Outputs
- **In:** a research/demographic question (no personal selector)
- **Out:** downloadable survey datasets, codebooks, and statistical reports (US-focused)
- **Empty/negative result looks like:** no dataset covers your exact question, or coverage is US-only when you needed another country — Pew is not a global source.

## Gotchas & OpSec
- Human-in-the-loop: dataset downloads require a free account login; reports do not.
- Microdata is released only after an embargo period, so the newest survey may not yet be downloadable.
- OpSec: passive, but registering leaks an email — use a dedicated research address.
- This is aggregate/statistical data; do not expect any personally identifying records.

## Overlaps ("do both")
- Complements person-level public-records tools: Pew tells you *how common* something is, while those tools tell you *who* — use Pew to interpret the significance of a hit, not to find it.

## Trust & verifiability
`trust: trusted` — Pew Research Center is a widely respected, methodologically transparent research organisation; datasets ship with full codebooks and methodology statements.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pew-research-center |
| category | public-records |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
