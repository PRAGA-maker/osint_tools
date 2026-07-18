---
id: apkleaks
name: APKLeaks
description: Use when you have an Android APK and want to extract its secrets — returns discovered URLs/API endpoints, hardcoded keys/tokens, and other sensitive strings.
url: https://github.com/dwisiswant0/apkleaks
category: documents-metadata
path:
- documents-metadata
- app-analysis
bestFor: Scanning an APK for URIs, API endpoints, and hardcoded credentials/secrets during app analysis.
selectorsIn:
- device-id
selectorsOut:
- domain
- password
status: live
pricing: free
costNote: Free, open-source (Apache 2.0); install via pip/Go, or run in Docker.
opsec: passive
opsecNote: The scan runs locally against an APK file you already hold — it makes no requests to the app's backend or to any subject, so it's passive. If you later probe the endpoints it finds, that becomes active recon; keep those steps separate and behind proper OpSec.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A widely-used open-source tool by dwisiswant0; results are literal strings extracted from the APK — genuine, but require human judgement to tell live secrets from placeholders.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- apkleaks
- dwisiswant0/apkleaks
tags:
- android
- apk
- app-analysis
- secrets-scanning
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
relatedTools:
- go-dork
---

# APKLeaks

> A CLI scanner that decompiles an Android APK and greps it for URIs, API endpoints, and hardcoded secrets — the quick "what's baked into this app" pass in mobile-app analysis.

## When to use
You have an Android `.apk` (a subject's app, a suspicious app, or one you're auditing) and want to know what infrastructure and secrets it embeds: backend `domain`s and API endpoints, hardcoded API keys/tokens/`password`s, cloud bucket URLs, and other sensitive strings. It maps an app to the servers and services behind it — a starting point for attributing or investigating the app's operator.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install apkleaks` (or the Go build / Docker image).
2. Run against the APK: `apkleaks -f target.apk` (add `-o output.txt` to save, `-p patterns.json` for custom regex).
3. It decompiles the APK and applies its pattern set; read the report: discovered URLs/endpoints, keys, tokens, and other matches.
4. Triage: distinguish live secrets/endpoints from example/placeholder values before acting on them.
5. Pivot: extracted `domain`s/endpoints feed WHOIS/host attribution; keys/tokens indicate the app's cloud providers — but do NOT use found credentials, only note their exposure.

## Inputs → Outputs
- **In:** an Android APK file (of a `device-id`/app under analysis)
- **Out:** `domain`s/API endpoints, hardcoded keys/tokens/`password`s, sensitive strings
- **Empty/negative result looks like:** few or no matches — a well-hardened/obfuscated app, or one that loads config remotely; absence of secrets isn't proof the app is clean.

## Gotchas & OpSec
- Matches are **raw string hits** — expect false positives (placeholders, library defaults); verify before treating anything as a live secret.
- Finding a credential ≠ permission to use it; document exposure, don't exploit it, unless you're authorised.
- Probing the discovered endpoints is a separate, **active** step — keep it isolated and OpSec-aware.

## Overlaps ("do both")
- Pairs with static analyzers (jadx/MobSF) and dynamic tools: APKLeaks is the fast secrets/endpoints sweep; jadx/MobSF give full decompilation and manifest/permission analysis it doesn't.

## Trust & verifiability
`trust: community` — a popular, actively-used open-source scanner. Its output is deterministic (strings that are actually in the APK), so findings are verifiable by inspecting the decompiled code, but interpreting them requires judgement.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | apkleaks |
