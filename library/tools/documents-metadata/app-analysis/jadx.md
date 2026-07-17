---
id: jadx
name: JADX
description: Use when you have an Android `document-id` app package (APK/DEX) and want to read its logic and extract embedded strings — returns `domain`, `email` and hard-coded identifiers.
url: https://github.com/skylot/jadx
category: documents-metadata
path:
- documents-metadata
- app-analysis
bestFor: Decompiling an APK to readable Java to recover hard-coded URLs, endpoints, API keys and developer contact strings.
selectorsIn:
- document-id
selectorsOut:
- domain
- email
status: live
pricing: free
costNote: Free and open source under Apache 2.0; no account, no network calls.
opsec: passive
opsecNote: Fully offline once you have the APK file — decompilation happens on your own machine and touches nothing belonging to the target. Obtaining the APK (from a store or device) is the only step with a footprint; do that with a clean account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Widely used, actively maintained open-source decompiler by Skylot; ~40k GitHub stars, mirrored in Homebrew/Arch/Flathub.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- jadx-gui
- Dex to Java decompiler
tags:
- app-analysis
- reverse-engineering
- apk
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# JADX

> An offline Android decompiler that turns an `.apk`/`.dex` into readable Java — used in OSINT to pull the URLs, endpoints, e-mail addresses and keys a developer baked into their app.

## When to use
You have an app package (an APK, its `document-id`/package name, or a DEX) tied to a person or small organisation and want to know what backend it talks to and who built it. Mobile apps routinely embed hard-coded server `domain`s, support `email` addresses, third-party API keys, Firebase URLs and analytics IDs. JADX exposes all of these in the decompiled source and resources, giving you infrastructure and contact pivots off a single app file.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `brew install jadx` / `pacman -S jadx`, or download a release binary (Java 11+ required).
2. Obtain the target `.apk` (from the device, or an APK-mirror site — use a clean account).
3. Decompile to a folder: `jadx -d out_dir target.apk`, or open it interactively with `jadx-gui target.apk` for search and jump-to-declaration.
4. Grep the output for pivots: `grep -rniE "https?://|@[a-z0-9.]+\.[a-z]{2,}|api[_-]?key" out_dir/` — this surfaces backend `domain`s, contact `email`s and embedded credentials. Also read `resources/AndroidManifest.xml` for the package name and permissions.
5. Pivot: feed recovered `domain`s to DNS/WHOIS/subdomain tools and `email`s to email-lookup tools.

## Inputs → Outputs
- **In:** `document-id` (an APK/DEX file or package name you can obtain the APK for)
- **Out:** `domain`, `email`, plus hard-coded keys, endpoints and the developer package namespace
- **Empty/negative result looks like:** decompiles cleanly but contains only generic library code and no unique strings — common for apps built on a boilerplate SDK, or where strings are obfuscated/encrypted (ProGuard/R8).

## Gotchas & OpSec
- OpSec: **passive** — analysis is local and never touches the target's systems. Your only footprint is downloading the APK.
- Obfuscated or packed apps yield garbled class/method names; you can still recover string literals but logic is harder to follow.
- Getting the APK for a paid or region-locked app can be the real bottleneck; the tool itself is trivial.

## Overlaps ("do both")
- Pairs with metadata/APK-info tools that read the manifest and signing certificate — those give you the developer's signing identity, while JADX gives you the embedded strings and logic.

## Trust & verifiability
`trust: trusted` — mature open-source tool; because it operates on the app's own bytecode offline, every string it recovers is verifiably present in the package you fed it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jadx |
| category | documents-metadata |
| selectorsIn → selectorsOut | document-id → domain, email |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
