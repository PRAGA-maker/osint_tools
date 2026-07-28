---
id: darknet-market-list
name: Darknet Market List (DarknetLive)
description: Use when you need a current, clearweb-readable list of active darknet markets and their onion addresses for investigation — a directory; returns domain (onion) and marketplace leads.
url: https://darknetlive.com/markets/
category: dark-web
path:
- dark-web
bestFor: Getting an up-to-date, curated list of live darknet markets and verified onion links from the clear web.
selectorsIn: []
selectorsOut:
- domain
status: live
pricing: free
costNote: Free to read on the clear web (DarknetLive). Actually visiting the listed markets requires Tor and is a separate, higher-risk step.
opsec: active
opsecNote: Reading the DarknetLive list on the clear web is low-risk, but ACTING on it is not — connecting to any listed onion market over Tor exposes you to malware, scam/phishing clones, and law-enforcement-monitored infrastructure, and may be illegal to browse in some contexts. Only proceed with Tor from an isolated, disposable, non-attributable environment (e.g. Tails/Whonix), never your normal machine, and only within an authorised investigation.
humanInLoop: true
humanInLoopReason:
- legal-gate
bestInteractionPattern: web-manual
trust: community
trustNote: DarknetLive is a well-known clear-web darknet-news/directory site. Its market list is curated but unofficial; onion links are frequently cloned/phished by scammers, so a listing is a lead, not a safety guarantee.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- darkweb-forums
- onions-darknetlive
- ahmia
tags:
- dark-web
- darknet-markets
- onion
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Darknet Market List (DarknetLive)

> A clear-web, regularly-updated directory of currently-active darknet markets with their (claimed) onion addresses — the reconnaissance layer before any Tor work.

## When to use
Your investigation touches darknet commerce (a vendor handle, a listing screenshot, a seized-market reference) and you need to know which markets are currently live and their addresses — without hunting through Tor blind. Useful for orienting; the actual market visit is a deliberate, higher-risk follow-up.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://darknetlive.com/markets/ on the clear web to read the current list, statuses (up/down/seized), and notes.
2. Note market names, statuses, and the listed onion URLs as leads.
3. Cross-check an onion address against multiple sources before trusting it — phishing clones are rampant.
4. If (and only if) authorised, connect via Tor from an isolated, disposable environment — never your normal system.
5. Pivot: a vendor handle → username search; a market's forum → `[[darkweb-forums]]`; discover onions via `[[ahmia]]`.

## Inputs → Outputs
- **In:** none (browse) — or a market name you're checking
- **Out:** `domain` (onion addresses) and market status/leads
- **Empty/negative result looks like:** a market marked down/seized or absent — the darknet market scene churns fast, so "not listed" means check other trackers, and a listed link may still be a scam clone.

## Gotchas & OpSec
- **The list is safe to read; the markets are not.** Treat visiting any onion as a discrete, authorised, high-risk action from Tails/Whonix only.
- Onion phishing clones are everywhere — verify addresses across sources; a DarknetLive listing is not a safety endorsement.
- Legal exposure varies by jurisdiction and action — stay within an authorised investigation (`legal-gate`).

## Overlaps ("do both")
- Pairs with `[[ahmia]]` (onion search) and `[[darkweb-forums]]` for the community/vendor side; `[[onions-darknetlive]]` for DarknetLive's broader onion directory.

## Trust & verifiability
`trust: community` — a reputable but unofficial darknet news/directory. Good for current status and orientation; independently verify any onion address and never treat a listing as vouching for safety or legality.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | darknet-market-list |
| category | dark-web |
| selectorsIn → selectorsOut | (browse) → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (legal-gate) |
