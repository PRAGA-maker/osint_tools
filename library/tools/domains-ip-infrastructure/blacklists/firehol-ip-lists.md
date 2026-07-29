---
id: firehol-ip-lists
name: FireHOL IP Lists
description: Use when you have an `ip-address` and want to check it against 400+ aggregated public reputation/blocklists (malware, spam, attacks, anonymizers) — returns ip-address reputation leads.
url: https://iplists.firehol.org/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- blacklists
bestFor: Checking an IP's reputation across a large aggregation of public blocklists, or downloading the lists in bulk.
selectorsIn:
- ip-address
selectorsOut:
- ip-address
status: live
pricing: free
costNote: Free and open. Lists are published on the website and as raw files on GitHub (ip-lists repo); no account or key.
opsec: passive
opsecNote: Fully passive — you check an IP against downloaded/hosted lists, never contacting the IP itself. Nothing reaches the target. Working from the raw GitHub lists locally is fully offline.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Reputable open aggregation maintained by the FireHOL project; it re-publishes third-party lists, so a listing reflects some source's opinion, and false positives happen.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- FireHOL IP Lists
- iplists.firehol.org
tags:
- ip-reputation
- blocklists
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# FireHOL IP Lists

> A curated aggregation of 400+ public IP blocklists — malware C2, spam sources, attackers, botnets, Tor/anonymizers — with an easy way to see which lists an IP is on, and history of when it was listed.

## When to use
You have an `ip-address` (from a log, a connection, a resolved domain) and want a fast reputation read: is it a known malicious/spam/attack source, a Tor exit or anonymizer, or clean across the major public lists. Also useful in bulk — download the lists to tag a whole dataset of IPs, or to build local blocking/allowlisting. Complements a single-source reputation check by showing consensus across many lists.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://iplists.firehol.org/ and search the `ip-address`, or browse the catalog of lists.
2. Read which lists include the IP, each list's category (attacks, malware, spam, anonymizers, reputation), and the listing history/first-seen.
3. For bulk/automation, pull the raw lists from the FireHOL `blocklist-ipsets`/`ip-lists` GitHub repo and match locally.
4. Weigh the result: many independent lists agreeing = strong signal; one obscure list = weak.
5. Pivot: a listed IP → `[[team-cymru-ip-to-asn]]` for the owning network; anonymizer listing → reassess whether the IP reflects the real user.

## Inputs → Outputs
- **In:** an `ip-address` (or a list of them, offline)
- **Out:** which blocklists/categories the IP appears on and when (`ip-address` reputation/history)
- **Empty/negative result looks like:** not on any list — the IP has no public bad reputation, which is not proof it's benign (fresh or low-volume malicious IPs are often unlisted).

## Gotchas & OpSec
- Aggregates third-party lists of varying quality — false positives occur, especially on shared/CGNAT and cloud IPs; weight by how many independent lists agree.
- Reputation is time-sensitive — check first-seen/last-seen, not just membership.
- OpSec: fully passive; the target IP is never contacted (fully offline if you use the raw lists).

## Overlaps ("do both")
- Pairs with AbuseIPDB, Spamhaus, and `[[ip-location-io]]` threat flags — FireHOL gives breadth (many lists at once); the others add crowd-reported abuse and geolocation context.

## Trust & verifiability
`trust: community` — well-maintained open aggregation, but it re-publishes others' verdicts; treat a listing as a lead weighted by source agreement, not proof.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | firehol-ip-lists |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
