---
id: find-a-postal-code-address
name: Find a Postal Code / Address
description: Use when you have a Canadian `address` and want its exact postal code (or to confirm the address is deliverable) — returns a normalized `address`/postal code.
url: https://www.canadapost.ca/info/mc/personal/postalcode/fpc.jsf
category: people-search
path:
- people-search
bestFor: Normalizing a Canadian street address to its official postal code before feeding it to other people-search tools.
selectorsIn:
- address
selectorsOut:
- address
status: live
pricing: free
costNote: Free Canada Post consumer tool; no account or payment needed.
opsec: passive
opsecNote: You are querying Canada Post's public postal-code database, not the target. Nothing about the subject is revealed to a third party beyond the address string you type. Safe to run from any browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Canada Post, the national postal authority; the postal-code data is authoritative.
missingPersonsRelevance: high
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- Canada Post Find a Postal Code
- FPC
tags:
- address
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# Find a Postal Code / Address

> Canada Post's official address-to-postal-code finder — an address-normalization/validation utility, not a person lookup.

## When to use
You have a partial or messy Canadian `address` for a subject (from a document, a listing, or another tool) and need its precise, official postal code, or need to confirm the civic/rural/PO-box address actually exists and is deliverable. Correct postal codes make downstream lookups (voter rolls, reverse-address people search, court/property records) far more reliable.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.canadapost.ca/info/mc/personal/postalcode/fpc.jsf (it redirects to the bilingual `canadapost-postescanada.ca` host — that is expected).
2. Choose the address type tab (street/civic, rural route, or post office box).
3. Enter the street number, street name, city, and province.
4. Read the output: the tool returns the matching postal code and the fully normalized address. If several units share the address it may return a code range or prompt for the unit number.
5. Pivot: feed the confirmed `address` + postal code into a Canadian reverse-address or voter/property tool.

## Inputs → Outputs
- **In:** `address` (Canadian street/rural/PO-box address)
- **Out:** normalized `address` + official postal code
- **Empty/negative result looks like:** "No results found" / "we could not match that address" — means the address as typed is not in Canada Post's database, not that the person is untraceable. This tool does **not** and cannot return names, phones, or occupants from a postal code — it is one-directional (address → code only).

## Gotchas & OpSec
- Do not expect reverse lookup: there is no "who lives at this postal code" function here; treat any tag suggesting it returns `name`/`phone`/`associate` as inaccurate.
- Canada-only. Useless for non-Canadian addresses.
- Passive and low-risk; the query never touches the subject.

## Overlaps ("do both")
- Feeds Canadian reverse-address and people-search tools — validate the address here first, then pivot, because a wrong postal code silently breaks those searches.

## Trust & verifiability
`trust: trusted` — first-party Canada Post service, so the postal-code mapping is authoritative and current.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | find-a-postal-code-address |
| category | people-search |
| selectorsIn → selectorsOut | address → address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
