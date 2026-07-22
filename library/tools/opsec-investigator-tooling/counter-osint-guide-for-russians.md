---
id: counter-osint-guide-for-russians
name: Counter-OSINT guide for Russians
description: Use when you want to reduce your own (or a source's) digital footprint against OSINT — a practical privacy/counter-investigation guide from a well-known OSINT author.
url: https://github.com/soxoj/counter-osint-guide-ru
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Learning concrete steps to harden personal privacy and shrink your OSINT-discoverable footprint.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open (a GitHub knowledge repo); written in Russian, readable via machine translation.
opsec: passive
opsecNote: This is a reference guide, not a tool that touches any target — reading it leaks nothing. Its purpose is defensive: understanding how investigators find people so you (or a vulnerable source/witness) can remove those traces.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Authored by soxoj, creator of Maigret and a respected OSINT-tooling developer; widely referenced counter-OSINT material.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- maigret
- socid-extractor
- marple
- osint-namecheckers-list
- username-generation-guide
aliases:
- Counter-OSINT guide
- soxoj counter-osint-guide-ru
tags:
- counter-osint
- privacy
source: osint4all
lastVerified: '2026-07-22'
enrichment: full
---

# Counter-OSINT guide for Russians

> A practical, well-regarded guide (by Maigret's author, soxoj) on shrinking your own OSINT footprint — how leaks happen and the concrete steps to close them.

## When to use
Reach for this when the "subject" to protect is you, your team, or a vulnerable source/witness. Because it's written from a working OSINT investigator's perspective, it doubles as a map of *how* people are found — email/phone enumeration, username reuse, data-broker exposure, metadata — which sharpens both your defensive hygiene and your understanding of offensive technique.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/soxoj/counter-osint-guide-ru (use in-browser/machine translation from Russian if needed).
2. Work through the chapters: securing accounts, breaking username/email reuse, opting out of data brokers/aggregators, scrubbing metadata, and phone/number hygiene.
3. Apply the checklists to the identity you're protecting; verify each fix by re-running the corresponding discovery technique against yourself.
4. Use the same techniques it describes as a checklist of *where to look* when you are the investigator.
5. Pivot: to test your exposure, run tools like `[[maigret]]` and `[[socid-extractor]]` against your own selectors and confirm the leaks are closed.

## Inputs → Outputs
- **In:** n/a — a knowledge resource, not a lookup taking a selector
- **Out:** actionable counter-OSINT guidance and checklists
- **Empty/negative result looks like:** not applicable; success is a measurably smaller footprint when you re-test yourself.

## Gotchas & OpSec
- Written in Russian and partly Russia-context specific (local services/registries) — the principles are universal, some service specifics are not.
- As a Git repo it can be updated or forked; note the commit/date you relied on.
- OpSec: passive reading; the value is defensive, and its techniques are exactly what an investigator uses offensively.

## Overlaps ("do both")
- Pairs with `[[maigret]]`, `[[socid-extractor]]` and `[[marple]]` — use those to *find* your exposed footprint, use this guide to *remove* it, then re-test.

## Trust & verifiability
`trust: trusted` — from soxoj, a recognised OSINT-tool author; guidance is practical and verifiable by testing your own exposure before and after.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | counter-osint-guide-for-russians |
