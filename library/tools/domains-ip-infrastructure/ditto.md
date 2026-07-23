---
id: ditto
name: Ditto
description: Use when you have a `domain` and want to find look-alike/homograph variants — generates confusable domain permutations and checks which are registered, surfacing phishing/typosquat domains.
url: https://github.com/evilsocket/ditto
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Generating IDN-homograph/look-alike domain variants and checking their registration status.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
opsec: passive
opsecNote: Ditto generates variant strings and checks registration/availability (WHOIS/DNS), which queries registries and resolvers rather than probing the look-alike sites — so it's passive toward any target. If you then visit a discovered phishing domain, do so from a sandbox/sock-puppet, as it may be hostile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source tool by evilsocket (Simone Margaritelli), a well-known security researcher; small, auditable Go/utility.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- xray
aliases:
- ditto
- evilsocket/ditto
tags:
- homograph
- typosquatting
- phishing-detection
- domain-and-ip-investigation
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Ditto

> A look-alike domain generator — feed it a domain and it produces homograph/confusable variants (IDN swaps, typos), then checks which are already registered, exposing typosquats and phishing infrastructure.

## When to use
You have a `domain` — a brand, an organization, or a subject's site — and want to find impersonating look-alikes: internationalized-homograph swaps (e.g. Cyrillic "а" for Latin "a"), common typos, and near-misses. Registered variants often point to phishing or brand-abuse infrastructure worth investigating; unregistered ones flag exposure. A defensive/attribution tool for uncovering domains built to imitate a target.

## How to use it (`bestInteractionPattern`: cli)
1. Install from https://github.com/evilsocket/ditto (Go); build/run the binary.
2. Run it against the target `domain`; it generates the homograph/variant set.
3. Read the output: each variant with its registration status (registered vs available) (`selectorsOut`).
4. Pivot: registered look-alikes → WHOIS/hosting/certificate analysis to attribute the impersonator; visit any suspicious site only from a sandbox.

## Inputs → Outputs
- **In:** `domain`
- **Out:** `domain` — a set of homograph/typo variants, each flagged registered or available
- **Empty/negative result looks like:** all variants unregistered — no active look-alikes found (good news defensively), NOT a guarantee none exist beyond ditto's permutation set.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive — it checks registration/DNS, not the look-alike sites themselves; only *visiting* a discovered phishing domain is risky, so sandbox it.
- Coverage is bounded by ditto's permutation logic; a determined impostor may use variants it doesn't generate — combine with other typosquat tools.

## Overlaps ("do both")
- Pairs with dnstwist/urlcrazy (other permutation engines) and certificate-transparency monitoring ([[censys]]/crt.sh) — cross-run because each generates different variants, and CT logs catch look-alikes as soon as they get a certificate.

## Trust & verifiability
`trust: community` — an open-source tool from a reputable security researcher; small and auditable. Its variant list and registration checks are reliable within its permutation scope, so treat a "no look-alikes" result as scoped to what it generates.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ditto |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
