---
id: awesome-forensics
name: awesome-forensics
description: Use when you need to pick a digital-forensics tool for a task — returns a curated, categorised list of free/open-source forensic analysis tools and resources.
url: https://github.com/Cugu/awesome-forensics
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Finding the right free/open-source tool for disk, memory, mobile, or network forensics.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, open GitHub list; the tools it points to are mostly free/open source.
opsec: passive
opsecNote: A static reference list on GitHub — reading it touches no target. OpSec applies to the forensic tools you then run, most of which operate on local evidence/images rather than remote targets.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Actively maintained "awesome" list (5.1k+ stars, 200+ commits) by Cugu; entries flag archived/unmaintained tools. Inclusion is curation, not vetting — confirm each tool's fit and status.
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
- osint-tools-yogsec
aliases:
- Cugu awesome-forensics
tags:
- directory
- forensics
- reference
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# awesome-forensics

> A curated directory of free, mostly open-source digital-forensics tools — a "which forensics tool do I use?" index spanning disk, memory, mobile, network, and timeline analysis.

## When to use
You have local digital evidence — a disk image, a memory dump, a phone extraction, a packet capture — and need the right analysis tool. This list groups vetted, free/open forensic tools by task, saving you from evaluating dozens of options. Relevant when an investigation moves from remote OSINT into examining seized or shared device data.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/Cugu/awesome-forensics and read the README.
2. Jump to the section matching your evidence type: Frameworks (Autopsy, Velociraptor), Memory (Volatility, Rekall), Network (Wireshark, NetworkMiner), Windows Artifacts, Mobile, Timeline (plaso, Timesketch), disk imaging/carving.
3. Note the status markers — archived (📦) and stale (💤) — and prefer actively maintained tools.
4. Follow the link, install the tool, and run it against your evidence.
5. Pivot: forensic output (browser history, contacts, media, metadata) feeds OSINT selectors — usernames, emails, EXIF geolocation — back into this library's lookup tools.

## Inputs → Outputs
- **In:** none (a discovery directory, not selector-driven)
- **Out:** categorised lists of forensic tools with maintenance-status markers and links
- **Empty/negative result looks like:** your niche isn't covered or the listed tool is archived — check a second forensics resource or the tool's own repo for a maintained fork.

## Gotchas & OpSec
- It is a reference, not a tool — value is in fast, curated tool selection.
- Heed the archived/unmaintained flags; forensic tooling ages and format support lapses.
- Forensic work has chain-of-custody and legal implications; follow proper evidence-handling procedure, which this list does not cover.

## Overlaps ("do both")
- Pairs with `[[osint-tools-yogsec]]` — that indexes remote-OSINT tools; awesome-forensics indexes local device/evidence tools. Use both to cover the full remote-to-device pipeline.

## Trust & verifiability
`trust: community` — a well-maintained, high-quality community list, but inclusion is not an endorsement. Verify each tool's current status and suitability for your evidence type.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | awesome-forensics |
