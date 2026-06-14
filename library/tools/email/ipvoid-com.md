---
id: ipvoid-com
name: ipvoid.com
description: Use when you have an email or its raw headers and want to trace the originating IP/route — returns sender IP, geolocation, and mail-route metadata.
url: https://www.ipvoid.com/email-tracer/
category: email
path:
- email
bestFor: Tracing an email's originating IP and mail route from its full headers.
selectorsIn:
- email
- metadata
selectorsOut:
- ip-address
- geolocation
- metadata
status: live
pricing: free
costNote: Free web tool; IPVoid also sells other paid lookups but the email tracer is free.
opsec: passive
opsecNote: You paste headers you already possess; nothing is sent to the subject. Purely client-submitted analysis against IPVoid's IP/reputation data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: IPVoid is a long-running, well-known suite of free IP/domain/email diagnostic tools; the email tracer parses standard Received headers, which is deterministic and reliable.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- IPVoid
- IPVoid Email Tracer
tags:
- emailheaders
- Email Header Related Sites
- header-analysis
source: uk-osint
lastVerified: ''
enrichment: full
---

# ipvoid.com

> Email header tracer — parses the full headers of a received email to extract the originating IP, mail route, and approximate sender geolocation.

## When to use
You have an actual email message from or about a subject and can copy its full/raw headers. Paste them here to recover the originating `ip-address`, intermediate mail servers, and an approximate `geolocation` of the sender's network. In missing-persons work this can place where a message was sent from (e.g., a ransom/contact email, a last message) or confirm/deny a claimed origin. Requires possession of the headers — it does not look anything up from an email address alone.

## How to use it (`bestInteractionPattern`: web-manual)
1. In the email client, view the original/raw message and copy the full headers.
2. Go to https://www.ipvoid.com/email-tracer/ and paste the headers (`metadata`).
3. Read the trace: extracted originating IP, the chain of Received hops, and IP geolocation/reputation.
4. Pivot: feed the originating `ip-address` into an IP geolocation/reputation tool or WHOIS to identify the ISP/network and approximate location.

## Inputs → Outputs
- **In:** full email headers (`metadata`); the subject `email` for context
- **Out:** originating `ip-address`, hop-by-hop route `metadata`, approximate sender `geolocation`
- **Empty/negative result looks like:** no usable originating IP — common with major webmail (Gmail/Outlook) that strip or proxy the sender IP, leaving only provider servers.

## Gotchas & OpSec
- Webmail providers often hide the true client IP, so a trace may only show provider infrastructure, not the person's network.
- Headers can be forged/spoofed; treat the originating IP as a lead to verify, not proof.
- OpSec: fully passive — you submit data you already hold; nothing reaches the subject.

## Overlaps ("do both")
- Pairs with [[ipqualityscore-com]] (validity/risk of the address) — IPVoid handles the message route, IPQS handles the address itself.

## Trust & verifiability
`trust: trusted` — established free diagnostic suite; header parsing is deterministic. Reliability of the result depends entirely on whether the provider preserved the originating IP and whether headers were spoofed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ipvoid-com |
| category | email |
| selectorsIn → selectorsOut | email, metadata → ip-address, geolocation, metadata |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
