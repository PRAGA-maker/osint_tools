---
id: onionshare-file-sharing-tool
name: OnionShare
description: Use when you need to share files, host a temporary site, or chat anonymously over Tor — an OpSec/tradecraft tool for investigators; no third-party server holds your data.
url: https://onionshare.org
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Anonymously sending/receiving files (or hosting a drop) directly over Tor with no intermediary service.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (GPL); desktop app for Windows, macOS, Linux.
opsec: passive
opsecNote: Everything runs on your own computer as a Tor onion service — no company sees the files. Anonymity depends on Tor: keep the app updated, share the onion address over a secure channel, and remember your machine is the server (it must stay online while sharing).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Open-source, security-audited project maintained under Micah Lee / the Tor community; widely used by journalists and reputable for anonymous transfer.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- onionshare.org
- OnionShare
tags:
- Proxy Servers, Online Privacy & Security Tools
source: toddington-resources
lastVerified: '2026-07-28'
enrichment: full
---

# OnionShare

> An open-source desktop app that turns your computer into a temporary Tor onion service so you can share files, host a simple site, or chat — anonymously and with no third party in the middle.

## When to use
This is an **investigator tradecraft/OpSec tool**, not a lookup. Use it to receive documents from a source anonymously, hand off evidence to a colleague without email/cloud metadata, or stand up a throwaway drop site — all without a company holding your data. It returns nothing about a subject; its value is protecting *your* operations and sources.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download and install OnionShare from https://onionshare.org (verify the signature).
2. Choose a mode: **Share** (send files), **Receive** (accept files into a drop box), **Host a Website**, or **Chat**.
3. Add your files / configure the mode; OnionShare starts a Tor onion service and gives you a `.onion` address (optionally password-protected).
4. Send the onion address (and password) to the recipient over a **separate secure channel**.
5. Keep your computer online until the transfer completes; stop the share to tear the service down.

## Inputs → Outputs
- **In:** files/text you choose to share (no investigative selector)
- **Out:** a temporary `.onion` address others use to fetch/send (no investigative selector)
- **Empty/negative result looks like:** N/A — if the recipient can't connect, the share was stopped, your machine went offline, or Tor is blocked on their side.

## Gotchas & OpSec
- **You are the server:** the share only works while your computer is on and OnionShare is running.
- Share the onion address over a secure out-of-band channel — anyone with the address (and password) can access it.
- Recipients need Tor Browser; anonymity is only as strong as Tor and your operational discipline.

## Overlaps ("do both")
- Complements the Tor Browser and disk-encryption tools in an investigator's OpSec kit — OnionShare handles anonymous transfer; pair it with encrypted storage and secure comms for end-to-end tradecraft.

## Trust & verifiability
`trust: trusted` — a well-known, audited open-source project from the Tor ecosystem, widely relied on by journalists; trustworthy for anonymous transfer when kept updated and used with proper Tor hygiene.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | onionshare-file-sharing-tool |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
