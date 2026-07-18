---
id: tor-download
name: Tor Browser Download
description: Use when you need to reach .onion sites or browse anonymously for an investigation — the official source for verified Tor Browser installers across platforms.
url: https://www.torproject.org/download/
category: dark-web
path:
- dark-web
- clients
bestFor: Obtaining the genuine, signature-verifiable Tor Browser so you can access dark-web (.onion) sites safely and anonymously.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source; no account. Available for Windows, macOS, Linux, and Android (and via alternative mirrors/GetTor if the site is blocked).
opsec: passive
opsecNote: Downloading Tor Browser from a network that monitors you reveals that you use Tor (not what you do with it) — an adversary may flag it. Download over a trusted connection/VPN if that matters, and ALWAYS verify the GPG signature to avoid a trojaned build. Tor protects the browsing that follows; the download itself is ordinary web traffic.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: The official Tor Project site — the authoritative, first-party source for Tor Browser. Signatures/checksums are published so you can cryptographically verify the binary.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- exonerator
- exonerator-ip-address-checker
- tor-browser
- tor-project
aliases:
- Tor Browser
- Tor Project download
tags:
- tor
- dark-web
- anonymity
- arf-seed
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Tor Browser Download

> The official Tor Project download page — the one trustworthy place to get Tor Browser, the client you need to reach .onion services and browse anonymously during an investigation.

## When to use
Any time an investigation points to the dark web — a leaked-data market, a forum, a paste, or an .onion link surfaced by another tool — you need Tor Browser to open it, and you need a version you can trust. This is the prerequisite/utility step: get the genuine client, verify it, and use it as the anonymized viewport for `.onion` `domain`s. Also the right download when you simply want to separate sensitive OSINT browsing from your real IP/identity.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Go to https://www.torproject.org/download/ and pick your platform (Windows / macOS / Linux / Android).
2. Download the installer **and** its `.asc` signature file.
3. Verify the signature (GPG, or the built-in verification instructions) so you know the binary wasn't tampered with — do not skip this.
4. Install and launch Tor Browser; connect to the Tor network (use a bridge if Tor is blocked on your network).
5. Paste an `.onion` address to reach the hidden service, or browse the clear web with your origin IP hidden.
6. If torproject.org is blocked, use GetTor (email/mirrors) to obtain a verified copy.

## Inputs → Outputs
- **In:** platform choice (and later, an `.onion` `domain` to visit)
- **Out:** a verified Tor Browser install that reaches `.onion` `domain`s anonymously
- **Empty/negative result looks like:** the download page is unreachable (Tor is censored on your network) — switch to GetTor or a mirror; a failed signature check means the file is compromised — discard it and re-download.

## Gotchas & OpSec
- **Always verify the signature** — a maliciously modified Tor Browser is a classic deanonymization trap.
- Merely downloading/using Tor is observable to your network operator (they see "uses Tor," not the content); use a bridge/VPN if that itself is sensitive.
- Tor anonymizes the browser, not sloppy behavior — don't log into personal accounts or enable risky plugins inside it.
- This entry is a client/utility, not a data source; the intelligence comes from where you go next.

## Overlaps ("do both")
- Pairs with `[[exonerator]]` (check whether an IP was a Tor exit node) and dark-web indexing/search tools — get and verify the client here, then use those to find and vet the `.onion` destinations.

## Trust & verifiability
`trust: trusted` — the first-party Tor Project distribution, and uniquely verifiable: published GPG signatures let you cryptographically confirm the binary before you run it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tor-download |
| category | dark-web |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
