---
id: sylva-identity-discovery
name: Sylva Identity Discovery
description: Use when you have a `username` and want to enumerate accounts across platforms AND branch out to discover linked identities — returns social-profile and username leads.
url: https://sylva.pfeister.dev/
category: username
path:
- username
- username-search-engines
bestFor: CLI username enumeration that "branches" — starting from one handle and recursively discovering connected identities across platforms.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free and open-source (install via pip/Docker). Some enrichment features require third-party API keys you supply yourself, which may have their own costs/limits.
opsec: active
opsecNote: Sylva makes live requests to each target platform to test whether a username exists, so your IP touches those sites. Any configured API keys route through third-party services. Run it from a VPN/clean IP and use throwaway API keys; do not run it from an IP tied to your identity.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Open-source project by Paul Pfeister, maintained on GitHub with a Python package and Docker image; community tool, not independently audited.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- sylva-identity-discovery-2
aliases:
- Sylva
- sylva.pfeister.dev
tags:
- username
- enumeration
- cli
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Sylva Identity Discovery

> A command-line username-enumeration tool with a twist: it doesn't just check one handle across sites, it *branches* — using each discovered identity to seed further searches and map a connected web of accounts.

## When to use
You have a `username` and want to go beyond a flat "is this handle taken on these 300 sites" check. Sylva's `branch` mode chains discovery: when it finds a profile that reveals another handle, email or name, it can pursue that too, expanding a single seed into a graph of linked identities. Reach for it when a target reuses or slightly varies handles across platforms and you want to trace the whole cluster rather than a single list.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install sylva` (or run the Docker image).
2. Configure API keys if you want the enrichment integrations: `sylva config --edit`.
3. Basic enumeration: `sylva search <username>` to check the handle across supported platforms.
4. Branching discovery: `sylva branch <username>` to start from the handle and recursively follow newly discovered identities.
5. Review the account list; confirm each hit manually (existence checks produce false positives).
6. Pivot: confirmed profiles feed platform-native OSINT; newly surfaced usernames/emails feed further enumeration or email lookups.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` (matched accounts across platforms), `username` (variant/linked handles discovered while branching)
- **Empty/negative result looks like:** no matches, or matches that turn out to be different people who happen to share the handle — always verify, since username availability ≠ identity.

## Gotchas & OpSec
- Existence checks are probabilistic: common handles produce false positives, and some sites return ambiguous responses. Verify each hit on the platform.
- API-key features are optional but expand coverage; supply throwaway keys.
- **Active:** it queries each platform directly from your IP — use a VPN and avoid an attributable IP.

## Overlaps ("do both")
- Pairs with broad username sweepers like Sherlock/WhatsMyName-style tools — those give a wide flat list, while Sylva's branching chases the connections between handles; run a flat sweep first, then branch the confirmed ones.

## Trust & verifiability
`trust: community` — an open-source tool with public source you can inspect; results are only as reliable as the per-site checks, so treat output as leads to confirm, not conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sylva-identity-discovery |
| category | username |
| selectorsIn → selectorsOut | username → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key) |
