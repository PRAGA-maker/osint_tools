---
id: altdns
name: AltDNS
description: Use when you have a set of known subdomains for a `domain` and want to discover more by permutation — returns resolved alternate subdomains.
url: https://github.com/infosec-au/altdns
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- subdomains
bestFor: Generating and resolving permutation-based subdomain guesses (dev-, staging-, -1, -old) from known subdomains.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free and open source (Python). Limited maintenance (open PRs/issues), but the core still works.
opsec: active
opsecNote: AltDNS resolves each generated permutation via DNS. Those lookups are active — they hit DNS resolvers (and, for the target's zone, ultimately its authoritative servers), which can be logged. Use your own/neutral resolvers and only enumerate domains you're authorised to assess; consider a VPS you're willing to attribute.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A long-known subdomain-permutation tool. Effectiveness depends on a good seed set (200+ known subdomains) and wordlist; it complements rather than replaces passive enumeration.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- subdomain-finder
aliases:
- infosec-au/altdns
tags:
- subdomains
- dns-recon
- permutation
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# AltDNS

> A DNS-permutation tool: take the subdomains you already know for a target, mutate them with a wordlist (dev-, staging-, -old, -1…), and resolve the guesses to find subdomains passive tools missed.

## When to use
You've already enumerated a target `domain`'s subdomains passively (e.g. via `[[subdomain-finder]]`) and want to squeeze out more — the predictable variants (`dev-api`, `staging-app`, `app-old`, `app2`) that only appear by guessing. AltDNS generates those permutations from your seed set and DNS-resolves them to confirm which exist.

## How to use it (`bestInteractionPattern`: cli)
1. Install from the repo (Python). Gather a solid seed list of known subdomains — it works best with 200+.
2. Run AltDNS with the seed list, a permutation wordlist, and the target `domain`; point it at your chosen resolvers with the desired thread count.
3. It generates altered candidates and resolves them, outputting the ones that resolve (with their IPs).
4. Verify hits are live and belong to the target before acting.
5. Pivot: newly found subdomains + resolved `ip-address` feed reverse-IP/infrastructure mapping and content review.

## Inputs → Outputs
- **In:** a seed list of known subdomains + wordlist + target `domain`
- **Out:** resolved alternate subdomains (`domain`) and their `ip-address`
- **Empty/negative result looks like:** few/no new subdomains — a thin seed set or wordlist, or the target simply doesn't use predictable naming. Enrich the seed set (passive enumeration first) and retry.

## Gotchas & OpSec
- **Active** DNS resolution: lookups are logged by resolvers and ultimately the target's authoritative DNS — authorise your scope and use neutral resolvers.
- Quality is bounded by the seed set and wordlist; garbage in, garbage out. Seed it from good passive enumeration.
- Limited maintenance; the concept is standard but consider modern equivalents (dnsgen, gotator) too.

## Overlaps ("do both")
- Complements passive enumerators like `[[subdomain-finder]]` — passive gives you the seed set, AltDNS permutes it to find the rest. Do passive first, then permute.

## Trust & verifiability
`trust: community` — a recognised subdomain-permutation tool. Reliable at *generating and resolving* candidates; every resolved host still needs verification that it's live and target-owned.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | altdns |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
