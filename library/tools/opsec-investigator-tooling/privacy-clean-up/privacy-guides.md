---
id: privacy-guides
name: Privacy Guides
description: Use when you're building an investigator's OpSec setup and need vetted privacy tools — returns curated, criteria-based recommendations for VPNs, browsers, email, and more.
url: https://www.privacyguides.org/en/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- privacy-clean-up
bestFor: Choosing trustworthy privacy/security tools to harden your own OSINT operational security and sock-puppet infrastructure.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, ad-free, nonprofit; not affiliated with the tools it lists.
opsec: passive
opsecNote: Passive reference — you read recommendations, submit nothing. This is about protecting *your* footprint as an investigator, not querying a subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A well-regarded nonprofit (since 2021) that publishes transparent selection criteria and takes no money from listed providers; recommendations are community-reviewed and open-source-friendly.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- privacyguides.org
- Privacy Guides
tags:
- opsec
- privacy
- tooling
- reference
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Privacy Guides

> Not an investigative tool but the reference that keeps *you* invisible while investigating — a nonprofit, criteria-driven catalog of privacy tools to build clean, compartmentalized OSINT infrastructure.

## When to use
Before or during an investigation, when you need to harden your own operational security: pick a VPN/browser/email/password-manager for a sock-puppet identity, set up compartmentalized DNS/Tor, or choose a hardened OS. Good OSINT depends on not leaking your identity, location, or intent to the platforms and subjects you query — Privacy Guides is where you assemble the toolkit that prevents that. It's a foundation resource, not a lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.privacyguides.org/en/ and start with the threat-modeling / "common threats" section to define what you're protecting against.
2. Browse the tool categories — VPNs, browsers, email, encryption, password managers, alternative OSes, hardware keys, DNS/Tor.
3. Use its transparent selection criteria and comparison tables to pick tools that fit your investigator threat model (separation from your real identity, no logging, open source).
4. Apply the picks to build compartmentalized sock-puppet infrastructure (dedicated browser profile, VPN/IP separation, isolated email).
5. Pivot: a hardened setup is the prerequisite for using *active* tools in this library (account-login lookups, uploads, adult/dating sites) without exposing yourself.

## Inputs → Outputs
- **In:** your own OpSec requirements/threat model (no subject selector)
- **Out:** curated, criteria-backed tool recommendations and comparisons for building a private, compartmentalized setup
- **Empty/negative result looks like:** N/A — it's a reference; the failure mode is skipping it and running investigations from an attributable, leaky environment.

## Gotchas & OpSec
- **For legitimate privacy, not deception:** the site targets self-protection; it won't teach identity fraud, and its advice must be applied lawfully.
- Recommendations evolve — re-check before relying on an older pick, as tools change ownership/trust status.
- It selects tools; you still have to configure them correctly (a recommended VPN misused still leaks).

## Overlaps ("do both")
- Underpins every *active* tool in this library — pair Privacy Guides' setup with account-login or upload-based lookups (e.g. `[[alt-com]]`, `[[breadcrumbs-app]]`, reverse-image uploads) so those queries never trace back to you.

## Trust & verifiability
`trust: trusted` — an established, ad-free nonprofit with published, auditable selection criteria and no financial ties to listed providers; among the most reputable privacy-tool references available.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | privacy-guides |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
