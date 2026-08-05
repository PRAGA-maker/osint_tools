---
id: sdorker
name: SDorker
description: Use when you have a Google dork query and want the resulting page list from the terminal — returns URLs matching the dork (with optional basic vuln flags).
url: https://github.com/TheSpeedX/SDorker
category: search-engines
path:
- search-engines
bestFor: Running Google dork queries from the CLI and collecting the matching URLs in bulk.
selectorsIn:
- name
selectorsOut:
- domain
- social-profile
status: degraded
pricing: free
costNote: Free and open-source; clone from GitHub. Note it is written in Python 2 (end-of-life), so it needs a legacy interpreter and may need fixes to run today.
opsec: active
opsecNote: Active — it issues automated Google queries from your IP. Google aggressively rate-limits and CAPTCHAs scripted dorking, and running many queries can flag/temporarily block your address. Route through a proxy/VPN and go slow; scraping search results also breaches Google's ToS.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: cli
trust: community
trustNote: A small community script (TheSpeedX) marked educational-only; unmaintained Python 2 code that includes basic SQLi/vuln checks, so review it before running and confine to authorised targets.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- SDorker
tags:
- Tools for Google
- google-dorking
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# SDorker

> A terminal Google-dork runner: give it a dork, it returns the pages Google surfaces for it (and optionally flags basic SQLi/XSS/LFI candidates).

## When to use
You have a crafted Google dork — a `site:`/`inurl:`/`intext:` query targeting a `name`, username, document type, or exposed path — and want the matching URLs collected in bulk from the command line instead of clicking through pages. Handy for sweeping for a subject's exposed documents, profiles, or leaked pages. The vuln-scanning side is offensive and out of scope for pure OSINT.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `github.com/TheSpeedX/SDorker`, make the script executable, and run `./SDork` (works on Linux/Termux). Expect to need a Python 2 interpreter and possibly minor fixes — it is EOL code.
2. Enter your Google dork and how many result pages to fetch (~10 sites per page).
3. Read the collected URL list — the pages Google returned for the dork.
4. Triage the URLs by hand for relevance to your subject; ignore the automated vuln checks unless you have authorisation to test.
5. Pivot: relevant `domain`s/`social-profile` URLs feed further OSINT (WHOIS, profile enrichment, document metadata).

## Inputs → Outputs
- **In:** a Google dork string (encoding a `name`/keyword/path)
- **Out:** a list of result URLs — `domain`s and `social-profile`/document links
- **Empty/negative result looks like:** an empty list or an immediate CAPTCHA/`429` block — Google refused the automated query. That means "blocked," not "nothing exists"; run the same dork manually in a browser to confirm.

## Gotchas & OpSec
- Python 2 EOL: it may not run out of the box on a modern system without tweaks; consider running the dork by hand or with a maintained dorking tool instead.
- Google blocks scripted dorking fast (rate limits, CAPTCHAs, temp IP bans) and it violates Google ToS.
- The bundled SQLi/vuln checks are active exploitation tooling — only against systems you are authorised to test.
- OpSec: active queries from your IP; use a proxy/VPN and low volume.

## Overlaps ("do both")
- Same intent as building queries with `[[boolean-builder-thebalazs]]` and running them manually — that route is more reliable against Google's anti-automation than an EOL scraper; use SDorker only when you want bulk CLI collection and accept the friction.

## Trust & verifiability
`trust: community` — an unmaintained educational script; read the source before running, keep the vuln features off unless authorised, and confirm any interesting dork result directly in a browser.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sdorker |
