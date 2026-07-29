---
id: s-i-g-i-t
name: S.I.G.I.T.
description: Use when you have a `name`, `username`, `phone`, `ip-address`, or `domain` and want a quick multi-tool recon pass — bundles username checks, mail/phone lookup, dorking, DNS/WHOIS, and IP geolocation.
url: https://github.com/termuxhackers-id/SIGIT
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: One CLI menu that runs common OSINT modules (userrecon, mailfinder, phoneinfo, dnslookup, iplocation) on Termux or Kali.
selectorsIn:
- username
- name
- phone
- ip-address
- domain
selectorsOut:
- social-profile
- email
- ip-address
- geolocation
status: live
pricing: free
costNote: Free and open-source; installs via a shell script on Termux or Kali. No account needed for the core modules.
opsec: active
opsecNote: Some modules (reverse IP, host/DNS lookups) query third-party APIs and the facedumper module needs your own Facebook cookies — those touch external services and, for facedumper, log you into Facebook. Run from a sock-puppet environment and avoid modules that require your real credentials.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: unverified
trustNote: A community Termux/Kali toolkit that shells out to various third-party sites/APIs; it aggregates other services rather than holding its own data, and those upstreams can change or break at any time.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools: []
aliases:
- SIGIT
- Simple Information Gathering Toolkit
tags:
- Code
- osint-toolkit
- termux
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# S.I.G.I.T.

> A menu-driven CLI that packages a dozen common recon modules — username checks, mail/phone lookup, Google dorking, DNS/WHOIS, IP geolocation — for fast triage on Termux or Kali.

## When to use
You have an early selector — a `username`, `name`, `phone`, `ip-address`, or `domain` — and want to sweep it through several quick lookups without wiring up each tool separately. SIGIT's menu (userrecon, mailfinder, phoneinfo, godorker, dnslookup, whoislookup, riplookup, iplocation, and more) is a convenient first-pass triage that points you toward whichever thread is worth pursuing with a dedicated tool.

## How to use it (`bestInteractionPattern`: cli)
1. Install:
   - Termux: `pkg install wget && wget https://raw.githubusercontent.com/termuxhackers-id/SIGIT/main/install.sh && bash install.sh`
   - Kali: `apt-get install wget && wget https://raw.githubusercontent.com/termuxhackers-id/SIGIT/main/installkali.sh && bash installkali.sh`
2. Run `sigit` to open the menu and pick a module.
3. Feed the module its input (username, name, phone, IP, or domain) and read the result.
4. Skip modules that demand your own credentials (e.g. facedumper needs your Facebook cookies) unless you have a burner account.
5. Pivot: a hit in `userrecon` → dedicated username tools; `iplocation`/`riplookup` → infrastructure OSINT; `mailfinder` → email verification.

## Inputs → Outputs
- **In:** `username`, `name`, `phone`, `ip-address`, or `domain` (per module)
- **Out:** `social-profile` hits, candidate `email`s, `ip-address`/`geolocation` and DNS/WHOIS data
- **Empty/negative result looks like:** a module returns nothing or errors — often because the upstream site/API it calls has changed or rate-limited; confirm the finding with a purpose-built tool before trusting it.

## Gotchas & OpSec
- Human-in-the-loop: some modules require logins/cookies (facedumper) or manual review of aggregated output.
- OpSec: **active** — several modules call third-party services that log queries, and credential-based modules log you in. Use a sock-puppet environment; avoid any module that would expose your real identity.
- It aggregates other people's services, so reliability is only as good as those upstreams; treat it as a convenience wrapper, not an authoritative source.
- Menu tools like this age quickly — verify a module still works before relying on its output in a report.

## Overlaps ("do both")
- Overlaps heavily with dedicated single-purpose tools (Sherlock/WhatsMyName for usernames, holehe for emails, IP geolocation services). Use SIGIT to *triage* which selector is productive, then confirm with the specialized tool that module wraps.

## Trust & verifiability
`trust: unverified` — a community aggregator that shells out to changeable third-party endpoints; never rely on a single SIGIT module for a conclusion — corroborate with the authoritative source behind it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | s-i-g-i-t |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | username, name, phone, ip-address, domain → social-profile, email, ip-address, geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login) |
