---
id: gumshoe
name: gumshoe
description: Use when you have a `name`, `username`, `email` or `domain` and want an automated recursive OSINT-Framework pivot engine — returns chained findings/leads across resource types.
url: https://github.com/tracelabs/gumshoe
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Automating recursive pivots across OSINT Framework resources — feed a seed selector, get chained follow-on findings.
selectorsIn:
- name
- username
- email
- domain
selectorsOut:
- social-profile
- associate
status: degraded
pricing: free
costNote: Free and open source (MPL-2.0) on GitHub. Self-hosted Go project — no account or fee, but you build/run it yourself.
opsec: passive
opsecNote: A local Go tool; OpSec depends on what resources it queries under the hood. As a proof-of-concept it may fan out requests to many third-party services — run from a sock-puppet IP and review which sources it touches before pointing it at a real target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Official Trace Labs project, but explicitly marked "[WIP] Proof of Concept"; ~19 commits, no releases, limited recent activity. Capable in principle, not production-ready.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- h8mail-trace-labs-fork
- the-osint-field-manual-tofm
- trace-labs-awesome-osint
- trace-labs-osint-vm-tlosint-vm
aliases:
- tracelabs gumshoe
tags:
- go
- recursion
- osint-framework
- tracelabs
- wip
source: tracelabs-repos
lastVerified: '2026-07-19'
enrichment: full
---

# gumshoe

> A Trace Labs proof-of-concept that models the OSINT Framework as a graph and recursively expands a seed selector into new findings until nothing new surfaces.

## When to use
You have a seed selector — a `name`, `username`, `email`, or `domain` — and want a tool that mechanically chases the "what could I pivot to next" question the way the OSINT Framework taxonomy suggests, recursively feeding each new finding back in. Reach for it when you want to prototype an automated pivot graph rather than click through the framework by hand. Because it's a WIP proof-of-concept from the Trace Labs (missing-persons CTF) ecosystem, treat it as an experiment/scaffold, not a finished product.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `https://github.com/tracelabs/gumshoe` and build it (Go toolchain; there's a Makefile).
2. In code, provide an initial finding and call the tool's `Run(...)` entry point with that seed.
3. The engine processes findings recursively through interconnected finding types, generating new leads from each.
4. Read the emitted findings/graph — these are candidate pivots, not verified facts.
5. Pivot: hand the surfaced leads to the concrete tools they point at (username/email/domain lookups) for actual enrichment.

## Inputs → Outputs
- **In:** a seed `name` / `username` / `email` / `domain`
- **Out:** recursively generated findings (candidate `social-profile` / `associate` leads / next-step resources)
- **Empty/negative result looks like:** the recursion terminates quickly with no new findings — either the seed was too sparse or (given WIP status) a finding type isn't yet implemented. Absence here is not evidence.

## Gotchas & OpSec
- Status is degraded: explicitly a WIP proof-of-concept with no releases — expect rough edges, gaps, and manual build effort; it may not run cleanly out of the box.
- It generates leads, not conclusions — everything it emits must be verified in the real target tool.
- OpSec: passive locally, but its recursion can touch many third-party services; audit and throttle before use.

## Overlaps ("do both")
- Sits within the Trace Labs stack — pair with `[[trace-labs-osint-vm-tlosint-vm]]` (the environment) and `[[trace-labs-awesome-osint]]` (the curated resource list) that its taxonomy mirrors.

## Trust & verifiability
`trust: trusted` — it's an official Trace Labs repository, so provenance is solid, but the WIP/PoC status means reliability is not: verify every finding downstream and don't depend on it for a live case yet.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gumshoe |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | name, username, email, domain → social-profile, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
