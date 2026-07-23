---
id: koodous
name: Koodous
description: Use when you have an Android APK (or its hash/`document-id`) and want community malware analysis — returns detection verdicts, YARA matches, and analyst annotations.
url: https://koodous.com
category: documents-metadata
path:
- documents-metadata
- hosted-automated-analysis
bestFor: Collaborative Android APK malware analysis with community YARA rules and threat intel.
selectorsIn:
- document-id
status: live
pricing: freemium
costNote: Free account for search and community analysis; higher-tier/API and bulk access are paid. Registration required for most features.
opsec: passive
opsecNote: Searching existing analyses by hash is passive. UPLOADING an APK shares it with the platform and community — never upload a sample that is sensitive to your investigation or that could tip off its author; assume uploads become searchable.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Established collaborative Android-malware platform used by analysts; verdicts blend automated detection with community-authored YARA rules, so quality varies by contributor.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Koodous platform
tags:
- documents-metadata
- android
- malware
- apk
- yara
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# Koodous

> A collaborative platform for Android malware analysts — look up an APK by hash to see detections, YARA matches, and what the community has flagged.

## When to use
You have an Android APK involved in a case (a suspicious app pushed to a victim, a stalkerware/spyware sample, a malicious link's payload) and want to know if it's known-bad. Search by the APK's hash/`document-id` to pull automated detection verdicts, community YARA-rule matches, and analyst notes — or upload it for analysis if it's not already covered.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://koodous.com and create a free account.
2. Search by the APK's hash (`document-id`) or package name; if unknown, upload the APK to have it analysed (mind the OpSec note).
3. Read the result: detection ratings, matched YARA rules, permissions/behaviour, and community comments.
4. Pivot: extracted network indicators (C2 `domain`s/`ip-address`es), certificates, and package identifiers feed infrastructure and reputation tools.

## Inputs → Outputs
- **In:** APK hash/`document-id` (or an uploaded APK)
- **Out:** detection verdicts, YARA matches, permissions/behaviour, and extracted indicators
- **Empty/negative result looks like:** no record for the hash — the sample is new/uncommon; you'd need to upload it (weighing the OpSec cost) to get analysis.

## Gotchas & OpSec
- Human-in-the-loop: an account is needed for most functions.
- Uploading an APK shares it — assume it becomes searchable, which can tip off a targeted attacker or expose case-sensitive tooling. Search by hash first.
- Community YARA rules vary in quality; corroborate a verdict before acting.

## Overlaps ("do both")
- Complements `[[malware-traffic-analysis-net]]` (network side) and multi-engine sandboxes — Koodous is Android-APK-specific; cross-check a hash against a broader sandbox for a second opinion.

## Trust & verifiability
`trust: community` — a respected but community-driven platform; automated + crowd-sourced verdicts are a strong signal, not proof, so confirm important findings independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | koodous |
| category | documents-metadata |
| selectorsIn → selectorsOut | document-id →  |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
