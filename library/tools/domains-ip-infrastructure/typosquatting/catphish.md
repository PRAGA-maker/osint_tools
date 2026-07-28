---
id: catphish
name: Catphish
description: Use when you have a `domain` and want to enumerate lookalike/typosquat variants (and which are registered or available) — returns candidate `domain`s.
url: https://github.com/ring0lab/catphish
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- typosquatting
bestFor: Generating and checking lookalike/typosquat domain variants of a target domain for typosquat monitoring and brand-protection.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source (Ruby CLI, or run via Docker).
opsec: passive
opsecNote: Generating permutations is local and passive. The availability/expired checks query domain registries/WHOIS, and the categorization feature queries proxy-vendor services — none of this contacts the target's own domain. This is a red-team tool; use it only in authorized/defensive contexts.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source tool (ring0lab, 600+ stars); its permutation logic is in the same family as dnstwist/urlcrazy. Results are candidate strings that must be checked and interpreted.
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
- catphish.rb
tags:
- typosquatting
- lookalike-domains
- brand-protection
- red-team
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# Catphish

> A domain-permutation generator: feed it one `domain` and it produces the lookalike/typosquat variants an attacker might use — then tells you which are already registered or free.

## When to use
You have a `domain` (a subject's, a client's, or one referenced in a scam) and want to enumerate the confusable variants around it: homoglyphs, plural/singular forms, added/removed dashes, double extensions, Punycode. Then you check which of those variants are actually registered — surfacing typosquats already sitting on a brand, or mapping the space of names a phishing campaign could adopt. Standard defensive/monitoring OSINT for domains.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `https://github.com/ring0lab/catphish` and `bundle install` (Ruby), or use the provided Docker image.
2. Generate variants for a target: `catphish.rb -D <domain> generate -A` (runs all permutation algorithms).
3. Find registrable/expired lookalikes: `catphish.rb -D <domain> expired`.
4. Review the output list of candidate `domain`s and their registration status.
5. Pivot: a **registered** lookalike is a live lead — run it through WHOIS, passive DNS, and hosting lookups to see who stood it up and whether it's serving a phishing clone.

## Inputs → Outputs
- **In:** a target `domain`
- **Out:** a list of lookalike/typosquat `domain` candidates with registration/availability status
- **Empty/negative result looks like:** all generated variants are unregistered — no one is currently squatting the obvious lookalikes (re-run periodically, since that changes).

## Gotchas & OpSec
- Output is **candidate strings**, not confirmed threats — every registered hit needs its own investigation before you attribute intent.
- This is red-team tooling; the availability/categorization features exist for offensive ops. Use it strictly for authorized assessment, typosquat monitoring, or investigating a domain already implicated in abuse.
- OpSec: it doesn't touch the target domain; the lookups it makes hit registries/proxy-vendors from your host.

## Overlaps ("do both")
- Same problem space as dnstwist/urlcrazy — run more than one, as each permutation engine generates a slightly different variant set; feed registered hits into WHOIS/passive-DNS tooling.

## Trust & verifiability
`trust: community` — a well-known open-source project; it only generates and status-checks names, so trust rests on you validating each registered lookalike rather than on the tool asserting anything.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | catphish |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
