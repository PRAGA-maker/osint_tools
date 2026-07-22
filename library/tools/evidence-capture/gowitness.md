---
id: gowitness
name: gowitness
description: Use when you have a list of `domain`s/`ip-address`es and want to bulk-screenshot their web interfaces for visual triage and evidence — returns `image` captures plus page `metadata-exif` (headers, tech).
url: https://github.com/sensepost/gowitness
category: evidence-capture
path:
- evidence-capture
bestFor: Bulk-screenshotting lists of URLs/hosts to visually triage and preserve a subject's web presence as evidence.
selectorsIn:
- domain
- ip-address
selectorsOut:
- image
- metadata-exif
status: live
pricing: free
costNote: Free and open-source (Go); runs locally with headless Chrome, no account.
opsec: active
opsecNote: gowitness loads each target in headless Chrome, so it makes real HTTP requests the target can log. Screenshotting a large list is noisy; throttle, and route through a VPN/proxy when capturing a subject's own sites.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: SensePost (Orange Cyberdefense) project, actively released (v3.x, 4k+ stars).
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- frack
aliases:
- gowitness
tags:
- screenshot
- recon
- evidence
- headless-chrome
source: gh-topic-footprinting
lastVerified: '2026-07-22'
enrichment: full
---

# gowitness

> A headless-Chrome bulk web-screenshot tool — used in OSINT to capture and preserve a subject's web presence (sites, profile pages, panels) as image evidence at scale.

## When to use
You have many `domain`s/`ip-address`es/URLs (e.g. a subject's sites plus discovered subdomains, or a hosting range) and want a fast visual index: what's actually live, what each page looks like, and a timestamped screenshot for the case file. Better than clicking each by hand and it records headers/tech alongside the image.

## How to use it (`bestInteractionPattern`: cli)
1. Install the binary from the releases page (or `go install`), with Chrome/Chromium present.
2. Screenshot a single target: `gowitness scan single --url https://example.com`; or a file of hosts: `gowitness scan file -f urls.txt`.
3. Browse results in the built-in report UI (`gowitness report server`) or the SQLite/JSON/CSV output — each entry has the `image` plus captured headers, tech and cookies.
4. Pivot: use the visual triage to prioritise which live hosts to investigate; keep the screenshots as dated evidence.

## Inputs → Outputs
- **In:** `domain` / `ip-address` / URL list (or Nmap/Nessus output)
- **Out:** `image` screenshots + `metadata-exif`-style page data (headers, tech, cookies), stored in SQLite/JSON/CSV
- **Empty/negative result looks like:** blank/error screenshots for hosts that are down, non-HTTP, or blocking headless Chrome — not proof the host is dead.

## Gotchas & OpSec
- **Active** — each capture is a real page load the target can see; large runs are conspicuous. Throttle and anonymise for sensitive subjects.
- Sites that block headless Chrome or require login render as errors/login walls; note this rather than treating them as empty.
- Capture-time timestamps matter for evidentiary use — preserve the output DB, don't just export images.

## Overlaps ("do both")
- Pairs with subdomain/asset discovery (feed its output list in) and with `[[frack]]`-style capture tools: discovery finds the hosts, gowitness turns them into a browsable visual evidence set.

## Trust & verifiability
`trust: trusted` — maintained by a reputable security vendor and widely used; the screenshots are direct captures, so evidentiary value is high when you preserve the original output.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gowitness |
| category | evidence-capture |
| selectorsIn → selectorsOut | domain, ip-address → image, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
