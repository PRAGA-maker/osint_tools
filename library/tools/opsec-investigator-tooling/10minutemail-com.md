---
id: 10minutemail-com
name: 10minutemail.com
description: Use when you need a throwaway `email` inbox to receive a one-off verification code without exposing a real address — an investigator OpSec tool, not a lookup on a subject.
url: https://10minutemail.com/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Spinning up an instant, no-signup disposable inbox to catch a single confirmation/verification email.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Core disposable inbox is free with no signup; a paid tier extends address lifetime and adds features. The free 10-minute (extendable) inbox covers most OpSec needs.
opsec: passive
opsecNote: Protects YOUR identity — no target is contacted. Anything sent to the inbox is readable by anyone with the address, so never route password resets or anything sensitive through it. Many sites block known disposable-mail domains, so it works for throwaway registrations only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running, widely-used disposable-mail service; treat every message in it as public and ephemeral.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- simplelogin
aliases:
- 10 Minute Mail
- 10minutemail
tags:
- opsec
- disposable-email
- sock-puppet
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# 10minutemail.com

> A zero-signup disposable inbox that self-destructs — the fastest way to catch one verification email without touching a real address.

## When to use
You are registering a low-stakes throwaway account (to view a gated page, test a signup flow, or stand up a quick sock puppet) and need to receive a single confirmation link or code without giving up an attributable `email`. It hands you a random address and a live inbox on the spot; the address expires after ~10 minutes (extendable). It protects the investigator, not a subject — it returns no data about anyone.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://10minutemail.com/ — a random address and empty inbox appear immediately, no signup.
2. Copy the address and paste it into the target signup form.
3. Watch the inbox on the page; incoming mail (verification links/codes) appears live.
4. Click "give me 10 more minutes" to extend if the code is slow.
5. Close the tab when done — the address and its mail are discarded.

## Inputs → Outputs
- **In:** none (you generate a throwaway address; you supply nothing about a target)
- **Out:** a temporary `email` inbox for operational use (not a harvested selector)
- **Empty/negative result looks like:** the signup form rejects the address ("disposable email not allowed") — the site blocklists throwaway domains; fall back to an alias service like `[[simplelogin]]`.

## Gotchas & OpSec
- The inbox is **public**: anyone who knows/guesses the address can read it — never use it for anything you need to keep private or recover later.
- Ephemeral by design; once it expires the mail is gone, so grab the code promptly.
- Widely blocklisted by mainstream services; it's for low-value throwaways, not durable sock-puppet mailboxes.

## Overlaps ("do both")
- Pairs with `[[simplelogin]]` — 10minutemail is instant-but-disposable-and-public, while SimpleLogin gives durable, private forwarding aliases for accounts you need to keep.

## Trust & verifiability
`trust: community` — a long-established free disposable-mail service. The software does what it says; the only caveat is inherent to disposable mail — it is public and ephemeral.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | 10minutemail-com |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
