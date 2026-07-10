---
id: secmail
name: SecMail
description: Use when you need a disposable, anonymous email address to register sock-puppet accounts without exposing a real inbox — provides throwaway/anonymous `email` accounts. (Operational infra, not a lookup.)
url: https://www.secure-email.org
category: email
path:
- email
bestFor: Creating anonymous/disposable email accounts to stand up sock-puppet identities for OSINT work.
selectorsIn:
- email
selectorsOut:
- email
status: live
pricing: freemium
costNote: Free anonymous accounts with paid premium tiers (multiple domains, extra features). No real identity required to sign up.
opsec: active
opsecNote: This is operational tradecraft, not a passive lookup — you are creating an identity you will act from. Never link it to your real details, use it over a clean/VPN'd browser, and treat the provider as untrusted with anything you send/receive. NOTE the service also advertises SMS sender "spoofing"; using spoofing to impersonate a person or organisation is illegal in many jurisdictions — do not use it, keep to anonymous email for legitimate sock-puppet registration only.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A privacy/anonymous-email provider of unclear operatorship; fine as throwaway sock-puppet infrastructure, but do not trust it with anything sensitive and be aware its spoofing features invite misuse.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: true
aliases:
- SecMail
- secure-email.org
tags:
- toddington
- curated-directory
- email-addresses
- sock-puppet
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# SecMail

> An anonymous/disposable email provider — spin up a throwaway inbox to register sock-puppet accounts without touching a real address. Operational infrastructure, not an investigative lookup.

## When to use
You need a burner email to create the sock-puppet accounts OSINT work requires (a research X/VK/Telegram account, a registration to view a gated site) without exposing a real inbox that could unmask you. SecMail provides free anonymous accounts across several domains for exactly that.

## How to use it (`bestInteractionPattern`: web-manual)
1. From a clean/VPN'd browser (no real identity, no personal cookies), open https://www.secure-email.org.
2. Create a free anonymous account on one of its domains.
3. Use that address to register your sock-puppet accounts and receive their verification emails.
4. Keep the burner strictly compartmentalized from your real identity and other operations.
5. Pivot: the sock-puppet inbox now underpins accounts for `[[x-com-4]]`, `[[vk-com-2]]`, `[[telegram-channel-joiner]]`, etc.

## Inputs → Outputs
- **In:** none (you create an identity) — issues an anonymous `email`
- **Out:** a disposable/anonymous `email` account (inbox) for sock-puppet registration
- **Empty/negative result looks like:** signup fails, or a target site blocks the domain (many services blocklist known throwaway-email domains). If a registration rejects the address, use a different burner provider or a longer-lived research account.

## Gotchas & OpSec
- **Untrusted provider:** never send/receive anything sensitive; assume it can read your mail.
- Many sites blocklist disposable-email domains — you may need a more "residential-looking" burner.
- **Do not use its SMS-spoofing feature to impersonate anyone — that is illegal in many places.** Keep to anonymous email for legitimate sock-puppet registration.
- Compartmentalize rigorously; one leak can deanonymize the whole persona.

## Overlaps ("do both")
- Pairs with `[[sms-receive-net]]` (disposable numbers for phone verification) — together they let you register sock-puppet accounts without exposing a real email or phone.

## Trust & verifiability
`trust: unverified` — throwaway infrastructure of unclear operatorship. Use it only as disposable sock-puppet plumbing, never for sensitive content, and stay well clear of its impersonation/spoofing features.
