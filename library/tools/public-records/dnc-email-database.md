---
id: dnc-email-database
name: DNC email database
description: Use when you have a `name`, `email`, or organisation and want to check whether they appear in the 2016 WikiLeaks DNC email leak — returns matching emails, sender/recipient addresses, and dates.
url: https://wikileaks.org/dnc-emails/
category: public-records
path:
- public-records
bestFor: Full-text searching the 2016 DNC email leak for a person's correspondence, addresses, and associates.
selectorsIn:
- name
- email
- employer-org
selectorsOut:
- email
- name
- associate
status: live
pricing: free
costNote: Free public WikiLeaks archive; no account, key, or payment required.
opsec: passive
opsecNote: Reading a public WikiLeaks archive is passive and does not touch the target, but the host is politically sensitive and may be logged/blocked on some networks — use a sock-puppet browser (WikiLeaks itself recommends Tor). The data is stolen correspondence, so weigh legal/ethical exposure before relying on it in a report.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Primary-source email dump published by WikiLeaks; the messages are widely regarded as authentic (several corroborated in litigation and reporting), but WikiLeaks is a partisan publisher, so treat individual attributions as needing corroboration.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- akp-email-database
- gi-files
- ice-patrol
- leaked-cables
- macron-campaign-emails
- sony-archives
- wikileaks
- wikileaks-search
aliases:
- WikiLeaks DNC emails
- DNC email leak 2016
tags:
- wikileaks
- leaked-emails
- breach-data
source: osint4all
lastVerified: '2026-07-22'
enrichment: full
---

# DNC email database

> The searchable WikiLeaks archive of ~44,000 leaked Democratic National Committee emails (2016) — a full-text corpus for finding a person's correspondence, contact addresses, and network.

## When to use
You are researching someone plausibly connected to US Democratic Party politics, staff, donors, contractors, or media circa 2015–2016, and you want to know whether they appear in the DNC leak. A hit can surface the subject's real email address, who they wrote to, dates and topics of correspondence, and named associates — corroborating identity, employer, and relationships that are hard to get elsewhere.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://wikileaks.org/dnc-emails/ in a sock-puppet browser.
2. Use the search box: enter the target's `name`, a known `email`, an `employer-org`, or a keyword. Use the advanced filters to narrow by sender, recipient, or date range.
3. Open individual messages to read full headers (From/To/CC), subject, date, body, and any attachment filenames.
4. Extract selectors: capture the confirmed `email` addresses, the display `name`, and every co-recipient as a candidate `associate`.
5. Pivot: run recovered email addresses through email-verification and breach tools, and cross-check the same person against the sibling WikiLeaks corpora ([[akp-email-database]], [[sony-archives]], [[macron-campaign-emails]]).

## Inputs → Outputs
- **In:** `name`, `email`, or `employer-org` / keyword
- **Out:** matching `email` messages with sender/recipient addresses, dates, subjects; the subject's `name`; co-recipients as `associate` leads
- **Empty/negative result looks like:** "no results" for the query — the person/term isn't in this specific 2016 DNC corpus; it says nothing about other leaks or their broader footprint.

## Gotchas & OpSec
- Scope is narrow and frozen: a single 2016 dump about one organisation. Absence means nothing beyond this corpus.
- Names and addresses can be spoofed within emails; verify a claimed address independently before attributing it to your subject.
- Politically charged, stolen data — some networks block WikiLeaks and courts/employers may view reliance on it critically; document provenance and corroborate.

## Overlaps ("do both")
- Pairs with [[wikileaks-search]] and the sibling leak archives ([[akp-email-database]], [[gi-files]], [[leaked-cables]], [[sony-archives]]) — search the same person across every corpus, because each leak covers a different organisation and time window.

## Trust & verifiability
`trust: community` — a primary-source dump hosted by a partisan publisher; the email set is broadly accepted as authentic and is directly readable, but individual claims inside the mails still need independent corroboration before they go in a report.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dnc-email-database |
| category | public-records |
| selectorsIn → selectorsOut | name, email, employer-org → email, name, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
