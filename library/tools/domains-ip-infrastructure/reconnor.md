---
id: reconnor
name: Reconnor
description: Use when you have a `domain`, `username`, or `email` and want a broad Python recon/OSINT toolkit in one place — returns subdomains, `social-profile` hits, breach/email data, and infra info.
url: https://github.com/enginestein/Reconnor
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: A single Python suite bundling ~90 recon/OSINT scripts (subdomains, username search, email finding, tech fingerprinting).
selectorsIn:
- domain
- username
- email
selectorsOut:
- domain
- social-profile
- email
status: degraded
pricing: free
costNote: Free and open-source (Python); `pip install -r requirements.txt`. Optional AI integrations (OpenAI/Anthropic/Gemini/Ollama) need your own keys.
opsec: active
opsecNote: Many modules actively query target platforms/hosts (username checks across 60+ sites, subdomain probing, port scanning). Treat it as active enumeration — run from a sock-puppet egress, and be aware some modules (port/SMB/LDAP scanning) directly touch target infrastructure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: A small single-author educational project (~2 stars, few commits); functional but low-maturity and low-adoption, so validate results and read the scripts before trusting them.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Reconnor
tags:
- educational
- recon-suite
source: gh-topic-footprinting
lastVerified: '2026-07-29'
enrichment: full
---

# Reconnor

> A broad, single-author Python recon suite: ~90 standalone scripts spanning subdomain discovery, username/email OSINT, and web/infra checks — capable but low-maturity.

## When to use
You want one toolkit to run a range of recon tasks from the CLI and don't need battle-tested tooling: given a `domain` you can enumerate subdomains/DNS/certs and fingerprint tech; given a `username` you can sweep 60+ platforms; given an `email` you can run finding/breach checks. Reasonable for learning or a quick broad pass — but verify anything important against a mature dedicated tool, since it's a small hobby project.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo and install: `pip install -r requirements.txt` (or `pip install .[ext]` for optional external tools).
2. Run a module: `python3 main.py <tool> <target>` (e.g. a username or domain).
3. Optionally wire an AI provider key for its analysis features.
4. Pivot: `social-profile` hits feed profile OSINT; discovered subdomains/`domain`s feed infra tooling; `email`/breach hits feed identity work.

## Inputs → Outputs
- **In:** `domain`, `username`, or `email` (module-dependent)
- **Out:** subdomains/DNS, `social-profile` matches, `email`/breach data, tech fingerprints
- **Empty/negative result looks like:** empty or errored module output — a low-maturity checker may simply be broken for a given site; don't read a non-hit as a confirmed negative.

## Gotchas & OpSec
- **Low maturity:** few stars/commits, single author — expect rough edges and broken checkers; read the script before relying on its output.
- **Active:** username/port/infra modules contact targets directly — use a sock-puppet egress and stay within authorised scope for any scanning module.
- AI features send data to third-party model APIs if you enable them.

## Overlaps ("do both")
- Overlaps with mature single-purpose tools (`[[osrframework]]`, Sherlock/Maigret for usernames, `[[dnsx]]` for DNS) — prefer those for load-bearing findings and use Reconnor for convenience/breadth.

## Trust & verifiability
`trust: unverified` — a small educational project; treat every result as a lead to confirm with an established tool, and inspect the relevant script since it isn't widely vetted.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reconnor |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, username, email → domain, social-profile, email |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
