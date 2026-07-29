---
id: intezer-analyzer
name: Intezer Analyze
description: Use when you have a file, file hash, URL, or `ip-address` from a subject and want malware/threat analysis via code reuse — returns malware-family and threat-actor attribution.
url: https://analyze.intezer.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Classifying a suspicious file/hash by code-reuse to a known malware family or threat actor.
selectorsIn:
- document-id
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: Free Community Edition allows up to ~10 file analyses per day plus hash/URL/IP lookups; higher volume and enterprise features are paid.
opsec: active
opsecNote: Uploading a file or querying an indicator sends it to Intezer's cloud, where it may be retained and (for uploads) potentially shared in threat-intel context. Never upload a file that itself contains a subject's private data. Prefer submitting a hash over the raw file; use hash/IP lookups (which reveal nothing new) when possible.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Intezer is a reputable commercial malware-analysis vendor known for its code-reuse "genetic" analysis; results are vendor-produced but well-regarded in the industry.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- virustotal
aliases:
- Intezer Analyze
- Intezer Community
tags:
- malware-analysis
- threat-intel
- file-analysis
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Intezer Analyze

> A malware-analysis platform that classifies files by *code reuse* — matching binary "genes" to known malware families and threat actors — with a free community tier.

## When to use
This is **infrastructure/artifact analysis**, not people search. Reach for it when a subject's digital trail includes a suspicious file, attachment, or indicator (a `document-id`/hash, a `domain`, an `ip-address`) and you need to know whether it's malicious and *whose* it is — Intezer's genetic analysis attributes samples to malware families and actors better than signature scanning. In a missing-persons context that's a narrow but real case: e.g. a device/account compromised by identifiable malware.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register for the free Community Edition and sign in at https://analyze.intezer.com/.
2. Submit an indicator: paste a file **hash** (preferred), a URL, or an `ip-address`; or upload a file (counts against the ~10/day quota).
3. Read the report: malware-family classification, code-reuse matches, related samples, and network indicators (C2 `domain`/`ip-address`).
4. Pivot: extracted C2 domains/IPs feed your infrastructure tooling; family/actor attribution frames the threat.
5. For automation, use the Community API within its rate limits.

## Inputs → Outputs
- **In:** file / hash (`document-id`), URL/`domain`, `ip-address`
- **Out:** malware-family + threat-actor attribution, related `domain`/`ip-address` indicators
- **Empty/negative result looks like:** "no genetic matches / not classified" — the sample may be benign, novel, or too small; not-attributed is not the same as clean.

## Gotchas & OpSec
- **Uploads leave your control:** submitting a file sends it to Intezer's cloud with possible retention/sharing — never upload files containing a subject's private content; submit a hash instead.
- Free tier is quota-limited (~10 files/day) and requires an account (human-in-the-loop login).
- OpSec: **active** — you are transmitting the artifact/indicator to a third party.

## Overlaps ("do both")
- Pairs with `[[virustotal]]` — VirusTotal gives broad multi-engine detection and community context; Intezer adds code-reuse attribution. Run both: agreement raises confidence, and each surfaces indicators the other misses.

## Trust & verifiability
`trust: trusted` — an established, well-regarded vendor whose genetic-analysis approach is respected; results are theirs to stand behind, and reproducible via the report's evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | intezer-analyzer |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | document-id, domain, ip-address → domain, ip-address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
