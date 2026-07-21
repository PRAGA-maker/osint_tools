---
id: ircp
name: IRCP
description: Use when you have an IRC server/network scope and want to enumerate its channels and users — returns `username`/`social-profile` and channel metadata to map who is on a network.
url: https://github.com/internet-relay-chat/IRCP
category: communities-forums
path:
- communities-forums
- irc-search
bestFor: Large-scale enumeration of IRC servers — listing channels and harvesting nick/user data across a network.
selectorsIn:
- domain
- ip-address
selectorsOut:
- username
- social-profile
status: live
pricing: free
costNote: Free, open-source Python tool; no cost.
opsec: active
opsecNote: ACTIVE and noisy. IRCP connects directly to target IRC servers, issues VERSION/INFO/LIST and joins channels to WHOIS users — this is visible in server logs and to operators/monitoring, and can get your IP/host banned. Use dedicated research infrastructure (never a personal IP), and honour the tool's opt-out list for administrators who decline scanning.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source IRC reconnaissance tool with an active commit history; it collects live protocol data, so results are current but self-reported by the servers.
missingPersonsRelevance: medium
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
- IRC Protocol
- internet-relay-chat/IRCP
tags:
- irc
- enumeration
source: arf-seed
lastVerified: '2026-07-21'
enrichment: full
---

# IRCP

> A reconnaissance scanner for Internet Relay Chat: point it at IRC servers/ranges and it enumerates channels, users, and network topology into structured JSON.

## When to use
You have a lead on an IRC network — a server `domain`/`ip-address`, or a suspicion that a subject or group uses a particular network — and you want to map it: which channels exist, who is present, and what nicks/hosts appear. Useful for chasing a `username` seen elsewhere into the IRC communities where it is active, or profiling a network tied to a group of interest.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `internet-relay-chat/IRCP` and set up Python.
2. Prepare a target file of IPs/hosts (optionally with ports; common IRC ports are 6660–6669, 6697, 7000).
3. Edit the in-script configuration (ports, timeouts, TLS) as needed.
4. Run the scanner — it tries SSL/TLS then plain connections, issues VERSION/INFO/LIST, and joins channels to WHOIS users.
5. Read the JSON output (organised by IRC numeric/event): server info, channel lists, user/nick data, topology.
6. Pivot: a recovered `username`/nick → username-search tools across other platforms; a channel → deeper manual observation.

## Inputs → Outputs
- **In:** IRC server target list (`ip-address`/`domain` + ports)
- **Out:** channel and user enumeration — `username`/nick and host data (`social-profile` leads), server/network metadata (JSON)
- **Empty/negative result looks like:** connection refused/timeout (server down, wrong port, or blocking you) or empty channel lists (server hides LIST) — a lack of data can mean access controls, not an empty network.

## Gotchas & OpSec
- **Active and logged.** Operators see your connections and channel joins; expect possible K-lines/bans. Never scan from a personal IP.
- Respect the project's admin opt-out mechanism and any network's terms; large-scale scanning can be abusive.
- Nicks/hosts are self-reported and easily spoofed; treat harvested identities as leads to corroborate.

## Overlaps ("do both")
- Pairs with username-search tools — IRCP finds the nicks active on a network, then a cross-platform username search ties that handle to profiles elsewhere.

## Trust & verifiability
`trust: community` — a maintained open-source recon tool; the data is pulled live from the servers themselves, so it is current but only as truthful as those servers and the (spoofable) user records they expose.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ircp |
| category | communities-forums |
| selectorsIn → selectorsOut | domain, ip-address → username, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
