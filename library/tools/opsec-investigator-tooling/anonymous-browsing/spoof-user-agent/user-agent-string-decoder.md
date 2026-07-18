---
id: user-agent-string-decoder
name: User Agent String Decoder
description: Use when you have a raw `user-agent` string (from a log or header) and want it parsed — returns browser family, version, OS, and device type.
url: https://tools.tracemyip.org/user-agent-string-decoder/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
- spoof-user-agent
bestFor: Decoding a raw user-agent string into readable browser/OS/device components for log analysis or fingerprint checking.
selectorsIn:
- device-id
selectorsOut:
- device-id
status: live
pricing: free
costNote: Free web utility from tracemyip.org; no account or payment.
opsec: passive
opsecNote: Submitting a UA string sends only that string to the tool's server — no exposure of your real browsing context if you paste a test/target string rather than letting it read your live one.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party parsing utility on an ad-supported IP-tools site; the decode logic is standard UA parsing, so output is generally reliable, but the operator is not an authoritative source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- trace-my-ip
- ip-dns-leak-detection
aliases:
- UA string decoder
- user agent parser
tags:
- opsec
- user-agent
- fingerprint
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# User Agent String Decoder

> Paste a raw User-Agent header and get back the browser, version, operating system, and device it claims to be.

## When to use
You have a raw `User-Agent` string — pulled from a server log, an email header, a webhook, or a device you're profiling — and want it broken into human-readable parts (browser family + version, OS + version, device/engine). Two uses in an investigation: log analysis (what browser/device visited or contacted something) and OpSec self-checks (confirming the UA your hardened/spoofed browser presents looks like the ordinary client you intend to imitate).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://tools.tracemyip.org/user-agent-string-decoder/.
2. Paste the raw UA string into the input box (or let it read your current browser's UA for a self-check).
3. Submit and read the parsed breakdown: browser name/version, OS name/version, layout engine, and device/type.
4. For self-checks, compare the result against a "normal" target client — an exotic or inconsistent UA (e.g. a desktop OS with a mobile browser token) is a fingerprint red flag.
5. Pivot: OS/device details can corroborate what platform a subject used; feed distinctive device tokens into other log/correlation work.

## Inputs → Outputs
- **In:** a raw `User-Agent` string (recorded as `device-id`-class fingerprint data)
- **Out:** parsed browser family/version, OS, layout engine, device type
- **Empty/negative result looks like:** "unknown"/blank fields for one or more components — the UA is malformed, spoofed with a nonstandard string, or too new for the parser's rules; it does not mean the client is fake, only unparsed.

## Gotchas & OpSec
- A UA string is trivially spoofable — treat it as a claim about the client, never proof of the actual device.
- Parser rule sets lag new browser/OS releases, so very recent versions may decode as "unknown."
- Passive: you only submit a text string; nothing about your live session leaks if you paste rather than auto-detect.

## Overlaps ("do both")
- Pairs with `[[ip-dns-leak-detection]]` — UA decoding covers the browser-fingerprint layer while ipleak covers the network layer (IP/DNS/WebRTC); run both when validating a spoofed/hardened setup. Also complements `[[trace-my-ip]]` from the same provider.

## Trust & verifiability
`trust: unverified` — a third-party ad-supported utility; UA parsing is a standard, low-risk operation so output is usually accurate, but the site is not an authoritative reference and should not be relied on for edge cases.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | user-agent-string-decoder |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | device-id → device-id |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
