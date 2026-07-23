---
id: rfc-fyi
name: RFC.fyi
description: Use when you have a protocol, keyword, or working-group name and want to find and read the relevant IETF RFC — returns RFC documents and their metadata, a reference tool not a people source.
url: https://rfc.fyi/
category: search-engines
path:
- search-engines
bestFor: Fast full-text search and filtered browsing of the IETF RFC index.
selectorsIn: []
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free and open (open-source front-end over the public RFC index); no account.
opsec: passive
opsecNote: You are searching public standards documents, not querying anything about a subject — fully passive with no target exposure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A community front-end over the authoritative IETF/RFC Editor index; the documents themselves are the canonical internet standards.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- RFC search
tags:
- search-engines
- reference
- protocols
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# RFC.fyi

> A fast, filterable search interface over the entire IETF RFC catalogue — for understanding the protocol behind an artifact, not for finding people.

## When to use
You have encountered a protocol, header, port behavior, or standards reference while investigating (an email header field, an unusual DNS/TLS behavior, a protocol name in a capture) and need to read the authoritative RFC to understand it. This is a technical reference aid that sharpens your interpretation of infrastructure/document evidence — it returns no information about any individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://rfc.fyi/.
2. Search a keyword (e.g. `IMAP search`, `congestion`, `DKIM`) or filter by collection, stream, level, or working group.
3. Sort by RFC number or by referencing RFCs to find the current/most-relevant document.
4. Open the RFC (`document-id`, e.g. RFC 5321) and read it on the IETF/RFC Editor site it links to.
5. Pivot: the RFC clarifies what a field/behavior means, feeding better analysis in [[wireshark]] or email-header tooling.

## Inputs → Outputs
- **In:** a keyword, protocol name, or working-group filter (no personal selectors).
- **Out:** matching RFC documents and their metadata (`document-id`, status, stream, WG).
- **Empty/negative result looks like:** a keyword search with no matching RFCs, or a transient "couldn't load the RFC index" error if the front-end can't reach the source — reload, or go to the RFC Editor directly.

## Gotchas & OpSec
- It's a convenience front-end; if it fails to load the index, the canonical source is rfc-editor.org / datatracker.ietf.org.
- RFCs have statuses (Proposed/Draft/Internet Standard, Obsoleted-by) — check that you're reading the current one.
- No investigative selectors involved; purely a knowledge lookup.

## Overlaps ("do both")
- Complements [[wireshark]] and email-header analysis: those show you the protocol behavior in the wild, RFC.fyi tells you what the standard says it should be.

## Trust & verifiability
`trust: trusted` — a thin community layer over the authoritative RFC index; the underlying documents are the canonical, citable standards.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rfc-fyi |
