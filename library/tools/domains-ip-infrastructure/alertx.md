---
id: alertx
name: alterx
description: Use when you have a `domain` and known subdomains and want more candidates to test — returns permutation-generated subdomain wordlists for active enumeration.
url: https://github.com/projectdiscovery/alterx
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Generating smart subdomain permutations from known results to feed a DNS resolver during subdomain discovery.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source (MIT) from ProjectDiscovery; install via Go (`go install github.com/projectdiscovery/alterx/cmd/alterx@latest`).
opsec: passive
opsecNote: alterx itself only generates candidate names locally from patterns — it sends nothing to the target. The active/observable step is when you resolve those candidates with a DNS tool; that traffic can be logged, so throttle and use resolvers deliberately.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Maintained by ProjectDiscovery, a well-known security-tooling vendor with widely used open-source projects; source is public and auditable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- dnsx
- subfinder
- cve-map
aliases:
- alterx
- projectdiscovery/alterx
tags:
- Domain/IP/Links
- Subdomains scan/brute
- subdomain-enumeration
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# alterx

> ProjectDiscovery's subdomain *permutation* generator: feed it the subdomains you already found and a DSL pattern, and it emits a tailored wordlist of likely additional subdomains to resolve.

## When to use
You are mapping a target `domain`'s attack surface and passive enumeration (`[[subfinder]]`) has returned a set of subdomains, but you suspect more exist behind predictable naming (dev-, staging-, api-, region prefixes). alterx generates permutations from those known names using customizable patterns, producing candidates you then resolve to discover hosts that passive sources missed.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `go install github.com/projectdiscovery/alterx/cmd/alterx@latest`.
2. Pipe known subdomains in: `subfinder -d example.com -silent | alterx` (optionally with a custom pattern using `{{sub}}`, `{{word}}`, `{{suffix}}`).
3. alterx prints permuted candidate subdomains — this step is local and sends nothing to the target.
4. Resolve the candidates to find live hosts: `alterx ... | dnsx` (this is the active, network-touching step).
5. Pivot: live subdomains feed port/service scanning and further infrastructure mapping.

## Inputs → Outputs
- **In:** a `domain` plus known subdomains + a permutation pattern
- **Out:** a wordlist of candidate `domain`s (subdomains) to resolve
- **Empty/negative result looks like:** few/no useful permutations — if the seed set is tiny or naming is random, generated candidates won't resolve; that's a data-poverty signal, not a tool failure.

## Gotchas & OpSec
- Human-in-the-loop: none; CLI, composable in a pipeline.
- OpSec: alterx alone is **passive** (local generation); the observable footprint is the subsequent DNS resolution (`dnsx`) — rate-limit and choose resolvers with care against the target.
- Quality in = quality out: permutations are only as good as the seed subdomains and pattern; pair with strong passive discovery first.

## Overlaps ("do both")
- Pairs with `[[subfinder]]` (passive discovery to seed it) and `[[dnsx]]` (to resolve its output) — the three form the standard permutation-enumeration chain.

## Trust & verifiability
`trust: trusted` — open-source and maintained by ProjectDiscovery; auditable code, and every candidate it emits is independently verified the moment you resolve it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
