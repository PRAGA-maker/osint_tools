---
id: email-leak-tests
name: Email IP Leak Test
description: Use when you want to confirm your own sock-puppet email doesn't expose your `ip-address` — send a test message and it reports whether your real IP appears in the outbound headers.
url: https://emailipleak.com/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
- vpn-tests
bestFor: Verifying that your investigative email account does not leak your real IP address in message headers.
selectorsIn:
- email
selectorsOut:
- ip-address
status: live
pricing: free
costNote: Free diagnostic; no account or payment.
opsec: active
opsecNote: This is an OPSEC self-check, not a lookup on a target. You send a test email from YOUR sock-puppet account to the address it gives you; the tool reads the headers of that message. Run it from the exact account/VPN setup you use for investigations, never from a personal account, and don't send anything sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Simple single-purpose header-inspection utility; it only reports what your own email's headers contain, so there's little to misrepresent, but it's an unofficial third-party service.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- emailipleak.com
- Email IP Leak
tags:
- opsec
- anonymity
- email-headers
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Email IP Leak Test

> A self-directed OPSEC check: send it a test email and it tells you whether your mail provider stamps your real IP address into the outbound headers — closing a leak before you email a target.

## When to use
Before you use a sock-puppet email account to contact or register with anything connected to an investigation, you want to be sure the account won't betray your real `ip-address`. Some providers (and some desktop mail clients) include the sender's originating IP in the `Received` headers; this tool inspects a message you send and reports whether yours does. It protects your own OPSEC — it does not look up anything about a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://emailipleak.com/ and start a test; it displays your currently-detected IP and gives you a unique test address.
2. From the exact investigative account, client, and VPN/Tor setup you intend to use, send an email to that address.
3. The tool parses the received message's headers and reports whether your real IP appeared — i.e. whether recipients would see it.
4. Act on the result: if your IP leaked, switch to a webmail provider that strips it (or route your client through a proxy) and re-test before using the account operationally.

## Inputs → Outputs
- **In:** a test `email` sent from your own account/setup
- **Out:** a verdict on whether your real `ip-address` is exposed in the message headers
- **Empty/negative result looks like:** "no IP leak detected" — your provider isn't stamping your originating IP; a positive result shows the leaked IP, telling you the setup is unsafe to use against a target.

## Gotchas & OpSec
- This is a test of YOUR setup — always run it from the same account/VPN you'll use operationally, or the result is meaningless.
- Marked **active** because you are sending an email; keep the test content innocuous and never send from a personal account.
- It only checks header IP leakage; it does not evaluate other de-anonymisation vectors (tracking pixels, login metadata) — treat a clean result as necessary, not sufficient.

## Overlaps ("do both")
- Pairs with browser/VPN leak-test tools in this suite — this one covers the email vector specifically, while WebRTC/DNS leak tests cover browsing; run the whole set before operating a sock puppet.

## Trust & verifiability
`trust: community` — a minimal third-party utility that just reports your own headers; low risk of misrepresentation, but confirm a critical result by inspecting the raw headers of the received message yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | email-leak-tests |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | email → ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
