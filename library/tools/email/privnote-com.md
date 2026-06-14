---
id: privnote-com
name: privnote.com
description: Use when you need to send a one-time, self-destructing encrypted note — an operational tool for sharing tips/links securely, not an email-lookup utility.
url: https://privnote.com/
category: email
path:
- email
bestFor: Sending a self-destructing, encrypted one-time message (e.g. sharing a sensitive link with a partner without leaving a trail).
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free; optional paid features (read receipts, password, expiry) on Privnote Plus.
opsec: passive
opsecNote: Notes are end-to-end encrypted client-side and destroyed after first read; the server cannot read content. Good for your own operational comms, reveals nothing about a third party.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Legitimate, long-running secure-note service, but it is NOT an OSINT subject-lookup tool. Miscategorized in the email harvest list.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- email
- Email Related Sites
- secure-comms
source: uk-osint
lastVerified: ''
enrichment: full
---

# privnote.com

> Privnote creates encrypted, self-destructing one-time notes — an operational/OPSEC comms tool for the investigator, not a way to research a subject.

## When to use
You (not a subject) need to share a sensitive piece of information — a witness contact, a case link, a credential — with a teammate or tipster and want it to vanish after one read. It takes no investigative `selectorsIn` and returns no `selectorsOut` about any person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to privnote.com and type the message.
2. Optionally set a password and expiry, then click to generate a unique link.
3. Send the link out-of-band (e.g. via a different channel than the recipient's normal email).
4. The note self-destructs after the first open; you can request a destruction notification.

## Inputs → Outputs
- **In:** none (free-text you author).
- **Out:** a single-use URL; no data about a subject.
- **Empty/negative result looks like:** if a link is opened twice it shows "note already read/destroyed."

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive and self-protective. Anyone with the link can read it once, so deliver the link securely. Be aware phishing actors abuse Privnote clones — verify you are on the real privnote.com.

## Overlaps ("do both")
- Operational sibling, not an OSINT pivot. Use alongside any subject lookup when you must relay findings discreetly.

## Trust & verifiability
`trust: unverified` — the service is real and reputable, but it produces no subject intelligence; it was harvested into an email list by mistake.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | privnote-com |
| category | email |
| selectorsIn → selectorsOut | (none) → (none) |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
