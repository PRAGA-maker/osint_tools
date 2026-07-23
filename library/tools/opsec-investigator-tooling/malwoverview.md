---
id: malwoverview
name: MALWOVERVIEW
description: Use when you have a file hash, `domain`, URL, or `ip-address` and want multi-source threat-intel triage — returns aggregated VT/Hybrid-Analysis/URLHaus/etc verdicts from one CLI.
url: https://github.com/alexandreborges/malwoverview
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: First-response CLI triage of files/URLs/IPs across many malware and threat-intel services at once.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free and open-source (Python); most integrated services need your own free API keys to return data.
opsec: passive
opsecNote: "Reputation lookups are passive toward the target, but Malwoverview submits your indicators (hashes, URLs, domains, IPs) to third-party services — VirusTotal, Hybrid Analysis, URLHaus, Triage, and more — which log and may share what you submit. Submitting a URL/hash can also tip off an operator monitoring VT. Use throwaway API keys and never submit sensitive/private indicators you don't want disclosed."
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Actively maintained open-source tool (Alexandre Borges); it aggregates other services, so verdict quality is inherited from those upstream sources, not Malwoverview itself.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
aliases:
- malwoverview
- alexandreborges/malwoverview
tags:
- ioc-enrichment
- threat-intel
- malware-triage
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# MALWOVERVIEW

> A first-response CLI that queries a file hash, URL, domain, or IP across VirusTotal, Hybrid Analysis, URLHaus, PolySwarm, MalShare, AlienVault, Malpedia, ThreatFox, Triage, and InQuest — one command, many verdicts.

## When to use
You have a suspicious file hash, `domain`, URL, or `ip-address` and want a fast, consolidated read on its reputation across the major threat-intel and sandbox services without visiting each site. Ideal for triaging an indicator that surfaced in an investigation. Malware/attribution-focused, so low direct missing-persons relevance, though a malicious `domain`/`ip-address` tied to a subject is worth scoring here.

## How to use it (`bestInteractionPattern`: cli)
1. Install from https://github.com/alexandreborges/malwoverview (`pip install malwoverview`) and configure `.malwapi.conf` with your (throwaway) API keys.
2. Query an indicator, e.g. `malwoverview -v 1 -V <hash>` (VirusTotal), or the flags for URLHaus/ThreatFox/Triage/etc.
3. Read the aggregated output: detection ratios, sandbox verdicts, related IOCs, and cross-references.
4. Note which engines actually ran (unkeyed engines are skipped — "clean" may mean "not queried").
5. Pivot related `domain`s/`ip-address`es into passive-DNS/geolocation tooling.

## Inputs → Outputs
- **In:** file hash, URL, `domain`, or `ip-address`
- **Out:** aggregated reputation/sandbox verdicts and related `domain`s/`ip-address`es (IOCs)
- **Empty/negative result looks like:** all engines clean/not-found — either genuinely unknown-bad, too fresh to be flagged, or the relevant engine lacked a key; absence isn't proof of benign.

## Gotchas & OpSec
- Requires your own API keys per service; without them those engines silently return nothing.
- Submitting an indicator to VT/Hybrid Analysis is observable — an operator watching for their sample being uploaded may be tipped off. Prefer *searching* by hash over *uploading* files.
- Verdicts are only as current/accurate as the upstream sources; validate anything critical at the originating service.

## Overlaps ("do both")
- Same job as [[cyberbro]] (web/self-host aggregator) — Malwoverview is the CLI/scriptable equivalent; use either to triage a batch, then drill into a flagged indicator with a specialist tool.

## Trust & verifiability
`trust: community` — a maintained, transparent open-source aggregator; because it summarizes other services, confirm any decision-critical verdict against the source engine rather than the summary line.
