---
id: sputnik
name: Sputnik
description: Use when you have a `domain`, `ip-address`, URL, or file hash on any page and want to fan it out across dozens of OSINT services — right-click to pull reputation, hosting, and threat data in one action.
url: https://chrome.google.com/webstore/detail/sputnik/manapjdamopgbpimgojkccikaabhmocd/related
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: One-right-click enrichment of a highlighted IP/domain/URL/hash across VirusTotal, Shodan, Censys, GreyNoise, AbuseIPDB and ~20 more OSINT services.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free, open-source browser extension (mitchmoser/sputnik); some destination services (Shodan, Censys, VirusTotal) may need their own free account for full results.
opsec: passive
opsecNote: Sputnik itself is a launcher — it opens the third-party service in a tab rather than querying the target directly, so it's passive toward the subject. But every service you fan out to sees the artifact and logs the lookup; you're broadcasting your interest to many vendors at once, so use a research browser profile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Popular open-source OSINT extension by Mitch Moser; it only forwards artifacts to well-known public services, so trust rests on those downstream sources, not on Sputnik itself.
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
- Sputnik OSINT extension
tags:
- Domain/IP/Links
- Domain/IP investigation
- browser-extension
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Sputnik

> A right-click OSINT launcher: highlight any IP, domain, URL, or file hash on a page and blast it to ~25 reputation and infrastructure services without copy-pasting.

## When to use
You're reading a page — a WHOIS record, an email header, a paste, a log — and spot a `domain`, `ip-address`, URL, or hash you want to enrich. Instead of manually opening VirusTotal, Shodan, Censys, GreyNoise, AbuseIPDB, SecurityTrails, URLhaus, etc. one at a time, Sputnik turns the selection into a right-click menu that jumps straight to any of them. It's a speed layer over infrastructure/threat OSINT, not a data source of its own.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install Sputnik from the Chrome Web Store (the linked webstore URL redirects to the new `chromewebstore.google.com` listing); a Firefox build also exists.
2. On any page, select the artifact — an IP, domain, URL, or file hash.
3. Right-click the selection and open the **Sputnik** context menu; pick a service (grouped by artifact type).
4. Sputnik opens that service's results for the artifact in a new tab. For services needing a captcha/login, it copies the artifact to your clipboard instead so you can paste it.
5. Work down the relevant services to triangulate: e.g. Shodan for open ports, Censys for certs, GreyNoise for scanner noise, AbuseIPDB for abuse history.

## Inputs → Outputs
- **In:** `domain`, `ip-address`, URL, or file hash (highlighted text)
- **Out:** whatever the chosen service returns — hosting/`ip-address`, passive DNS `domain` history, reputation, open ports, certificates
- **Empty/negative result looks like:** the service opens with "no results / not found" — the artifact is unknown to that source; try another service before concluding it's clean.

## Gotchas & OpSec
- Sputnik doesn't fetch anything itself; the *destination* services do the lookup, so accuracy and freshness are theirs, not Sputnik's.
- Some services require their own accounts/API keys for full data — Sputnik just gets you to the query.
- You're revealing the artifact to many vendors quickly; do it from a compartmentalised research profile, not a personal browser.
- Right-clicking a live URL into a scanner that *fetches* the page (e.g. urlscan) becomes active toward that target — know which services fetch vs. look up cached data.

## Overlaps ("do both")
- Overlaps with other right-click OSINT extensions (e.g. Mitaka) — they cover slightly different service lists, so investigators often keep both and use whichever has the source they need.

## Trust & verifiability
`trust: community` — open-source and widely used; it adds no data of its own, so verifiability is inherited from the authoritative services it links to.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sputnik |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
