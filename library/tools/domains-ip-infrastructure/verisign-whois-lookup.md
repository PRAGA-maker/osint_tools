---
id: verisign-whois-lookup
name: Verisign WHOIS Lookup
description: Use when you have a `.com`/`.net` `domain` and want the authoritative registry record — returns the registrar of record, registration/expiry dates, nameservers, and domain status.
url: https://www.verisign.com/en_US/whois/index.xhtml
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Getting the authoritative registry-level WHOIS (registrar, dates, nameservers) for a .com or .net domain.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free public WHOIS provided by Verisign, the registry operator for .com and .net; no account, no payment, generous manual-lookup use.
opsec: passive
opsecNote: A WHOIS query goes to Verisign's registry, not to the domain owner, so the target is not notified. It reveals nothing about you beyond a standard lookup. Registrant contact details are typically redacted/at the registrar, not exposed here.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Verisign is the official registry operator for .com/.net; this is the authoritative source for thin registry data on those TLDs, not a third-party scraper.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- lookup-icann-org
- godaddy-whois-lookup
- easywhois
- who-is
aliases:
- Verisign WHOIS
- webwhois.verisign.com
- Verisign Whois Lookup
tags:
- toddington
- whois-ip-lookups-website-analysis
- domain-registration
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Verisign WHOIS Lookup

> The registry operator's own WHOIS for `.com` and `.net`: the authoritative record of which registrar holds a domain, when it was registered/expires, and its nameservers.

## When to use
You have a `.com` or `.net` `domain` and want ground-truth registry data — the sponsoring registrar, the creation/updated/expiry dates, the current nameservers, and the domain's EPP status codes (e.g. `clientHold`, `pendingDelete`). Because Verisign *is* the registry for those TLDs, its answer is authoritative for the "thin" fields and tells you where to go next: the sponsoring registrar's own WHOIS for any registrant details.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.verisign.com/en_US/whois/ (the tool lives at webwhois.verisign.com).
2. Enter the `.com`/`.net` domain and submit.
3. Read the registry record: sponsoring registrar, registrar WHOIS server/URL, creation/updated/expiry dates, nameservers, and status codes.
4. For registrant contact data, follow the "Registrar WHOIS Server" to that registrar's WHOIS (Verisign's thin registry does not carry contacts).
5. Pivot: nameservers hint at the hosting/DNS provider; the registrar and dates anchor a domain-history timeline; feed the domain to full-history WHOIS and infrastructure tools.

## Inputs → Outputs
- **In:** `domain` (must be `.com` or `.net`)
- **Out:** `domain` — sponsoring registrar, registrar WHOIS pointer, registration/updated/expiry dates, nameservers, EPP status codes
- **Empty/negative result looks like:** "No match for domain" — the name is unregistered/available, or you queried a TLD Verisign doesn't run (e.g. `.org`, `.io`); use ICANN's lookup or the correct registry for those.

## Gotchas & OpSec
- Thin registry only: Verisign's WHOIS for .com/.net does not include registrant name/email — those live at the sponsoring registrar (and are usually redacted post-GDPR/privacy). This tool tells you *which* registrar to ask.
- TLD scope: authoritative only for the TLDs Verisign operates (.com, .net, plus .cc/.tv/.name); other TLDs return no match.
- OpSec: fully passive; a WHOIS lookup never touches the domain owner.

## Overlaps ("do both")
- Pairs with `[[lookup-icann-org]]` (ICANN's registry-agnostic lookup) and registrar-side tools `[[godaddy-whois-lookup]]`, `[[easywhois]]`, `[[who-is]]` — use Verisign for the authoritative registry facts, then a full/historical WHOIS for registrant leads.

## Trust & verifiability
`trust: trusted` — this is the registry operator's first-party WHOIS, the definitive source for .com/.net registry fields; no third-party data-quality risk on the fields it returns.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | verisign-whois-lookup |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
