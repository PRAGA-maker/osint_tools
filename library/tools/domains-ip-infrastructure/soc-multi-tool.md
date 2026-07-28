---
id: soc-multi-tool
name: SOC Multi Tool
description: Use when you have a `domain`, `ip-address`, hash or `mac-address` and want fast reputation/OSINT lookups from a right-click menu — returns VirusTotal/AbuseIPDB reputation, WHOIS and decoded values.
url: https://chromewebstore.google.com/detail/soc-multi-tool/diagjgnagmnjdfnfcciocmjcllacgkab
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: One right-click to run an IP/domain/hash through reputation and OSINT services during triage.
selectorsIn:
- domain
- ip-address
- mac-address
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free, open-source Chrome extension (by Zachary Henard); underlying VirusTotal/AbuseIPDB lookups open their web pages, which may have their own limits.
opsec: active
opsecNote: Each lookup submits the indicator to third-party services (VirusTotal, AbuseIPDB, WHOIS), so those providers — and anyone watching them — see what you're investigating. Never submit indicators that are sensitive or attacker-visible; use a research browser profile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Open-source SOC/analyst extension (~3k users, 4.9★); the developer states no data is collected. It orchestrates other services rather than holding its own data.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- scumware-org
- dr-web-anti-virus-link-checker-extension-chrome
aliases:
- SOC Multi-tool
tags:
- Domain/IP/Links
- Dorks/Pentest/Vulnerabilities
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# SOC Multi Tool

> A security-analyst right-click toolbox — highlight an IP, domain, hash or MAC and fire it through VirusTotal, AbuseIPDB, WHOIS and decoders in one menu.

## When to use
You are triaging an indicator — a `domain`, `ip-address`, file hash, or `mac-address` from a log, header or suspect message — and want its reputation and basic OSINT without hand-copying it into five sites. Built for SOC workflows; peripheral to missing-persons cases but efficient for vetting infrastructure that shows up in one.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "SOC Multi-tool" from the Chrome Web Store (open source).
2. On any page, select the indicator text (IP, domain, hash, base64/hex, filename, MAC, Windows event ID).
3. Right-click → SOC Multi-tool → pick the lookup (IP/Domain/Hash reputation via VirusTotal & AbuseIPDB, WHOIS, decode, MAC vendor, etc.).
4. Results open in new tabs.
5. Pivot: a flagged IP/domain → related indicators; a decoded string → the next selector.

## Inputs → Outputs
- **In:** `domain` / `ip-address` / hash / `mac-address` / base64-hex / filename
- **Out:** reputation verdicts (VirusTotal/AbuseIPDB), WHOIS, MAC vendor, decoded values → related `domain`/`ip-address`
- **Empty/negative result looks like:** the downstream service returns "not found"/clean or rate-limits you — that's the provider's answer, not the extension failing; treat "clean" as no-record, not proof of safety.

## Gotchas & OpSec
- Human-in-the-loop: none in the extension; downstream sites may show CAPTCHAs or rate limits.
- OpSec: **active** — indicators are sent to third-party reputation services, which is visible to them. Don't submit indicators an adversary controls or could monitor; use a research profile.
- It's a launcher: quality and coverage come from VirusTotal/AbuseIPDB/WHOIS, not from SOC Multi-tool itself.

## Overlaps ("do both")
- Pairs with `[[scumware-org]]` for a second malware-database opinion, and with `[[dr-web-anti-virus-link-checker-extension-chrome]]` for a single-vendor link verdict — together they give multi-source reputation instead of one engine's view.

## Trust & verifiability
`trust: community` — a transparent open-source analyst tool; it's trustworthy as an orchestrator, and the verdicts inherit the authority (and limits) of the services it queries.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | soc-multi-tool |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address, mac-address → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | no |
