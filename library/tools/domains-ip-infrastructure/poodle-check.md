---
id: poodle-check
name: Poodle Check
description: Use when you have a `domain`/host and want to know if its SSL/TLS is vulnerable to the POODLE (SSLv3) downgrade attack — returns a pass/fail vulnerability verdict.
url: https://osint.sh/poodle/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: A quick check of whether a server still allows the insecure SSLv3 protocol (POODLE-vulnerable).
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free web check as part of the osint.sh tool suite; no account for basic use.
opsec: active
opsecNote: The check makes a real TLS handshake to the target host to test SSLv3 support, so the host sees a connection (from osint.sh's servers, not your IP). Low-touch, but it is contact with the target's server, not a purely passive database lookup.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Part of osint.sh (secgron), a popular free all-in-one OSINT suite; a convenience wrapper around a standard SSL protocol test.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- osint.sh poodle
- SSL POODLE checker
tags:
- ssl-tls
- vulnerability-check
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Poodle Check

> An osint.sh one-click test: does this host still speak insecure SSLv3, making it POODLE-vulnerable?

## When to use
A narrow infrastructure/security check with minimal people-finding value: you have a `domain`/host tied to a subject or investigation and want to gauge its security hygiene — specifically whether it still permits SSLv3 (the protocol POODLE exploits to downgrade and decrypt CBC-mode traffic). Mostly useful as one signal that a server is old/poorly-maintained, which can hint at a low-effort or abandoned operator.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://osint.sh/poodle/.
2. Enter the target `domain`/host and run the check.
3. Read the verdict: vulnerable (SSLv3 accepted) vs not vulnerable (SSLv3 disabled).
4. Pivot: a "still on SSLv3" result is a weak indicator of a neglected/outdated server; combine with WHOIS age and header/tech fingerprints for a fuller maintenance picture.

## Inputs → Outputs
- **In:** `domain`/host
- **Out:** POODLE/SSLv3 vulnerability verdict for that host
- **Empty/negative result looks like:** "not vulnerable" / SSLv3 disabled — normal for any modern server; the absence of the flaw tells you little on its own.

## Gotchas & OpSec
- **Active** — it handshakes with the target to test the protocol; low-touch but not a passive lookup.
- Single-purpose: it answers only the SSLv3/POODLE question, not broader TLS posture.
- POODLE is an old flaw; most live hosts pass, so a positive result is the noteworthy (and rare) case.

## Overlaps ("do both")
- Pairs with a full SSL/TLS scanner (e.g. testssl.sh, SSL Labs) for complete cipher/protocol posture — this osint.sh tool is the fast single-flag version.

## Trust & verifiability
`trust: community` — a convenience wrapper in the osint.sh suite around a standard protocol test; the verdict is reproducible with any SSLv3-capable scanner.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | poodle-check |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
