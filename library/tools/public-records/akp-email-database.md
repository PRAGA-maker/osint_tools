---
id: akp-email-database
name: AKP Emails (WikiLeaks)
description: Use when you have a `name`, `email`, or keyword tied to Turkey's AKP party and want leaked emails — returns messages, senders/recipients, and attachments.
url: https://wikileaks.org/akp-emails/
category: public-records
path:
- public-records
bestFor: Searching ~400k leaked emails from Turkey's ruling AKP party by sender, recipient, keyword, or attachment.
selectorsIn:
- name
- email
selectorsOut:
- email
- name
- associate
status: live
pricing: free
costNote: Free and public; WikiLeaks hosts the searchable interface with no account.
opsec: passive
opsecNote: Read-only search of a public archive. Queries hit WikiLeaks' servers; on a monitored network, accessing a politically sensitive leak may itself be notable, so use a clean browser/VPN. Do not download and redistribute unredacted personal data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Hosted by WikiLeaks; the corpus is genuine leaked material but individual message authenticity/context is unverified and politically charged.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- dnc-email-database
- gi-files
- leaked-cables
- macron-campaign-emails
- sony-archives
- wikileaks
- wikileaks-search
aliases:
- AKP emails
- akparti.org.tr leak
tags:
- leaks
- email-leak
- wikileaks
source: osint4all
lastVerified: '2026-07-22'
enrichment: full
---

# AKP Emails (WikiLeaks)

> A searchable dump of ~400,000 emails from the akparti.org.tr domain (Turkey's ruling AKP party, 2010 onward) — a targeted corpus for tracing people and correspondence in that network.

## When to use
You have a `name`, an `email` address, or a keyword connected to the Turkish AKP party, its officials, or associated organisations, and you want to find their actual correspondence. Because the archive is fully indexed, you can pull every message to/from a given address, find who a person emailed, and recover attachments — useful for mapping `associate` relationships and confirming an email belongs to a specific individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://wikileaks.org/akp-emails/ and use the search box.
2. Search by keyword in body/subject, by `email` in the From/To fields, by attachment filename, or by date range; use the include/exclude subject filters to cut spam and duplicates.
3. Open a matching message for full headers (sender, recipients, CC), body, and attachments.
4. Read the header graph: recipients and CCs of a target are `associate` leads; repeated addresses tie aliases to a real person.
5. Pivot: an address feeds email-existence and breach checks; named people feed people-search; attachments may carry `metadata-exif` or document IDs.

## Inputs → Outputs
- **In:** `name` / `email` / keyword
- **Out:** email messages, `email` addresses of correspondents, `name`/`associate` links from headers
- **Empty/negative result looks like:** no matching messages — the person/term is not in this specific corpus. This covers only the AKP domain leak, so absence says nothing about the wider world; try other leak archives.

## Gotchas & OpSec
- Scope is narrow and political (one Turkish party's mail); relevance is high only for that milieu.
- Leaked context can be incomplete or manipulated — treat any single message as a lead, not proof, and be cautious redistributing personal data.
- Turkish-language content dominates; keyword searches may need Turkish spellings.

## Overlaps ("do both")
- Pairs with `[[wikileaks-search]]` (cross-collection search) and other email leaks like `[[dnc-email-database]]` — an address absent here may appear in another corpus, so search across collections.

## Trust & verifiability
`trust: community` — genuine leaked material hosted by WikiLeaks, but individual messages are unverified and politically sensitive; corroborate identities and claims against independent sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | akp-email-database |
| category | public-records |
| selectorsIn → selectorsOut | name, email → email, name, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
