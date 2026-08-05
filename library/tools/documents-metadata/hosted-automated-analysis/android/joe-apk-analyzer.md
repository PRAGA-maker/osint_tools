---
id: joe-apk-analyzer
name: Joe APK Analyzer (Joe Sandbox)
description: Use when you have an Android `.apk` (e.g. stalkerware or a suspicious app off a subject's device) and want its behavior and IOCs — returns a malware/behavior report with network, permissions, and device-id artifacts.
url: https://www.apk-analyzer.net/
category: documents-metadata
path:
- documents-metadata
- hosted-automated-analysis
- android
bestFor: Dynamic + static analysis of an Android APK to reveal its behavior, network callbacks, and IOCs.
input: Android APK file
output: Behavior report, network/C2 indicators, permissions, extracted artifacts (`ip-address`, `domain`, `device-id`)
selectorsIn: []
selectorsOut:
- ip-address
- domain
- device-id
status: live
pricing: freemium
opsec: active
opsecNote: You upload the APK to Joe Sandbox's cloud, so the file leaves your control and the analysis is visible to the vendor; free/Community reports may be published publicly. Never upload an APK that itself contains a victim's private data, and assume any C2 the sample contacts may log the sandbox's activity. Use the paid tier if you need private reports.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: trusted
trustNote: Joe Sandbox (Joe Security) is a well-established commercial malware-analysis platform; apk-analyzer.net now redirects to its unified Cloud service, which has a free Community/Basic tier.
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
- Joe Sandbox
- Joe Sandbox Cloud Basic
- apk-analyzer.net
tags:
- android
- malware-analysis
- sandbox
source: arf-seed
lastVerified: '2026-08-05'
enrichment: full
---

# Joe APK Analyzer (Joe Sandbox)

> A hosted Android malware sandbox (the old apk-analyzer.net now folds into Joe Sandbox Cloud): submit an APK, get back a deep behavior report and IOCs — the tool of choice when a suspicious app matters to a case.

## When to use
You have recovered an Android `.apk` that is relevant to an investigation — suspected stalkerware/spyware from a victim's phone, a lure app sent to a subject, or an unknown app pulled from a device — and you need to know what it does: what servers it calls, what permissions and data it grabs, what identifiers it leaks. Joe Sandbox runs it in an instrumented Android VM and reports the behavior. It analyzes an artifact you hold; it does not search for people, but its extracted IOCs (C2 `domain`/`ip-address`, embedded `device-id`) can pivot an investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.apk-analyzer.net/ (redirects to Joe Sandbox Cloud) and sign in to the free Community/Basic tier.
2. Upload the `.apk` (or submit via API); choose the Android analysis profile.
3. Wait for the automated run, then read the report: permissions, network traffic/PCAP, dropped files, C2 endpoints, and a maliciousness verdict.
4. Download the HTML/PDF report and PCAP for your case file.
5. Pivot: a C2 `domain`/`ip-address` feeds infrastructure OSINT; an embedded account/`device-id` can link the app to an operator.

## Inputs → Outputs
- **In:** an Android `.apk` file
- **Out:** behavior report, network/C2 indicators (`domain`, `ip-address`), permissions, `device-id`/artifact leaks
- **Empty/negative result looks like:** a benign verdict with no notable network or permission behavior — the app may be clean, obfuscated, or refuse to run in the sandbox (anti-analysis); a clean report is not proof of safety.

## Gotchas & OpSec
- Human-in-the-loop: free-tier registration and submission rate limits apply; heavy use needs the paid tier.
- OpSec: **active** — the sample is uploaded to a third-party cloud and free reports can be public. Do not upload anything containing a victim's private data; sensitive samples belong on a private/paid tier or a local sandbox.
- Anti-sandbox malware may behave differently in the VM; corroborate with static analysis.

## Overlaps ("do both")
- Pairs with other hosted analyzers (e.g. a second sandbox or a static APK decompiler) — run the same sample through two engines to catch evasion and cross-check the IOCs before acting on them.

## Trust & verifiability
`trust: trusted` — Joe Security is a reputable commercial vendor and its reports are detailed and reproducible; still verify critical IOCs (does the C2 resolve? is the domain live?) independently before pivoting on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | joe-apk-analyzer |
| category | documents-metadata |
| selectorsIn → selectorsOut | — → ip-address, domain, device-id |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (rate-limit) |
