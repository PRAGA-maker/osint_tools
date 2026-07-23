---
id: surveilliance-self-defense
name: EFF Surveillance Self-Defense
description: Use when you need authoritative guidance on investigator OpSec and anti-surveillance practice — provides EFF's guides on encryption, secure tools, and threat-model scenarios (a reference, not a lookup).
url: https://ssd.eff.org
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Learning sound OpSec/threat-modeling and secure-tool setup before and during sensitive investigations.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, member-supported educational resource from the Electronic Frontier Foundation; no account required.
opsec: passive
opsecNote: A reading resource — nothing is queried and no target is involved. Its value is teaching you to protect your own operation: build a threat model, pick secure comms (Signal, Tor), and avoid exposing your identity while investigating.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by the EFF, a 35-year digital-rights nonprofit; the guidance is expert-reviewed and widely regarded as authoritative.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Surveillance Self-Defense
- EFF SSD
- ssd.eff.org
tags:
- opsec
- privacy
- threat-modeling
- education
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# EFF Surveillance Self-Defense

> The EFF's expert guide to protecting yourself from online surveillance — the reference for building an investigator's OpSec and threat model.

## When to use
Before or during a sensitive investigation, when you need to think clearly about *your own* security: what your threat model is, how to communicate securely, and how to avoid leaking your identity or intent to the subject. SSD is a learning resource, not an investigative tool — but sound OpSec is a prerequisite for safe OSINT, and this is the canonical, plain-language reference for it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ssd.eff.org.
2. Start with **Basics** (threat modeling, passwords, encryption fundamentals).
3. Read the **Tool Guides** relevant to your workflow (Signal, Tor, disk encryption).
4. Read the **Security Scenario** closest to your situation (e.g. journalist, activist, researcher) for tailored guidance.
5. Apply it: set up secure comms and a persona/OpSec plan before touching the target.

## Inputs → Outputs
- **In:** none (a knowledge resource)
- **Out:** guidance — threat models, secure-tool setup instructions, scenario playbooks
- **Empty/negative result looks like:** n/a — success is a concrete OpSec plan you can act on.

## Gotchas & OpSec
- Guidance is general; adapt it to your specific threat model rather than following it blindly.
- Tool recommendations evolve — check the article's date and cross-reference current best practice.
- Reading it is passive, but *acting* on it (installing Tor, Signal) has its own setup considerations.

## Overlaps ("do both")
- Complements concrete OpSec tools in this library (`[[macchanger]]`, VPN/Tor, sock-puppet browsers) — SSD gives the doctrine; those are the implementations.

## Trust & verifiability
`trust: trusted` — authored and maintained by the EFF; expert-reviewed, widely cited, and freely available.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | surveilliance-self-defense |
