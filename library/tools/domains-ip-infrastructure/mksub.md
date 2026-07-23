---
id: mksub
name: mksub
description: Use when you have a `domain` and want a large candidate subdomain list to brute-force — returns permuted multi-level subdomain names for resolvers.
url: https://github.com/trickest/mksub
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Generating tens of thousands of multi-level subdomain permutations from a wordlist to feed a DNS brute-forcer.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open source (MIT). Binary, Docker, or `go install`.
opsec: passive
opsecNote: mksub only *generates* candidate names locally — it performs no DNS queries itself, so it's passive. The active exposure comes from whatever resolver/brute-forcer you feed its output to; anonymise that step.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Maintained by Trickest, a reputable recon-automation vendor; small auditable Go utility.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- mkpath
- trickest-inventory
aliases:
- mksub
tags:
- subdomain-enumeration
- wordlist-generator
- recon
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# mksub

> A permutation generator: take a wordlist and a domain, get every multi-level subdomain combination to throw at a resolver.

## When to use
You're mapping an organisation's attack surface from a `domain` and want an exhaustive candidate subdomain list for brute-force resolution — including deep nesting like `prod.dev.example.com`. mksub does one job fast: it expands a wordlist into subdomain permutations up to a chosen depth. It produces *candidates only* — you still resolve them with another tool. Infrastructure recon; low, indirect missing-persons value.

## How to use it (`bestInteractionPattern`: cli)
1. Install: download a binary/Docker image or `go install github.com/trickest/mksub@latest`.
2. Generate candidates:
   ```
   mksub -d example.com -w words.txt -l 2 -o candidates.txt
   ```
   `-d` single domain (`-df` for a file of domains), `-w` wordlist, `-l` subdomain depth, `-r` regex filter, `-o` output.
3. Note scale: a 500-word list at level 2 yields ~250,000 names — size the wordlist and depth to what your resolver can handle.
4. Pivot: feed `candidates.txt` into a fast resolver/brute-forcer (puredns, massdns, shuffledns) or Amass to find which subdomains actually resolve.

## Inputs → Outputs
- **In:** `domain` + a wordlist
- **Out:** a list of candidate `domain` (subdomain) names — unresolved permutations
- **Empty/negative result looks like:** an empty/tiny output means an empty wordlist or bad flags; mksub always emits combinations if given words — it does not tell you which exist (that's the resolver's job).

## Gotchas & OpSec
- Output is *unvalidated* candidates — none are confirmed to exist until you resolve them.
- Depth grows results combinatorially; level 3+ on a big wordlist can be unusably large.
- OpSec: mksub itself is passive (no DNS); the resolving step is where you touch infrastructure — route it through anonymised resolvers.

## Overlaps ("do both")
- Upstream of DNS brute-forcers (massdns/puredns/shuffledns) and complements passive enumeration (Amass, subfinder) — passive tools find *known* subdomains, mksub+brute-force finds *unlisted* ones. Sibling tool `[[mkpath]]` does the same for URL paths.

## Trust & verifiability
`trust: community` — small, auditable Go tool from Trickest; it generates strings and makes no external claims, so the only verification needed is resolving the candidates.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mksub |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
