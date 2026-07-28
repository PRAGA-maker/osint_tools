---
id: checkphishai
name: CheckPhishAI
description: Use when you have a `domain`/URL and want to detect phishing or typosquats of it — returns scan verdicts, screenshots, and lookalike `domain`s.
url: https://checkphish.bolster.ai/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Scanning a URL for phishing/scam signals and finding registered typosquat domains of a brand.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: Free real-time URL scans (no login for basic checks); typosquat monitoring and higher-volume/API use are on freemium/paid Bolster tiers.
opsec: passive
opsecNote: Passive from the target's view — CheckPhish fetches and renders the URL from its own infrastructure, so the site sees Bolster's crawler, not you. Still, submitting a URL discloses your interest to Bolster; use a puppet account for sensitive investigations.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Free scanner from Bolster (a commercial anti-phishing vendor); verdicts are automated ML classifications, useful as leads but not authoritative rulings.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- CheckPhish
- checkphish.bolster.ai
tags:
- Domain/IP/Links
- Domain/IP investigation
- phishing
- typosquat
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# CheckPhishAI

> A free URL/domain phishing scanner and typosquat finder — submit a link and get an automated scam verdict, a live screenshot, and lookalike domains.

## When to use
You have a suspicious `domain` or URL (from a phishing email, a scam SMS, a fake-shop report) and want a fast risk read plus the technical context — where it resolves, what it renders, and which typosquatted variants of a brand are registered. Useful both for triaging a link and for mapping a scam-domain cluster.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://checkphish.bolster.ai/ and paste the URL into the real-time scanner.
2. Read the scan: phishing/scam verdict, a rendered screenshot (safe to view without visiting the live site), hosting/`ip-address`, and detected brand.
3. For brand protection, use the typosquat search to list registered lookalike `domain`s of a target brand.
4. Pivot: the resolved `ip-address`/host feeds passive-DNS and infrastructure clustering; screenshots corroborate what the page shows without you touching it.

## Inputs → Outputs
- **In:** `domain` / URL (or a brand name for typosquat search)
- **Out:** phishing verdict, screenshot, hosting `ip-address`, and lookalike `domain`s
- **Empty/negative result looks like:** a "clean"/low-risk verdict, or no typosquats found — automated and non-final; a clean score doesn't prove safety, and coverage of new domains lags.

## Gotchas & OpSec
- Verdicts are ML classifications from a vendor — treat as a strong lead, corroborate with WHOIS/passive-DNS before acting.
- The scanner renders the URL for you (good OpSec) — don't open the raw live link yourself.
- Deeper features (continuous typosquat monitoring, bulk API) sit behind Bolster's paid tiers.
- New/just-registered phishing domains may not yet be classified.

## Overlaps ("do both")
- Pairs with urlscan.io and passive-DNS tooling — CheckPhish adds a phishing verdict and typosquat discovery, while urlscan/passive-DNS give richer request-level and historical infrastructure detail.

## Trust & verifiability
`trust: community` — a useful free vendor scanner, but its verdicts are automated and commercial; the screenshot and hosting data are verifiable, the risk label is advisory.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | checkphishai |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
