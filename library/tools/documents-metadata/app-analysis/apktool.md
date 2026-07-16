---
id: apktool
name: APKtool
description: Use when you have an Android `.apk` file and want to decompile it to recover hardcoded endpoints, credentials, and developer identifiers — returns domain, email, metadata-exif.
url: https://apktool.org/
category: documents-metadata
path:
- documents-metadata
- app-analysis
bestFor: Decoding an APK to nearly-original resources, AndroidManifest, and smali so you can read the strings/URLs/keys a mobile app ships with.
selectorsIn:
- metadata-exif
selectorsOut:
- domain
- email
status: live
pricing: free
costNote: Free and open source (Apache 2.0). No account, no paid tier; you only need a Java runtime installed.
opsec: passive
opsecNote: Fully offline reverse engineering — you operate on an APK you already hold, so nothing touches the app publisher or a network. The only leak risk is your own: analyze in a disposable VM, and never execute the app or its extracted binaries on your investigation host.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Long-standing, widely-used open-source project (iBotPeaches/Apktool) with public source, releases, and an active issue tracker; output is deterministic disassembly, not a third-party data claim.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- mobsf
- frida
aliases:
- apktool
- Android APK decompiler
tags:
- app-analysis
- reverse-engineering
- documents-metadata
source: arf-seed
lastVerified: '2026-07-16'
enrichment: full
---

# APKtool

> Offline Android APK reverse-engineering tool: unpacks an app back to readable resources, manifest, and smali so you can mine the identifiers baked into it.

## When to use
You have a subject's Android app (`.apk`) — a self-hosted "tracker" APK, a niche dating/community app, a scam app, or any package tied to a person or group — and you want the identifiers hidden inside it: hardcoded backend `domain`s and API endpoints, analytics/notification keys, support/developer `email`s, embedded phone numbers, and the signing certificate. It converts an opaque binary into a browsable source tree you can grep.

## How to use it (`bestInteractionPattern`: cli)
1. Install a Java runtime, then Apktool (Homebrew `brew install apktool`, a distro package, or the wrapper script + JAR from https://apktool.org/).
2. Decode the package: `apktool d target.apk -o target_src`. This rebuilds `AndroidManifest.xml`, `res/`, assets, and `smali/` (disassembled bytecode) in near-original form.
3. Mine the tree for selectors:
   - `grep -rEo 'https?://[^"]+' target_src` → backend `domain`s / endpoints.
   - `grep -rEi '[a-z0-9._%+-]+@[a-z0-9.-]+' target_src` → developer/support `email`s.
   - Read `AndroidManifest.xml` for package name, permissions, and declared services; check `res/values/strings.xml` for app name and hardcoded text.
   - `keytool -printcert -jarfile target.apk` → signing certificate (org/name/locality hints).
4. Pivot: feed recovered domains to WHOIS/DNS tooling, emails to email-OSINT, and the package name to Play/store listing lookups.

## Inputs → Outputs
- **In:** an `.apk` file (metadata-exif — a mobile app package you already possess)
- **Out:** `domain` (backend/analytics endpoints), `email` (developer/support contacts), plus package name, permissions, and signing-cert strings
- **Empty/negative result looks like:** the decode succeeds but strings are obfuscated/encrypted or the app is fully server-driven — you get a valid source tree with no useful plaintext identifiers. A hard failure (unsupported/corrupt APK) errors out at decode time.

## Gotchas & OpSec
- Human-in-the-loop: none — it's a one-shot command, no captcha or login.
- OpSec: **passive/offline**. It never contacts the publisher; risk is only from running untrusted code. Decompile inside a throwaway VM and never launch the app itself.
- Heavily obfuscated (ProGuard/R8) or packed apps yield little readable smali; pair with a dynamic tool to see runtime behavior.
- Apktool disassembles resources/smali; it does **not** produce Java. For readable Java, add jadx.

## Overlaps ("do both")
- Pairs with `[[mobsf]]` — MobSF wraps static + dynamic analysis and a report UI, while Apktool gives you the raw, greppable tree for precise identifier hunting.
- Pairs with `[[frida]]` — Apktool reads what the app *ships* statically; Frida hooks what it *does* at runtime (live URLs, decrypted strings).

## Trust & verifiability
`trust: trusted` — mature open-source project with public source and releases; output is a faithful disassembly you can independently re-run, so there is no third-party data-quality risk.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | apktool |
| category | documents-metadata |
| selectorsIn → selectorsOut | metadata-exif → domain, email |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
