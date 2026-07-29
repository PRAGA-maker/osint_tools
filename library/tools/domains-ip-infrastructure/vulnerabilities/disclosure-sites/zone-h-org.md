---
id: zone-h-org
name: Zone-H.org
description: Use when you have a `domain` or `ip-address` and want its history of recorded website-defacement incidents with mirrored evidence — returns domain, ip-address.
url: https://zone-h.org/archive
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- vulnerabilities
- disclosure-sites
bestFor: Checking a domain/host/IP for a history of recorded website defacements and who claimed them.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free public archive; submitting/notifier features require a free account, browsing does not.
opsec: passive
opsecNote: Passive — you browse a third-party archive of past events; the target's own infrastructure is never contacted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Long-running (Estonia, since 2002) defacement archive; entries are attacker-submitted "notifications," so individual claims are self-reported and should be mirror-checked before trusting.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- Zone-H
- zone-h.org
tags:
- defacement
- hacktivism
- archive
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# Zone-H.org

> The internet's long-running archive of website defacements — search a domain, host, or IP to see whether it's been defaced, when, and which handle claimed it.

## When to use
You want the **compromise history** of a `domain` or `ip-address`: has this site been defaced, how often, and by whom? That tells you the host has been vulnerable (weak security posture, shared-hosting neighbours also hit), and the attacker handles/notifier names in each record are pivots into hacktivist crews and pseudonyms you can track elsewhere. Also useful in reverse — enumerating everything a particular notifier handle has claimed.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://zone-h.org/archive.
2. Filter or search by domain, IP, or notifier handle (e.g. `.../archive/notifier=NAME`, `.../archive/ip=1.2.3.4`).
3. Read each record: target, timestamp, notifier handle, defacement reason/method, and the mirrored copy of the defaced page.
4. Open the mirror to confirm the claim is real rather than a bogus submission.
5. Pivot: a notifier handle feeds `username`/social-profile OSINT; a defaced IP feeds `[[bgpview-io]]` and neighbour-domain checks; timestamps anchor a compromise timeline.

## Inputs → Outputs
- **In:** `domain`, `ip-address`, or a notifier handle
- **Out:** defacement records — target `domain`/`ip-address`, timestamp, notifier handle, method, and a mirrored evidence page
- **Empty/negative result looks like:** no archived defacement for that target/handle — either genuinely none recorded, or the incident was never submitted to Zone-H (absence isn't proof it was never compromised).

## Gotchas & OpSec
- Entries are **self-submitted by attackers** — some are exaggerated or falsely claimed; always view the mirror to verify.
- Older mirrors may be broken or missing; timestamps reflect submission, not necessarily the exact attack time.
- Passive to the target, but note Zone-H itself sees your browsing; use a sock-puppet session for sensitive research.

## Overlaps ("do both")
- Pairs with web archives (Wayback/archive.today) — Zone-H shows the defacement event and claimant, while a general archive shows the site's normal state before/after for context.

## Trust & verifiability
`trust: unverified` — a venerable but unmoderated, crowd-submitted archive; treat each entry as an unverified claim and confirm via its mirror before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | zone-h-org |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
