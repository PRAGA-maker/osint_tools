---
id: extendclass
name: ExtendsClass
description: Use when you have raw data or a token from an investigation (JSON/XML/CSV, a JWT, a base64 blob, a regex to test) and want to parse, decode or format it in-browser — a free developer toolbox.
url: https://extendsclass.com/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Decoding/parsing/formatting investigation data (JSON, JWT, base64, regex, CSV) in one place.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: The online toolbox is free with no login for the core tools; an optional account and some hosted/mock-API features exist but aren't required.
opsec: passive
opsecNote: These are client-side/server-assisted utilities; some (e.g. mock APIs, SQL playgrounds) send your input to ExtendsClass servers. Never paste live credentials, session tokens you need kept secret, or sensitive PII — decode only sanitized fragments, and prefer a local tool for anything confidential.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known free developer-tools site; reliable for format conversion and decoding, but a third party that may process pasted data server-side.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- python-code-checker
aliases:
- extendsclass.com
- extendclass
tags:
- Tools collections/toolkits
- data-parsing
- decoding
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# ExtendsClass

> A free browser toolbox for developers — JSON/XML/CSV parsers and converters, a JWT decoder, base64/URL/HTML encoders, regex and XPath testers, and code/SQL playgrounds — handy for wrangling raw data you pull during an investigation.

## When to use
You've extracted structured data or an encoded value during OSINT work — a JSON API response, a base64 blob from a URL, a JWT from a captured request, a messy CSV export, a regex you want to test against sample text — and need to parse, decode, validate or reformat it fast. ExtendsClass is a utility layer for analysis, not a data source: it makes evidence readable so you can pull selectors out of it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://extendsclass.com/ and pick the relevant tool from the toolbox (JSON validator, JWT decoder, base64 decoder, regex tester, CSV↔JSON, etc.).
2. Paste the (sanitized) input into the tool.
3. Run it — get formatted/validated output, decoded contents, or match results.
4. Read the result for anything pivotable: a JWT payload may expose a `username`, `email` or issuer; a JSON blob may hold IDs, timestamps or handles.
5. Pivot: feed extracted selectors (emails, usernames, IDs) into the appropriate people/username/email tools.

## Inputs → Outputs
- **In:** raw data/tokens you supply (no OSINT selector fed to the site as a query)
- **Out:** parsed/decoded/reformatted data — which may *contain* selectors like `email`, `username`, IDs
- **Empty/negative result looks like:** a validation error or empty decode — usually malformed/mistyped input, not a failed lookup. It only processes what you paste.

## Gotchas & OpSec
- Human-in-the-loop: none, but you interpret the output.
- OpSec: **passive** toward your subject, but some tools process your paste on ExtendsClass servers — never submit live secrets or unredacted PII; use a local/offline decoder for confidential material.
- It's a utility toolbox, not an intelligence source; it doesn't find data, it formats data you already have.

## Overlaps ("do both")
- Complements `[[python-code-checker]]` and local CLI utilities — ExtendsClass is the quick web option; a local tool is the safer choice for sensitive data.

## Trust & verifiability
`trust: community` — a reputable free dev-tools site; its parsers/decoders are deterministic and reliable, but treat it as a third party that may see whatever you paste.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | extendclass |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
