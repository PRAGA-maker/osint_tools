---
id: frack
name: Frack
description: Use when you have raw breach-dump files and want to parse, store, and query them by domain to extract `email`/`password` pairs — returns credential analytics and per-domain reports.
url: https://github.com/sensepost/Frack
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Locally ingesting and querying large leaked-credential datasets you already possess, by domain.
selectorsIn:
- email
- domain
selectorsOut:
- email
- password
status: degraded
pricing: free
costNote: Free, open-source (GPL-3.0) from SensePost; but the repo is archived and no longer maintained (a rewrite is promised, not yet linked).
opsec: passive
opsecNote: Runs fully offline against dumps you already hold — no target is queried over the network, so it leaks nothing. The real risk is legal/ethical: handling breach data implicates privacy and data-protection law. Only process data you are authorized to hold, keep it encrypted at rest, and follow your jurisdiction's rules.
humanInLoop: true
humanInLoopReason:
- legal-gate
bestInteractionPattern: cli
trust: community
trustNote: Authored by SensePost (a respected security firm) and presented at DEF CON 29; credible provenance, but the project is explicitly archived/unmaintained.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- gowitness
aliases:
- Frack
- sensepost Frack
tags:
- breach-data
- credentials
- ai-analysis-automation
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Frack

> A local breach-data pipeline: parse messy leaked-credential dumps, load them into a queryable store, and pull per-domain `email`/`password` analytics — offline and on your own hardware.

## When to use
You already **lawfully hold** raw breach files (CSV-style `<email>,<password>` or `<email>,<hash>,<salt>`) and need to turn a heap of dumps into something searchable: "which credentials exist for `@example.com`", top passwords, per-site statistics. It is an ingestion/analysis engine for data you possess, not a lookup service that fetches breaches for you — for that, use an online breach checker instead.

## How to use it (`bestInteractionPattern`: cli)
1. Clone: `git clone https://github.com/sensepost/Frack` and follow its README (Python; expect dependency drift since it's archived).
2. **Parse** module: clean/validate the raw dump — strips invalid entries and non-ASCII, normalizes to `email,password[,hash,salt]`.
3. **Database** module: ingest the cleaned data; get analytics like top passwords and per-website counts.
4. **Query** module: search by `domain` and export an Excel report of the matching credentials.
5. Handle all output as sensitive: encrypt at rest, restrict access, log your authorization.

## Inputs → Outputs
- **In:** local breach dump files; query by `email` or `domain`
- **Out:** parsed `email`/`password` records, top-password and per-domain analytics, Excel reports
- **Empty/negative result looks like:** a domain with no rows returns an empty report — means those credentials aren't in *your* dataset, not that the person was never breached.

## Gotchas & OpSec
- **Archived / unmaintained** (`status: degraded`) — the README says a new offline version is coming; expect setup friction and consider maintained alternatives.
- **Legal gate:** possessing and processing breach data is regulated. Only use data you're authorized to hold; this is the human-in-the-loop decision, not a technical one.
- OpSec: **passive/offline** — no network calls to any target; the exposure risk is your own data-handling, not tipping off a subject.

## Overlaps ("do both")
- Different layer from online credential-exposure checkers: those tell you *whether* an address appears in a breach without you holding the data; Frack lets you *work* dumps you already have. Use an online checker for discovery, Frack for bulk local analysis.

## Trust & verifiability
`trust: community` — strong pedigree (SensePost, DEF CON 29) but explicitly archived; trust the provenance, verify it still builds before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | frack |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | email, domain → email, password |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (legal-gate) |
