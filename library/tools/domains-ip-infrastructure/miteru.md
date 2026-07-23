---
id: miteru
name: Miteru
description: Use when you want to hunt live phishing kits — it pulls suspicious `domain` URLs from phishing feeds and flags those exposing a downloadable kit — returning the malicious `domain`s and kit archives.
url: https://github.com/ninoseki/miteru
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Continuously detecting phishing-kit archives exposed by directory listing on freshly-reported phishing URLs.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source (MIT, ninoseki); a Ruby gem. Feeds like urlscan.io are free; heavy use may want your own API keys.
opsec: active
opsecNote: Miteru visits live phishing URLs to test for directory listing and fetch kit archives, so it makes real requests to attacker infrastructure from your IP. Run it from an isolated sock-puppet/VM environment and treat downloaded kits as malware.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: From ninoseki (author of Mitaka/Mihari), a respected threat-intel toolmaker; explicitly labelled experimental/research-only.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- ninoseki/miteru
tags:
- Domain/IP/Links
- Domain/IP investigation
- phishing
- threat-intel
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- mihari
- mitaka
---

# Miteru

> Experimental phishing-kit hunter: watches phishing feeds and flags URLs that leave their kit archive downloadable via open directory listing.

## When to use
You are doing threat-intel/anti-phishing work and want to catch the phishing kits themselves, not just the URLs. Miteru ingests freshly-reported suspicious `domain` URLs from feeds (urlscan.io, Phishing.Database, ayashige), then checks each for directory listing and the presence of a compressed kit (`.zip`/`.rar`/`.tar`). It surfaces the malicious domains that are leaking their source kit — valuable for attribution, IOC extraction, and understanding a campaign.

## How to use it (`bestInteractionPattern`: cli)
1. Install the Ruby gem: `gem install miteru` (Ruby 3.x).
2. Run the detector: `miteru execute` (add `--post-to-slack` / feed and threshold options as documented).
3. It walks the current feed URLs, tests each for open directory listing, and reports those exposing a kit archive.
4. Optionally download flagged kits for analysis — do this only in an isolated/sandboxed environment.
5. Pivot: feed detected `domain`s and kit indicators into `[[mihari]]` for ongoing tracking and `[[mitaka]]` for enrichment.

## Inputs → Outputs
- **In:** live phishing feeds (no manual selector needed) — it discovers candidate `domain` URLs itself
- **Out:** malicious `domain`s currently exposing a phishing-kit archive, plus links to those kits
- **Empty/negative result looks like:** no detections this run — the current feed URLs either aren't listing directories or are already down; phishing infra is short-lived, so re-run frequently.

## Gotchas & OpSec
- OpSec: **active and higher-risk** — you're touching live attacker sites and pulling malware; use an isolated VM, sock-puppet IP, and handle kits as hostile.
- Labelled experimental — expect feed/format churn and false positives.
- Time-sensitive: phishing sites vanish fast, so a URL that listed a kit minutes ago may already be gone.

## Overlaps ("do both")
- Pairs with `[[mihari]]` and `[[mitaka]]` (same author) — Miteru discovers exposed kits, Mihari persists and tracks the indicators over time, and Mitaka enriches any single indicator on demand.

## Trust & verifiability
`trust: community` — open source from a well-regarded threat-intel author, but self-described as experimental; detections are leads to verify, and everything it fetches is untrusted attacker content.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | miteru |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
