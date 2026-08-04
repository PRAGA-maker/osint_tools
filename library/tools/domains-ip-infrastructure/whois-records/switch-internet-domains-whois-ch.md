---
id: switch-internet-domains-whois-ch
name: SWITCH Internet Domains Whois (.ch)
description: Use when you have a `.ch`/`.li` `domain` and want registry ownership data — returns registrar, nameservers, status and dates from Switzerland's official registry.
url: https://www.nic.ch/whois/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- whois-records
bestFor: Authoritative WHOIS for Swiss (.ch) and Liechtenstein (.li) domains straight from the SWITCH registry.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free official registry WHOIS; no account. Registrant personal data is withheld for privacy under Swiss rules.
opsec: passive
opsecNote: Queries SWITCH's own registry database, not the target's server, so it does not alert the domain holder. Passive. A captcha may appear.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: SWITCH is the official registry operator for .ch and .li; this is the authoritative source for those TLDs.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- SWITCH WHOIS
- nic.ch whois
tags:
- whois-records
- ccTLD
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# SWITCH Internet Domains Whois (.ch)

> The official registry WHOIS for Swiss (.ch) and Liechtenstein (.li) domains — authoritative registration data, straight from SWITCH.

## When to use
You have a `.ch` or `.li` `domain` and want registry-authoritative details: registrar, nameservers, status, and creation/expiry dates. Generic WHOIS services often return incomplete data for these TLDs, so query the registry directly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.nic.ch/whois/.
2. Enter the `.ch`/`.li` domain and submit (solve the captcha if shown).
3. Read the registrar, nameservers, status, and dates.
4. Pivot the nameservers/hosting into passive DNS and the registrar into further research — but note registrant identity is privacy-withheld under Swiss law.

## Inputs → Outputs
- **In:** a `.ch` or `.li` `domain`
- **Out:** registrar, nameservers, status, creation/expiry dates
- **Empty/negative result looks like:** "domain not found" (unregistered) — and note that registrant name/contact is deliberately NOT shown for privacy, so absence of a name is normal here.

## Gotchas & OpSec
- Human-in-the-loop: a **captcha** may appear — solve it manually.
- OpSec: passive — you query the registry, not the domain's server.
- Swiss privacy law withholds registrant personal data, so this gives infrastructure facts, not an owner's identity — combine with historical WHOIS and hosting pivots.

## Overlaps ("do both")
- Complements historical-WHOIS and passive-DNS tools: the registry gives the current authoritative record; history/DNS tools surface the person or network behind a privacy-masked domain.

## Trust & verifiability
`trust: trusted` — the official .ch/.li registry; the authoritative source for these ccTLDs.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | switch-internet-domains-whois-ch |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
