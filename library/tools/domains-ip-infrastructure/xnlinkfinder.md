---
id: xnlinkfinder
name: xnLinkFinder
description: Use when you have a target `domain`/URL and want to discover its endpoints, parameters, and leaked secrets — returns a list of discovered links/endpoints (and a target wordlist) from crawling, JS, and archives.
url: https://github.com/xnl-h4ck3r/xnLinkFinder
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Extracting endpoints, parameters, and potential secrets for a target by crawling it and mining JS/HAR/archive/Burp data — attack-surface and hidden-endpoint discovery.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source; pip-installable Python 3 CLI. No account or key required (though pulling archive data may use optional free sources).
opsec: active
opsecNote: Crawling mode connects directly to the target and can generate noticeable traffic/logs; passive modes (parsing existing JS/HAR/Burp/waymore output) touch nothing new. Prefer the passive inputs for stealth, and run active crawling from a sock-puppet host when needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular, actively maintained OSS by xnl-h4ck3r (1.6k+ stars); community-trusted. Output is raw discovered strings — expect noise and validate endpoints before acting.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- waymore
- burp-suite
- crt-sh
aliases:
- xnLinkFinder
- xnl-h4ck3r linkfinder
tags:
- Domain/IP/Links
- Dorks/Pentest/Vulnerabilities
- endpoint-discovery
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# xnLinkFinder

> A versatile endpoint/link discovery tool: point it at a target (or at your Burp/HAR/wayback data) and it mines out endpoints, parameters, a target-specific wordlist, and possible secrets.

## When to use
You're mapping the attack surface of a target `domain` — its API endpoints, hidden paths, parameters, and any secrets accidentally exposed in JavaScript. xnLinkFinder both crawls live and parses data you already have (Burp/ZAP/Caido exports, HAR files, `waymore` archive output), making it strong at pulling endpoints out of JS and archived responses. It's an infrastructure-recon tool; missing-persons relevance is indirect (deep analysis of a subject's own site/app).

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install xnLinkFinder` (or clone the repo).
2. Choose an input with `-i`:
   - a live domain/URL to **crawl** (active), or
   - a directory of JS files, a HAR file, a Burp/ZAP/Caido project, or a `waymore` results dir (passive).
3. Run e.g. `xnLinkFinder -i https://target.com -sf target.com -o endpoints.txt` (`-sf` scopes to the target; `-o` writes output).
4. Review outputs: discovered endpoints, potential parameters, a target-specific wordlist, and flagged secrets (JSON). Expect false positives — validate before use.
5. Pivot: feed endpoints into `[[burp-suite]]` for hands-on inspection; pair with `[[waymore]]` upstream to supply archived URLs, and `[[crt-sh]]` for related hosts.

## Inputs → Outputs
- **In:** `domain`/URL (crawl) or files (JS dir, HAR, Burp/ZAP/Caido export, waymore output).
- **Out:** `domain`/endpoint list — discovered endpoints, parameters, a wordlist, and possible secrets.
- **Empty/negative result looks like:** few/no endpoints — a static site with little JS, an out-of-scope filter, or an input source with nothing to parse. Not necessarily a failure.

## Gotchas & OpSec
- Human-in-the-loop: none, but results need triage — raw discovered strings include noise, duplicates, and false-positive "secrets."
- OpSec: **active** in crawl mode (direct hits, logs, possible WAF alerts); fully **passive** when parsing existing Burp/HAR/waymore data. Prefer passive inputs for stealth; run active crawls from a sock-puppet host.
- Only test targets you're authorised to; endpoint discovery shades into active recon.

## Overlaps ("do both")
- Pairs with `[[waymore]]` — waymore harvests archived URLs/responses; feed its output into xnLinkFinder to extract endpoints passively without touching the live target.
- Feeds `[[burp-suite]]` — validate and interact with discovered endpoints in Burp's proxy/repeater.

## Trust & verifiability
`trust: community` — well-regarded, actively maintained OSS. The tool is reliable; its *output* is raw and noisy, so verify each endpoint/secret before drawing conclusions or acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | xnlinkfinder |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
