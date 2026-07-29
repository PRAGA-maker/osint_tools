---
id: x86-and-x64-intel-assembler
name: x86 and x64 Intel Assembler
description: Use when you have x86/x64 assembly or raw machine-code bytes and want to convert between them in-browser — returns assembled opcodes or disassembled Intel-syntax instructions.
url: https://defuse.ca/online-x86-assembler.htm
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Quick bidirectional assemble/disassemble of short x86/x64 snippets without local tooling.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free web tool (Defuse Security); no account, no limits noted.
opsec: passive
opsecNote: You paste short assembly/hex into the page, which is processed server-side (it runs GCC/objdump). Fine for benign snippets; for sensitive or malicious shellcode you don't want to share, use a local assembler instead.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Part of defuse.ca (Defuse Security / Taylor Hornby), a long-standing, well-regarded set of free security utilities.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- big-number-calculator
- defuse
- html-sanitizer-tool
- text-and-file-hash-calculator
aliases:
- defuse online assembler
tags:
- assembler
- reverse-engineering
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# x86 and x64 Intel Assembler

> Defuse.ca's in-browser assembler/disassembler: turn Intel-syntax assembly into opcodes and hex bytes back into instructions, no local toolchain needed.

## When to use
A niche RE utility, not a people tool. Useful when analysing a suspect binary/shellcode and you need to quickly assemble a snippet or decode a short hex byte-string into readable instructions — e.g. to understand an exploit fragment or confirm what some opcodes do. Its OSINT value is helping you interpret compiled artefacts so you can extract pivots from them.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://defuse.ca/online-x86-assembler.htm.
2. To assemble: paste Intel-syntax assembly, pick x86/x64, and read the resulting opcodes/hex.
3. To disassemble: paste a hex byte-string and read the decoded instructions.
4. Use it to sanity-check or annotate fragments while reverse-engineering elsewhere.

## Inputs → Outputs
- **In:** x86/x64 assembly, or a hex machine-code string (not an OSINT selector)
- **Out:** assembled opcodes/bytes, or disassembled Intel-syntax instructions
- **Empty/negative result looks like:** an assembler error or nonsense disassembly — invalid syntax, or the bytes aren't valid code for the chosen mode.

## Gotchas & OpSec
- Server-side processing: don't paste sensitive/restricted shellcode you can't share — use a local assembler (nasm/objdump) for those.
- Best for short snippets, not whole binaries; use `[[oda-the-online-disassembler]]` or Ghidra for full files.
- Pick the correct bitness (x86 vs x64) or the encoding will be wrong.

## Overlaps ("do both")
- Complements `[[oda-the-online-disassembler]]` — ODA handles whole files, this is the fast snippet-level assemble/disassemble scratchpad.

## Trust & verifiability
`trust: community` — from a reputable, long-lived security site; output is deterministic (GCC/objdump under the hood) and easily reproduced locally.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | x86-and-x64-intel-assembler |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
