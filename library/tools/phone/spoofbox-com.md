---
id: spoofbox-com
name: Spoofbox Trash Mobile
description: Use when you need a disposable phone number to receive an SMS verification code while standing up a sock-puppet account — returns a temporary public number and its incoming texts.
url: https://www.spoofbox.com/en/tool/trash-mobile
category: phone
path:
- phone
bestFor: Getting a throwaway number to receive a one-time SMS code so you can create a research/sock-puppet account without exposing a real number.
selectorsIn: []
selectorsOut:
- phone
status: live
pricing: free
costNote: The public "trash mobile" receive-SMS numbers are free. Spoofbox's other products (spoof calls/SMS) are paid and are a separate, sensitive category — see gotchas.
opsec: active
opsecNote: This is sock-puppet INFRASTRUCTURE, not a lookup on a target. Every incoming message to a trash number is PUBLIC — anyone can read codes sent to it, so never use one for an account you care about, and never route a target's real traffic through it. Spoofbox's caller-ID/SMS spoofing features can be unlawful (fraud/harassment) in many jurisdictions — do not use them.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial spoofing/disposable-number site of unverified operator; treat its infrastructure as untrusted (public, logged) and use only for throwaway, non-sensitive verifications.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- trash mobile
- spoofbox
tags:
- mobilephone
- Mobile & Phone Related
- sock-puppet
- disposable-number
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- create-spoof-fake-text-sms-messages
---

# Spoofbox Trash Mobile

> A free bank of public disposable phone numbers for receiving SMS — investigator sock-puppet plumbing, not a way to identify anyone.

## When to use
You are building a sock-puppet identity for passive research and a platform demands an SMS verification code. Rather than burn a real or attributable number, you grab a free public "trash" number, receive the code, and move on. Its direct missing-persons value is low — it protects the investigator's attribution rather than revealing anything about a subject. (Secondary, niche use: because these inboxes are public, you can check whether a subject foolishly registered an account to a known public disposable number.)

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.spoofbox.com/en/tool/trash-mobile and pick one of the free public numbers (various country codes).
2. Enter that number where a service asks for SMS verification.
3. Return to the trash-number page and read the incoming SMS to grab the code.
4. Treat the number as burned immediately — it is shared and public.
5. Pivot: with the sock-puppet account created, proceed to whatever passive research you needed it for.

## Inputs → Outputs
- **In:** (none — you are provisioning infrastructure, not querying a selector)
- **Out:** a temporary `phone` number and its publicly-visible incoming SMS
- **Empty/negative result looks like:** the number is blocked by the target service (many platforms blacklist known disposable ranges), or no SMS arrives — try another number or a different provider.

## Gotchas & OpSec
- **Everything is public**: any code sent to a trash number is readable by strangers — never use it for anything you need to keep or secure.
- **Blacklisted ranges**: major platforms (WhatsApp, Google) often reject public disposable numbers; success is hit-or-miss.
- **Legal line**: Spoofbox also sells caller-ID/SMS spoofing — impersonating a number to deceive can be illegal (fraud/harassment). Stay strictly on the receive-SMS trash-number feature.
- OpSec: labelled **active** because it is part of creating accounts; use only throwaway puppets.

## Overlaps ("do both")
- Pairs with other public receive-SMS services (receive-sms-online style sites) — rotate providers when one range is blacklisted.
- Pairs with sock-puppet email tooling when a platform needs both email and phone verification.

## Trust & verifiability
`trust: unverified` — an untrusted commercial spoofing site; safe only as disposable, public infrastructure. Never rely on it for anything sensitive, and avoid its spoofing products entirely.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | spoofbox-com |
