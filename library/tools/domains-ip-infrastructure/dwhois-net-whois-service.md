---
id: dwhois-net-whois-service
name: Dwhois.net Whois Service
description: Use when you have a domain and want its registration/ownership record across many TLDs — returns registrant contacts, associated domains, and name-server infrastructure.
url: http://dwhois.net
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Quick, no-CAPTCHA WHOIS lookups across a wide range of gTLDs and ccTLDs.
selectorsIn:
- domain
selectorsOut:
- domain
- email
- name
- address
status: live
pricing: free
costNote: Free web WHOIS lookup; no account or payment.
opsec: passive
opsecNote: WHOIS queries go through Dwhois's servers to the relevant registry; the domain owner is not notified. As with any third-party WHOIS front-end, the operator can log what you look up — use a clean browser for sensitive targets.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Small independent WHOIS front-end; it relays registry data but is not an authoritative registrar. Confirm anything critical against the registry or an official RDAP/WHOIS source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- dwhois
- dwhois.net
tags:
- domains-ip-infrastructure
- whois
- domain-registration
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Dwhois.net Whois Service

> A no-frills, CAPTCHA-free WHOIS front-end covering a broad set of TLDs — enter a domain, get whatever registration record the registry still exposes.

## When to use
You have a `domain` tied to a subject (from an email address, a website, or a social bio) and want the registration record: who registered it, when, through which registrar, and on which name servers. Registrant contacts and shared infrastructure can link a domain back to a `name`, `email`, or `address`, and to other domains the same party controls.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://dwhois.net and enter the domain (it supports .com/.org plus many ccTLDs like .co.uk, .jp).
2. Read the returned WHOIS record: registrar, creation/expiry dates, registrant/admin contacts (where not privacy-masked), and name servers.
3. Note pivotable fields — a registrant `email` or `name`, an organization, a physical `address`, or a distinctive name-server pair.
4. Pivot: run the registrant email through email-OSINT; use the name servers or a registrant email in a reverse-WHOIS tool to find other domains by the same owner. Corroborate any hit against official RDAP.

## Inputs → Outputs
- **In:** `domain`
- **Out:** `domain` (registrar/status), `email`, `name`, `address` (registrant/admin contacts, where exposed)
- **Empty/negative result looks like:** a record fully behind WHOIS privacy/GDPR redaction (contacts show as "REDACTED FOR PRIVACY" or a privacy-service proxy), or "no match for domain" for an unregistered/unsupported TLD — increasingly common, so absence of contacts is normal, not a bug.

## Gotchas & OpSec
- Human-in-the-loop: none — the operator advertises no CAPTCHA.
- OpSec: passive; the domain owner is not alerted. A third-party WHOIS proxy can log your queries, so use a clean browser for sensitive lookups.
- Post-GDPR, most gTLD registrant details are redacted; treat a privacy-masked record as expected and pivot to historical WHOIS or RDAP where richer data may survive.

## Overlaps ("do both")
- Pairs with reverse-WHOIS and historical-WHOIS tools — Dwhois gives the current live record, while those surface prior unmasked contacts and other domains registered by the same party.

## Trust & verifiability
`trust: unverified` — it is a small third-party relay of registry data, not an authoritative source; verify any actionable field against official RDAP/registry WHOIS.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dwhois-net-whois-service |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, email, name, address |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
