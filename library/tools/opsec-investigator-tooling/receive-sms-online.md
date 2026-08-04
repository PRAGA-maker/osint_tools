---
id: receive-sms-online
name: Receive SMS Online
description: Use when you need a disposable public `phone` number to receive an SMS verification code for a sock-puppet account — returns free shared numbers and their inboxes.
url: http://receive-sms-online.com/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Getting a throwaway number to pass SMS verification when standing up an investigator sock-puppet account.
selectorsIn: []
selectorsOut:
- phone
status: degraded
pricing: free
costNote: Free; no account needed. Numbers are shared/public and rotate frequently, so any given one may already be burned or blocked.
opsec: active
opsecNote: These numbers are PUBLIC — anyone can read the inbox, so never route codes for a real or sensitive account through them. They are for disposable sock-puppet signups only; many services (banks, WhatsApp) detect and reject virtual numbers.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A free public-SMS aggregator; numbers are shared, unreliable and often already blacklisted by major platforms. Treat as best-effort infrastructure, not a dependable service.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- receive-sms-free-2
aliases:
- receive-sms-online.com
tags:
- disposable-number
- sock-puppet
- sms-verification
source: osint4all
lastVerified: '2026-08-04'
enrichment: full
---

# Receive SMS Online

> A free directory of public, shared phone numbers whose incoming SMS is displayed on the page — used to pass one-time SMS verification when creating a disposable sock-puppet account.

## When to use
You are standing up an investigator sock-puppet (a burner social/email account) and a service demands an SMS code you don't want tied to your real number. Pick a public number here, use it for the signup, and read the code from its shared inbox. This is OpSec plumbing for *your* identity, not a way to look up a subject — its only "output" is a usable throwaway `phone`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://receive-sms-online.com/ and pick an available public number (choose a country the target service accepts).
2. Enter that number in the service you are registering; request the SMS code.
3. Return to the number's page and read the incoming message inbox for your code (messages are public and appear without login).
4. Fall back to another number/site if the code never arrives — popular numbers are often rate-limited or blacklisted.

## Inputs → Outputs
- **In:** none (you select a number)
- **Out:** a disposable public `phone` number and its live SMS inbox
- **Empty/negative result looks like:** the code never arrives, or the service rejects the number as "virtual/VoIP" — very common on major platforms; switch numbers/providers or use a paid private number.

## Gotchas & OpSec
- Human-in-the-loop: none, but expect trial-and-error across numbers.
- OpSec: **active/exposed** — inboxes are fully public; anyone can see the codes and any linked account is trivially compromised. Never use for accounts you need to keep, and never for anything sensitive or real-identity.
- Reliability: numbers are shared and heavily abused, so many are pre-blocked by Google/Facebook/WhatsApp; this is a degraded, best-effort resource.

## Overlaps ("do both")
- Pairs with `[[receive-sms-free-2]]` and other disposable-SMS sites because any single number may be burned — having several sources raises the odds one works.

## Trust & verifiability
`trust: community` — a free public-SMS aggregator with no reliability guarantees; treat it as throwaway infrastructure, verify the code arrived, and never depend on retaining the number.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
