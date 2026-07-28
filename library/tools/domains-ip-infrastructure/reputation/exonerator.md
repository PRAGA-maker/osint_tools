---
id: exonerator
name: ExoneraTor
description: Use when you have an `ip-address` and a date and want to know whether that IP was a Tor relay at the time — returns a yes/no with relay details.
url: https://exonerator.torproject.org/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- reputation
bestFor: Confirming whether a given IP was part of the Tor network (relay/exit) on a specific date.
selectorsIn:
- ip-address
selectorsOut: []
status: live
pricing: free
costNote: Free, first-party Tor Project service; no account.
opsec: passive
opsecNote: You query the Tor Project's historical relay archive, not the IP's owner — the subject is not alerted. It is a lookup against public consensus data; nothing you enter reaches the address in question.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Tor Project from its own signed consensus archives — the authoritative source for historical Tor relay membership.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- tor-browser
- tor-project
- exonerator-ip-address-checker
- tor-download
aliases:
- ExoneraTor
- Tor relay checker
tags:
- tor
- ip-reputation
- attribution
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# ExoneraTor

> The Tor Project's own archive lookup: was this IP a Tor relay on this date? The authoritative way to tell whether traffic from an address could have been anonymized Tor exit traffic rather than the address owner.

## When to use
You have an `ip-address` (from a log, an email header, an abuse report, a connection record) and a date/time, and you need to know whether that IP was running a Tor relay — especially an exit node — at that moment. This is the key disambiguation step in attribution: if the IP was a Tor exit at the time, the traffic likely belongs to an anonymous Tor user passing through, not to whoever owns the IP. It exonerates (or fails to exonerate) the address holder.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://exonerator.torproject.org/.
2. Enter the target `ip-address` and the date (UTC) you're asking about.
3. Read the result:
   - "**...was a Tor relay**" (with a fingerprint and whether it permitted exit traffic) → the address was part of the Tor network then; traffic from it may be anonymous Tor traffic.
   - "**...was not a Tor relay**" → the IP was not in the Tor consensus at that date; treat it as a normal address.
4. Pivot: a positive exit-node result usually means you cannot attribute the activity to the IP owner and should look elsewhere; a negative keeps the IP as a genuine lead.

## Inputs → Outputs
- **In:** `ip-address` + date
- **Out:** boolean Tor-relay status at that date, with relay fingerprint and exit-permission detail
- **Empty/negative result looks like:** "we did not find IP address X ... running on Y" — the IP was not a known Tor relay then; that does not rule out other anonymization (VPN, open proxy).

## Gotchas & OpSec
- Date/time matters — Tor relays come and go; always check the specific date of the activity, in UTC.
- "Not a Tor relay" only rules out Tor, not VPNs, proxies, or shared/CGNAT addresses.
- OpSec: **passive** — you query Tor's archive, not the address; nothing reaches the subject.

## Overlaps ("do both")
- Do both with a reverse-DNS/WHOIS lookup on the IP: ExoneraTor tells you whether to *distrust* the IP as attributable (Tor), while WHOIS/reverse-DNS characterises the address when it is a genuine, non-Tor lead.

## Trust & verifiability
`trust: trusted` — a first-party Tor Project service built on the network's own signed consensus archives. It is the authoritative record of historical relay membership; results can be cited directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | exonerator |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
