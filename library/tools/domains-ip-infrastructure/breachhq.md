---
id: breachhq
name: BreachHQ
description: Use when you have a threat-actor or APT-group name and want a reference profile — returns actor origin, type, aliases, and linked references (not a breach-lookup for individuals).
url: https://breach-hq.com/threat-actors
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Looking up a named cyber threat actor / APT group's profile, origin, and references.
selectorsIn: []
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free public reference (by Beyond Identity); the core threat-actor database is openly readable, contribution optional via signup.
opsec: passive
opsecNote: A public catalog you browse by actor name — you submit no subject selector, so nothing about your investigation leaves your browser. Fully passive reading.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Curated/aggregated threat-actor listings published by a security vendor with community contribution; a secondary reference, confidence levels noted per entry.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- BreachHQ
- breach-hq.com
tags:
- threat-actors
- threat-intel
- reference
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# BreachHQ

> A free, browsable catalog of known cyber threat actors / APT groups — origin, type, aliases, and references, one profile per actor.

## When to use
This is a **threat-intel reference**, not a personal breach checker. When an investigation touches a named adversary — an APT group, ransomware crew, or organized-crime cyber actor mentioned in a report or attribution — BreachHQ gives a quick profile: country of origin, actor type, confidence level, aliases, and a list of source references. It does **not** take a person's `email`/`name` and tell you if *they* were breached (use a breach-exposure checker for that). Its selector value is the `employer-org`/group identity of an actor.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://breach-hq.com/threat-actors.
2. Browse or page through the actor list; find the group by name/alias.
3. Read the profile: origin country, type (APT / ransomware / organized crime), confidence, and reference count.
4. Follow the linked references out to primary threat-intel reporting for detail.

## Inputs → Outputs
- **In:** a threat-actor / group name (no personal selector)
- **Out:** actor profile — origin, type, aliases (`employer-org`-level identity), references
- **Empty/negative result looks like:** the actor isn't catalogued or has few references — this is an aggregated list, so absence means "not covered here," not "doesn't exist." Cross-check MITRE ATT&CK / vendor reporting.

## Gotchas & OpSec
- **Not a per-person breach lookup** — don't confuse "BreachHQ" with a credential-exposure service; it profiles *actors*, not victims.
- Secondary/aggregated source with per-entry confidence — verify against primary reporting before attributing.
- OpSec: **passive** — public reference, no subject data submitted.

## Overlaps ("do both")
- Complements primary threat-intel references (MITRE ATT&CK groups, vendor APT reports) — BreachHQ is a quick index/entry point; the linked references are where you confirm and go deep.

## Trust & verifiability
`trust: community` — a real, freely-readable vendor-published catalog with community input and explicit confidence levels; treat it as a signpost and verify attributions upstream.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | breachhq |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut |  → employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
