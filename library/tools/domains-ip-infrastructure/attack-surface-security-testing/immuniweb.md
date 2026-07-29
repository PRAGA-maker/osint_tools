---
id: immuniweb
name: ImmuniWeb
description: Use when you have a `domain` (or email/org) and want free passive posture reports — returns SSL, website, email, privacy and dark-web/breach exposure findings.
url: https://www.immuniweb.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- attack-surface-security-testing
bestFor: Free non-intrusive security/privacy posture checks on a domain, plus a dark-web & breach exposure snapshot for an organisation.
selectorsIn:
- domain
- email
- employer-org
selectorsOut:
- domain
- email
- employer-org
status: live
pricing: freemium
costNote: Community Edition tests (SSL, Website, Email, Privacy, Mobile, Dark Web Exposure) are free and run without an account. Full continuous monitoring and pentest services are paid enterprise products.
opsec: passive
opsecNote: The free Community tests query ImmuniWeb's own telemetry and public sources; the SSL/Email/Privacy tests are effectively passive fingerprinting. The Website Security Test does perform a light non-intrusive scan of the target — treat that one as mildly active and only run it against assets you may test. No target-owner alert is generated. ImmuniWeb logs and publishes results to a shared statistics board unless you opt out.
humanInLoop: true
humanInLoopReason:
- captcha
- rate-limit
bestInteractionPattern: web-manual
trust: trusted
trustNote: ImmuniWeb (Geneva-based application security vendor, formerly High-Tech Bridge) is an established commercial firm; its free tools are widely cited in industry and its scan engines are its own products.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- immuniweb-directory
aliases:
- High-Tech Bridge
- ImmuniWeb Community Edition
tags:
- ssl-test
- dark-web-exposure
- attack-surface
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# ImmuniWeb

> A vendor-run suite of free "Community Edition" security tests — point it at a domain, email, or company name and get an SSL/website/email/privacy grade plus a dark-web & breach exposure snapshot, no login required.

## When to use
You have a subject's `domain`, `email`, or `employer-org` and want a fast, passive read on their web/email hygiene and whether the organisation shows up in breach or dark-web exposure data. Useful early in infrastructure profiling to grade an asset and surface leaked-credential leads without touching the target intrusively.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.immuniweb.com/ and pick a free test from the Community Edition menu:
   - **SSL Security Test** — enter a hostname; grades TLS config, ciphers, PCI/HIPAA/NIST compliance.
   - **Website Security Test** — enter a URL; checks headers, CMS/software fingerprint, GDPR/PCI hints (lightly active).
   - **Email Security Test** — enter a domain; checks SPF/DKIM/DMARC and blacklist status.
   - **Dark Web / Threat Exposure Test** — enter a domain/org; returns count and samples of exposed credentials, mentions, and phishing.
2. Solve the CAPTCHA when prompted and submit.
3. Read the graded report (A+…F) and expand the findings sections; the Dark Web test lists exposure incidents you can pivot on.
4. Pivot: leaked-credential/domain findings feed breach-lookup and email tools; SSL/website fingerprints feed `[[immuniweb-directory]]`-style asset mapping.

## Inputs → Outputs
- **In:** `domain` (SSL/website/email), `email`/`employer-org` (dark-web exposure)
- **Out:** posture grade, misconfiguration list, exposed `email`/credential counts, `domain`/`employer-org` exposure incidents
- **Empty/negative result looks like:** "no exposure found" on the dark-web test, or a clean A+ grade — means nothing surfaced in ImmuniWeb's sources, not that no exposure exists anywhere.

## Gotchas & OpSec
- Human-in-the-loop: a CAPTCHA gates each run and free tests are rate-limited (a handful per IP per day).
- OpSec: the SSL/email/dark-web tests are passive; the Website Security Test lightly probes the live host — scope it to authorised targets. Results may be added to ImmuniWeb's public statistics unless you decline the option.
- The API exists but full programmatic access is a paid tier; the free path is the web UI.

## Overlaps ("do both")
- Pairs with `[[immuniweb-directory]]` and other attack-surface mappers — ImmuniWeb grades a single asset's posture, while directory/asset tools enumerate the full footprint. Grade the primary domain here, then enumerate siblings elsewhere.

## Trust & verifiability
`trust: trusted` — first-party scan engine from an established security vendor; grades are reproducible and standards-referenced. Dark-web exposure counts are indicative leads to confirm against dedicated breach tools, not exhaustive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | immuniweb |
