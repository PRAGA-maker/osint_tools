---
id: dr-web-anti-virus-link-checker-extension-chrome
name: Dr Web Anti-Virus Link Checker Extension (Chrome)
description: Use when you have a suspicious `domain`/link and want to scan it for malware or phishing before you click — returns a safe/malicious verdict.
url: https://chromewebstore.google.com/detail/drweb-anti-virus-link-che/aleggpabliehgbeagmfhnodcijcmbonb
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Vetting a link or small download for malware/phishing from the browser context menu before opening it.
selectorsIn:
- domain
selectorsOut: []
status: live
pricing: free
costNote: Free Chrome extension from Dr.Web; no account required.
opsec: active
opsecNote: Scanning a link sends that URL to Dr.Web's cloud, so the vendor sees which addresses you check — do not scan links whose existence is sensitive to your investigation. It also loads/scans the target for you, which can touch the destination server.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: trusted
trustNote: Published by Doctor Web (Dr.Web), an established antivirus vendor; ~60k users, 4.4★. Verdicts reflect Dr.Web's own reputation engine.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- soc-multi-tool
aliases:
- Dr.Web Link Checker
tags:
- toddington
- curated-directory
- add-ons-apps-extensions
source: toddington-resources
lastVerified: '2026-07-28'
enrichment: full
---

# Dr Web Anti-Virus Link Checker Extension (Chrome)

> A browser-context malware/phishing screener — right-click any link and let Dr.Web's cloud tell you whether it's dangerous before you visit it.

## When to use
You are chasing a lead through untrusted territory (paste sites, forums, shortened links, dark-web mirrors, a suspect's shared file) and want to check whether a `domain`/URL or a small download is malicious before opening it on your investigation machine. This is an OpSec/hygiene tool, not a data-yielding OSINT source.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Dr.Web Link Checker" from the Chrome Web Store.
2. Right-click a hyperlink (or a page) and choose the Dr.Web "scan link" context-menu item.
3. The extension submits the URL to Dr.Web and returns a verdict: clean, or flagged (phishing/malware).
4. It can also scan files up to ~12 MB before they are saved.
5. Act on the verdict: a flagged link means do not open it on your primary/host machine — pivot to a disposable VM or a passive archive view instead.

## Inputs → Outputs
- **In:** `domain` / URL (or a small download)
- **Out:** a safety verdict (clean / phishing / malware) — no OSINT selectors are returned
- **Empty/negative result looks like:** "no threats found" — meaning Dr.Web has nothing on record, NOT a guarantee the link is safe. Zero-day or freshly-registered malicious sites can still pass.

## Gotchas & OpSec
- Human-in-the-loop: none for the scan itself.
- OpSec: **active** — the URL leaves your machine for Dr.Web's cloud, and scanning may cause the destination to be fetched. Treat "clean" as a weak signal, not clearance.
- It bundles ad/tracker blocking that can alter page behaviour; disable if you need to see a target page exactly as a normal visitor would.

## Overlaps ("do both")
- Pairs with `[[soc-multi-tool]]` — SOC Multi-tool cross-checks a domain/IP/hash against VirusTotal and AbuseIPDB from the same right-click menu, giving a multi-engine reputation view alongside Dr.Web's single verdict.

## Trust & verifiability
`trust: trusted` — maintained by Doctor Web, a long-established AV vendor; the verdict is as good as their reputation database, which is authoritative but not exhaustive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dr-web-anti-virus-link-checker-extension-chrome |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | domain → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | no |
