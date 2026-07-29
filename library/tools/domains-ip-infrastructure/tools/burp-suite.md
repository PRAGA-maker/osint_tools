---
id: burp-suite
name: Burp Suite
description: Use when you need to intercept, inspect, and manipulate a web app's HTTP(S) traffic to understand or test it — returns a full proxy view of requests/responses plus manual testing tools.
url: https://portswigger.net/burp
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- tools
bestFor: Intercepting and analysing web/app traffic as a proxy — seeing the API calls, cookies, tokens and hidden endpoints behind a site during investigation or testing.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Burp Suite Community Edition is free (manual proxy, repeater, decoder). Professional/DAST editions (automated scanning) are paid. The free edition covers most investigative proxy work.
opsec: active
opsecNote: Interception is passive, but Burp's active scanner, intruder, and repeated requests hit the target server directly, generate heavy logs, and can trip WAF/IDS alerts — only run active tooling against systems you're authorised to test. Route through a sock-puppet IP where appropriate.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Industry-standard web-security toolkit by PortSwigger; the Community Edition is legitimate first-party software. "Trusted" as a tool — findings still require your interpretation.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- owasp-zap
- xnlinkfinder
aliases:
- Burp
- Burp Suite Community Edition
- PortSwigger Burp
tags:
- web-proxy
- pentest
- traffic-analysis
- Dorks/Pentest/Vulnerabilities
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# Burp Suite

> The standard web-security proxy: sit between your browser and a target site to see, capture, and modify every request/response — and reveal the API calls and endpoints a page uses under the hood.

## When to use
You need to understand how a website or mobile app actually talks to its backend — the hidden API endpoints, the tokens/cookies it sends, the JSON it returns, the parameters you could vary. In an OSINT/investigative context, Burp's intercepting proxy exposes data a page fetches but never displays, and surfaces endpoints worth pivoting on. It's an infrastructure/testing tool, not a person-lookup; missing-persons relevance is indirect (deep analysis of a subject's own site/app).

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download **Burp Suite Community Edition** (free) from https://portswigger.net/burp and launch it.
2. Configure your browser (or use Burp's built-in browser) to proxy through Burp; install Burp's CA cert to see HTTPS.
3. Browse the target normally — every request/response appears in **Proxy → HTTP history**. Read the API calls, auth tokens, and endpoints.
4. Use **Repeater** to hand-modify and resend a request and study responses; use **Decoder** for encoded values. (Automated **Scanner/Intruder** are Pro-only and actively hit the target — use only with authorisation.)
5. Pivot: feed discovered endpoints/hostnames into `[[xnlinkfinder]]` for broader endpoint discovery, and extract any leaked selectors (emails, IDs) from responses into your normal enrichment chain.

## Inputs → Outputs
- **In:** `domain`/URL of the web app whose traffic you proxy.
- **Out:** `domain`/endpoint inventory — the full request/response history, hidden API endpoints, cookies, tokens, and any data embedded in responses.
- **Empty/negative result looks like:** no HTTP history (proxy/cert misconfigured) or a fully static site with no interesting backend calls — the latter just means there's little dynamic traffic to analyse.

## Gotchas & OpSec
- Human-in-the-loop: none, but interpreting traffic takes skill.
- OpSec: interception is **passive**, but Repeater/Intruder/Scanner send real, repeated, sometimes malicious-looking requests to the target — heavy logs and WAF/IDS alerts. Only run active features against systems you have permission to test; there are legal lines here.
- HTTPS interception needs Burp's CA installed in the browser — don't leave it trusted in your everyday profile.
- Community Edition throttles/omits automation; that's fine for observation, not for large-scale scanning.

## Overlaps ("do both")
- Overlaps with `[[owasp-zap]]` — a free, open-source intercepting proxy with automated scanning included; use ZAP when you want free automation, Burp for its superior manual workflow.
- Feeds `[[xnlinkfinder]]` — export Burp project files into xnLinkFinder to mine endpoints/parameters at scale.

## Trust & verifiability
`trust: trusted` — legitimate, industry-standard first-party software from PortSwigger. The tool is reliable; conclusions still depend on how you read the traffic, and active use carries authorisation/legal obligations.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | burp-suite |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | no |
