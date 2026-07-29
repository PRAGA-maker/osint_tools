---
id: osint-techniques
name: OSINT Techniques
description: Use when you need a technique reference or a vetted tool for a selector — returns methodology write-ups and a curated OSINT tools directory.
url: https://www.osinttechniques.com/blog
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Learning OSINT methods and finding vetted tools via a well-known practitioner's resource hub.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Blog, tools directory, and resources are free to read; the reference content is open. (Note this is osinttechniques.com — distinct from Michael Bazzell's inteltechniques.com.)
opsec: passive
opsecNote: A public reference site — reading it touches no target. Apply the OpSec each linked tool requires when you go on to use it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running, widely cited OSINT resource hub with a curated tools directory and forensic-OSINT guidance. Methodology-focused; verify any linked third-party tool's current status yourself.
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
- nixintel
- osint-tools-yogsec
- bellingcat-online-investigation-toolkit
aliases:
- osinttechniques.com
tags:
- osint-blogs
- methodology
- reference
- directory
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# OSINT Techniques

> A veteran OSINT resource hub — practitioner blog posts, a curated tools directory, forensic-OSINT guidance, and a newsletter.

## When to use
Reach for it when you need *method or tool discovery* rather than a data lookup: how to approach a selector (username, image, location), which vetted tool to pick, and worked investigative examples (e.g. mapping incidents from news and law-enforcement releases). A good first stop to orient an investigation and find the right downstream tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.osinttechniques.com/ and open the **Tools** directory or the **Blog**.
2. For tool discovery: browse the categorised directory and follow links to the specific tools.
3. For method: read the relevant blog write-up; posts are practical and reproducible.
4. Use the site's advanced-search and resource pages to broaden into books, videos, and forensic-OSINT material.
5. Pivot: apply the chosen tool to your live case — many are covered by dedicated skills in this library.

## Inputs → Outputs
- **In:** none (a knowledge/directory resource, not selector-driven)
- **Out:** methodology, curated tool links, worked examples
- **Empty/negative result looks like:** no article/tool covers your niche — cross-reference another practitioner hub.

## Gotchas & OpSec
- Reference content ages; check dates and confirm a linked tool is still live before relying on it.
- Returns guidance and links, not investigation results — pair with the actual lookup tools it names.

## Overlaps ("do both")
- Pairs with `[[nixintel]]`, `[[osint-tools-yogsec]]`, and `[[bellingcat-online-investigation-toolkit]]` — cross-referencing two or three hubs covers method + breadth better than any one alone.

## Trust & verifiability
`trust: trusted` — established, well-regarded OSINT resource. Guidance is reproducible; verify each third-party tool's status and safety before use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-techniques |
