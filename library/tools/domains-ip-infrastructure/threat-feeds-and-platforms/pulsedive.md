---
id: pulsedive
name: Pulsedive
description: Use when you have an `ip-address`, `domain` or URL (IOC) and want enrichment, risk scoring and linked indicators — returns threat context and related `domain`s/`ip-address`es.
url: https://pulsedive.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- threat-feeds-and-platforms
bestFor: Enriching an indicator (IP/domain/URL) with risk score, threat context and linked IOCs from aggregated feeds.
selectorsIn:
- ip-address
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: Free account gives web search and a limited API quota; higher volume, active scanning and bulk features are paid.
opsec: passive
opsecNote: Passive lookups query Pulsedive's aggregated database, not the target — the subject sees nothing. Note Pulsedive can also actively scan an indicator on request; that would touch the target, so keep to passive enrichment unless you intend a live probe.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: A well-established threat-intelligence enrichment platform aggregating public feeds; risk scores are derived and best treated as a signal to corroborate.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- onyphe
- securitytrails
- leakix
aliases:
- Pulsedive
- pulsedive.com
tags:
- threat-intel
- ioc-enrichment
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# Pulsedive

> A threat-intelligence enrichment platform — drop in an IP, domain or URL and get a risk score, aggregated feed context, and the other indicators it's linked to.

## When to use
You have an indicator from an investigation — an `ip-address`, `domain`, or URL from a header, log, or sandbox report — and want fast context: is it flagged across threat feeds, what's its risk score, what related infrastructure (co-resolving domains, associated IPs) is known? Pulsedive aggregates many public feeds so you don't have to check each one.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a free account and open https://pulsedive.com/.
2. Search the indicator (IP/domain/URL); read its risk score and the feeds/threats it appears in.
3. Review linked indicators and properties (DNS, WHOIS, ports) to pivot to related infrastructure.
4. Keep to passive lookups; only trigger an active scan if you intend to probe the target live.
5. Pivot: related `domain`/`ip-address` feed deeper infrastructure OSINT via `[[onyphe]]`, `[[securitytrails]]`, `[[leakix]]`.

## Inputs → Outputs
- **In:** an `ip-address`, `domain`, or URL (IOC)
- **Out:** risk score, threat-feed context, and linked indicators (`domain`, `ip-address`)
- **Empty/negative result looks like:** a clean/unknown indicator returns little context and a low/none risk score — "not in feeds" isn't proof of safety, just absence from aggregated intel.

## Gotchas & OpSec
- Human-in-the-loop: a free account is required; the free API quota is limited.
- Risk scores are derived from feed reputation — treat as a signal, corroborate before acting on a verdict.
- Distinguish passive lookup (safe) from Pulsedive's active scan (touches the target) — choose deliberately.

## Overlaps ("do both")
- Pairs with VirusTotal-style multi-engine checks and scan engines like `[[onyphe]]`/`[[leakix]]` — Pulsedive aggregates feed reputation and links, those add first-party scan observations for the same indicator.

## Trust & verifiability
`trust: trusted` — an established enrichment platform; the linked technical properties are verifiable, while the risk score is a derived signal to corroborate against primary sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pulsedive |
