---
id: keyfinder
name: keyFinder
description: Use when you have a `domain` and want to catch secrets it leaks in front-end code — scans a site's pages/JS and returns exposed API keys, tokens and credentials.
url: https://github.com/momenbasel/keyFinder
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Finding API keys, tokens and secrets accidentally exposed in a website's client-side source/JavaScript.
selectorsIn:
- domain
selectorsOut:
- password
status: live
pricing: free
costNote: Free and open-source (MIT) on GitHub; no account required.
opsec: active
opsecNote: keyFinder fetches the target site's pages/JavaScript to scan them, so requests come from your IP and are visible to the target's logs/CDN. It's active recon — proxy it and only scan sites you're authorised to assess. Any keys found are live credentials; handle and report them responsibly, never use them.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A community security tool (momenbasel); it pattern-matches for known secret formats, so results include false positives and require manual confirmation. Audit the code before running.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- keyFinder
- momenbasel keyFinder
tags:
- other-tools
- secrets-detection
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# keyFinder

> A secret-hunter for websites: point it at a domain and it combs the pages and JavaScript for exposed API keys, tokens and credentials that developers left in the client-side code.

## When to use
You're assessing a `domain`'s exposure and want to know whether its front-end leaks secrets — cloud API keys, payment tokens, third-party service credentials embedded in bundled JavaScript. These leaks are common and directly actionable in a security/recon context, and finding them can also reveal which services and vendors a target relies on.

## How to use it (`bestInteractionPattern`: cli)
1. Get keyFinder from https://github.com/momenbasel/keyFinder (clone the repo; some versions ship as a browser extension — use whichever the current README documents).
2. Run it against the target `domain`/URL so it fetches and scans the site's pages and linked JavaScript.
3. Read the flagged matches: the secret type (e.g. AWS key, Google API key, Stripe token) and where it appeared.
4. Manually verify each hit — pattern matches produce false positives (example keys, placeholders).
5. Pivot: a leaked third-party key reveals which services the target uses (feeding infra mapping); confirmed leaks are a report-worthy finding.

## Inputs → Outputs
- **In:** `domain` (a site/URL to scan)
- **Out:** exposed secrets — API keys/tokens/credentials (`password`-class secrets) with their location
- **Empty/negative result looks like:** no matches — the site may genuinely expose nothing client-side, load secrets only server-side, or use formats the tool doesn't recognise; absence isn't a guarantee of good hygiene.

## Gotchas & OpSec
- **Active:** it requests the target's assets from your IP — proxy and stay in scope.
- **False positives:** regex-based detection flags placeholders and example keys; confirm every hit before acting or reporting.
- Found credentials are real and sensitive — do not test or use them; report through the proper channel.

## Overlaps ("do both")
- Complements recon/scraping tools like [[rextract]] (custom regex over pages) and site fingerprinters — keyFinder specialises in secret patterns, the others give you the broader source and stack picture.

## Trust & verifiability
`trust: community` — an open, inspectable security tool; it introduces no external data, so every "hit" is verifiable by looking at the flagged source location yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | keyfinder |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain → password |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
