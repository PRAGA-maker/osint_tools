---
id: moartls-analyzer
name: moarTLS Analyzer
description: Use when you have a `domain`/web page and want to spot its non-secure (HTTP) links — returns a flagged list of insecure references on the page.
url: https://chromewebstore.google.com/detail/moartls-analyzer/ldfbacdbackkjhclmhnjabngnppnkagh
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Quickly flagging every non-HTTPS link/resource on a web page you are examining.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free Chrome extension; no account or payment.
opsec: active
opsecNote: The extension inspects pages you load, so analysing a target site means your browser actually visits it — use a sock-puppet browser/VPN if the visit itself is sensitive. The analysis happens locally in your browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Open-source extension by Eric Lawrence (ericlaw); source is on GitHub and auditable, though it is a small niche utility with little recent maintenance.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- moarTLS
tags:
- Domain/IP/Links
- browser-extension
- tls
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# moarTLS Analyzer

> A Chrome extension that adds a toolbar button to flag every non-secure (HTTP) link and resource on the current page — a quick mixed-content and insecure-reference check while examining a site.

## When to use
You are examining a `domain`/web page and want to see, at a glance, which of its links and embedded resources load over plain HTTP rather than HTTPS. Insecure references can hint at neglected infrastructure, third-party hosts, or leak points worth pivoting on. It is a light triage aid during manual site review, not a person-finding tool.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install moarTLS Analyzer from the Chrome Web Store.
2. Navigate to the target page (in a sock-puppet browser if the visit is sensitive).
3. Click the moarTLS toolbar button; it scans the page and flags all non-secure (HTTP) link references.
4. Review the flagged links — note external HTTP hosts and resources as leads.
5. Pivot: take flagged third-party domains/hosts into WHOIS, DNS and infrastructure tools.

## Inputs → Outputs
- **In:** `domain`/web page currently open in the browser
- **Out:** a flagged list of the page's non-secure (HTTP) links/resources (`domain`s/URLs)
- **Empty/negative result looks like:** no flags — the page's links are all HTTPS (or the button found nothing to flag); not evidence of anything beyond good transport hygiene.

## Gotchas & OpSec
- Human-in-the-loop: none beyond clicking the button; analysis is local.
- OpSec: **active** — you must load the target page for the extension to scan it, so the visit reaches the target's server; browse via VPN/sock-puppet when that matters.
- Scope: it only reports transport security of on-page links; it is a triage hint, not a vulnerability assessment.

## Overlaps ("do both")
- Pairs with TLS/certificate and infrastructure analyzers because moarTLS only surfaces insecure links, while those inspect the certificates and hosts behind them.

## Trust & verifiability
`trust: community` — an open-source, auditable extension by a known author, but niche and lightly maintained; confirm any flagged host directly rather than relying on the flag alone.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
