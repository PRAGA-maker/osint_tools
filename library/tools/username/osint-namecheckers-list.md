---
id: osint-namecheckers-list
name: osint-namecheckers-list
description: Use when you have a `username` and need to choose the right enumeration tool — a soxoj-curated catalog of username-search/account-discovery tools that ultimately return `social-profile` links.
url: https://github.com/soxoj/osint-namecheckers-list
category: username
path:
- username
bestFor: Picking the best current username-enumeration tool (Maigret, Sherlock, WhatsMyName, etc.) for a given job.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free, open (MIT-licensed) GitHub catalog; no account. The listed tools are themselves mostly free/open-source.
opsec: passive
opsecNote: Reading the list is fully passive. The tools it points to make requests to hundreds of platforms when you run them — that part is active toward those sites, so run the actual enumerators from a sock-puppet browser/VPN.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by soxoj (author of Maigret), a respected OSINT developer; ~690 stars and actively curated, with explicit notes on which listed tools are deprecated.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- digital-footprint-check
- 1c-database-converter
- awesome-osint-mcp-servers
- counter-osint-guide-for-russians
- fravia-soxoj
- gitcolombo
- maigret
- maigret-via-socid-extractor-soxoj-ecosystem
- mailto-analyzer
- marple
- socid-extractor
- username-generation-guide
aliases:
- soxoj namecheckers
- username tools list
tags:
- username
- namechecker
- catalog
- username-enumeration
source: gh-topic-osint-resources
lastVerified: '2026-07-15'
enrichment: full
---

# osint-namecheckers-list

> soxoj's curated catalog of username-search, account-discovery, and handle-availability tools — the map you consult to pick the *right* enumerator before you run one.

## When to use
You have a `username`/nickname and want to enumerate where it exists, but the tooling landscape churns (projects die, coverage shifts). Rather than default to whatever you used last, check this list for the currently-best option — Maigret (3,000+ sites), Sherlock, WhatsMyName, Usersearch, Enola, Snoop and more — with notes on what's maintained vs. deprecated. It's a reference/catalog, not a lookup itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/soxoj/osint-namecheckers-list.
2. Skim the sections: open-source CLI tools, online web tools, branding/availability checkers, and toolkits.
3. Note the deprecation flags — pick a tool that's still maintained and covers the platforms you care about.
4. Go run that tool on your `username` (e.g. install Maigret, or use a web checker like WhatsMyName).
5. Pivot: enumerated `social-profile` hits feed per-platform OSINT; cross-linked handles expand the search.

## Inputs → Outputs
- **In:** `username` (conceptually — you bring the handle to the tool you choose here)
- **Out:** a shortlist of enumeration tools that themselves return `social-profile` links
- **Empty/negative result looks like:** not applicable to the list itself; the real "empty" is when the enumerator you chose finds no accounts — try a second tool from the list, since coverage differs.

## Gotchas & OpSec
- It's a directory, not a scanner — you still run a separate tool to actually enumerate.
- Some listed tools are explicitly marked no-longer-maintained; heed those notes or you'll waste time on dead projects.
- Same-handle ≠ same-person applies to whatever enumerator you end up running — verify each hit.

## Overlaps ("do both")
- Complements `[[digital-footprint-check]]` (a ready-to-use WhatsMyName web checker) — use this list to choose a CLI tool for depth/scripting, and the web checker for a fast no-install pass.

## Trust & verifiability
`trust: trusted` — maintained by a well-known OSINT author and actively curated; the recommendations are reliable, though you should still confirm a listed tool's current status before depending on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-namecheckers-list |
| category | username |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
