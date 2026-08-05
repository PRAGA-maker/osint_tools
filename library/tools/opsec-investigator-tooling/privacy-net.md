---
id: privacy-net
name: Privacy.net
description: Use when you want a vetted starting list of privacy and browser-security tools for your own OpSec — returns links to leak-checkers, breach lookups, and privacy orgs.
url: https://privacy.net/resources/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A curated jump-off list of privacy/OpSec tools and organisations for the investigator's own hygiene.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free reference page; no account.
opsec: passive
opsecNote: Passive — a static directory of links. Reading it exposes nothing about any target. It is for hardening your own operating posture (leak checks, encryption, breach monitoring), not for querying a subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Privacy.net is an independent privacy-education site; the resources page points to reputable third parties (EFF, Tor Project, Have I Been Pwned, BrowserLeaks), so its value is the curation, and each linked tool carries its own trust.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- privacy-net-privacy-analyzer
aliases:
- Privacy.net Resources
- privacy.net
tags:
- toddington
- curated-directory
- proxy-servers-online-privacy-security-tools
- opsec
source: toddington-resources
lastVerified: '2026-08-05'
enrichment: full
---

# Privacy.net

> A short, curated directory of privacy and browser-security resources — a sensible reading/tooling list for keeping your own investigative OpSec tight.

## When to use
Before or during an investigation you want to check and harden your own footprint — what your browser leaks, whether your working identities appear in breaches, which encryption and privacy tools to reach for. This page is an orientation index, not a lookup you run against a subject. Reach for it to assemble your OpSec toolkit, then use the linked tools directly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://privacy.net/resources/.
2. Scan the curated entries — it points to things like BrowserLeaks (browser/IP leak checks), Have I Been Pwned (breach exposure), GnuPG (encryption), and advocacy orgs (EFF, EPIC, Tor Project).
3. Follow a link to the actual tool and use it there (e.g. run BrowserLeaks from your sock-puppet browser to confirm it isn't leaking your real IP/WebRTC/fingerprint).
4. Also note Privacy.net's own Analyzer (linked in its nav) for a quick "what does my connection reveal" check.
5. Use it to build a repeatable pre-op checklist for your operating identities.

## Inputs → Outputs
- **In:** none — it is a directory, not a query tool
- **Out:** links to privacy/OpSec tools and organisations (leak checkers, breach lookups, encryption, advocacy)
- **Empty/negative result looks like:** n/a — a static list; the only "failure" is a rotted outbound link, in which case find the tool directly (these are well-known services).

## Gotchas & OpSec
- It is a curated list, deliberately short — not an exhaustive catalogue; treat it as a starting point.
- The real work happens on the linked third-party tools, each with its own trust and caveats.
- Confirm links are current — directories age.
- OpSec: reading it is passive and target-neutral; it exists to improve *your* OpSec, not to profile others.

## Overlaps ("do both")
- Pairs with `[[privacy-net-privacy-analyzer]]` (the site's own connection-leak analyzer) and any dedicated browser-fingerprint checker — use the directory to pick tools, then the tools themselves to verify your setup.

## Trust & verifiability
`trust: community` — an independent privacy site whose value is curation; it links to reputable, verifiable third-party tools, and you should judge each linked service on its own merits.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | privacy-net |
