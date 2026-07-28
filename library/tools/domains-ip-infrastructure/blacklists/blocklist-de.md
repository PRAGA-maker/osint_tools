---
id: blocklist-de
name: Blocklist.de
description: Use when you have an `ip-address` and want to know whether it has been reported for attacks (SSH, mail, web) — returns blacklist status and the attack types logged.
url: https://www.blocklist.de/en/index.html
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- blacklists
bestFor: Checking whether an IP is on a community attack-reporting blocklist and what it was flagged for.
selectorsIn:
- ip-address
selectorsOut:
- ip-address
status: live
pricing: free
costNote: Free voluntary abuse-reporting service; an account is only needed to SUBMIT reports, never to look up an IP.
opsec: passive
opsecNote: Lookups query Blocklist.de's own database and DNSBL, not the target host — no packets are sent to the subject IP, so this is passive. Still run it from a sock-puppet session as a habit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-run German abuse-reporting network, widely used as a DNSBL. Entries are attacker-reported, so treat a hit as a reputation signal, not proof of identity.
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
- blocklist.de
tags:
- blacklist
- ip-reputation
- dnsbl
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# Blocklist.de

> A free community DNSBL/abuse feed that answers one question about an IP: has it been reported attacking servers, and how?

## When to use
You have an `ip-address` — pulled from email headers, a log, a chat metadata leak, or a WHOIS/hosting record — and want a quick reputation read: is it a known bad/attacking host, or clean? A hit tells you the IP has been reported for SSH brute-forcing, mail abuse, web exploits, botnet or DDoS activity, which helps you tell an ordinary residential/subject IP from shared attack/proxy infrastructure.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.blocklist.de/en/index.html and go to the **Search (IP, ASN)** section.
2. Enter the target `ip-address` (or an AS-Number to check a whole network) and submit.
3. Read the response:
   - **Listed** — the page shows the report count and the attack categories logged (ssh, mail, apache, ftp, sip/voip, bots, etc.), often with last-seen timestamps.
   - **Not listed** — no reports; the IP is clean in this dataset (which is not the same as "never malicious").
4. For automation, the same data is available via their Search/GET API and DNS (RBL) service — query `<reversed-ip>.bl.blocklist.de`.
5. Pivot: a listed IP argues the address is shared/abused infrastructure rather than a person's own line; cross-check with a passive-DNS or IP-reputation tool before attributing it to the subject.

## Inputs → Outputs
- **In:** `ip-address` (or ASN)
- **Out:** blacklist status + attack-type categories and report counts (reputation metadata on the same `ip-address`)
- **Empty/negative result looks like:** "not listed" / zero reports — no evidence of attack activity here; do not read it as confirmation the IP is residential or belongs to your subject.

## Gotchas & OpSec
- Data is **attacker-reported** — false positives happen (shared NAT, compromised-then-cleaned hosts). One list is never enough; corroborate.
- Human-in-the-loop: none for lookups; account/registration is only for submitting your own attack reports.
- OpSec: passive — you query Blocklist.de, not the subject IP. Nothing reaches the target.

## Overlaps ("do both")
- Pair with a broader IP-reputation/geolocation lookup — Blocklist.de tells you *whether it attacked*, those tell you *where and whose network it is*.

## Trust & verifiability
`trust: community` — a long-standing volunteer abuse network, credible as a DNSBL but not an identity source; every hit is community-submitted and should be treated as a lead.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | blocklist-de |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
