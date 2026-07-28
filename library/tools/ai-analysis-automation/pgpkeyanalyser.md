---
id: pgpkeyanalyser
name: PGPKeyAnalyser
description: Use when you have a PGP/OpenPGP public key and want the identities baked into it — returns `name`, `email`, and key metadata (fingerprint, dates).
url: https://kriztalz.sh/pgp-key-analyser/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Extracting the user IDs (names, emails, comments) and metadata from a PGP public key, entirely in-browser.
selectorsIn: []
selectorsOut:
- name
- email
status: live
pricing: free
costNote: Free browser tool; no login. Processing is client-side (OpenPGP.js) — the key never leaves your browser.
opsec: passive
opsecNote: Fully passive and local — parsing happens in your browser, nothing is uploaded and no keyserver or target is contacted. Safe to analyse a key you've already obtained. (Separately fetching a key from a keyserver is a different, low-signal step.)
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Client-side tool by developer kriztalz using the well-known OpenPGP.js library; because it's local you can verify it makes no network calls, and the parsed fields are checkable against gpg.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- domainrecon
- faviconhash
- githubrecon
- metadata-viewer
- searchdorks
- traceroutevisualizer
aliases:
- PGP Key Analyser
- OpenPGP key analyser
tags:
- pgp
- key-analysis
- identity
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# PGPKeyAnalyser

> A client-side tool that parses an OpenPGP public key and lays out its embedded identities — the names, emails and comments in the User ID packets — plus fingerprint, algorithm, and dates.

## When to use
You've obtained a subject's PGP public key — from an email signature, a keyserver, a GitHub profile, a forum, a Keybase — and want the human-readable identity data inside it. PGP keys are an underrated selector: the User ID fields routinely carry a real `name` and one or more `email` addresses (sometimes several, revealing alternate/older addresses), and the creation date hints at when the persona started. Genuinely useful when a subject uses PGP but you only see the key, not who's behind it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://kriztalz.sh/pgp-key-analyser/.
2. Paste the ASCII-armored public key block (`-----BEGIN PGP PUBLIC KEY BLOCK-----` … `-----END …-----`).
3. Read the parsed output: User IDs (name/email/comment), key ID and fingerprint, algorithm, creation/expiry dates, and capabilities.
4. Note every email in the User IDs — older keys often list multiple addresses.
5. Pivot: each `email`/`name` feeds email-verification and people/username search; the fingerprint lets you cross-reference the same key elsewhere.

## Inputs → Outputs
- **In:** a PGP/OpenPGP public key (armored text)
- **Out:** `name` and `email`(es) from the User IDs, plus fingerprint, key ID, algorithm, and dates
- **Empty/negative result looks like:** a key with a User ID that's a pseudonym and a throwaway/no email — real by format but low-signal for attribution; or a parse error if the pasted block is malformed.

## Gotchas & OpSec
- Passive and local: nothing is uploaded, no keyserver is queried by this tool.
- The identities are self-asserted — anyone can put any name/email in a key's User ID, so treat them as claims to corroborate, not proof.
- To find the key in the first place, search keyservers (keys.openpgp.org) by email/name; that lookup, not this parser, is where the collection step happens.

## Overlaps ("do both")
- Pairs with `[[metadata-viewer]]` and `[[githubrecon]]` — different artefacts (documents, GitHub, keys) that each leak names/emails; run whichever matches what you've got.

## Trust & verifiability
`trust: community` — an independent client-side tool built on OpenPGP.js; being local, its no-upload claim is verifiable, and every field it shows can be double-checked with `gpg --show-keys`.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pgpkeyanalyser |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | — → name, email |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
