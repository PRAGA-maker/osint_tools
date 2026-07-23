---
id: owasp-maryam
name: OWASP Maryam
description: Use when you have a `domain`, `email`, or `username` and want modular recon in one framework — returns subdomains, docs/metadata, related `email`s and `social-profile`s.
url: https://github.com/saeeddhqan/Maryam
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- subdomains
bestFor: Running scriptable, multi-module OSINT recon (subdomains, search, metadata, contacts) from one framework.
selectorsIn:
- domain
- email
- username
selectorsOut:
- domain
- email
- social-profile
status: live
pricing: free
costNote: Free and open-source (OWASP project); install via pip/git. Some modules need free API keys to reach their sources.
opsec: active
opsecNote: "Maryam is a framework of modules with mixed OpSec: passive modules read search engines and third-party APIs, but others issue DNS queries or fetch documents directly from the target. Know which module you're running — an active one hits the target from your IP. Route through a proxy/VPN and a sock-puppet, and supply throwaway API keys, not personal ones."
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: An OWASP-affiliated open-source framework (saeeddhqan); modular and auditable, but results are aggregated from many upstream sources of varying reliability.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Maryam
- OWASP Maryam
tags:
- recon-framework
- subdomains
- osint-automation
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# OWASP Maryam

> A Recon-ng-style modular OSINT framework: load a module, feed it a domain/email/username, and it pulls subdomains, documents, metadata, and contacts from many sources — scriptable for repeatable workflows.

## When to use
You have a `domain`, `email`, or `username` and want an extensible, one-stop recon framework rather than a dozen separate tools — enumerating subdomains, harvesting documents and their metadata, gathering related `email`s and `social-profile`s, and chaining modules into a workflow. Best for analysts comfortable on the CLI who want repeatable, automatable recon. Broad infrastructure/org recon, so low direct missing-persons relevance.

## How to use it (`bestInteractionPattern`: cli)
1. Install from https://github.com/saeeddhqan/Maryam (`pip install maryam` or clone + install).
2. Launch the interactive console; list modules (`search`, `footprint`, `subdomain`, `email`, `docs_search`, etc.).
3. Configure any needed API keys (throwaway ones) for modules that require them.
4. Set the target input and run the module; **check whether the module is passive or active** before running against a live target.
5. Chain modules and export results; pivot discovered subdomains/emails/profiles into specialist tools.

## Inputs → Outputs
- **In:** `domain`, `email`, or `username` (module-dependent)
- **Out:** subdomains (`domain`), related `email`s, `social-profile`s, document metadata
- **Empty/negative result looks like:** a module returning no rows — often a missing/invalid API key or a source with nothing indexed, not necessarily "nothing exists." Re-run with keys configured and other modules.

## Gotchas & OpSec
- **Mixed passive/active:** some modules directly query the target (DNS, doc fetch) from your IP — identify and proxy those; don't assume the whole framework is passive.
- Module coverage and source availability drift as upstream APIs change; a broken module is a tooling issue, not a finding.
- Results aggregate many sources of uneven quality — treat as leads and de-duplicate/verify.

## Overlaps ("do both")
- Overlaps with focused tools like [[dns-dumpster]] (subdomains) and [[metafinder]] (document metadata) — Maryam automates a broad sweep, those give deeper single-purpose results; use Maryam to discover, specialists to confirm.

## Trust & verifiability
`trust: community` — an OWASP-affiliated, auditable open-source framework; reliability depends on the upstream source behind each module, so verify key findings against the originating service.
