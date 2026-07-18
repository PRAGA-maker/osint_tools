---
id: the-hitchhiker-s-guide-to-online-anonymity
name: The Hitchhiker’s Guide to Online Anonymity
description: Use when you (the investigator) need to build anonymous OSINT infrastructure and threat-model your own OPSEC — returns a comprehensive, free anonymity/OPSEC manual.
url: https://anonymousplanet.net/guide/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- privacy-clean-up
bestFor: A deep, first-principles reference for building anonymous OSINT setups and protecting the investigator's own identity.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Completely free; open-source community guide, also mirrored and available as PDF/on the Internet Archive.
opsec: passive
opsecNote: This is reading material about OPSEC, not a tool you point at a target — consuming it leaks nothing. Its purpose is the opposite: to teach you how to keep your own investigation unattributable before you touch active tools.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running, community-maintained anonymity guide (Anonymous Planet) with a public changelog and GitLab repo; widely cited in the OSINT/privacy community.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- THGTOA
- Anonymous Planet
- anonymousplanet.net
tags:
- opsec
- anonymity
- threat-modeling
- guide
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# The Hitchhiker’s Guide to Online Anonymity

> A book-length, free OPSEC manual — the reference for building an anonymous OSINT working environment and threat-modeling your own exposure before an investigation.

## When to use
Before you run active tools against a target, or whenever you need to harden the investigator side of an operation. This is not a lookup service; it is the definitive walk-through for creating anonymous identities, choosing and compartmentalising devices/VPNs/Tor, avoiding correlation and de-anonymisation, and reasoning about your own threat model from first principles. Reach for it when a case is sensitive enough that your own attribution is a risk.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://anonymousplanet.net/guide/ (mirrors and a PDF/Internet-Archive copy exist if the primary is unreachable — the project moved off the old `.org` domain).
2. Start with the threat-modeling and "requirements" chapters to scope how much anonymity your case actually needs.
3. Follow the relevant build sections — anonymous OS/VM setup, network layering (VPN/Tor), creating and maintaining sock-puppet identities, and behavioural OPSEC.
4. Apply it operationally: use it to design the sock-puppet environment you then run other tools from.
5. Pivot: it underpins every `opsec: active` tool in this library — read it first, then execute.

## Inputs → Outputs
- **In:** none (it's a reference you read, not a query you run)
- **Out:** OPSEC knowledge — anonymous-infrastructure blueprints, threat models, de-anonymisation pitfalls
- **Empty/negative result looks like:** N/A — this is documentation; the failure mode is skipping it and getting yourself attributed.

## Gotchas & OpSec
- It's long and detailed by design — treat it as a manual to consult per-topic, not a quick checklist.
- The canonical domain has changed over the years (`.org` → current `.net`); use a mirror or the archived copy if the live site is down.
- No tool leaks here; the risk is *not* reading it before running active OSINT.

## Overlaps ("do both")
- Pairs with every active/high-leak tool in the library (e.g. account-existence checks, messenger lookups) — this guide is the "set up your sock puppet first" prerequisite those tools assume.

## Trust & verifiability
`trust: trusted` — a well-established, openly-maintained community guide with a public repository and changelog. It's opinionated reference material rather than a data source, so its authority comes from community review and its transparent editing history.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-hitchhiker-s-guide-to-online-anonymity |
