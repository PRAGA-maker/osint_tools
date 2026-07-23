---
id: whoxy
name: Whoxy
description: Use when you have a `name`, `email`, or `domain` and want linked domains via WHOIS history — returns reverse-WHOIS matches and a domain's registration-change timeline.
url: https://www.whoxy.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Reverse-WHOIS (find domains registered by a name/email/org) and viewing a domain's historical WHOIS records.
selectorsIn:
- name
- email
- domain
selectorsOut:
- domain
- email
- name
status: live
pricing: freemium
costNote: Free live-WHOIS and limited previews on the site; reverse-WHOIS, WHOIS history, and bulk/API access are cheap paid credits (not a full free tier).
opsec: passive
opsecNote: "Whoxy answers from its own WHOIS database, so you never query the registrar or target directly — passive and invisible to the subject. Your searches are tied to your Whoxy account/API key; use a sock-puppet account. Registrant data is only present where WHOIS privacy wasn't enabled, and historical records may expose details later redacted."
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: web-manual
trust: community
trustNote: An established commercial WHOIS-data provider with a large historical database; coverage is good for gTLDs but patchy for privacy-protected and some ccTLD domains.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools: []
aliases:
- Whoxy
- whoxy.com
tags:
- whois
- reverse-whois
- domain-history
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Whoxy

> A WHOIS-history and reverse-WHOIS service: find every domain registered under a name/email/organization, and see how a single domain's registration details changed over time.

## When to use
You have a registrant `name`, `email`, or organization and want their other `domain`s (reverse WHOIS), or you have a `domain` and want its **historical** WHOIS records — the registrant details from before privacy protection was switched on. This is a core pivot for tying a person/org to their web infrastructure. Infrastructure/attribution work, so low direct missing-persons relevance, though an old WHOIS record can leak a real name, email, phone, or address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.whoxy.com/ and try a free live-WHOIS lookup on a `domain`.
2. For **reverse WHOIS**, search a `name`/`email`/company to list domains registered with those details (paid credits/API).
3. For **WHOIS history**, pull a domain's past records to catch details redacted in the current record.
4. Read the output: registrant `name`/`email`, other `domain`s, and change dates.
5. Pivot a discovered `email`/`name` into people/breach search; corroborate co-registration before asserting common ownership.

## Inputs → Outputs
- **In:** `name`, `email`, or `domain`
- **Out:** related `domain`s, registrant `name`/`email`, historical registration timeline
- **Empty/negative result looks like:** no matches or only privacy-proxy records ("WhoisGuard", "Domains By Proxy") — the registrant used WHOIS privacy or a ccTLD Whoxy doesn't cover; absence isn't proof the person owns no domains.

## Gotchas & OpSec
- Post-GDPR, current WHOIS is heavily redacted — the value is in **historical** records from before privacy/GDPR; recent registrations often show only a proxy.
- Reverse-WHOIS and history need paid credits (cheap, but not free); the free site is mostly live lookups.
- A shared registrant email/proxy can group unrelated domains — weight the link by how specific the shared detail is.

## Overlaps ("do both")
- Pairs with WHOIS-history siblings and passive-DNS like [[dns-dumpster]] and reverse-IP [[whoismind]] — Whoxy links domains by *registrant*, passive-DNS/reverse-IP link them by *infrastructure*; combine to separate real ownership from coincidence.

## Trust & verifiability
`trust: community` — a solid commercial WHOIS-data provider; records are real registrar data (authoritative where present), so verify a co-ownership claim by checking the specific shared detail across the historical records, not just the count.
