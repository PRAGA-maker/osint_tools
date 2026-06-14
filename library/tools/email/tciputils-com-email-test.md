---
id: tciputils-com-email-test
name: TCIPUTILS.com Email Test
description: Use when you have an email address and want to validate its domain MX/SMTP deliverability — returns mail-server metadata, not identity data.
url: http://www.tcpiputils.com/email-test
category: email
path:
- email
bestFor: Checking whether an email domain has valid MX records and a reachable SMTP server.
selectorsIn:
- email
- domain
selectorsOut:
- domain
- ip-address
- metadata
status: degraded
pricing: free
costNote: Free web utility; TCP/IP Utils has reduced/limited free lookups over time.
opsec: passive
opsecNote: Queries DNS/MX and probes the destination mail server from TCP/IP Utils' infrastructure, not yours. It does not send mail to or notify the target person.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: unverified
trustNote: General-purpose network-tools site (TCP/IP Utils); the email-test endpoint validates mail infrastructure, not people. Free quota and endpoint availability are inconsistent.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- tcpiputils email test
tags:
- email
- email-validation
source: metaosint
lastVerified: ''
enrichment: full
---

# TCIPUTILS.com Email Test

> A network-diagnostics utility that checks an email domain's MX records and SMTP reachability — a deliverability/validity check, not a person finder.

## When to use
You have an `email` (or just its `domain`) and want to know whether mail to it could plausibly be delivered: does the domain publish MX records, and does the mail server respond? Useful for triaging whether an address harvested elsewhere is real/active before pivoting. It does not return a person's `name`, `phone`, or `social-profile` despite the seed metadata implying so — treat those as out of scope.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open `http://www.tcpiputils.com/email-test`.
2. Enter the email address (or domain) and submit; clear any CAPTCHA.
3. Read the MX/SMTP result: valid MX hostnames, the mail server's banner, and whether the SMTP handshake/RCPT check succeeds.
4. Pivot: a valid, active address is worth running through people/breach tools like [[thatsthem]] or [[venacus]]; a dead domain is a dead end.

## Inputs → Outputs
- **In:** `email`, `domain`
- **Out:** `domain` (MX hostnames), `ip-address` (mail server), `metadata` (SMTP banner / validity verdict)
- **Empty/negative result looks like:** "no MX record" / connection refused / catch-all that accepts anything — none of which confirm the specific mailbox exists.

## Gotchas & OpSec
- Human-in-the-loop: occasional CAPTCHA and free-tier rate limits.
- Many mail servers use catch-all or greylisting, so a "valid" verdict is weak evidence the exact mailbox is real.
- OpSec: passive from your side; the probe originates from TCP/IP Utils, not you.

## Overlaps ("do both")
- Pairs with [[verify-email]] / [[verify-an-email-address-mailtester]] for SMTP-level confirmation, and with [[validateemailaddress-org]] for syntax/MX checks.

## Trust & verifiability
`trust: unverified` — a general IP/DNS tools site; the email endpoint is a mail-infrastructure validator, not an identity source, and its free availability has been spotty.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tciputils-com-email-test |
| category | email |
| selectorsIn → selectorsOut | email, domain → domain, ip-address, metadata |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
