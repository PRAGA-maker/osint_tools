---
id: osint-san
name: OSINT-SAN
description: Use when you have an `ip-address`, `phone`, `username` or `name` and want a multi-module recon sweep — returns `geolocation`, `social-profile` and infrastructure leads across bundled tools.
url: https://github.com/Bafomet666/OSINT-SAN
category: people-search
path:
- people-search
bestFor: Running many OSINT modules (IP/Shodan, phone, social, geolocation) from one Python framework.
selectorsIn:
- ip-address
- phone
- username
- name
selectorsOut:
- geolocation
- social-profile
- ip-address
- phone
status: degraded
pricing: free
costNote: Free (a paid PRO variant exists). The free framework needs several third-party API keys (Shodan, ZoomEye, numverify, VirusTotal, whatcms). The README notes some GitHub-tool modules are no longer maintained.
opsec: active
opsecNote: MIXED and partly AGGRESSIVE. Passive modules (Shodan/ZoomEye/numverify lookups) query third parties about a selector. But OSINT-SAN also ships IP-logger/"grabber" modules that generate a link you send to the target so their browser leaks IP/geo — that is intrusive, interacts directly with the subject, and may be unlawful without consent. Use ONLY the passive lookup modules for casework; never deploy the grabber/deanon-by-link modules against a person without explicit legal authorisation. Run from research infrastructure with burner API keys.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Community deanonymization framework (600+ stars); useful as a launcher for standard APIs, but it bundles intrusive grabber techniques and some modules are unmaintained — treat outputs as leads, not proof.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- osintsan
- OSINT SAN
tags:
- deanonymization
- geolocation
- ip
- phone
source: gh-topic-osint-framework
lastVerified: '2026-07-21'
enrichment: full
---

# OSINT-SAN

> A Python OSINT launcher that bundles many recon modules — Shodan/ZoomEye IP scans, phone validation, social and geolocation lookups — behind one menu. Powerful, but it also ships intrusive IP-grabber tooling you must avoid on real subjects.

## When to use
You have an `ip-address`, `phone`, `username`, or `name` and want to run a batch of standard OSINT lookups without invoking each tool separately. Reach for it as a **passive-module launcher** — IP/infrastructure enrichment (Shodan, ZoomEye), phone validation (numverify), CMS/malware/torrent history — early in a case to fan out cheaply.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `Bafomet666/OSINT-SAN`, then `pip3 install -r requirements.txt` (Python 3).
2. Add your API keys (Shodan, ZoomEye, numverify, VirusTotal, whatcms) in the config — most modules do nothing without them.
3. Launch the free build: `python3 osintsan.py`, then pick a **passive** module from the menu and feed it the selector.
4. Read the module output (IP → `geolocation`/host, phone → carrier/validity, username → `social-profile` hits).
5. **Skip** the IP-logger/grabber modules unless you have explicit legal authorisation; they send the target a tracking link.
6. Pivot: IP/geo → mapping and infra tools; social hits → the specific platform for confirmation.

## Inputs → Outputs
- **In:** `ip-address`, `phone`, `username`, or `name`
- **Out:** `geolocation`, host/`ip-address` data, carrier info, `social-profile` candidates
- **Empty/negative result looks like:** a module returning nothing usually means a missing/expired API key or an unmaintained module, not that the selector is clean — check keys and cross-verify elsewhere.

## Gotchas & OpSec
- **Human-in-the-loop: api-key.** Most value is gated behind third-party keys you must supply.
- **The grabber modules are active and intrusive** — link-based IP capture against a person can be illegal; do not use them in casework without authorisation.
- Some GitHub-tool modules are explicitly unmaintained; treat every result as a lead to confirm with a primary source.

## Overlaps ("do both")
- It wraps tools you can also run directly (Shodan, numverify) — use OSINT-SAN to fan out quickly, then confirm any hit in the underlying service's own interface for an authoritative record.

## Trust & verifiability
`trust: community` — an unofficial framework aggregating third-party APIs; reliability equals whatever the underlying service returns, and the bundled deanon-by-link features mean you should audit exactly which module you run before running it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-san |
| category | people-search |
| selectorsIn → selectorsOut | ip-address, phone, username, name → geolocation, social-profile, ip-address, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key) |
