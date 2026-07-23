---
id: urlcrazy
name: URLCrazy
description: Use when you have a `domain` and want its typo/look-alike variants — returns permutations plus which are registered and their resolving `ip-address`.
url: https://www.morningstarsecurity.com/research/urlcrazy
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- typosquatting
bestFor: Generating typosquat/look-alike domain permutations and checking which are registered.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free and open-source; ships with Kali Linux and installs from source (Ruby).
opsec: active
opsecNote: "URLCrazy generates ~2000 permutations and then does DNS lookups to see which resolve — those DNS queries go out from your resolver/IP. It does not connect to the target site itself, but resolving thousands of names is observable to your DNS provider. Use a privacy-respecting resolver or route through a proxy; the generated variants are only leads until you check each."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A long-standing open-source tool (Morningstar Security) bundled in Kali; permutation logic is deterministic and the registration/DNS data is read live, so results are verifiable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- urlcrazy
- URLCrazy
tags:
- typosquatting
- domain-permutation
- phishing-detection
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# URLCrazy

> Generates typo, homoglyph, and look-alike permutations of a domain, then checks which are actually registered — the classic way to find typosquats and phishing look-alikes.

## When to use
You have a `domain` and want to find the mistyped/look-alike variants of it — to detect phishing/impersonation targeting a brand, to discover a scammer's family of look-alike domains, or to enumerate infrastructure an actor registered around a real name. It outputs the variants plus which resolve and to what `ip-address`. Infrastructure/anti-phishing work, so low direct missing-persons relevance.

## How to use it (`bestInteractionPattern`: cli)
1. Run on Kali (pre-installed) or install from source: see https://www.morningstarsecurity.com/research/urlcrazy.
2. `urlcrazy -k <keyboard-layout> example.com` generates permutations (typos, character swaps, homoglyphs, TLD changes).
3. It performs DNS resolution and reports which variants are **registered**, with A/MX records and country.
4. Investigate registered look-alikes: WHOIS them, check hosting, and see if they mimic the real site.
5. Pivot resolving `ip-address`es into reverse-IP/passive-DNS to find the actor's other domains.

## Inputs → Outputs
- **In:** `domain`
- **Out:** permutation list with registration status, resolving `ip-address`, MX/country
- **Empty/negative result looks like:** most variants unregistered/NXDOMAIN — no active typosquats found (good news for a brand, or the squatter used a pattern URLCrazy didn't generate); absence isn't exhaustive proof.

## Gotchas & OpSec
- It generates ~2000 names and DNS-resolves them — visible to your DNS provider; use a privacy resolver/proxy.
- Permutation logic is heuristic; a determined squatter may use variants it doesn't produce — combine with other permutation tools (dnstwist).
- Registration status is a point-in-time DNS read; re-check for changes.

## Overlaps ("do both")
- Complements other domain-permutation tools (dnstwist) and reverse-IP/passive-DNS like [[dns-dumpster]] — URLCrazy finds the look-alikes, passive-DNS clusters the ones a single actor registered together.

## Trust & verifiability
`trust: community` — an established, Kali-bundled open-source tool; permutations are deterministic and registration data is read live via DNS, so every result is directly verifiable with a WHOIS/DNS check.
