---
id: international-numbering-plans-database
name: International Numbering Plans Database
description: Use when you have a `phone` (or SIM/IMSI) number and want to identify its country, network operator, and number-range validity — returns the carrier/operator and geographic assignment.
url: http://numberingplans.com
category: phone
path:
- phone
bestFor: Identifying the country, operator, and validity of a phone/SIM number from its numbering range.
selectorsIn:
- phone
selectorsOut:
- name
- phone
status: live
pricing: free
costNote: Core number-analysis lookups are free with no account; some advanced/bulk features and the live HLR (network status) lookup may be paid or gated.
opsec: passive
opsecNote: Ordinary number-range analysis is fully passive — it consults a static numbering database, not the live network, so nothing reaches the target. A live HLR lookup (if used) DOES ping the network and can be logged; avoid it unless you specifically need real-time status and understand it is active.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A long-standing, authoritative reference for global numbering plans and operator ranges, widely cited in telecoms and OSINT; the range/operator data is reliable, though real-world ports mean the current carrier can differ from the assigned one.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- numberingplans.com
- International Numbering Plans
tags:
- toddington
- curated-directory
- telephone-numbers
- carrier-lookup
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# International Numbering Plans Database

> The reference for global telephone numbering: paste a number and learn its country, assigned operator, and whether the range is valid — the passive first step in phone OSINT.

## When to use
You have a `phone`, SIM (ICCID), or IMSI number and need to characterise it before deeper work: which country and region it belongs to, which network operator the range is assigned to, and whether it's a validly-allocated number at all. Ideal early triage — it tells you whether a number is even plausible and what carrier to expect, entirely passively.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://numberingplans.com and pick the relevant analysis tool (Number analysis, SIM number analysis, or IMSI analysis).
2. Enter the `phone`/SIM/IMSI in full international form.
3. Read the output: country, area/region, assigned operator/`name`, and range validity.
4. Note the caveat: this shows the *originally assigned* operator — number portability means the current carrier may differ (use a live HLR lookup only if you truly need real-time status).
5. Pivot: the country/region narrows `geolocation`; the operator and validity guide which national reverse-phone and caller-ID tools to try next.

## Inputs → Outputs
- **In:** `phone`, SIM (ICCID), or IMSI number
- **Out:** country/region, assigned network operator (`name`), number-range validity
- **Empty/negative result looks like:** "invalid/unallocated range" — the number isn't a validly-assigned number (typo, spoofed, or fake), which is itself a useful finding.

## Gotchas & OpSec
- Shows the *assigned* operator, not necessarily the current one — ported numbers will mislead; confirm with an HLR/live lookup if it matters.
- Static database analysis is passive; a live HLR lookup is active and network-logged — don't conflate the two.
- Identifies the carrier/geography, not the person — pair with a reverse-phone tool to get a name.

## Overlaps ("do both")
- Pairs with reverse-phone/caller-ID tools ([[true-caller]], [[sync-me]]) — this establishes country/operator/validity; those attach a probable identity.

## Trust & verifiability
`trust: trusted` — an authoritative, long-maintained numbering reference; range/operator data is reliable, with portability the main caveat to verify.
