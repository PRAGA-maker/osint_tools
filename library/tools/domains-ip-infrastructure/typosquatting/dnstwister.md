---
id: dnstwister
name: dnstwister
description: Use when you have a `domain` and want its typosquat/look-alike permutations and whether they're registered — returns candidate domain variants with registration/DNS/IP status.
url: https://dnstwister.report/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- typosquatting
bestFor: Generating look-alike domain permutations of a target and checking which are registered/resolving.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free web tool and API (the .report site now redirects to dnstwister.com); no account needed for lookups.
opsec: active
opsecNote: Generating permutations is passive, but resolving/checking each variant issues DNS queries (and the tool may probe them), which is active against the variant domains' infrastructure. For sensitive work, be aware you're touching DNS for look-alike domains that a phisher may control.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known, long-running free typosquatting tool; permutation generation is deterministic, and registration/DNS status is only as fresh as its last resolution.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- dnstwister.report
- dnstwister.com
tags:
- typosquatting
- domain-permutation
- phishing
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# dnstwister

> A free typosquatting engine: give it a domain and it generates the look-alike permutations a phisher might register, then tells you which are actually live.

## When to use
You have a `domain` (a brand, an org, a target site) and want to find its impersonators or defensive gaps: which typo/homoglyph/TLD-swap variants exist, which are registered, and where they resolve. Reach for dnstwister to hunt phishing/lookalike domains around a target, or to map a cluster of confusable domains that may share an operator. It both *generates* the candidate space and *checks* live status.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the site and enter the base `domain`.
2. It generates permutations (character swaps, omissions, homoglyphs, TLD changes, insertions).
3. For each variant, check the reported registration/DNS status and resolved IP.
4. Focus on registered variants that resolve — those are live look-alikes worth investigating (phishing, brand abuse, or co-owned infra).
5. Pivot: a live variant's IP/host feeds infrastructure analysis (`[[technology-lookup]]`, passive-DNS); use the API to monitor a domain's permutation space over time.

## Inputs → Outputs
- **In:** `domain`
- **Out:** look-alike `domain` variants with registration/DNS status and resolved `ip-address`
- **Empty/negative result looks like:** most permutations unregistered/non-resolving — normal; the signal is the small set that *are* live, not the long list of unused variants.

## Gotchas & OpSec
- Registration/DNS status reflects when it last checked — re-resolve a promising variant to confirm it's currently live.
- OpSec: **active** in that checking variants issues DNS queries against domains a threat actor may control; keep that in mind for sensitive investigations.
- Permutation coverage is broad but not exhaustive — combine with other typosquatting generators for edge cases.

## Overlaps ("do both")
- Pairs with certificate-transparency search and passive-DNS — dnstwister *predicts* look-alike domains, CT/passive-DNS *confirm* ones that actually exist and issued certs. Feed live variants into `[[technology-lookup]]` to link them by shared stack/IDs.

## Trust & verifiability
`trust: community` — a mature, widely-used free tool; permutation generation is deterministic and reliable, while live-status fields should be re-verified since they depend on the tool's last resolution.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dnstwister |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
