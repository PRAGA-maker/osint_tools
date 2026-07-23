---
id: intodns-ai
name: intoDNS.ai
description: Use when you have a `domain` and want a deterministic health check of its DNS and email security posture — SPF, DKIM, DMARC, DNSSEC, MTA-STS, BIMI, FCrDNS, blacklists — returns config findings and issues.
url: https://intodns.ai
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: One-shot DNS + email-security audit of a domain (SPF/DKIM/DMARC/DNSSEC/MTA-STS/blacklists).
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free forever for the public web tools; an optional API/monitoring tier exists but basic scans need no key or account.
opsec: passive
opsecNote: Passive from your side — you query intoDNS.ai, which resolves the domain's public DNS records; it does not contact the target's users and sends no notification. It reads published DNS/mail configuration, all of which is public data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A modern successor to the classic intoDNS check; runs deterministic, standards-based checks (references internet.nl-style methodology) whose results are reproducible with dig.
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
- intoDNS
- intodns.ai
tags:
- dns
- email-security
- spf-dkim-dmarc
- domain-health
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# intoDNS.ai

> A free, deterministic DNS and email-security health checker: SPF, DKIM, DMARC, DNSSEC, MTA-STS, BIMI, FCrDNS, blacklists and web-security signals for a domain.

## When to use
You have a `domain` and want to understand its DNS and mail configuration — is email authentication (SPF/DKIM/DMARC) set up, is DNSSEC enabled, is the domain on any blacklists, what nameservers and mail hosts does it use. Useful for profiling an organization's technical hygiene, spotting spoofable domains, or fingerprinting infrastructure during an investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://intodns.ai and enter the `domain`.
2. Run the scan and read the section-by-section report: NS/DNS config, SPF, DKIM, DMARC, DNSSEC, MTA-STS, BIMI, reverse DNS (FCrDNS), blacklist status.
3. Note pass/warn/fail flags — e.g. missing DMARC (spoofable), no DNSSEC, blacklisted mail IP.
4. Cross-check any finding with `dig`/`nslookup` since all inputs are public DNS records.
5. Pivot: mail hosts and nameservers reveal hosting/provider; a spoofable domain is a phishing-risk signal.

## Inputs → Outputs
- **In:** `domain`
- **Out:** DNS + email-security findings, nameservers, mail hosts, resolved `ip-address`es, blacklist status
- **Empty/negative result looks like:** a domain that doesn't resolve returns errors, not a report — verify the domain is live/correctly spelled first.

## Gotchas & OpSec
- Reads only published DNS/mail records — it can't see internal or private config.
- "Fail"/"warn" flags reflect best-practice standards; a warning isn't necessarily a compromise.
- Results are point-in-time; DNS changes propagate, so re-scan if timing matters.

## Overlaps ("do both")
- Pairs with WHOIS and certificate-transparency tools — intoDNS.ai covers DNS/mail posture while those cover registration and issued certs; together they profile a domain's full footprint.

## Trust & verifiability
`trust: community` — a modern, standards-based DNS checker; every finding is reproducible with `dig`, so results are easy to independently confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | intodns-ai |
