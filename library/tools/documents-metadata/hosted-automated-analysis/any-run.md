---
id: any-run
name: ANY.RUN
description: Use when you have a suspicious file or URL and want to detonate it in an interactive cloud sandbox — returns behavior, process graph, and IOCs (`domain`, `ip-address`).
url: https://app.any.run/
category: documents-metadata
path:
- documents-metadata
- hosted-automated-analysis
bestFor: Interactive detonation of malware/suspicious files and URLs in a cloud VM you can click around in, extracting IOCs and TTPs.
selectorsIn: []
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: Free tier allows a few PUBLIC analyses per day (visible to everyone); private analyses, Windows-version choice, and API scale require paid plans.
opsec: active
opsecNote: This detonates real malware and connects out to its C2/infrastructure from ANY.RUN's sandbox — which can tip off the operator that their sample is being analysed. Crucially, FREE-tier submissions are PUBLIC: never upload anything sensitive, victim-identifying, or confidential, as it becomes searchable by anyone.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: A widely-used, reputable interactive malware sandbox; the behavioral evidence (network calls, process tree) is observable and reproducible.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Any.Run
- app.any.run
tags:
- malware-sandbox
- dynamic-analysis
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# ANY.RUN

> An interactive online malware sandbox — detonate a file or URL in a real VM you can click around in live, and watch its behaviour, network calls and dropped files unfold into IOCs.

## When to use
You have a suspicious attachment, executable, or link and need to know what it *does* — what it drops, which domains/IPs it contacts (`domain`, `ip-address`), and which ATT&CK techniques it uses — without running it on your own machine. ANY.RUN's interactivity lets you dismiss dialogs, enter fake credentials, and follow multi-stage payloads that automated-only sandboxes miss.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register an account and open https://app.any.run/.
2. Submit a file or URL; choose OS/options (free tier is limited and **public**).
3. Interact with the live VM as needed (click through installers/prompts) to trigger behaviour.
4. Read the results: process graph, network connections, dropped files, extracted config, MITRE ATT&CK mapping, and the IOC list.
5. Pivot: harvested `domain`/`ip-address` IOCs feed infrastructure OSINT (`[[onyphe]]`, `[[securitytrails]]`) and threat-intel correlation (`[[malpedia]]`).

## Inputs → Outputs
- **In:** a suspicious file, document, APK, or URL
- **Out:** behavioral report — process tree, network IOCs (`domain`, `ip-address`), dropped files, ATT&CK TTPs
- **Empty/negative result looks like:** benign or sandbox-evasive samples may show little activity — malware that detects the VM can lie dormant; low activity isn't proof of safety.

## Gotchas & OpSec
- **Free = public:** free-tier analyses are visible and searchable by everyone — never submit sensitive, confidential, or victim-identifying material; use private mode (paid) for those.
- **Active detonation:** the sample reaches out to live infrastructure, potentially alerting the operator; and the analysis is attributable to your account.
- Evasive malware may not fully execute in a sandbox — corroborate with static analysis.

## Overlaps ("do both")
- Pairs with VirusTotal/Hybrid Analysis and `[[malpedia]]` — static/multi-engine verdicts plus family attribution complement ANY.RUN's live behavioral view; run both for a fuller picture.

## Trust & verifiability
`trust: trusted` — a reputable, widely-used sandbox; its behavioral evidence (network/process activity) is observable and reproducible, and IOCs can be independently confirmed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | any-run |
