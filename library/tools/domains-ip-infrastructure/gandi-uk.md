---
id: gandi-uk
name: Gandi WHOIS
description: Use when you have a `domain` and want its registration record (registrar, dates, nameservers, and any unredacted registrant details) — returns `domain` WHOIS data, occasionally `name`/`email`.
url: https://whois.gandi.net
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: A free, no-account WHOIS lookup for domain ownership and registration metadata.
selectorsIn:
- domain
selectorsOut:
- domain
- name
- email
- ip-address
status: live
pricing: freemium
costNote: The WHOIS lookup at whois.gandi.net is free and needs no account; Gandi's registrar/hosting products are separate paid services.
opsec: passive
opsecNote: WHOIS queries hit registry/registrar servers, not the domain owner, so the subject is not alerted. Standard passive recon; keep it distinct from actually registering a domain (which creates an account trail).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Gandi is a long-established ICANN-accredited registrar (France/UK); its WHOIS reflects authoritative registry/registrar data.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- easy-dns-canada
aliases:
- Gandi (UK)
- whois.gandi.net
tags:
- toddington
- curated-directory
- whois-ip-lookups-website-analysis
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# Gandi WHOIS

> A free, account-free WHOIS lookup from a major registrar — check who owns a domain and when it was registered.

## When to use
You have a `domain` connected to your subject (a personal or business site, a suspicious/phishing domain, a host of interest) and want its registration record: registrant (when unredacted), registrar, creation/expiry dates, and nameservers. In a missing-persons or fraud investigation this can attribute a domain to an identity, date its activity, and cluster related domains sharing a registrant email or nameservers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://whois.gandi.net.
2. Enter the target `domain` and submit — no account needed.
3. Read the record: registrar, creation/updated/expiry dates, status, nameservers, and any registrant/admin `name`/`email`/organisation not hidden by privacy protection.
4. Pivot: an unredacted registrant `email`/`name` feeds email- and people-search tools; shared nameservers/registrant fields help cluster domains; dates anchor a timeline.

## Inputs → Outputs
- **In:** `domain`
- **Out:** `domain` WHOIS record (registrar, dates, nameservers), and where unredacted `name`, `email`, organisation, `ip-address` (via nameservers)
- **Empty/negative result looks like:** most records are GDPR/privacy-redacted, showing only registrar + dates + "REDACTED FOR PRIVACY." That is normal redaction, not proof the domain is unowned.

## Gotchas & OpSec
- Redaction is standard post-GDPR; registrant identity is usually behind a privacy proxy. Historical-WHOIS databases may retain pre-redaction records.
- Some ccTLDs expose little through generic WHOIS; use the relevant registry's own lookup for those.
- OpSec: passive — queries touch registry/registrar servers, never the domain owner.

## Overlaps ("do both")
- Pairs with `[[easy-dns-canada]]` and other WHOIS front-ends, and with historical/reverse-WHOIS tools to recover redacted registrants and find other domains owned by the same party.

## Trust & verifiability
`trust: trusted` — Gandi is an ICANN-accredited registrar, so returned WHOIS is authoritative; only redaction limits completeness, not accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gandi-uk |
| category | domains-ip-infrastructure |
