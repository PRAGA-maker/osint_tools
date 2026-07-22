---
id: whoisds-com
name: WhoisDS.com
description: Use when you want the list of domains newly registered on a given day (to catch a subject's or scammer's fresh domains) — returns downloadable lists of new `domain`s plus WHOIS lookups.
url: http://whoisds.com/newly-registered-domains
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Downloading daily lists of newly registered domains and running individual WHOIS lookups to catch fresh infrastructure.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Daily newly-registered-domain lists and basic WHOIS are free (with quotas/limits); bulk downloads, larger history and API access are paid.
opsec: passive
opsecNote: Downloading published new-domain lists and running WHOIS is passive — you query WhoisDS' data and registry records, not the target host. Registrant PII is largely GDPR-redacted; correlate on dates/patterns rather than expecting names.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A domain-data aggregator; the newly-registered lists are compiled from zone files, useful but best cross-checked against a registry or second source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- WhoisDS
- newly registered domains list
tags:
- Domain/IP/Links
- Databases of domains
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
---

# WhoisDS.com

> A source for daily lists of newly registered domains plus WHOIS lookups — used to spot fresh domains as they appear (a scammer's new site, a subject's just-registered project).

## When to use
You're tracking newly created infrastructure: phishing/scam domains spun up around an event, or a subject who just registered a domain. WhoisDS publishes a downloadable list of domains registered each day, which you can grep for keywords/brands/names, and lets you run WHOIS on any single domain to see registrar and (where not redacted) registration details.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://whoisds.com/newly-registered-domains and pick a date to download that day's new-domain list (free, with limits).
2. Search the list for keywords — a brand, a surname, a project name — to surface relevant fresh registrations.
3. Run WHOIS on a domain of interest via the site to get registrar, creation date, and any non-redacted registrant/name-server data.
4. Repeat across consecutive days to catch a campaign or a pattern of registrations.
5. Pivot: name servers, registrar, and creation timing feed DNS-history tools like `[[securitytrails]]` and hosting/passive-DNS pivots.

## Inputs → Outputs
- **In:** a date (for the new-domain list) or a `domain` (for WHOIS)
- **Out:** list of newly registered `domain`s; WHOIS record (registrar, dates, name servers, redacted registrant)
- **Empty/negative result looks like:** a keyword that matches nothing in a day's list just means no such domain was registered that day — check adjacent dates; a WHOIS with all-redacted contacts is normal post-GDPR, not a failure.

## Gotchas & OpSec
- Free access is quota-limited; bulk/historical lists and API need a paid plan.
- Registrant names/emails are mostly GDPR-redacted — rely on creation dates, name servers and hosting to correlate, not on personal contact fields.
- List completeness varies by TLD (some ccTLDs aren't covered) — cross-check for critical work.

## Overlaps ("do both")
- Pairs with `[[securitytrails]]` and certificate-transparency monitors — WhoisDS flags the domain the day it's born; those then reveal its DNS history and TLS certificates as it comes online.

## Trust & verifiability
`trust: community` — an aggregator compiling zone-file data; the new-domain lists are convenient but best corroborated against a registry or a second passive-DNS source for high-stakes work.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whoisds-com |
