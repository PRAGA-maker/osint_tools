---
id: trace-labs-awesome-osint
name: Trace Labs awesome-osint
description: Use when you are starting or stuck in a missing-persons investigation and want a vetted, category-organized catalog of OSINT tools to work through — returns a curated directory of tools by selector type.
url: https://github.com/tracelabs/awesome-osint
category: search-engines
path:
- search-engines
bestFor: Authoritative starting catalog of missing-persons-relevant OSINT tools, curated and endorsed by Trace Labs and organized by investigative category.
selectorsIn:
- name
- username
- email
- phone
- image
selectorsOut:
- social-profile
- geolocation
- metadata-exif
status: live
pricing: free
costNote: Free open GitHub repository (curated list); many linked tools are themselves free, some are commercial.
opsec: passive
opsecNote: Reading the list is a passive GitHub page view that reveals nothing about your target. OpSec risk lives entirely in the individual tools you then launch from it — assess each one's active/passive profile before use.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Trace Labs curated list, explicitly scoped to missing-persons OSINT and maintained by the organization that runs the Search Party CTF; entries are vetted rather than scraped.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- osint-framework
- start-me-osint
- gumshoe
- h8mail-trace-labs-fork
- the-osint-field-manual-tofm
- trace-labs-osint-vm-tlosint-vm
aliases:
- awesome-osint tracelabs
- Trace Labs OSINT list
tags:
- curated-list
- tracelabs
- missing-persons
- meta-resource
source: tracelabs-repos
lastVerified: '2026-07-15'
enrichment: full
---

# Trace Labs awesome-osint

> The missing-persons OSINT reading list, curated by Trace Labs: a category-by-category index of the tools that actually help locate people.

## When to use
You are working a missing-persons case (or a Search Party CTF) and want a vetted map of where to look next, filtered to tools that matter for finding people rather than general OSINT. Reach for it at the start to plan your approach, or mid-case when a line of inquiry stalls and you need to know what other tool classes exist for the selector you're holding (an email, a username, a face, a location).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/tracelabs/awesome-osint and read the README's table of contents.
2. Jump to the category matching the selector you currently have: Email, Multi (multi-source), Username, Social, Phone, People, Images/Video, Documentation & Capture, Geolocation, Domain/IP, Wireless, or Translation.
3. Pick tools from that section and open them; because the list is scoped to missing-persons work, you can trust the entries are relevant rather than generic.
4. Work the selector through several listed tools (coverage rarely overlaps fully), then move to the category for whatever new selector you surfaced.
5. Pivot: this is the meta-index — every entry is itself a tool to run; use it to decide *which* tool, then execute there.

## Inputs → Outputs
- **In:** whatever selector you're holding (`name`, `username`, `email`, `phone`, `image`, geo hints) — you use it to choose the right category.
- **Out:** a shortlist of vetted tools that consume that selector and can yield `social-profile`s, `geolocation`, EXIF/`metadata-exif`, and more.
- **Empty/negative result looks like:** not applicable — it is a static list, so it never "fails to find." The risk is that a linked tool has since gone offline; verify each tool is still live before relying on it.

## Gotchas & OpSec
- It is a directory, not an engine: it points you at tools but runs nothing itself, so no lead comes from the list alone.
- Curated lists drift — some linked tools die or change scope over time; treat a broken/dead link as "check for a successor," not a dead end.
- OpSec is deferred to the tools you launch: some are passive (archives, viewers), others active (account probes) — evaluate each individually.

## Overlaps ("do both")
- Pairs with `[[osint-framework]]` and `[[start-me-osint]]` — those are broader, general-purpose OSINT directories; use Trace Labs' list for its missing-persons focus and the others when you need breadth beyond people-finding.

## Trust & verifiability
`trust: trusted` — maintained by Trace Labs, the nonprofit behind the missing-persons Search Party CTF, with entries chosen for relevance to locating people. It curates rather than aggregates data, so the trust question is only whether each linked tool is still current.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | trace-labs-awesome-osint |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, email → social-profile, geolocation, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
