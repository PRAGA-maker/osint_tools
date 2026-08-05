---
id: disasm-pro
name: disasm.pro
description: Use when you have a chunk of machine-code bytes (shellcode, a hex blob from a malware sample) and want to disassemble it live in the browser, or assemble instructions back to bytes — an analysis utility, not a data source.
url: https://disasm.pro/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Live in-browser assembling/disassembling of machine code (x86/x64/ARM) for reverse engineering.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free web tool; no account required.
opsec: active
opsecNote: Bytes you paste are processed by the site (server/client side), so treat submissions as leaving your control — do not paste sensitive or case-identifying payloads. For confidential samples, use a local disassembler (objdump/Ghidra/Cutter) instead.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A convenient third-party online (dis)assembler; fine for quick public snippets, but for authoritative analysis verify against a local, trusted toolchain.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- disasm pro
- online disassembler
tags:
- reverse-engineering
- malware-analysis
source: osint4all
lastVerified: '2026-08-05'
enrichment: full
---

# disasm.pro

> A live, in-browser assembler/disassembler — paste bytes to read them as instructions, or type instructions to get bytes, updating as you edit.

## When to use
Reverse-engineering support, not a person lookup. You've pulled a blob of machine-code bytes out of a malware sample, exploit, or firmware and want to see what instructions it is — or you're crafting/verifying a short sequence and want the encoded bytes. disasm.pro does both interactively for common architectures, which is faster than spinning up a full toolchain for a quick snippet.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://disasm.pro/.
2. Choose the architecture/mode (e.g. x86/x64/ARM).
3. Paste your hex bytes to disassemble, or type assembly to assemble — output updates live.
4. Read the decoded instructions to understand the code's behaviour.
5. Pivot: understanding what the shellcode does (e.g. a network call) points you to C2 `domain`s/`ip-address`es to chase with infrastructure OSINT.

## Inputs → Outputs
- **In:** machine-code bytes (to disassemble) or assembly (to assemble) — no person selector
- **Out:** disassembled instructions or assembled byte encoding
- **Empty/negative result looks like:** garbage/invalid instructions — usually the wrong architecture/mode or a misaligned/incomplete byte sequence; adjust the mode or offset.

## Gotchas & OpSec
- **Active/third-party:** don't paste sensitive or confidential bytes; use a local disassembler for anything real or evidentiary.
- Correct architecture/mode selection is essential — the same bytes disassemble differently across ISAs.
- It handles snippets, not full binaries; for whole-file RE use Ghidra/Cutter/IDA.

## Overlaps ("do both")
- For anything beyond a quick snippet — or anything sensitive — prefer local tooling (objdump, Ghidra, Cutter); use disasm.pro only for fast, disposable public checks.

## Trust & verifiability
`trust: unverified` — a handy third-party utility; cross-check important disassembly against a trusted local toolchain before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | disasm-pro |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
