---
id: canadian-numbering-administrator
name: Canadian Numbering Administrator (CNA)
description: Use when you have a Canadian `phone` number and want the carrier behind it — returns the operating company (carrier) assigned that NPA-NXX central-office code.
url: http://cnac.ca/
category: dark-web
path:
- dark-web
bestFor: Identifying which Canadian carrier owns the CO code (NPA-NXX) of a phone number.
selectorsIn:
- phone
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free public regulatory lookup; no account required.
opsec: passive
opsecNote: You query a regulatory database of code assignments, not the subscriber; the number's owner is never contacted or notified.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The CNA operates under CRTC oversight (administered by COMsolve/CNAC); its code-assignment data is the authoritative Canadian source.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- CNA
- CNAC
- cnac.ca
- Canadian CO Code Lookup
tags:
- toddington
- curated-directory
- specialty-search
- phone-osint
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Canadian Numbering Administrator (CNA)

> The authoritative registry of Canadian phone-number block assignments: given a number, find which carrier was assigned its central-office code.

## When to use
You have a Canadian `phone` number and need to know the carrier/operating company behind it — the first step in phone OSINT before porting muddies the picture. CNA's CO Code lookup maps an NPA-NXX (area code + prefix) to the telecom that holds that block, and shows the code's status. Useful to confirm a number is Canadian, identify the original carrier, and understand the geography/type of the line.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://cnac.ca/ and find the "CO Code / Phone Number Lookup" tool.
2. Enter the number's NPA-NXX (first six digits, e.g. `416-555`) or the full number.
3. Read the result: the assigned operating company (carrier), rate centre, and code status.
4. Note the carrier and rate centre (a geographic anchor for landline/original assignment).
5. Pivot: the carrier feeds lawful-process/known-carrier context; the rate centre gives a rough `geolocation`; combine with a portability check since the number may have been ported.

## Inputs → Outputs
- **In:** a Canadian `phone` number / NPA-NXX
- **Out:** the assigned carrier `employer-org`, rate centre, and code status
- **Empty/negative result looks like:** an unassigned or non-Canadian code returns no owner — meaning the prefix isn't a live Canadian assignment, not that the tool failed.

## Gotchas & OpSec
- Shows the *code block* assignee, not the current carrier if the number was **ported** — treat as the original/underlying carrier and cross-check portability.
- Rate centre indicates the code's geography, which mobile numbers can outlive; use as a hint, not a live location.
- OpSec: passive; queries a regulatory registry, not the subscriber.

## Overlaps ("do both")
- Pairs with the US NANPA/telecom lookups and reverse-phone tools — CNA is the Canadian authority for who owns the block; reverse-phone services attempt the subscriber.

## Trust & verifiability
`trust: trusted` — an official CRTC-overseen numbering administrator; its assignment records are the authoritative Canadian source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | canadian-numbering-administrator |
| category | dark-web |
| selectorsIn → selectorsOut | phone → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
