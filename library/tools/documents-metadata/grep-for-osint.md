---
id: grep-for-osint
name: Grep for OSINT
description: Use when you have a text corpus or file directory (a dump, scraped pages, logs) and want to bulk-extract selectors — returns email, phone, ip-address and crypto-wallet leads.
url: https://github.com/cipher387/grep_for_osint
category: documents-metadata
path:
- documents-metadata
bestFor: Bulk-extracting emails, phones, URLs, IPs, and crypto wallets from text files/directories with ready-made grep patterns.
selectorsIn:
- email
- phone
selectorsOut:
- email
- phone
- ip-address
- crypto-wallet
status: live
pricing: free
costNote: Free, open-source collection of grep patterns/commands (cipher387). No install beyond grep on any Unix-like system.
opsec: passive
opsecNote: Fully passive and offline — it runs local grep over files you already have, making no network calls. Nothing leaves your machine, so it's safe to run against sensitive dumps in an air-gapped environment.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source pattern collection by cipher387 (a prolific OSINT author); it's just grep regexes, so quality depends on the pattern — expect the usual regex false positives.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- advanced-search-operators-list
- apis-for-osint
- awesome-grep
- code-understanding-tools-list
- dorks-collections-list
- maltego-transforms-list
- python-osint-automation-examples
aliases:
- grep_for_osint
- Grep for OSINT
tags:
- Files
- extraction
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Grep for OSINT

> A cheat-sheet of ready-made grep patterns for OSINT — point them at a text dump or file directory and pull out every email, phone number, URL, IP, and crypto wallet, entirely offline.

## When to use
You've collected a blob of unstructured text — a breach/leak dump, scraped web pages, chat exports, log files, an OCR'd document set — and you need to rapidly harvest the selectors buried in it: `email`s, `phone`s, URLs, `ip-address`es, and `crypto-wallet`s. Instead of writing regexes from scratch, you copy the tested patterns from this toolkit. It's the fast, offline first pass over any corpus before you enrich the extracted selectors.

## How to use it (`bestInteractionPattern`: cli)
1. Open the repo (https://github.com/cipher387/grep_for_osint) and copy the pattern for the selector you want (emails, phones, URLs, IPs, BTC/ETH addresses, etc.).
2. Run it over your data, e.g. `grep -aoiE '<pattern>' -r ./corpus/ | sort -u`.
3. Collect the deduplicated extraction into a candidate list.
4. Sanity-check the output — regex over messy text yields false positives (partial matches, non-real values).
5. Pivot: extracted `email`s → email-verification/breach tools; `phone`s → phone OSINT; `crypto-wallet`s → chain explorers; IPs → `[[team-cymru-ip-to-asn]]`.

## Inputs → Outputs
- **In:** a local text file or directory of collected data (a dump, scraped pages, logs)
- **Out:** deduplicated lists of `email`s, `phone`s, URLs, `ip-address`es, `crypto-wallet`s extracted from the text
- **Empty/negative result looks like:** no matches — the corpus genuinely lacks that selector type, or it's encoded/obfuscated so the regex misses it; try a looser pattern or decode the data first.

## Gotchas & OpSec
- Regex extraction → false positives (and misses on obfuscated data); always review before enriching.
- It extracts; it does not validate — an extracted email/phone still needs verification that it's real and current.
- OpSec: fully offline/passive — ideal for sensitive dumps you must not upload anywhere.

## Overlaps ("do both")
- Sits alongside `[[awesome-grep]]`, `[[dorks-collections-list]]`, and `[[python-osint-automation-examples]]` — grep for quick offline extraction; the Python examples for structured, repeatable pipelines.

## Trust & verifiability
`trust: community` — a maintained open-source pattern collection; it's plain grep, so the only trust question is the regex quality, which you verify by reviewing output.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | grep-for-osint |
| category | documents-metadata |
| selectorsIn → selectorsOut | email, phone → email, phone, ip-address, crypto-wallet |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
