---
id: guardian-project
name: Guardian Project
description: Use when you need vetted privacy/anti-surveillance apps for OpSec — Guardian Project builds open-source tools (Orbot, ProofMode, Haven) for secure investigative work.
url: https://guardianproject.info
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Sourcing trusted open-source privacy, anonymity and media-verification apps to harden an investigator's own OpSec.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source; all apps are free to download (many via F-Droid/Play). No account required.
opsec: passive
opsecNote: This is defensive OpSec tooling for the INVESTIGATOR, not a lookup against a subject. Its apps (Orbot for Tor routing, ProofMode for verifiable media capture, Haven for device monitoring) reduce your own exposure. Verify downloads via official channels/signatures, and understand each tool's threat model — anonymity tools are only as good as how you use them.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: mobile-app
trust: trusted
trustNote: A long-established, respected open-source collective (Guardian Project) behind widely audited privacy tools used by journalists and human-rights defenders; code is public and reviewed.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- GuardianProject
- guardianproject.info
tags:
- privacy-and-encryption-tools
- opsec
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Guardian Project

> An open-source collective building privacy and anti-surveillance apps. Not a data source — it's where an investigator gets vetted tools to protect their own OpSec.

## When to use
When you need to harden your **own** operational security rather than look up a subject. Guardian Project maintains free, audited tools that matter for investigative tradecraft: **Orbot** (route apps through Tor), **Orfox/Tor-based browsing**, **ProofMode** (capture photos/video with verifiable, tamper-evident metadata for evidence), **Haven** (turn a spare phone into a physical-intrusion/tamper detector), and secure-comms libraries. Reach for it to build a safer working setup or to capture court-defensible media.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Go to guardianproject.info to browse the current app lineup and their threat models.
2. Install the app you need from an official channel (F-Droid, Play Store, or signed APK) and verify signatures.
3. Examples: run investigative mobile apps through **Orbot** for Tor routing; use **ProofMode** when you need chain-of-custody-grade media; deploy **Haven** to monitor a device/room for tampering.
4. Learn each tool's limits — read its docs; anonymity/verification only holds within the tool's intended threat model.
5. Combine with your broader OpSec (VPN, sock puppets, compartmentalized devices).

## Inputs → Outputs
- **In:** none (a source of OpSec tools, not a selector lookup)
- **Out:** vetted privacy/anonymity/media-verification apps for your own use — no subject `selectorsOut`
- **Empty/negative result looks like:** N/A — it's a toolmaker; the "failure" is choosing a tool whose threat model doesn't match your risk, so read before deploying.

## Gotchas & OpSec
- Defensive tooling for you, not an investigative data source.
- Anonymity tools fail when misused (e.g. mixing Tor and logged-in personal accounts) — understand each app's model.
- Always install from official, signature-verified channels to avoid trojaned builds.

## Overlaps ("do both")
- Complements other OpSec/browser-hardening tools in the library (VPNs, sock-puppet setups); ProofMode overlaps with metadata/EXIF-verification tooling for evidence capture.

## Trust & verifiability
`trust: trusted` — a respected, long-running open-source privacy collective whose tools are public, audited, and relied on by journalists and human-rights defenders worldwide.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | guardian-project |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | mobile-app |
| opsec | passive |
| human-in-loop | no |
