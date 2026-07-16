---
id: h8mail-trace-labs-fork
name: h8mail (Trace Labs fork)
description: Use when you have an `email` and want breach/leak exposure — searches breach databases and leaked-credential sources — returns linked `email`s, `username`s, passwords, and `associate` accounts.
url: https://github.com/tracelabs/h8mail
category: email
path:
- email
bestFor: Finding breach exposures, leaked credentials, and linked accounts tied to an email address.
selectorsIn:
- email
selectorsOut:
- email
- username
- associate
status: live
pricing: freemium
costNote: The tool is free (pip install h8mail) and runs against local breach dump files at no cost; premium sources (HIBP, Snusbase, Leak-Lookup, Hunter.io, etc.) require your own paid API keys.
opsec: passive
opsecNote: Querying local breach files is entirely passive and offline — nothing touches the subject. If you enable online API integrations, you disclose the target email to those third-party services (and consume your keyed quota); choose integrations knowingly. Handle any recovered credentials ethically and legally — never attempt to log in as the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Trace Labs fork of the well-known khast3x/h8mail; Trace Labs is a reputable nonprofit focused on OSINT for missing persons.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- h8mail
tags:
- python
- email
- breach
- credentials
- tracelabs
source: tracelabs-repos
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- gumshoe
- the-osint-field-manual-tofm
- trace-labs-awesome-osint
- trace-labs-osint-vm-tlosint-vm
---

# h8mail (Trace Labs fork)

> A command-line email breach-hunter — feed it an address and it mines breach dumps and leak sources for exposures, linked usernames, and reused credentials.

## When to use
You have an `email` and want its breach footprint: which leaks it appears in, what usernames/passwords are associated, and what other accounts or emails link to it. In missing-persons and profiling work this surfaces old usernames, alternate emails, and platform accounts that give you fresh selectors to pivot on. The Trace Labs fork is tuned for OSINT-for-good workflows.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install h8mail` (Python).
2. Simplest run (uses free/local sources): `h8mail -t target@example.com`.
3. To search local breach dumps offline: `h8mail -t target@example.com --local-breach breaches.txt` (or `--bc` for a chunked directory) — fully offline, no third-party disclosure.
4. For richer results, add API keys in a config (`-c config.ini`) for HIBP/Snusbase/Leak-Lookup/etc. and pass `--power-chase` to follow discovered emails.
5. Read output: exposures, linked emails/usernames, and (from keyed sources) credential hits. Pivot usernames into `[[sherlock]]`/`[[maigret]]`, alternate emails into further h8mail runs.

## Inputs → Outputs
- **In:** `email` (single, a comma list, or a file of targets)
- **Out:** breach names/exposures, linked `email`s and `username`s, associated accounts (`associate`), and credentials from keyed sources
- **Empty/negative result looks like:** no hits — with only free/local sources this often means your dumps don't cover the address, not that it's clean. Coverage scales with the breach data and API keys you supply.

## Gotchas & OpSec
- Results are only as good as your data: without local dumps or API keys, expect thin output. The real power comes from breach corpora and keyed sources.
- Online integrations disclose the target email to third parties and consume paid quota — decide deliberately which to enable.
- Recovered credentials are for intelligence only; using them to access accounts is illegal.

## Overlaps ("do both")
- Pairs with `[[haveibeenpwned]]` (quick breach check) and `[[holehe]]`/`[[epieos]]` (account-existence by email) — h8mail digs into credential-level detail while those enumerate where the email is registered.

## Trust & verifiability
`trust: trusted` — maintained by Trace Labs, a reputable OSINT nonprofit; still, verify recovered links (breach data can be stale or contain same-email collisions).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | h8mail-trace-labs-fork |
| category | email |
| selectorsIn → selectorsOut | email → email, username, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
