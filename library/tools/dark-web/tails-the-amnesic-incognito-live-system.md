---
id: tails-the-amnesic-incognito-live-system
name: Tails — The Amnesic Incognito Live System
description: Use when you need a disposable, anonymous investigation OS that leaves no trace and routes everything through Tor — an OpSec platform, not a lookup tool.
url: https://tails.net/
category: dark-web
path:
- dark-web
bestFor: A bootable, amnesic, Tor-routed live OS for anonymous, trace-free browsing (incl. .onion) during sensitive investigations.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source (part of the Tor ecosystem). You supply a USB stick; no cost or account.
opsec: active
opsecNote: Tails is itself an OpSec control — it forces all traffic through Tor and forgets everything on shutdown, so your investigation leaves no local trace and your real IP is hidden from sites you visit. Caveats — logging into a personal/attributable account inside Tails deanonymises you anyway, and the exit-node/site still sees a Tor connection. Use dedicated sock-puppet accounts only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Reputable, long-established, open-source project audited by the security community and tied to the Tor Project. The anonymity guarantees hold only if you follow its guidance (no personal logins, no persistence of identifiers).
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Tails
- The Amnesic Incognito Live System
tags:
- darkweb
- Dark Web Links
- anonymity
- opsec
source: uk-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Tails — The Amnesic Incognito Live System

> A bootable "live" operating system that routes everything through Tor and forgets everything on shutdown — the standard OpSec platform for anonymous, trace-free investigation, including the dark web.

## When to use
You're conducting sensitive research where attribution or local traces are unacceptable — viewing hostile infrastructure, browsing `.onion` sites, or working a case where your real IP/machine must never be exposed. Tails isn't a search tool; it's the *safe environment* you run your other tools and browsing inside. Boot it, work anonymously, shut down, leave nothing behind.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download Tails from https://tails.net/ and **verify the download** (signature/checksum) — this matters, since a tampered image would defeat the purpose.
2. Write it to a USB stick with the official installer and boot your machine from it.
3. Connect to the network; Tails forces all traffic through Tor. Use the bundled Tor Browser for both clearnet and `.onion` browsing.
4. Do your work with **sock-puppet identities only** — never log into any personal/attributable account, which would deanonymise the whole session.
5. Shut down: Tails is amnesic and wipes RAM, so nothing persists (unless you deliberately configured encrypted Persistent Storage). Capture any evidence to encrypted storage *before* shutdown.

## Inputs → Outputs
- **In:** N/A — it's an operating environment, not a query tool
- **Out:** an anonymous, amnesic workspace; your outward IP appears as a Tor exit node
- **Empty/negative result looks like:** N/A — success is simply that the session leaves no local trace and your real IP was never exposed.

## Gotchas & OpSec
- **One personal login blows it** — authenticating to any account tied to you links the anonymous session back to you. Sock puppets only.
- Sites still see a *Tor* connection (some block Tor, some flag it); anonymity ≠ invisibility.
- Verify the image before use; skipping verification undermines every guarantee.
- Amnesia cuts both ways: save evidence to encrypted Persistent Storage/external media before powering off, or it's gone.

## Overlaps ("do both")
- The environment you run other tooling inside — e.g. use Tails as the anonymous base for dark-web search engines and sensitive browsing rather than your daily machine.

## Trust & verifiability
`trust: trusted` — a mature, community-audited, open-source anonymity system from the Tor ecosystem. Its guarantees are strong *if* you follow the operational rules (verified image, no personal logins, deliberate handling of persistence).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tails-the-amnesic-incognito-live-system |
| category | dark-web |
| selectorsIn → selectorsOut | (none) → (none) |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | no |
