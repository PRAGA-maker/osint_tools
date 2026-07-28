---
id: ewhois
name: Ewhois
description: Use when you have a `domain` and want registration, DNS, hosting and traffic analytics in one panel — returns registrant email/name, IP, and related infrastructure.
url: https://www.ewhois.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- analytics
bestFor: One-stop WHOIS plus DNS, subdomain, SSL and traffic-analytics panel for a domain.
selectorsIn:
- domain
selectorsOut:
- ip-address
- email
- name
- domain
status: live
pricing: free
costNote: Free browser lookups; an optional free account only unlocks saved searches/favorites, not the core data.
opsec: passive
opsecNote: You query eWhois's own servers, not the target's infrastructure, so the subject is not alerted. eWhois relays public WHOIS/DNS and SimilarWeb data; use a clean browser if you don't want the lookup tied to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Independent commercial aggregator; data mirrors registry WHOIS and SimilarWeb, so verify anything decisive against an authoritative source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- eWhois
- ewhois.com
tags:
- whois
- domain-analytics
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# Ewhois

> A WHOIS lookup that bundles DNS, subdomain, SSL and traffic analytics on one page — a fast first pass on any domain tied to a subject.

## When to use
You have a `domain` (a personal site, a small business, a domain named in a listing or profile) and want a quick, consolidated read: who registered it, when, on what registrar and IP, what subdomains and SSL posture it has, and roughly how much traffic it gets. It is a triage tool — one query surfaces the pivot points (registrant `email`/`name` if unredacted, hosting `ip-address`) you then chase in dedicated tools.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.ewhois.com/ in a browser (a clean/sock-puppet session if you don't want the lookup associated with you).
2. Enter the target `domain` in the search box and submit.
3. Read the panel:
   - **Registration** — registrar, creation/expiry dates, and registrant `name`/`email` when not privacy-masked.
   - **DNS / hosting** — nameservers and the hosting `ip-address`, plus detected subdomains.
   - **Analytics** — SSL/security headers and SimilarWeb-derived traffic estimates.
4. Pivot: feed the hosting `ip-address` into a reverse-IP tool to find co-hosted domains; feed a registrant `email`/`name` into email- and name-search tools.

## Inputs → Outputs
- **In:** `domain`
- **Out:** `ip-address`, `email`, `name`, `domain` (subdomains / related domains)
- **Empty/negative result looks like:** "no data" or a WHOIS record where registrant fields read `REDACTED FOR PRIVACY` / a WHOIS-privacy proxy — the domain exists but ownership is shielded; fall back to historical WHOIS.

## Gotchas & OpSec
- Most consumer domains now use WHOIS privacy, so the registrant `name`/`email` are frequently masked — absence of a name is not proof of anything.
- Traffic numbers are SimilarWeb estimates, not measured; treat as rough scale only.
- OpSec: **passive** — you hit eWhois, not the subject's server, so no alert reaches the target. No account is needed for the core lookup.

## Overlaps ("do both")
- Do both with a reverse-IP lookup: eWhois hands you the hosting `ip-address`, and a reverse-IP tool turns that IP into the full list of co-hosted domains that eWhois's single-domain view won't show.

## Trust & verifiability
`trust: unverified` — a commercial aggregator mirroring registry WHOIS, DNS and SimilarWeb data. The raw WHOIS/DNS is authoritative; the analytics are estimates. Confirm anything case-critical against the registry or an authoritative WHOIS.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ewhois |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → ip-address, email, name, domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
