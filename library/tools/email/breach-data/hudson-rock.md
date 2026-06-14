---
id: hudson-rock
name: Hudson Rock
description: Use when you want to know whether an email/domain/username/IP was captured by infostealer malware — i.e. whether the person's device was compromised.
url: https://www.hudsonrock.com/threat-intelligence-cybercrime-tools
category: email
path:
- email
- breach-data
bestFor: Checking an email/domain/username against infostealer (malware-captured credential) datasets.
selectorsIn:
- email
- domain
- username
- ip-address
selectorsOut:
- email
- domain
- metadata-exif
- device-id
status: live
pricing: freemium
costNote: Free "Cavalier"/"Bayonet" lookup tools and a free email/domain checker on the site; full dataset detail and API are commercial.
opsec: passive
opsecNote: Queries a database compiled from infostealer malware logs; the target is not contacted. You disclose the searched value to Hudson Rock.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Hudson Rock is a recognised threat-intelligence vendor specialising in infostealer data; its free checkers are widely cited. Free results are summarised (counts/flags); detailed records require their commercial product.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- have-i-been-pwned
- h8mail
- holehe
aliases:
- Cavalier
- Bayonet
tags: []
source: arf-seed
lastVerified: ''
enrichment: full
---

# Hudson Rock

> Infostealer intelligence: tells you whether an email, domain, username, or IP appears in malware-captured "stealer logs" — i.e. whether a device tied to the person was infected and its saved credentials/cookies harvested.

## When to use
You have an `email`, `domain`, `username`, or `ip-address` and want to know if the person's machine was compromised by an infostealer. A hit is high-value: stealer logs reveal which sites the victim had saved logins for (a live footprint), the infected device, and sometimes IPs — strong pivots in a missing-persons trail.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to Hudson Rock's free tools page (https://www.hudsonrock.com/threat-intelligence-cybercrime-tools).
2. Use the free email/domain/username checker; enter the selector.
3. Read the summary: whether the value appears in stealer logs, count of compromised machines, and the kinds of data exposed.
4. For full record detail (URLs, credentials, device fingerprints), use the commercial Cavalier product / API.
5. Pivot: site URLs in the logs → accounts to enumerate; `device-id`/`ip-address` → other investigative angles.

## Inputs → Outputs
- **In:** `email`, `domain`, `username`, `ip-address`
- **Out:** infostealer hit flags/counts, exposed service URLs, `device-id`/`metadata-exif`-style attributes (full detail is paid)
- **Empty/negative result looks like:** "not found in our database" — the value isn't in known stealer logs (does not rule out other breaches).

## Gotchas & OpSec
- Free tier returns summaries; the actionable credential/URL detail is behind the commercial offering.
- Stealer-log data is sensitive — handle within legal/ethical bounds; never reuse captured credentials.
- OpSec: passive toward the target; you reveal the queried value to Hudson Rock.

## Overlaps ("do both")
- Complements `[[have-i-been-pwned]]` (breach-index) and `[[holehe]]` (registered accounts) — Hudson Rock specifically covers malware-stolen data the others don't, and `[[h8mail]]` for broader credential search.

## Trust & verifiability
`trust: community` — established infostealer-intelligence vendor whose free checkers are well-regarded; verify depth via their product since free output is summarised.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hudson-rock |
| category | email |
| selectorsIn → selectorsOut | email, domain, username, ip-address → email, domain, metadata-exif, device-id |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
