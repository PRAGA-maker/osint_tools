---
id: mobsf
name: MobSF
description: Use when you have a mobile app (`.apk`/`.ipa`) and want to extract its secrets and identity leads — returns hardcoded URLs, keys, emails, trackers, permissions, and dev artifacts.
url: https://github.com/MobSF/Mobile-Security-Framework-MobSF
category: documents-metadata
path:
- documents-metadata
- app-analysis
bestFor: Static analysis of an APK/IPA to pull out hardcoded endpoints, API keys, emails, third-party trackers, and developer/signing artifacts.
selectorsIn:
- document-id
selectorsOut:
- domain
- email
- device-id
status: live
pricing: free
costNote: Free and open-source (self-hosted); run locally via Python or Docker. No cloud account required.
opsec: passive
opsecNote: Static analysis runs entirely on your own machine against a file you hold — no traffic goes to the app's operator. (Dynamic analysis, which actually runs the app, DOES generate network traffic — keep that on an isolated sandbox/VM behind a VPN.) The app binary itself is safe to dissect statically.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: docker
trust: community
trustNote: Widely used, actively maintained open-source mobile-security framework (MobSF org); results are auditable and reproducible since you run it yourself.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- Mobile Security Framework
- Mobile-Security-Framework-MobSF
tags:
- app-analysis
- reverse-engineering
- mobile
- arf-seed
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# MobSF

> Mobile Security Framework — a self-hosted tool that statically (and optionally dynamically) analyses Android/iOS apps, surfacing the hardcoded endpoints, credentials, trackers, and developer artifacts baked into a binary.

## When to use
Your investigation involves a mobile app — one a subject built, distributed, or used — and you want to know what's inside it. Static analysis of an `.apk`/`.ipa` extracts hardcoded server `domain`s and API endpoints, embedded `email`s, API keys/tokens, third-party SDKs/trackers, requested permissions, and signing-certificate details. These are strong pivots: a backend domain reveals infrastructure to map, an embedded email or cert name can identify the developer, and tracker SDKs reveal who receives the app's data. Reach for it when an app is the artifact and you need to attribute or map it.

## How to use it (`bestInteractionPattern`: docker)
1. Run it locally — easiest via Docker: `docker run -it -p 8000:8000 opensecurity/mobile-security-framework-mobsf:latest` (or install the Python package).
2. Open the web UI at `http://localhost:8000` and upload the `.apk`/`.ipa`.
3. Read the **static analysis** report:
   - Hardcoded **URLs/domains**, **emails**, and secrets found in the code/resources.
   - Permissions, exported components, third-party trackers/SDKs.
   - Signing certificate (developer identity) and app metadata.
4. Manually review flagged strings — separate real secrets/endpoints from library noise.
5. (Optional) Use dynamic analysis on an emulator/VM to watch live network calls — but sandbox it (see OpSec).
6. Pivot: a backend `domain` → WHOIS/infrastructure mapping; an embedded `email`/cert → developer identity; tracker `device-id`s/SDK keys → attribution.

## Inputs → Outputs
- **In:** a mobile app binary — `.apk` / `.ipa` / source (`document-id`)
- **Out:** hardcoded `domain`s/URLs, `email`s, API keys, `device-id`/tracker identifiers, permissions, signing cert
- **Empty/negative result looks like:** a clean report with only standard-library strings — the app hardcodes nothing useful (well-built apps externalise secrets); it doesn't mean the app has no backend, just none embedded in the binary.

## Gotchas & OpSec
- Human-in-the-loop: reports are noisy — most "findings" are library boilerplate; manually confirm which strings are real endpoints/secrets.
- **Static is passive; dynamic is not** — running the app makes real network calls; do that only in an isolated sandbox/VM behind a VPN.
- Self-hosting means the binary and results stay on your machine — good for OpSec and chain-of-custody.

## Overlaps ("do both")
- Complements WHOIS/infrastructure tools (feed it the extracted domains) and general reverse-engineering utilities — MobSF gives the fast structured extraction; deeper manual RE goes further on obfuscated apps.

## Trust & verifiability
`trust: community` — a mature, actively maintained open-source framework you run yourself, so every finding is reproducible and auditable; just apply manual judgement to filter false positives.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mobsf |
| category | documents-metadata |
| selectorsIn → selectorsOut | document-id → domain, email, device-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | docker |
| opsec | passive |
| human-in-loop | yes (manual-review) |
