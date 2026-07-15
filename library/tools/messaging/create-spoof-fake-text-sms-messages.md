---
id: create-spoof-fake-text-sms-messages
name: Create Spoof / Fake Text / SMS Messages
description: Use when you are assessing whether a text/SMS "from" a `phone` could be spoofed — this Spoofbox tool sends messages with a forged sender ID, so it returns nothing about a target but proves how unreliable caller/sender numbers are.
url: https://www.spoofbox.com/en/app/spoof-sms
category: messaging
path:
- messaging
bestFor: Understanding and demonstrating that an SMS sender number can be forged, so a text "from" someone is not proof of who sent it.
selectorsIn:
- phone
selectorsOut:
- phone
status: live
pricing: freemium
costNote: Credit-based — each spoof SMS costs credits (~50 per message); a small number of free spoofs are available via promo/social engagement, but sustained use is paid. Registration required.
opsec: active
opsecNote: Actually SENDING a spoofed SMS contacts a real recipient and impersonates a number — that is active, potentially illegal (fraud/harassment), and traceable back to the Spoofbox account. Use this only to understand the threat (that inbound texts can be forged); do not send spoofed messages to targets or witnesses.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: untrustworthy
trustNote: A commercial spoofing service. It produces no intelligence; its only investigative value is counter-forensic — it demonstrates that sender IDs on SMS are trivially forgeable.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- zeoob-com
aliases:
- Spoofbox
- Spoof SMS
- fake text message sender
tags:
- messengerapps
- Messenger Apps
- spoofing
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Create Spoof / Fake Text / SMS Messages (Spoofbox)

> A sender-ID spoofing service, catalogued as a warning: it is why an SMS "from the missing person's number" cannot be trusted at face value.

## When to use
You are weighing a text message as a lead — "she texted me from her number last night," or a ransom/extortion SMS — and you need to reason about whether the sender ID could be forged. Spoofbox demonstrates that the "From" number on an SMS is user-settable, which reframes any such message from proof into an unverified claim requiring carrier-level confirmation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Understand the capability (recommended default): the Spoofbox spoof-SMS app lets a registered user set an arbitrary sender number, recipient, and message body. That alone tells you a sender ID is not trustworthy.
2. If you must confirm hands-on in an authorised test, register, note the credit cost, and send a spoof only to a phone you own — never to a target, witness, or the subject's contacts.
3. Treat any suspicious inbound SMS accordingly: seek the truth from the carrier (subpoena/records) or the device, not from the displayed number.
4. Pivot: escalate real message-origin questions to law enforcement / carrier records; use device forensics for genuine content.

## Inputs → Outputs
- **In:** a forged sender `phone`, a recipient `phone`, and message text (all attacker-supplied)
- **Out:** a delivered spoofed SMS — no data about any real person is returned
- **Empty/negative result looks like:** N/A — there is no lookup; the "output" is the message itself. The takeaway is that success proves nothing about identity.

## Gotchas & OpSec
- **Legal/ethical:** sending spoofed SMS to real people can be criminal (impersonation, harassment, fraud) and is logged to your account. Do not do it against a target or their circle.
- Sender IDs and even displayed timestamps are attacker-controlled; never authenticate a person by the number a text appears to come from.
- OpSec: **active and attributable** if you send — this is not a passive lookup.

## Overlaps ("do both")
- Pairs with `[[zeoob-com]]` — same counter-forensic lesson for chat screenshots: spoofed SMS and generated chat images both look real, so message "evidence" always needs source-side corroboration.

## Trust & verifiability
`trust: untrustworthy` — a spoofing utility with no investigative data. It is listed to make the point defensively: because tools like this exist and are cheap, an SMS sender number is never sufficient identification.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | create-spoof-fake-text-sms-messages |
| category | messaging |
| selectorsIn → selectorsOut | phone → phone |
| pricing / cost | freemium |
| trust | untrustworthy |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
