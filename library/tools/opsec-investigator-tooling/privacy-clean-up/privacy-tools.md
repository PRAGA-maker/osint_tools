---
id: privacy-tools
name: PrivacyTools.io
description: Use when you're building an investigator OPSEC toolkit and want vetted privacy/security alternatives — returns a curated directory of tools by category.
url: https://www.privacytools.io/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- privacy-clean-up
bestFor: Choosing privacy-respecting tools (VPNs, browsers, email, DNS, etc.) to harden your own investigative OPSEC setup.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free curated directory; no account. Some recommended services (VPNs, paid email) charge, but the directory itself is free and many picks are free/open-source.
opsec: passive
opsecNote: This is an OPSEC-hardening reference for the investigator, not a lookup tool against a target. Reading it has no subject footprint. Use it to build a compartmentalized research environment before you touch a case.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-run privacy-tools directory established 2015; recommendations reflect maintainer/community judgment and criteria, not independent audits — evaluate picks yourself.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- privacytools.io
- Privacy Tools directory
tags:
- opsec
- privacy
- toolkit
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# PrivacyTools.io

> A long-running curated directory of privacy- and security-respecting software — a reference for building the compartmentalized OPSEC environment you investigate *from*, not a tool you point at a subject.

## When to use
Before (or between) investigations, when you're assembling or hardening your own operational setup: a privacy-respecting browser, VPN, DNS, email, password manager, and OS choices that keep your research activity from tracing back to you. This is meta-tooling — it improves your `opsec: passive` posture rather than producing intel on a target.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.privacytools.io/ and browse by category (browsers, VPNs, email, DNS, messaging, etc.).
2. Read the picks and the stated selection criteria; note open-source/free vs. paid options.
3. Choose tools that fit a compartmentalized research profile (separate browser, sock-puppet email, VPN/IP isolation).
4. Pivot: pair choices with `[[fake-us-identities]]`-style persona data to run a fully isolated investigative identity.

## Inputs → Outputs
- **In:** none (reference directory)
- **Out:** curated privacy/security tool recommendations by category (no target selectors)
- **Empty/negative result looks like:** n/a — it's a reference; the risk is choosing a recommendation uncritically, so vet each pick against your threat model.

## Gotchas & OpSec
- Recommendations are curated opinion, not audits — the "best" privacy tool depends on your threat model; don't adopt blindly.
- The directory has had governance/forks over the years (cf. PrivacyGuides); cross-reference before committing.
- OpSec: reading is passive; the value is in hardening your own footprint.

## Overlaps ("do both")
- Pairs with persona/sock-puppet tooling like `[[fake-us-identities]]` — this hardens the infrastructure, that supplies the isolated identity to run on it.

## Trust & verifiability
`trust: community` — a reputable community directory, but its picks are editorial judgment; verify each tool's current standing and licensing yourself before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | privacy-tools |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | (none) → (none) |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
