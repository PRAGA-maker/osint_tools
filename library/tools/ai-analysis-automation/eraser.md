---
id: eraser
name: Eraser
description: Use when you need to securely wipe files or free space on a Windows machine so investigative material can't be recovered — an open-source secure-deletion utility.
url: https://eraser.heidi.ie
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Securely erasing sensitive files/free space on Windows so they can't be forensically recovered.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (Eraser by Heidi Computers, GPL); Windows only.
opsec: passive
opsecNote: A purely local defensive/OpSec tool — it runs on your own machine and touches no network or subject. Its job is to protect *your* operational hygiene; deletion is irreversible, so double-check targets before wiping.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: A long-established, well-known open-source Windows secure-erase tool; widely used and audited by the community.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- encsf-mp
- nixory
aliases:
- Eraser by Heidi
- eraser.heidi.ie
tags:
- privacy-and-encryption-tools
- secure-deletion
- opsec
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# Eraser

> A free, open-source Windows utility that overwrites files and free space so deleted investigative material can't be forensically recovered — an OpSec hygiene tool, not a lookup.

## When to use
This is defensive tradecraft, not data collection. After working with sensitive downloads — case files, screenshots, scraped data, puppet-account artifacts — on a Windows machine, use Eraser to overwrite them (and the free space they left behind) so a normal delete doesn't leave recoverable traces. Reach for it to keep your own operational footprint clean between engagements.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download and install Eraser from https://eraser.heidi.ie (Windows).
2. Right-click a file/folder in Explorer → **Eraser → Erase**, or schedule tasks in the Eraser UI.
3. Choose an overwrite method (e.g. multi-pass or a single-pass standard); confirm the target.
4. Optionally run an "erase unused disk space" task to scrub previously-deleted remnants.
5. Verify completion. There is no pivot — this is a terminal OpSec step, not an intelligence source.

## Inputs → Outputs
- **In:** local files / free space to wipe (no OSINT selector)
- **Out:** securely overwritten, unrecoverable data (no selector output)
- **Empty/negative result looks like:** N/A — success is a completed erase task; failures are usually locked/in-use files (close the app holding them and retry).

## Gotchas & OpSec
- Human-in-the-loop: none, but **deletion is irreversible** — confirm targets carefully.
- OpSec: **passive** and local — no network, no subject contact; it exists to protect your own hygiene.
- Windows-only; on SSDs, overwrite-based erasure is less deterministic than on spinning disks (wear-leveling), so combine with full-disk encryption for strong guarantees.

## Overlaps ("do both")
- Complements full-disk encryption and other privacy tools (`[[encsf-mp]]`, `[[nixory]]`) — encryption protects data at rest; Eraser removes the residue of files you no longer want to exist.

## Trust & verifiability
`trust: trusted` — a mature, community-audited open-source tool with a long track record; it does exactly one well-understood thing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | eraser |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
