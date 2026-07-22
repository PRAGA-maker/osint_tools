---
id: the-osint-field-manual-tofm
name: The OSINT Field Manual (TOFM)
description: Use when you need a structured missing-persons OSINT methodology — the Trace Labs playbook of workflows, selectors, and tradecraft to run and document an investigation end to end.
url: https://github.com/tracelabs/tofm
category: training-ctf
path:
- training-ctf
bestFor: Reference methodology and tradecraft for running a missing-persons / person-of-interest OSINT investigation.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, open document on GitHub (Markdown); no account or payment.
opsec: passive
opsecNote: Reading the manual reveals nothing about any target. Its value is that it teaches OpSec-aware workflow — sock-puppet use, avoiding contact with the subject, evidence handling — so applying it improves your operational hygiene rather than creating exposure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Trace Labs documentation repo, companion to their OSINT VM and Search Party CTFs used for real missing-persons crowdsourcing.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- TOFM
- OSINT Field Manual
tags:
- methodology
- guide
- tracelabs
- tradecraft
source: tracelabs-repos
lastVerified: '2026-07-22'
enrichment: full
relatedTools:
- gumshoe
- h8mail-trace-labs-fork
- trace-labs-awesome-osint
- trace-labs-osint-vm-tlosint-vm
---

# The OSINT Field Manual (TOFM)

> Trace Labs' field manual: the workflow-and-tradecraft playbook behind their missing-persons Search Party CTFs, distilled into a single reference document.

## When to use
You are running (or planning) a person-centred OSINT investigation — especially a missing-persons case — and want a proven methodology rather than an ad-hoc search: how to structure the investigation, which selectors to pivot on and in what order, how to categorise and document findings, and how to stay OpSec-safe and legally clean. Read it before you start a case and refer back when you're stuck on where to pivot next.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/tracelabs/tofm and read `tofm.md` (the manual body).
2. Use its investigation phases and selector-pivot guidance as a checklist for your own case — e.g. what to do with a name vs a username vs a photo.
3. Adopt its evidence-documentation and categorisation conventions so findings are reportable (Trace Labs designed these for handing intelligence to law enforcement).
4. Apply its OpSec guidance (sock puppets, no contact with the subject or family, jurisdictional caution).
5. Pivot: pair the methodology with concrete tools — the manual points at the Trace Labs OSINT VM and awesome-osint tool lists to execute each step.

## Inputs → Outputs
- **In:** none (a methodology reference, not a selector-driven lookup)
- **Out:** structured investigation workflows, selector-pivot strategies, documentation and OpSec conventions
- **Empty/negative result looks like:** N/A — it is guidance, not a query; the "gap" it reveals is a step in your process you haven't covered.

## Gotchas & OpSec
- It is a manual, not a tool: it tells you *how*, not *what the answer is* — you still need the individual lookup tools.
- The repo is intentionally minimal (README + `tofm.md`); don't expect an app.
- OpSec: the whole point is safer tradecraft; internalise its no-contact and sock-puppet rules before working a live case.

## Overlaps ("do both")
- Pairs with `[[trace-labs-osint-vm-tlosint-vm]]` and `[[trace-labs-awesome-osint]]` — TOFM supplies the method, those supply the environment and the tool inventory to carry it out.

## Trust & verifiability
`trust: trusted` — first-party Trace Labs documentation, maintained on their official GitHub and tied to their real crowdsourced missing-persons operations.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-osint-field-manual-tofm |
| category | training-ctf |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
