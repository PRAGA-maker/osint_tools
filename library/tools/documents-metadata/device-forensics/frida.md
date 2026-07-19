---
id: frida
name: Frida
description: Use when you have a device you control (`device-id`) running a target app and want to inspect/intercept its runtime — returns intercepted secrets, tokens and data (password, metadata-exif).
url: https://frida.re/
category: documents-metadata
path:
- documents-metadata
- device-forensics
bestFor: Dynamic instrumentation of a running app on a device you control — hooking functions to observe API calls, decrypt data, and pull credentials/tokens.
selectorsIn:
- device-id
selectorsOut:
- password
- metadata-exif
status: live
pricing: free
costNote: Free and open source (wxWindows/BSD-style licensing); no paid tier.
opsec: active
opsecNote: This runs ON a device you control and modifies a target app's runtime — it is only lawful/appropriate on devices and accounts you own or are authorized to examine (e.g. a recovered phone in an authorized investigation). Apps can detect Frida (anti-instrumentation), and instrumenting an account can trip its security signals. Never point it at infrastructure or accounts you don't control.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: cli
trust: community
trustNote: A mature, widely used open-source project (maintained by Ole André Vadla Ravnås / NowSecure community); auditable source and huge user base.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- frida.re
- frida-tools
- frida-trace
tags:
- device-forensics
- dynamic-instrumentation
- reverse-engineering
- mobile
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# Frida

> A dynamic-instrumentation toolkit that injects scripts into a running process to hook functions, watch API calls and pull decrypted data — the standard tool for examining what an app on a device you control is actually doing.

## When to use
You have physical/authorized control of a device (`device-id`) — a recovered phone, an emulator, a suspect's own handset in an authorized examination — and need to see inside an app whose data isn't accessible statically: what it sends, what it stores, the tokens/credentials it holds, or content it shows only at runtime. Frida hooks live methods so you can observe or modify behavior without the source code. In a missing-persons/forensics context, it can surface an app's cached messages, login tokens, or account identifiers from a device you're authorized to inspect.

## How to use it (`bestInteractionPattern`: cli)
1. Install tooling on your workstation: `pip install frida-tools` (Python bindings also on PyPI, Node bindings on npm).
2. Put the target on a controlled device: a rooted Android / jailbroken iOS device or an emulator, with `frida-server` running on it (or use a repackaged app for non-rooted cases).
3. Enumerate processes: `frida-ps -U`. Trace an app's calls: `frida-trace -U -i "*http*" com.target.app`.
4. Attach a script (`frida -U -l hook.js com.target.app`) to hook specific methods — read arguments, return values, decrypted buffers, stored tokens.
5. Capture the observed data and document your method (chain-of-custody / manual review of what each hook returned).
6. Pivot: recovered account IDs/tokens → the corresponding platform's OSINT; extracted contacts/messages → associate mapping.

## Inputs → Outputs
- **In:** a controlled `device-id` running the target app + the function/method you want to hook
- **Out:** intercepted API parameters, return values, decrypted data, stored `password`/tokens, and file/`metadata-exif` an app exposes at runtime
- **Empty/negative result looks like:** the app fails to launch under instrumentation, detaches, or crashes — a sign of Frida/anti-tamper detection (RASP), or you hooked the wrong method (no calls observed).

## Gotchas & OpSec
- Detection: many apps ship anti-Frida/anti-root checks; you may need stealth loading, `frida-server` renaming, or bypass scripts.
- Requires a rooted/jailbroken device or emulator and, usually, root on the device running `frida-server`.
- OpSec/legal: **active and intrusive** — only run against devices/apps/accounts you own or are legally authorized to examine; instrumenting live accounts can trigger security alerts.
- Human-in-the-loop: interpreting hooked output requires manual analysis and script writing.

## Overlaps ("do both")
- Complements static forensics (device imaging, APK/IPA decompilation) — static analysis tells you where to hook, Frida shows the runtime values those code paths actually produce.

## Trust & verifiability
`trust: community` — a battle-tested, widely audited open-source toolkit; results are as reliable as your hooks, and everything it reports comes directly from the app's own runtime, which you can re-observe.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | frida |
| category | documents-metadata |
| selectorsIn → selectorsOut | device-id → password, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (manual-review) |
