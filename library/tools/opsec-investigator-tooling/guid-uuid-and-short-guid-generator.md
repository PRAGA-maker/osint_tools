---
id: guid-uuid-and-short-guid-generator
name: GUID/UUID and Short GUID Generator
description: Use when you need to generate a GUID/UUID or convert between full and short (Base64) GUID forms while handling `device-id`/token artifacts — returns a generated or reformatted identifier.
url: https://richardkundl.github.io/shortguid/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Generating throwaway GUIDs/UUIDs and decoding short-GUID (22-char Base64) values back to standard form.
selectorsIn:
- device-id
selectorsOut:
- device-id
status: live
pricing: free
costNote: Free static web page; runs client-side, no account.
opsec: passive
opsecNote: Fully client-side — nothing you enter leaves the browser. Use it to mint burner/placeholder identifiers for sock-puppet accounts, or to normalize a short GUID you found in a URL/cookie/API response so it can be matched against a standard GUID elsewhere.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source demo (richardkundl on GitHub Pages) of standard GUID/UUID and short-GUID Base64 encoding; the transform is a well-defined, reversible standard.
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
- GUID generator
- UUID generator
- short GUID
tags:
- utility
- identifiers
- uuid
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# GUID/UUID and Short GUID Generator

> A browser utility that generates GUIDs/UUIDs and converts them to and from the compact 22-character "short GUID" Base64 form.

## When to use
Two investigator uses. First, generate a fresh GUID/UUID when you need a unique throwaway identifier — a placeholder `device-id`, a burner reference for a sock-puppet, or test data. Second, and more useful in analysis: when you find a short GUID (a 22-char Base64 string) embedded in a URL, cookie, or API response, convert it back to the standard 36-char GUID so you can match it against identifiers seen elsewhere and recognize that two differently-formatted values are the same underlying ID.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://richardkundl.github.io/shortguid/.
2. To generate: click generate to mint a new GUID/UUID and its short form.
3. To decode: paste a short GUID into the field to expand it to standard GUID form (and vice-versa).
4. Copy the result and compare it against `device-id`/token values found in your source material.

## Inputs → Outputs
- **In:** an existing GUID/short-GUID (`device-id`), or nothing (to generate)
- **Out:** a standard GUID/UUID and/or its short (Base64) equivalent
- **Empty/negative result looks like:** malformed input isn't converted — a string that isn't a valid GUID or 22-char short GUID won't decode, which itself tells you it's a different kind of token.

## Gotchas & OpSec
- Generated GUIDs are random placeholders, not tied to anything real — don't mistake a generated value for evidence.
- The short↔standard transform is deterministic and reversible; two encodings of the same GUID are provably the same identifier.
- Client-side only; safe to run offline.

## Overlaps ("do both")
- Pairs with metadata/EXIF and token-decoding tools — when you extract a GUID-shaped identifier from a document or request, use this to normalize it before correlating across sources.

## Trust & verifiability
`trust: community` — an open implementation of the standard GUID and Base64 short-GUID encodings; results are reproducible with any UUID library.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | guid-uuid-and-short-guid-generator |
