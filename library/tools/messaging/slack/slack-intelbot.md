---
id: slack-intelbot
name: slack-intelbot
description: Use when you have an `ip-address`, `domain` or file hash and want reputation/threat context posted in-channel — returns aggregated verdicts from VirusTotal, AbuseIPDB, URLhaus, Hybrid Analysis and OTX.
url: https://github.com/pun1sh3r/slack-intelbot
category: messaging
path:
- messaging
- slack
bestFor: In-Slack enrichment of atomic indicators (IP, domain, hash) with aggregated threat-intelligence reputation data.
selectorsIn:
- ip-address
- domain
selectorsOut:
- ip-address
- domain
status: live
pricing: free
costNote: The bot is free/open-source, but it queries third-party APIs (VirusTotal, AbuseIPDB, URLhaus, Hybrid Analysis, AlienVault OTX) that each require your own API key; free API tiers are rate-limited. You self-host the bot in your Slack workspace.
opsec: passive
opsecNote: Passive toward any human subject — it queries reputation databases about infrastructure, not the person, and doesn't touch the target's systems. Note that submitting an indicator to VirusTotal/OTX makes that lookup visible to those platforms (and potentially the indicator's owner if they monitor VT), so treat submissions as semi-public; don't upload sensitive private hashes.
humanInLoop: true
humanInLoopReason:
- api-key
- account-login
bestInteractionPattern: cli
trust: unverified
trustNote: Community GitHub project (pun1sh3r/slack-intelbot); it's a thin aggregator over well-known reputation APIs, so trust rests on those upstream sources — audit the code before deploying it with your API keys.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: true
invitationOnly: false
relatedTools: []
aliases:
- pun1sh3r/slack-intelbot
- Slack IntelBot
tags:
- slack
- threat-intelligence
- ioc-enrichment
source: arf-seed
lastVerified: '2026-07-15'
enrichment: full
---

# slack-intelbot

> A self-hosted Slack bot that enriches atomic indicators (IP, domain, file hash) in-channel with aggregated reputation data from five threat-intel APIs.

## When to use
You're triaging **infrastructure** selectors, not people directly: an `ip-address`, a `domain`, or a file hash surfaced in a case (a suspicious message header, a scam site, a link a subject sent) and you want a fast reputation read — is it known-malicious, who else has flagged it. It shines when a team works in Slack and wants one-command enrichment without leaving the channel. For missing-persons work its role is peripheral: vetting the infrastructure around a subject (scam domains, hosting), not locating the person.

## How to use it (`bestInteractionPattern`: cli)
1. Clone https://github.com/pun1sh3r/slack-intelbot and deploy it into your Slack workspace (self-hosted).
2. Configure API keys for VirusTotal, AbuseIPDB, URLhaus, Hybrid Analysis and AlienVault OTX.
3. In Slack, post an indicator (IP/domain/hash) or upload a file for bulk lookup.
4. Read the bot's aggregated response: reputation verdicts and context across the five sources; export as text/CSV.
5. Pivot: a domain's registration/hosting feeds domain-OSINT (WHOIS, passive DNS); a flagged IP contextualises where a message or site originated.

## Inputs → Outputs
- **In:** `ip-address`, `domain`, or file hash (MD5/SHA1/SHA256)
- **Out:** aggregated reputation/threat context on that `ip-address`/`domain` (malicious/clean verdicts, references)
- **Empty/negative result looks like:** "no detections / not found" across sources — the indicator is unknown to these DBs, which is not proof it's benign, just that it isn't catalogued.

## Gotchas & OpSec
- Needs your own API keys; free tiers rate-limit, so bulk lookups can stall.
- It's an aggregator — verdicts are only as good/current as VT/AbuseIPDB/etc.; a "clean" result can be stale.
- OpSec: **passive** toward people, but submitting indicators to VT/OTX is semi-public — don't submit sensitive private hashes you don't want exposed.

## Overlaps ("do both")
- Pair with dedicated domain/IP OSINT (WHOIS, passive DNS, Shodan-style tools) — intelbot gives a quick reputation verdict; those give the ownership, history and exposure detail behind the same indicator.

## Trust & verifiability
`trust: unverified` — a community bot wrapping reputable APIs. The upstream reputation data is trustworthy; the wrapper is not independently vetted, so review the code before giving it your API keys, and confirm critical verdicts directly on the source platforms.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | slack-intelbot |
| category | messaging |
| selectorsIn → selectorsOut | ip-address, domain → ip-address, domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
