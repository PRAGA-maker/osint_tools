---
id: exonerator-ip-address-checker
name: ExoneraTor (Tor relay IP checker)
description: Use when you have an `ip-address` and a date and want to know whether that IP was a Tor relay at that time — returns a yes/no that reframes what an IP in your logs means.
url: https://metrics.torproject.org/exonerator.html
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Confirming whether a specific IP was running as a Tor relay/exit on a specific date.
selectorsIn:
- ip-address
selectorsOut: []
status: live
pricing: free
costNote: Free official Tor Project service; no account.
opsec: passive
opsecNote: Passive query against the Tor Project's historical relay archive; you disclose only the IP/date you look up, nothing to any subject. No sock puppet needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Tor Project from its own historical consensus/relay data; authoritative for whether an IP was a listed Tor relay at a given time.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- exonerator
- tor-browser
- tor-project
- tor-download
aliases:
- ExoneraTor
tags:
- tor
- ip-analysis
- attribution
source: toddington-resources
lastVerified: '2026-07-28'
enrichment: full
---

# ExoneraTor (Tor relay IP checker)

> The Tor Project's historical lookup: was this IP address a Tor relay on this date? A yes changes how you interpret an IP found in logs — it may be an anonymised exit, not the actual origin.

## When to use
You have an `ip-address` (from server logs, an email header, an abuse report, a login record) and a date, and you need to know whether that address was a Tor relay/exit at that time. If it was, the IP is very likely just a Tor exit node — it does **not** identify the real user, and you should stop treating it as the origin. If it wasn't, the IP is a normal lead you can attribute. It's a crucial "don't chase the wrong IP" check.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://metrics.torproject.org/exonerator.html.
2. Enter the `ip-address` and the date of the event.
3. Read the verdict: whether a Tor relay was running at that IP on that date (and its role/exit status).
4. Interpret: a match means the IP is an anonymising node — redirect the investigation away from the IP as an identity. No match means treat it as a normal IP lead.
5. Pivot: for a non-Tor IP, proceed with WHOIS/geolocation/`[[hurricane-electric-bgp-toolkit]]`; for a Tor exit, pivot to other selectors entirely.

## Inputs → Outputs
- **In:** an `ip-address` + a date
- **Out:** whether that IP was a listed Tor relay/exit at that time (no person-level `selectorsOut`)
- **Empty/negative result looks like:** "no Tor relay found" for that IP/date — the address was not a public Tor relay then; treat it as an ordinary IP (note it doesn't rule out other VPN/proxy anonymisation).

## Gotchas & OpSec
- OpSec: passive; only your IP/date query is disclosed.
- Date-sensitive: relays change constantly — always check the exact event date, not "now."
- A "no" only rules out *Tor relays*; the IP could still be a VPN/proxy or bridge that isn't in the public relay list.

## Overlaps ("do both")
- Do both with WHOIS/geolocation/BGP tools — ExoneraTor tells you whether the IP is even worth attributing; if it's not Tor, those tools do the attribution.

## Trust & verifiability
`trust: trusted` — first-party Tor Project data from historical relay consensus; authoritative for the Tor-relay question.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | exonerator-ip-address-checker |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | ip-address → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
