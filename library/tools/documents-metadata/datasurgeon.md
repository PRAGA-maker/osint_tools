---
id: datasurgeon
name: DataSurgeon
description: Use when you have a blob of text (breach dump, log, scraped page, document) and want to pull every selector out of it — returns `email`, `phone`, `ip-address`, `crypto-wallet`, `mac-address` and hashes.
url: https://github.com/Drew-Alleman/DataSurgeon
category: documents-metadata
path:
- documents-metadata
bestFor: Fast regex extraction of emails/phones/IPs/wallets/hashes from dumps, logs or scraped text.
selectorsIn: []
selectorsOut:
- email
- phone
- ip-address
- mac-address
- crypto-wallet
- password
status: live
pricing: free
costNote: Free, open-source (Rust). Build from source; no account.
opsec: passive
opsecNote: Runs entirely locally on files/text you already hold — nothing is sent to any server, so it is safe to run against sensitive dumps offline. Keep the source material and outputs on an encrypted disk.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Actively used open-source utility (~900 stars); does simple regex extraction with no external calls, so behaviour is easy to audit.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- ds
- Drew-Alleman/DataSurgeon
tags:
- data-extraction
- regex
- rust
- parsing
- breach-dumps
source: gh-topic-reconnaissance
lastVerified: '2026-07-17'
enrichment: full
---

# DataSurgeon

> A fast Rust CLI that scrapes structured selectors — emails, phones, IPs, MACs, crypto wallets, credit cards, SSNs, hashes — out of any pile of text.

## When to use
You already have raw material tied to your subject — a breach dump, chat/log export, a scraped web page, a PDF's extracted text, pastebin content — and you need to harvest every actionable selector from it quickly. DataSurgeon (`ds`) reads stdin, files, or directories and emits the emails, phone numbers, IPs, MAC addresses, crypto wallets and password hashes it finds, so you can triage a large dump into pivots in seconds rather than eyeballing it.

## How to use it (`bestInteractionPattern`: cli)
1. Install (needs Rust + git). Linux/macOS: run the repo's install script, e.g.
   `bash <(curl -s https://raw.githubusercontent.com/Drew-Alleman/DataSurgeon/main/install/install.sh)`; Windows has a PowerShell installer.
2. Pipe or point it at your text:
   - `cat dump.txt | ds` — extract everything.
   - `ds -f dump.txt -i -m` — only IPs (`-i`) and MAC addresses (`-m`).
   - `ds -D ./scrape_dir -e -o found.csv` — recurse a directory, pull emails, write CSV.
3. Read the output in the terminal or the CSV; each match is a candidate selector.
4. Pivot: feed extracted `email`/`phone` into account-existence and breach-lookup tools, `crypto-wallet` into chain explorers, `ip-address` into geo/IP intel.

## Inputs → Outputs
- **In:** raw text — a file, a directory of files, stdin, or a fetched URL's body (no fixed selector; you supply the corpus)
- **Out:** `email`, `phone`, `ip-address`, `mac-address`, `crypto-wallet`, credit-card numbers, SSNs, URLs, and password/hash strings (MD5/SHA/NTLM/bcrypt, etc.)
- **Empty/negative result looks like:** no lines printed — the corpus contained none of the patterns, or the data is obfuscated/encoded (base64, images) so regex can't see it. Absence isn't proof the selector isn't in the source.

## Gotchas & OpSec
- Pure pattern matching: it will surface false positives (random hex that looks like a hash, numbers that look like phones). Validate before acting.
- It cannot read binary/encoded content — extract text first (OCR a scanned PDF, decode base64) before feeding it in.
- Fully offline and local; ideal for sensitive breach data you must not upload. Handle inputs/outputs on encrypted storage.

## Overlaps ("do both")
- Complements any collection tool that produces bulk text: scrape or download first, then run DataSurgeon to structure the haul into selectors.

## Trust & verifiability
`trust: community` — a popular, actively-maintained open-source CLI. Because it makes no network calls and just applies published regexes, its behaviour is fully auditable from the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | datasurgeon |
| category | documents-metadata |
| selectorsIn → selectorsOut |  → email, phone, ip-address, mac-address, crypto-wallet, password |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
