---
id: bevigil
name: BeVigil
description: Use when you have an app/package name, developer, or `domain` and want mobile-app intelligence — returns exposed secrets, endpoints, developer `email`, and linked `employer-org`.
url: https://bevigil.com/search
category: search-engines
path:
- search-engines
bestFor: Searching indexed mobile-app (APK) code and metadata for exposed secrets, endpoints, and developer contact details.
selectorsIn:
- domain
- employer-org
selectorsOut:
- email
- employer-org
status: live
pricing: freemium
costNote: Free tier after registration (limited searches/scans); higher volume and API access require a paid plan / API key.
opsec: passive
opsecNote: You search BeVigil's pre-crawled index of public apps, not the developer's live systems, so no target is alerted. Registration is required — use a sock-puppet email. Uploading your own APK to scan sends that file to CloudSEK, so only submit files you're authorised to.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Operated by security firm CloudSEK; a legitimate, well-known mobile-app security search engine. Findings (exposed keys, endpoints) are concrete but reflect the app version indexed, which may be outdated.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools: []
aliases:
- bevigil.com
- CloudSEK BeVigil
tags:
- mobile-app-osint
- appsec
- secrets-search
- speciality-search-engines
source: awesome-osint
lastVerified: '2026-07-18'
enrichment: full
---

# BeVigil

> A security search engine for mobile apps — index into APK code and metadata to surface a developer's exposed secrets, backend endpoints, and contact details.

## When to use
You're profiling an organisation or developer that ships a mobile app, or you have a `domain`/company and want the apps and infrastructure tied to it. BeVigil crawls public Android apps and lets you search their code and metadata: developer `email`, package/framework, permissions, and — critically — exposed API keys, secrets, and backend endpoints. Useful for mapping an org's tech footprint, finding a developer's contact, or discovering infrastructure hidden inside an app.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a free account at https://bevigil.com/search (sock-puppet email).
2. Search by app name, package name, developer, or a `domain`/keyword.
3. Read the app report: metadata (developer email, framework, permissions, downloads), risk score, and matched secrets/endpoints in the code.
4. Optionally scan a specific APK on demand (only files you're authorised to submit).
5. Pivot: developer `email` feeds email OSINT; exposed endpoints/domains feed infrastructure recon; the `employer-org`/app links map the target's product footprint.

## Inputs → Outputs
- **In:** app/package name, developer, or `domain`/keyword
- **Out:** developer `email`, `employer-org`/app associations, exposed API keys/secrets, backend endpoints, permissions/metadata
- **Empty/negative result looks like:** no indexed apps for the query — the org may ship no Android app, or BeVigil hasn't crawled it; absence isn't proof of no mobile presence.

## Gotchas & OpSec
- Human-in-the-loop: registration is required; the free tier is rate-limited.
- Findings reflect the indexed app version — an exposed key may already be rotated; treat as leads, and never test/abuse a discovered secret.
- Android-app focused; iOS coverage is limited.

## Overlaps ("do both")
- Pairs with domain/infrastructure tools in the [[domains-ip-infrastructure]] set — BeVigil surfaces the app-side assets and secrets, while WHOIS/DNS/cert tools map the web-side infrastructure they connect to.

## Trust & verifiability
`trust: community` — a reputable CloudSEK product. Exposed-secret and endpoint findings are concrete evidence within the indexed app; verify they're still live before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bevigil |
| category | search-engines |
| selectorsIn → selectorsOut | domain, employer-org → email, employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
