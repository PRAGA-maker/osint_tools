---
id: passive-only-reconnaissance-with-sock-puppets-and-no-subject-contact
name: Passive-only reconnaissance with sock puppets and no subject contact
description: Use when Always, as the standing rules of engagement for any missing-persons investigation.
type: pattern
summary: 'Missing-persons OSINT is strictly passive: never contact the subject or their family, never attempt password resets or account-recovery probes, and never take any action that tips off the subject or alters the situation. Conduct all research from sock-puppet accounts (pre-logged-in before you start), behind a VPN, ideally geolocated to the subject''s region so local search engines and content surface correctly. Your investigation must leave no trace and create no traceable activity. This protects the family, the investigation, and you.'
missingPersonsRelevance: high
phase: opsec
steps:
- Pre-create and pre-login sock-puppet accounts on the relevant platforms before the event starts.
- Connect through a VPN, positioned in the subject's region when local content matters.
- Use local/regional search engines for geographically-specific subjects.
- Never message, friend, or attempt recovery flows on the subject or associates.
- Keep investigation activity invisible and non-traceable; know what is allowed during and after.
signals:
- No interaction with any real person tied to the case
- Local-region content surfaces correctly through a regionally-placed VPN
pitfalls:
- Attempting a password reset to confirm an email (active, forbidden)
- Contacting family for clarification
- Logging in from a personal account and leaving a footprint
- Searching only from your own country for an overseas subject
toolsUsed:
- VPN
- sock-puppet accounts
tags:
- opsec
- passive-recon
- sock-puppet
- ethics
- no-contact
evidence:
- type: writeup
  url: https://www.osintme.com/index.php/2021/11/14/a-noobs-guide-to-trace-labs-search-party-ctf/
  note: Passive recon only; never password-reset or contact family; investigation must be invisible; use regional VPN/search engines
- type: writeup
  url: https://shandyman.online/blog/on-a-mission-a-tracelabs-ctf-missing-persons-writeup/
  note: Pre-login sock-puppet accounts; VPN standard; VMs unnecessary for typical CTF activity
trust: community
source: searchparty-writeups
---

# Passive-only reconnaissance with sock puppets and no subject contact

> Missing-persons OSINT is strictly passive: never contact the subject or their family, never attempt password resets or account-recovery probes, and never take any action that tips off the subject or alters the situation. Conduct all research from sock-puppet accounts (pre-logged-in before you start), behind a VPN, ideally geolocated to the subject's region so local search engines and content surface correctly. Your investigation must leave no trace and create no traceable activity. This protects the family, the investigation, and you.

**When to use:** Always, as the standing rules of engagement for any missing-persons investigation.

## Steps
- Pre-create and pre-login sock-puppet accounts on the relevant platforms before the event starts.
- Connect through a VPN, positioned in the subject's region when local content matters.
- Use local/regional search engines for geographically-specific subjects.
- Never message, friend, or attempt recovery flows on the subject or associates.
- Keep investigation activity invisible and non-traceable; know what is allowed during and after.

## Signals it's working
- No interaction with any real person tied to the case
- Local-region content surfaces correctly through a regionally-placed VPN

## Pitfalls
- Attempting a password reset to confirm an email (active, forbidden)
- Contacting family for clarification
- Logging in from a personal account and leaving a footprint
- Searching only from your own country for an overseas subject

**Tools:** VPN, sock-puppet accounts

_Harvested from `searchparty-writeups` — methodology only, no case PII. Promote/curate as needed._
