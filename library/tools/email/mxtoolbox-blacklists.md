---
id: mxtoolbox-blacklists
name: 'MXToolbox: Blacklists'
description: Use when you have a mail domain or IP and want to check it against the major email blacklists (RBLs) in one query — returns per-list listed/not-listed status.
url: https://mxtoolbox.com/blacklists.aspx
category: email
path:
- email
bestFor: One-shot email blacklist (RBL) reputation check for a domain or IP.
selectorsIn:
- domain
- ip-address
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free blacklist lookup; monitoring/alerts are paid.
opsec: passive
opsecNote: Passive — queries public blacklist (RBL) servers about the domain/IP; the target is not contacted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: MxToolbox is a reputable, widely used email/DNS diagnostics service; this is its dedicated blacklist-check page.
missingPersonsRelevance: low
coverage: []
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- mxtoolbox
- multirbl
aliases: []
tags:
- email
source: metaosint
lastVerified: ''
enrichment: full
---

# MXToolbox: Blacklists

> The dedicated blacklist-check page of MxToolbox — tells you whether a mail domain or IP is on the major RBLs.

## When to use
A narrow infrastructure check: you have a `domain` or `ip-address` (e.g. a suspicious sender that contacted a subject, or a host behind a profile) and want its spam/abuse reputation. Heavy listing suggests bulk-mail, disposable, or compromised infrastructure. It does not identify a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to mxtoolbox.com/blacklists.aspx.
2. Enter the `domain` or `ip-address`.
3. Read the per-RBL results (listed / not listed).
4. Pivot: pair with the full `[[mxtoolbox]]` lookup for MX/SPF/DMARC and header tracing, or `[[multirbl]]` for a wider blacklist set.

## Inputs → Outputs
- **In:** `domain`, `ip-address`
- **Out:** blacklist-reputation report (`metadata-exif`)
- **Empty/negative result looks like:** "not listed on any" — normal for legitimate hosts; says nothing about a person.

## Gotchas & OpSec
- Low direct value for finding a missing person; characterizes infrastructure only.
- Listings can be stale or shared-IP collateral — interpret carefully.
- For origin tracing of an actual email, use the header analyzer (`[[mxtoolbox-com-2]]`), not this page.

## Trust & verifiability
`trust: trusted` — reputable MxToolbox service. MP relevance set `low` because it reports mail-infrastructure reputation, not identity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mxtoolbox-blacklists |
| category | email |
| selectorsIn → selectorsOut | domain, ip-address → metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
