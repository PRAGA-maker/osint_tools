---
id: checkphish-ai
name: Checkphish.ai
description: Use when you have a suspicious URL (`domain`) and want a free real-time verdict on whether it is phishing/scam plus a screenshot — returns a risk verdict and page capture.
url: https://checkphish.ai/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Free real-time scanning of a URL for phishing/scam indicators with a rendered screenshot and hosting details.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: Free URL scans available (a free Bolster account may be required); the underlying commercial platform (Bolster) sells brand-protection/API tiers.
opsec: passive
opsecNote: CheckPhish loads the URL from its own sandbox, so your IP never touches the suspicious site — this is the safe way to inspect a link a subject sent. It does log your submitted URL to their service.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Operated by Bolster (a commercial anti-phishing vendor); verdicts are automated ML classifications — useful triage, but confirm before acting.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- CheckPhish
- checkphish.bolster.ai
tags:
- phishing
- url-scanner
source: osint4all
lastVerified: '2026-07-22'
enrichment: full
---

# Checkphish.ai

> A free real-time URL scanner from Bolster: submit a suspicious link and get an automated phishing/scam verdict, a live screenshot, and hosting details — without loading the site yourself.

## When to use
You have a suspicious `domain`/URL — from a phishing report, a scam message a subject received, or a link in your investigation — and you want a fast safety verdict plus a visual of what the page shows, all without touching it from your own browser. CheckPhish renders the page in its sandbox and classifies it, giving you triage on whether it's a phishing/scam site.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://checkphish.ai/ (redirects to the Bolster CheckPhish scanner; a free account may be prompted).
2. Paste the URL and start the scan.
3. Read the result: a phishing/scam/clean verdict, a rendered **screenshot** of the page, plus hosting/registrar and `ip-address` details.
4. Use the screenshot to see the page content safely (brand impersonated, credential form, etc.).
5. Pivot: hosting/registrar and IP feed domain/WHOIS OSINT; the verdict informs whether to warn the subject or preserve evidence.

## Inputs → Outputs
- **In:** a suspicious `domain`/URL
- **Out:** phishing/scam risk verdict, live screenshot, hosting/registrar and `ip-address` info
- **Empty/negative result looks like:** a clean/benign verdict, or a page that fails to load (site already taken down) — a "clean" result is a probabilistic judgment, not a guarantee of safety.

## Gotchas & OpSec
- Verdicts are automated ML classifications: expect occasional false positives/negatives — corroborate a high-stakes call with a second scanner.
- Some features/scan volume may require a free Bolster account or hit a paid tier.
- OpSec: passive and safe — the sandbox loads the URL, keeping your IP off the target; your submitted URL is logged by the service.

## Overlaps ("do both")
- Run alongside urlscan.io / VirusTotal-style scanners and `[[where-does-this-link-go]]` — different engines and sandboxes catch different things; agreement across two raises confidence, disagreement flags "look closer."

## Trust & verifiability
`trust: community` — a commercial vendor's free tool giving automated verdicts; the screenshot and hosting data are objective, but the phishing classification is a model's opinion to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | checkphish-ai |
