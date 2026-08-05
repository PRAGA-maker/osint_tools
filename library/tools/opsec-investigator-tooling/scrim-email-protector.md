---
id: scrim-email-protector
name: Scrim Email Protector
description: Use when you (the investigator) want to share a sock-puppet email as a captcha-gated short link, or when you encounter an scr.im link hiding a target's email and need to recognise/resolve it — deals in email obfuscation.
url: http://scr.im
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Publishing your own decoy/sock-puppet email as a spam-proof scr.im short link (an opsec-side utility).
selectorsIn:
- email
selectorsOut:
- email
status: degraded
pricing: free
costNote: Free service; no account historically required to create a link. Note the site has been intermittently unreachable — verify it loads before relying on it.
opsec: passive
opsecNote: Primarily a defensive/opsec tool for YOUR side — turning a sock-puppet email into a captcha-gated link so scrapers can't harvest it. If you resolve someone else's scr.im link, you only view a public page; the email owner is not notified. Do not create links from your real address.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing but lightly-maintained anti-spam link service; treat its uptime and longevity as uncertain (status degraded).
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- scr.im
- scrim
tags:
- toddington
- curated-directory
- proxy-servers-online-privacy-security-tools
source: toddington-resources
lastVerified: '2026-08-05'
enrichment: full
---

# Scrim Email Protector

> scr.im turns an email address into a captcha-gated short link — mainly an opsec convenience for sharing a sock-puppet address, and something to recognise when a target hides their email behind it.

## When to use
Two thin but real cases. **Offensively-defensive (your side):** when running a sock-puppet identity, publish that decoy email as an scr.im link so automated scrapers/bots can't harvest it — humans solve a captcha to see it. **Investigative:** when you find an `scr.im/xxxx` link on a target's profile or page, recognise it as an email-obfuscation wrapper and resolve it (solve the captcha) to reveal the underlying address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://scr.im in a browser (confirm it loads — the service is intermittently up).
2. **To create:** enter the (sock-puppet) email you want to share and generate the short link; share that link instead of the raw address.
3. **To resolve:** open the `scr.im/...` link you found, solve the captcha, and read the revealed `email`.
4. Pivot: a resolved email feeds standard email-OSINT (breach checks, account-existence oracles, reverse email lookups).

## Inputs → Outputs
- **In:** `email` (yours to protect) or an scr.im link (to resolve)
- **Out:** a shareable captcha-gated link, or the revealed `email` behind a link
- **Empty/negative result looks like:** the site failing to load, or a dead/expired link that no longer reveals an address — common given the service's shaky uptime.

## Gotchas & OpSec
- **Uptime is unreliable** (status degraded) — don't build a workflow that depends on it being available.
- It is an obfuscation tool, so its investigative value is narrow: recognising and unwrapping scr.im links, not discovering new ones.
- Captcha gate is the human-in-the-loop step, both to create and to resolve.
- Never wrap your real address; use it only for decoy/sock-puppet emails.

## Overlaps ("do both")
- Once you resolve an email here, run it through your email-enrichment stack (breach and account-existence checks) — this tool only exposes the address, it does nothing with it.

## Trust & verifiability
`trust: community` — a legacy anti-spam utility with uncertain maintenance; treat any address it reveals as a lead to confirm through independent email tooling.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scrim-email-protector |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | email → email |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
