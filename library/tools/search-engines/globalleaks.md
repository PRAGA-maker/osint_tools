---
id: globalleaks
name: GlobaLeaks
description: Use when you need to RECEIVE tips securely or recognise a whistleblowing intake site — open-source software that powers anonymous, encrypted submission platforms (not a person-lookup tool).
url: https://www.globaleaks.org/
category: search-engines
path:
- search-engines
bestFor: Standing up (or identifying) a secure, anonymous whistleblower/tip intake platform for an investigation.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (AGPL). You self-host it (or use a hosted instance); no licence cost, though hosting/Tor setup takes effort.
opsec: passive
opsecNote: For an investigator RUNNING an intake, GlobaLeaks is designed to protect sources — offer it over Tor and follow its hardening guide so submitters aren't deanonymised. As a submitter, only send tips through an instance you trust; the platform protects the transport, not your OPSEC hygiene.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by the Hermes Center; the reference open-source whistleblowing framework, used by journalists, NGOs and anti-corruption bodies worldwide and independently audited.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- GlobalLeaks
- globaleaks
tags:
- whistleblowing
- secure-submission
- tor
- toddington
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# GlobaLeaks

> The open-source engine behind most secure whistleblowing/tip sites — infrastructure for *receiving* confidential leads anonymously, not a database you search.

## When to use
This is not a lookup tool; it's the platform you use when your investigation needs to **collect** sensitive information from anonymous sources safely (e.g. a public appeal for tips about a missing person or a corruption case where informants fear exposure). GlobaLeaks lets an investigator, newsroom or NGO run an encrypted, Tor-accessible intake where sources submit documents and messages without revealing their identity. You'll also encounter it defensively — recognising that a "SecureDrop-style" tip page is GlobaLeaks tells you how a source's submission is protected.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read the docs at https://www.globaleaks.org/ and the "Whistleblowing.it" implementation guides.
2. Deploy the software on a hardened server (Debian/Ubuntu; it ships as a package/Docker) — ideally reachable as a Tor onion service so submitters stay anonymous.
3. Configure your intake questionnaire, recipients (who can read tips) and retention/encryption settings.
4. Publish the intake URL through your appeal; sources submit tips and files, and can return anonymously to answer follow-ups via a receipt code.
5. Manually triage submissions (human-in-the-loop) — vet each tip before acting, since anonymous intake attracts both genuine leads and noise.

## Inputs → Outputs
- **In:** — (you receive submissions; you don't query it with a selector)
- **Out:** anonymous tips — documents, messages, and any selectors a source chooses to share
- **Empty/negative result looks like:** an intake with no submissions — normal; secure tip lines are low-volume. Absence of tips says nothing about the underlying facts.

## Gotchas & OpSec
- Running it well requires real infrastructure and OPSEC (Tor, hardened hosting, careful recipient management) — a misconfigured instance can endanger sources.
- It protects the *submission channel*; it does not vet the truth of what's submitted. Corroborate every tip.
- Not a search/discovery tool — don't expect to "look someone up" here.

## Overlaps ("do both")
- Conceptually adjacent to SecureDrop as a secure-intake option; choose based on your hosting/anonymity needs. Pair the tips it collects with your normal verification toolchain.

## Trust & verifiability
`trust: trusted` — GlobaLeaks is the reference open-source whistleblowing framework, maintained by the non-profit Hermes Center, widely deployed by reputable media and NGOs, and independently security-audited. The software is trustworthy; individual submissions are not, until verified.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | globalleaks |
| category | search-engines |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
