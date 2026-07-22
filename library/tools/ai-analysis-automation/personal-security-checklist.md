---
id: personal-security-checklist
name: personal-security-checklist
description: Use when you (or a source/witness) need to harden digital privacy and security — a comprehensive, prioritized checklist of concrete protective actions.
url: https://github.com/Lissy93/personal-security-checklist
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: A prioritized, actionable checklist for locking down accounts, devices, network and data against tracking and compromise.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source; readable on GitHub or the companion site (digital-defense.io).
opsec: passive
opsecNote: This is defensive reference material — reading it touches no target. Its purpose is to reduce your (or a vulnerable contact's) exposure; like any counter-OSINT guide, it doubles as a map of how people get exposed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A very widely-starred, community-maintained checklist (Lissy93) with sourced recommendations; guidance is mainstream and verifiable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- awesome-privacy
- counter-osint-guide-for-russians
aliases:
- Personal Security Checklist
- digital-defense.io
tags:
- related-awesome-lists
- privacy
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# personal-security-checklist

> A comprehensive, prioritized checklist of concrete digital-security actions — the practical playbook for shrinking your own (or a source's) attack and OSINT surface.

## When to use
The person to protect is you, your team, or a vulnerable source/witness whose exposure could endanger them. This checklist walks through accounts, authentication, browsing, mobile, network, and data with tiered recommendations (essential → advanced). It's also a useful mental model of *how* people get compromised or found, which sharpens your investigative technique in reverse.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the checklist at https://github.com/Lissy93/personal-security-checklist (or the digital-defense.io site).
2. Start with the highest-priority ("essential") items — password manager, 2FA/passkeys, account recovery, device encryption.
3. Work down through browsing/network/data sections, applying items to the identity you're protecting.
4. Verify each fix by re-testing your exposure (e.g. check breach databases, run username/email searches on yourself).
5. Re-review periodically — recommendations and threats change; note the commit/date you followed.

## Inputs → Outputs
- **In:** n/a — a reference resource, not a lookup taking a selector
- **Out:** a prioritized set of protective actions with rationale and tool suggestions
- **Empty/negative result looks like:** not applicable; success is a measurably reduced footprint when you re-test yourself after applying items.

## Gotchas & OpSec
- Guidance is general and best-effort — adapt to the specific threat model (a stalking victim, an activist, and a journalist differ).
- Tool recommendations age; verify a suggested tool is still maintained before adopting it.
- OpSec: passive reading; defensive by intent.

## Overlaps ("do both")
- Pairs with `[[counter-osint-guide-for-russians]]` and `[[awesome-privacy]]` — this is the actionable checklist, those add region-specific counter-OSINT technique and a curated tool directory; use them together to both find and close exposure.

## Trust & verifiability
`trust: trusted` — a heavily-used, source-backed community checklist; its recommendations are mainstream security practice you can corroborate against other reputable guides.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | personal-security-checklist |
