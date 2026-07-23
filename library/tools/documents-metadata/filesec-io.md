---
id: filesec-io
name: Filesec.io
description: Use when you have a suspicious file's extension (`document-id`/attachment) and want to know how attackers abuse that file type and which OSes are affected — returns per-extension attack context and defenses.
url: https://filesec.io/
category: documents-metadata
path:
- documents-metadata
bestFor: Reference lookup of a file extension's known malicious uses and which platforms it can attack.
selectorsIn:
- document-id
selectorsOut: []
status: live
pricing: free
costNote: Free public knowledge base; community-contributed, no account needed.
opsec: passive
opsecNote: Fully passive — you read a static reference site; you never upload the file itself, so nothing about your sample or subject leaves your machine. It explains the file type; it does not analyze your specific file.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open community reference in the style of GTFOBins/LOLBAS; curated by security practitioners, so entries are informative but community-maintained.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Filesec.io
- filesec
tags:
- file-extensions
- malware
- attack-reference
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Filesec.io

> A curated reference of file extensions attackers abuse — what each type can do, which OSes it hits, and how to defend against it.

## When to use
During document/attachment analysis you encounter an unusual or risky file extension (in an email, an archive, a phishing sample) and want to understand why it matters: how that extension is weaponized (execution, macro abuse, phishing, archive smuggling) and which platforms (Windows/Mac/Linux) are affected. It's a knowledge base for triaging file-based threats — a companion to actually detonating or scanning the file elsewhere.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://filesec.io/.
2. Find the extension in question (browse or search the catalog).
3. Read the entry: how attackers use it, affected OSes, notable real-world usage, and mitigation/blocking advice.
4. Decide handling: whether the extension warrants blocking, and how to safely examine the actual sample.
5. Pivot: take the actual file to a sandbox/hash-lookup tool for sample-specific analysis.

## Inputs → Outputs
- **In:** a file extension (`document-id`/attachment type)
- **Out:** attack techniques for that extension, affected platforms, and defense recommendations
- **Empty/negative result looks like:** the extension isn't cataloged — it may be benign or simply not (yet) documented; that's not proof it's safe.

## Gotchas & OpSec
- It explains the *type*, not your *specific file* — always analyze the actual sample separately (hash lookup, sandbox).
- Community-maintained, so coverage grows over time; a missing entry isn't a clean bill.
- Never rely on extension alone; attackers rename and double-extension files.

## Overlaps ("do both")
- Pairs with hash-reputation/sandbox tools (VirusTotal, etc.) and LOLBAS/GTFOBins — Filesec explains the file type's risk while those analyze the concrete sample or the binaries it may invoke.

## Trust & verifiability
`trust: community` — an open, practitioner-curated reference; entries are informative and cite real usage, but treat it as guidance and confirm sample behavior with dynamic analysis.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | filesec-io |
