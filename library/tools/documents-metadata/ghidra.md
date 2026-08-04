---
id: ghidra
name: Ghidra
description: Use when you have a suspicious executable or `document-id`/binary artifact and want to disassemble and decompile it to recover behaviour, strings, and embedded indicators — returns human-readable pseudo-code and static IOCs.
url: https://github.com/NationalSecurityAgency/ghidra
category: documents-metadata
path:
- documents-metadata
bestFor: Static reverse engineering of unknown executables and malware to extract embedded strings, URLs, and behavioural logic offline.
selectorsIn:
- document-id
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free and open-source (NSA Research Directorate). No licence fee, no account. Only cost is a local JDK 21 install.
opsec: passive
opsecNote: Fully local desktop analysis — nothing is uploaded, so the sample's author gets no callback (unlike online sandboxes). Analyse malware only in an isolated VM; opening a binary in Ghidra is safe (it doesn't execute the code) but handling the sample file itself is not.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Built and maintained by the NSA and released open-source; source is public and widely audited by the security community.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- NSA Ghidra
- ghidra SRE
tags:
- reverse-engineering
- malware-analysis
- binary
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# Ghidra

> The NSA's open-source reverse-engineering suite: load an unknown binary and get back disassembly plus C-like decompiled pseudo-code, entirely offline.

## When to use
You have a compiled artifact — an executable, driver, firmware image, or a malware sample attached to a case — and need to understand what it *does* without running it. In an OSINT/investigative context this is how you pull static indicators out of a binary: hard-coded `domain`s, C2 `ip-address`es, embedded strings, usernames, or wallet addresses that then become new pivots. It's not a people-search tool; it's the step that turns "here's a mystery file" into "here are the network indicators inside it."

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install a 64-bit JDK 21 (Adoptium), download the release zip from the GitHub releases page, unzip, and launch `./ghidraRun` (`ghidraRun.bat` on Windows).
2. Create a project and import the target file (ELF, PE, Mach-O, or a raw binary — Ghidra supports a wide range of processor architectures).
3. Accept the auto-analysis prompt; let it disassemble and decompile.
4. Work the results: the **Symbol Tree** and **Defined Strings** window surface embedded URLs, domains, IPs, and messages; the **Decompiler** pane shows C-like pseudo-code for any function.
5. For batch/scripted work use the headless analyzer or the Java/Python scripting API (`api: true`).
6. Pivot: extracted `domain`/`ip-address` indicators feed infrastructure lookups; strings and IDs feed the rest of your investigation.

## Inputs → Outputs
- **In:** `document-id` (a binary/executable artifact)
- **Out:** `domain`, `ip-address` (plus strings, function logic, control-flow graphs)
- **Empty/negative result looks like:** a heavily packed/obfuscated sample decompiles to noise with no readable strings — indicating packing, not absence of indicators; unpack first, then re-analyse.

## Gotchas & OpSec
- Human-in-the-loop: reverse engineering is inherently `manual-review`; Ghidra automates disassembly but you interpret the code.
- OpSec: analysis is passive and offline (no upload, no execution), so it won't tip off a sample's operator the way an online sandbox can — but always keep the sample in an isolated VM.
- Steep learning curve; JDK version mismatches are the most common install failure.

## Overlaps ("do both")
- Complements dynamic sandboxes and online scanners: Ghidra gives you the static, offline view (safe, no network callback) while a sandbox shows runtime behaviour — do both when a sample matters, and cross-check the indicators.

## Trust & verifiability
`trust: trusted` — released and maintained by the NSA as open source; the codebase is public and heavily scrutinised, and output is deterministic against the binary you feed it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ghidra |
| category | documents-metadata |
| selectorsIn → selectorsOut | document-id → domain, ip-address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | yes (manual-review) |
