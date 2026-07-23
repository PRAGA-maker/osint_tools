---
id: alienvault-open-threat-exchange
name: AlienVault Open Threat Exchange
description: Use when you have an `ip-address`, `domain`, URL, or file hash and want community threat-intel context — returns pulses and IOCs showing whether it's associated with known malicious activity.
url: https://otx.alienvault.com/browse/pulses/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- reputation
bestFor: Checking an indicator (IP/domain/hash) against crowd-sourced threat-intel "pulses" and IOCs.
selectorsIn:
- ip-address
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free (LevelBlue/AlienVault OTX). A free account and API key unlock full search, subscriptions, and API pulls.
opsec: passive
opsecNote: You query OTX's shared threat database, not the indicator's host — passive, no signal to any target. Register with a sock-puppet account; note that submitting your own indicators/pulses shares them with the community.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Large, established open threat-intel platform; pulses are community-contributed, so quality and false-positive rates vary by author.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- OTX
- AlienVault OTX
- LevelBlue OTX
tags:
- domains-ip-infrastructure
- reputation
- threat-intel
- ioc
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- alienvault-otx
---

# AlienVault Open Threat Exchange

> A crowd-sourced threat-intelligence exchange — check any indicator (IP, domain, URL, hash) against community "pulses" to see if it's tied to known malicious campaigns.

## When to use
You have an `ip-address`, `domain`, URL, or file hash from an investigation and want to know whether the security community has flagged it: which threat "pulses" reference it, what campaign/malware it's linked to, and what related IOCs (other `domain`s/`ip-address`es) travel with it. A fast reputation-and-context check that also expands one indicator into a cluster.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://otx.alienvault.com/ and register a free account (needed for full search/API).
2. Search the indicator (IP/domain/URL/hash), or browse pulses.
3. Read the results: pulses referencing it, tags (malware family/campaign), and the associated IOC list.
4. Pivot: related IOCs (other `domain`s/`ip-address`es) extend your infrastructure map; subscribe to relevant pulses or pull them via the API to automate.

## Inputs → Outputs
- **In:** `ip-address`, `domain`, URL, or file hash
- **Out:** matching threat pulses + related IOC `domain`s/`ip-address`es and campaign context
- **Empty/negative result looks like:** no pulses reference the indicator — it's not in community reporting (not proof it's clean); corroborate with other reputation sources.

## Gotchas & OpSec
- Human-in-the-loop: full search and API need a (free) account.
- Pulses are community-authored — accuracy varies; a single low-quality pulse can create noise. Weigh corroboration across pulses.
- Contributing your own indicators shares them publicly — don't upload case-sensitive IOCs you need to keep quiet.

## Overlaps ("do both")
- Pairs with `[[malwareurl]]`, VirusTotal-style engines, and `[[bgp-malicious-content-ranking]]` — OTX adds campaign/community context; cross-check verdicts because each source has different coverage.

## Trust & verifiability
`trust: community` — a major, well-known platform, but its data is crowd-sourced; treat pulse attributions as leads to corroborate, not settled facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | alienvault-open-threat-exchange |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address, domain → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
