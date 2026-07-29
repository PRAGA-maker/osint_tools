---
id: edgar-command-line-interface-edgar-tool
name: EDGAR Command Line Interface (edgar-tool)
description: Use when you have a `name`, company, or ticker and want to pull or monitor SEC EDGAR filings from the command line — returns employer-org, associate and address leads.
url: https://pypi.org/project/edgar-tool/
category: financial-crypto
path:
- financial-crypto
bestFor: Scripted full-text search and RSS monitoring of SEC EDGAR corporate filings by person, company, ticker, or CIK.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
- address
status: live
pricing: free
costNote: Free, open-source (GPLv3) Python CLI maintained by Bellingcat. Install via pip; SEC EDGAR itself is free and needs no key.
opsec: passive
opsecNote: Queries hit the SEC's public EDGAR endpoints from your IP; SEC asks automated users to set a descriptive User-Agent and rate-limit. It's passive against the target (you're reading public filings), but the SEC logs your requests — use a proxy if you must not have your IP in those logs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Maintained by Bellingcat; wraps the authoritative SEC EDGAR database, so the underlying filings are primary-source government records.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- edgar-tool
- EDGAR CLI
tags:
- bellingcat-toolkit
- companies-finance
- sec
source: bellingcat-toolkit
lastVerified: '2026-07-29'
enrichment: full
---

# EDGAR Command Line Interface (edgar-tool)

> A Bellingcat-maintained CLI that turns SEC EDGAR full-text search and filing feeds into scriptable, exportable queries — find every filing that names a person or company and monitor new ones as they land.

## When to use
You have a `name` (person or company), a ticker, or a CIK and want to search across US securities filings for mentions, or track a company's new filings in real time. EDGAR filings expose officers and directors, related entities, ownership stakes, and business addresses — so a person's name in a 10-K, 8-K, or Form 4 can reveal their `employer-org`, `associate` network, and a filing `address`. The CLI is the efficient path when you need bulk results as CSV/JSON rather than clicking through the web UI.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install edgar-tool` (Python 3.9+).
2. Set a descriptive User-Agent (SEC policy) via the tool's config/flag.
3. **Text search:** run the `text_search` subcommand with your person/company/phrase, optionally filtering by date range, form type (10-K, 8-K, Form 4…), or incorporation/office location.
4. **Monitor:** use the RSS subcommand with a ticker to track new filings as they post.
5. Export to CSV/JSON/JSONL and pivot: named officers → people-search; related entities → corporate-registry tools; addresses → geolocation/address lookups.

## Inputs → Outputs
- **In:** `name` / company / ticker / CIK (+ optional date, form-type, location filters)
- **Out:** matching filings with filer/company (`employer-org`), officers & related parties (`associate`), and filing `address` — exportable as CSV/JSON
- **Empty/negative result looks like:** zero hits for a name/phrase — the person/company isn't named in EDGAR filings (private companies and most individuals aren't), not proof they have no business ties.

## Gotchas & OpSec
- Coverage is US securities filings only — private firms and non-filers are absent.
- SEC enforces a fair-access policy: set a proper User-Agent and throttle, or you'll be blocked.
- OpSec: passive on the target; your IP is logged by the SEC — proxy if that matters.

## Overlaps ("do both")
- Pairs with corporate-registry tools (e.g. `[[federalcorporation]]` for Canada) and OpenCorporates-style sources — EDGAR covers US securities filers; registries cover incorporation records the SEC doesn't.

## Trust & verifiability
`trust: trusted` — Bellingcat-maintained client over the authoritative SEC EDGAR database; results trace directly to primary-source filings.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | edgar-command-line-interface-edgar-tool |
| category | financial-crypto |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
