---
id: haklistgen
name: HakListGen
description: Use when you have a target's text/pages (from a `domain` or file) and want a custom wordlist for fuzzing — returns a deduplicated word/token list to feed subdomain/path discovery.
url: https://github.com/hakluke/haklistgen
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Generating a bespoke wordlist from any text or web page to fuel targeted subdomain/content discovery.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source (Go); install/build yourself. No account.
opsec: passive
opsecNote: Building the wordlist is offline/passive. The downstream fuzzing you feed it into is ACTIVE against the target — that step, not this one, needs a sock-puppet IP and care.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: A small open-source utility by hakluke (well-known in the recon community); code is short and auditable, but it is a personal project, not a supported product.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- hakrawler
aliases:
- haklistgen
- hakluke wordlist generator
tags:
- Domain/IP/Links
- Wordlists generators
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# HakListGen

> A tiny Go utility that turns any text or web page into a deduplicated wordlist — raw material for targeted subdomain and content discovery.

## When to use
You are doing infrastructure recon on a `domain` and want a wordlist tuned to the target rather than a generic one — e.g. scrape the target's site and turn its vocabulary into candidate subdomain/path names for fuzzing. It produces a wordlist; it does not itself query the target.

## How to use it (`bestInteractionPattern`: cli)
1. Install from https://github.com/hakluke/haklistgen (Go: `go install`), or clone and build.
2. Pipe text or a URL's content into it; it extracts and deduplicates tokens into a wordlist on stdout.
3. Save the list and feed it to a fuzzer/subdomain tool (e.g. ffuf, gobuster, a subdomain bruteforcer).
4. The discovery step against the live target is the active part — do that from a sock-puppet environment.

## Inputs → Outputs
- **In:** text or a page from a `domain`
- **Out:** a deduplicated wordlist (candidate `domain`/path tokens)
- **Empty/negative result looks like:** a tiny/empty list because the input had little unique text — feed it more source material or combine with a standard wordlist.

## Gotchas & OpSec
- Human-in-the-loop: none, but you must have Go/build tooling.
- OpSec: generating the list is passive; the fuzzing you feed it into is **active** recon — mind rate limits and attribution there.
- It only tokenises text — quality depends entirely on the source material you give it.

## Overlaps ("do both")
- Pairs with `[[hakrawler]]` — crawl the target with hakrawler to gather text, then pipe that into HakListGen to build the wordlist; two halves of one recon pipeline.

## Trust & verifiability
`trust: unverified` — a small, auditable personal open-source tool from a respected author; read the (short) source before running, as with any recon utility.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | haklistgen |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
