---
id: mxtoolbox
name: MxToolbox
description: Use when you have an email domain (or full email headers) and want MX/SPF/DKIM/DMARC, blacklist, and header-trace data — returns the mail infrastructure and originating-IP picture.
url: https://mxtoolbox.com/
category: email
path:
- email
- mail-blacklists
bestFor: Email-server diagnostics, blacklist checks, and email-header tracing.
selectorsIn:
- domain
- email
selectorsOut:
- ip-address
- domain
- metadata-exif
status: live
pricing: freemium
costNote: Most lookups (MX, blacklist, header analyzer) are free; monitoring/bulk and the full feature set are paid.
opsec: passive
opsecNote: Passive — public DNS lookups, blacklist queries, and client-side header parsing; the target's mail server is not alerted (a delivery check makes a standard SMTP connection that the receiving server logs).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: MxToolbox is a widely used, reputable commercial email/DNS diagnostics service. Behavior is well documented and stable.
missingPersonsRelevance: medium
coverage: []
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- multirbl
- mxtoolbox-blacklists
- mxtoolbox-com-2
aliases: []
tags:
- mail-blacklists
source: arf-seed
lastVerified: ''
enrichment: full
---

# MxToolbox

> Reputable all-in-one email/DNS diagnostics — MX/SPF/DKIM/DMARC, blacklist status, and an email-header analyzer that exposes the originating IP.

## When to use
- You have a mail `domain` (a subject's provider, an employer, or a site that emailed them) and want to map its mail infrastructure.
- You have full **email headers** from a message to/from a subject and want to trace the originating `ip-address` and relay path — the investigatively useful path here.

## How to use it (`bestInteractionPattern`: web-manual)
1. For infrastructure: go to mxtoolbox.com, enter the `domain`, and run MX / SPF / DMARC / blacklist lookups.
2. For header tracing: use the Email Header Analyzer (see `[[mxtoolbox-com-2]]`), paste the raw headers, and read the hop list and originating IP.
3. Read results: MX hosts, auth status, blacklist flags, and the source IP from headers.
4. Pivot: an originating `ip-address` feeds IP-geolocation/ISP lookups; `domain` data feeds WHOIS and provider research.

## Inputs → Outputs
- **In:** `domain`, or full `email` headers
- **Out:** `ip-address` (from headers), `domain`/MX records, blacklist + auth status (`metadata-exif`)
- **Empty/negative result looks like:** clean/no-blacklist and standard MX — normal; header analysis with stripped or proxied headers yields only the provider's egress IP, not the person's device.

## Gotchas & OpSec
- Header-derived IPs are often the sending provider's, not the author's device (especially webmail); treat geolocation cautiously.
- Blacklist/MX data describes infrastructure, not the person — useful as corroboration, not identification.
- Heavy free use is rate-limited; an account/API is needed for volume.

## Trust & verifiability
`trust: trusted` — established, reputable diagnostics service with documented, stable behavior. MP relevance set `medium`: directly useful for email-header origin tracing, otherwise infrastructure-only.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mxtoolbox |
| category | email |
| selectorsIn → selectorsOut | domain, email → ip-address, domain, metadata-exif |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
