---
id: email-extractor
name: Email Extractor
description: Use when you have a block of text or a web page and want every email address in it — returns a deduplicated list of extracted addresses.
url: https://99tools.net/email-extractor/
category: email
path:
- email
bestFor: Pulling all email addresses out of pasted text (or a page's content) into a clean list.
selectorsIn:
- metadata
selectorsOut:
- email
status: live
pricing: free
costNote: Free web utility on 99tools.net; ad-supported, no account.
opsec: passive
opsecNote: Extraction runs on text you paste; it does not contact any address. If you paste a URL for it to fetch, that fetch may originate from the tool's servers (or your browser) — paste raw text when you want zero target contact.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A generic free utility site; the regex-style extraction is straightforward, but avoid pasting sensitive source material into a third-party page.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- email-search-email-check
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Email Extractor

> A free 99tools utility that scans pasted text and returns a deduplicated list of all email addresses found.

## When to use
You have a chunk of text — a scraped profile, a document dump, a forum thread, a contact page — and want to harvest every `email` address inside it quickly rather than eyeballing. Useful for turning unstructured material around a missing person into a list of addresses to validate and pivot on.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://99tools.net/email-extractor/.
2. Paste the source text into the input box.
3. Submit; it returns a deduplicated list of email addresses.
4. Pivot: run each extracted address through `[[email-dossier]]` / `[[email-address-validator]]` to find the live ones, then `[[email-breach-analysis]]`.

## Inputs → Outputs
- **In:** raw text / page content (`metadata`)
- **Out:** list of `email` addresses (deduplicated)
- **Empty/negative result looks like:** no addresses returned — the text contained none, or they were obfuscated (e.g. "name [at] domain [dot] com"), which this won't catch.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive on pasted text; if you ask it to fetch a URL, that introduces a fetch you don't control — prefer pasting raw text.
- It only matches plain-format addresses; obfuscated or image-based emails are missed, so absence is not proof.

## Overlaps ("do both")
- Feeds `[[email-permutator]]` indirectly: once you have real addresses you can confirm the org's format; pairs with any validator to triage the harvested list.

## Trust & verifiability
`trust: community` — simple, transparent extraction utility; reliability is high for plain-text addresses, but it is a third-party host so don't paste sensitive material.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | email-extractor |
| category | email |
| selectorsIn → selectorsOut | metadata → email |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
