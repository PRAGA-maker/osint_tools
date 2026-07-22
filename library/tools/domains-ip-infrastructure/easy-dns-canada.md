---
id: easy-dns-canada
name: easyDNS WHOIS
description: Use when you have a `domain` and want registration metadata (registrar, dates, nameservers, and any unredacted registrant details) — returns `domain` WHOIS records, occasionally `name`/`email`.
url: https://whois.easydns.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: A free, no-account WHOIS lookup for a domain's registration record.
selectorsIn:
- domain
selectorsOut:
- domain
- name
- email
- ip-address
status: live
pricing: freemium
costNote: The WHOIS lookup at whois.easydns.com is free and needs no account; easyDNS's registrar/hosting services are separate paid products.
opsec: passive
opsecNote: WHOIS queries hit registry/registrar servers, not the domain owner, so the subject is not alerted. Standard passive recon. Do not confuse the free lookup with registering/transferring a domain (which would create an account trail).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: easyDNS is an established ICANN-accredited registrar (Canada); its WHOIS reflects authoritative registry/registrar data.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- gandi-uk
aliases:
- Easy DNS (Canada)
- whois.easydns.com
tags:
- toddington
- curated-directory
- whois-ip-lookups-website-analysis
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# easyDNS WHOIS

> A free, account-free WHOIS lookup from an established registrar — get a domain's registration record without signing up anywhere.

## When to use
You have a `domain` tied to your subject (a personal site, a business, a scam/phishing domain, a forum host) and want its registration metadata: who registered it, when, through which registrar, and its nameservers. In a missing-persons or fraud context this can link a domain to a registrant identity (when not GDPR-redacted), establish a timeline from creation/expiry dates, and cluster related domains via shared nameservers or registrant email.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://whois.easydns.com.
2. Enter the target `domain` and submit — no login required.
3. Read the record: registrar, creation/updated/expiry dates, status codes, nameservers, and any registrant/admin `name`/`email`/organisation that isn't privacy-protected.
4. Pivot: an unredacted registrant `email`/`name` feeds email- and people-search tools; shared nameservers or registrant details help cluster related domains; creation dates anchor a timeline.

## Inputs → Outputs
- **In:** `domain`
- **Out:** `domain` WHOIS record (registrar, dates, nameservers), and where unredacted `name`, `email`, organisation, `ip-address` (via nameservers)
- **Empty/negative result looks like:** most modern records are privacy/GDPR-redacted, showing only registrar + dates + "REDACTED FOR PRIVACY." That is normal — absence of a name is redaction, not absence of an owner.

## Gotchas & OpSec
- Redaction is the norm post-GDPR; personal registrant data is usually hidden behind privacy services. Historical WHOIS (paid databases) may still hold pre-redaction records.
- ccTLDs vary: some registries expose little via generic WHOIS; use the registry's own lookup for those.
- OpSec: passive — queries hit registry/registrar infrastructure, not the domain owner.

## Overlaps ("do both")
- Pairs with `[[gandi-uk]]` and other WHOIS front-ends (different services occasionally parse/expose fields differently), and with historical-WHOIS and reverse-WHOIS tools to recover redacted or clustered registrant data.

## Trust & verifiability
`trust: trusted` — easyDNS is an ICANN-accredited registrar, so the WHOIS it returns is authoritative registry/registrar data; only the completeness (redaction) limits it, not the accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | easy-dns-canada |
| category | domains-ip-infrastructure |
