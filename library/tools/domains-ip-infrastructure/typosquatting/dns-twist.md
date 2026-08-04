---
id: dns-twist
name: DNS Twist
description: Use when you have a `domain` and want to find look-alike/typosquatted variants and check which are registered or hosting phishing — returns permuted domains with their DNS, geolocation and page-similarity data.
url: https://github.com/elceef/dnstwist
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- typosquatting
bestFor: Generating and live-checking look-alike domains around a target domain to spot phishing/impersonation.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
- geolocation
status: live
pricing: free
costNote: Free and open-source (Apache-2.0). No paid tier or API keys.
opsec: active
opsecNote: It performs live DNS (and optionally HTTP/banner) lookups against the permuted domains — a large permutation set can mean hundreds of thousands of queries from your resolver/IP. It does not touch the original target's owner, but the lookups are observable to DNS operators; throttle and use a research resolver.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Widely used, long-maintained open-source tool (Marcin Ulikowski / elceef); packaged in major distros and Docker.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- dnstwist
tags:
- typosquatting
- phishing
- domain-permutation
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# DNS Twist

> A domain-permutation engine: give it one domain and it generates the homoglyph/typo variants, then checks which are live, where they resolve, and how closely they mimic the original.

## When to use
You have a `domain` (a subject's business, a brand being impersonated in a scam tied to your case, or a site you suspect has phishing clones) and want to enumerate look-alike domains and see which are registered and serving content. Useful for mapping impersonation infrastructure and finding related registrants/IPs to pivot on.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install dnstwist[full]` (or `apt/brew install dnstwist`, or Docker).
2. Basic run: `dnstwist --registered example.com` to list only variants that actually resolve.
3. Add detection: `--lsh` (fuzzy HTML similarity) and `--phash` (visual/screenshot similarity) to flag pages mimicking the original; `--geoip` for location.
4. Export: `--format csv|json` for downstream analysis.
5. Pivot: registered look-alikes give you new `domain`/`ip-address`/registrant leads — feed them into WHOIS and host-enrichment tools.

## Inputs → Outputs
- **In:** a single `domain`.
- **Out:** a table of permuted `domain`s with resolved `ip-address`, `geolocation`, DNS/MX records, and similarity scores for registered ones.
- **Empty/negative result looks like:** with `--registered`, an empty list means no permutations are currently registered — normal for low-value or well-defended names.

## Gotchas & OpSec
- **Active & noisy:** large brands generate huge permutation sets and correspondingly large query volumes; throttle and expect resolver rate-limits.
- Registration ≠ malice — a registered look-alike may be defensive (owned by the brand) or parked; use the similarity/HTTP checks to prioritise.
- Perceptual-hash/HTML checks need the `[full]` extras installed.

## Overlaps ("do both")
- Feed its registered variants into host enrichment like `[[hostintel-keithjjones-github]]` and recon frameworks like `[[recon-ng]]` to attribute the infrastructure behind the impersonating domains.

## Trust & verifiability
`trust: trusted` — a mature, widely packaged open-source tool; its permutations and live checks are deterministic and reproducible, so results are easy to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dns-twist |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
