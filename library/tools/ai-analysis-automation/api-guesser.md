---
id: api-guesser
name: API Guesser
description: Use when you have a leaked API key/token and want to know which service it belongs to — returns the likely provider inferred from the key's format/prefix.
url: https://api-guesser.netlify.app/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Identifying which service an unknown API key or token is for, based on its recognisable format/prefix.
selectorsIn:
- password
selectorsOut: []
status: live
pricing: free
costNote: Free web tool; no account required.
opsec: passive
opsecNote: Identification is pattern-based on the key's format and runs client-side; it does not (and you should not) validate the key against the live service, which would be an active, potentially unauthorised use of someone else's credential. Never test or use a found key against its provider.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community tool (Muhammad Daffa's "all-about-apikey"); it recognises known key formats, so a match is a strong hint but not proof, and it cannot identify novel or generic-looking keys.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- deaditarchive-netlify-app
- dorksearch-netlify-app
- search-it
- reddit-timer
aliases:
- API Key Guesser
- api-guesser.netlify.app
tags:
- Code
- api-keys
- secret-identification
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# API Guesser

> A format recogniser for API keys and tokens: paste a mystery key and it tells you the service it most likely belongs to, based on the provider-specific patterns (prefixes/lengths) that keys follow.

## When to use
You have found a credential — a key in a leaked repo, a config dump, a breach, an exposed blob — and need to know what it unlocks before you can assess the exposure. Providers use recognisable key formats (e.g. `sk-...`, `AKIA...`, `ghp_...`, `xoxb-...`), and API Guesser maps the format to the likely service. That identification lets you scope the risk and route it to responsible disclosure — without ever using the key.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://api-guesser.netlify.app/ and paste the unknown key/token.
2. Read the inferred service; note it is based on format, so treat it as a strong hint.
3. Do NOT validate the key against the live provider — that would be unauthorised use of someone else's credential.
4. Pivot: report the exposure to the affected provider/owner for revocation; document where you found it as part of the exposure finding.

## Inputs → Outputs
- **In:** an API key/token (a `password`-class secret)
- **Out:** the likely originating service, inferred from the key's format/prefix
- **Empty/negative result looks like:** "unknown" or no confident match — a generic, custom, or novel key format the tool doesn't recognise; absence of a match is not proof the key is invalid.

## Gotchas & OpSec
- Human-in-the-loop: none; identification is local/pattern-based.
- OpSec: passive — it only inspects the string's format. The hard rule is **never test the key** against its provider; that is active, likely unauthorised, and possibly unlawful.
- Confidence: a format match is a hint, not verification; some providers share or change formats.

## Overlaps ("do both")
- Pairs with secret-scanning tools (e.g. gitleaks/trufflehog) because those *find* keys in code/dumps while API Guesser *identifies* an isolated one so you can route it for revocation.

## Trust & verifiability
`trust: community` — a small community utility that recognises known key formats; reliable for common providers, blind to novel formats, and the identification should be confirmed only via responsible disclosure, never by using the key.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
