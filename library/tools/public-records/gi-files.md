---
id: gi-files
name: GI Files
description: Use when you have a `name`/`email` possibly tied to Stratfor's 2004–2011 intelligence emails and want mentions or correspondence — returns matching leaked emails.
url: https://search.wikileaks.org/gifiles/
category: public-records
path:
- public-records
bestFor: Full-text searching WikiLeaks' 5M+ Stratfor "Global Intelligence Files" emails for a name, address, or topic.
selectorsIn:
- name
- email
selectorsOut:
- email
- associate
- employer-org
status: live
pricing: free
costNote: Free public WikiLeaks archive; no account or payment.
opsec: passive
opsecNote: Searching runs server-side on WikiLeaks' host; your query and IP hit their infrastructure. WikiLeaks is a sensitive/monitored domain — use a sock-puppet browser and consider Tor/VPN. You are only reading a published archive; nothing reaches the people named in it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Authentic WikiLeaks publication of Stratfor's leaked emails; the archive is genuine, but individual email *claims* are Stratfor staff opinions/rumor, not verified fact.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- wikileaks
- wikileaks-search
- leaked-cables
- akp-email-database
- dnc-email-database
- ice-patrol
- macron-campaign-emails
- sony-archives
tags:
- wikileaks
- leaks
- email-search
source: osint4all
lastVerified: '2026-07-16'
enrichment: full
---

# GI Files

> WikiLeaks' searchable archive of 5+ million Stratfor emails (2004–2011) — a full-text corpus where a subject's name, email, or affiliation may appear in private intelligence-firm correspondence.

## When to use
You have a `name`, `email`, or organization that might surface in the private-intelligence world of the 2000s–2011: sources, analysts, corporate/government contacts, or people Stratfor was reporting on. The GI Files let you full-text search that correspondence for mentions, contact details, and relationship threads.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the search page in a sock-puppet browser (consider Tor/VPN given the domain).
2. Enter your query — it supports search across the whole email, plus filters for From/To addresses, subject, attachment filename, email ID, and date range, with boolean AND/OR/NOT and phrase/proximity operators.
3. Sort results by relevance/date/sender and open individual emails.
4. Read: each hit shows sender, recipients, date, subject, and body — mine for a subject's `email`, named `associate`s, and `employer-org` affiliations.
5. Pivot: recovered email addresses feed email-OSINT; named associates feed link analysis; dates anchor a timeline.

## Inputs → Outputs
- **In:** `name`, `email`, keyword, or organization
- **Out:** matching emails exposing `email` addresses, `associate` relationships, `employer-org` ties, dates
- **Empty/negative result looks like:** zero results — the selector doesn't appear in the Stratfor corpus (a narrow 2004–2011 window; absence means nothing about the wider world).

## Gotchas & OpSec
- Scope is narrow: only Stratfor emails through Dec 2011 — irrelevant to anyone outside that orbit or timeframe.
- Content reliability: emails contain rumor, speculation, and unverified source claims — treat any assertion as a lead to corroborate, not fact.
- OpSec: WikiLeaks is a monitored domain; browse with a persona and network hygiene.
- Legal/ethical: this is leaked private correspondence — handle per your engagement's rules.

## Overlaps ("do both")
- Pairs with `[[wikileaks-search]]` and `[[leaked-cables]]` — run the same selector across WikiLeaks' other corpora (Cablegate, other leaks) since GI Files only covers Stratfor.

## Trust & verifiability
`trust: community` — the archive is an authentic WikiLeaks publication (the *documents* are real), but the *content* is a private firm's internal chatter, so verify any factual claim independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gi-files |
| category | public-records |
| selectorsIn → selectorsOut | name, email → email, associate, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
