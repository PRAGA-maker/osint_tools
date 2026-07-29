---
id: hunting-new-registered-domains
name: Hunting-New-Registered-Domains
description: Use when you have a brand/keyword/domain and want to catch newly registered look-alike domains (typosquat/phishing) from the daily new-domains feed — returns domain, ip-address and metadata-exif leads.
url: https://github.com/gfek/Hunting-New-Registered-Domains
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- tools
bestFor: Detecting typosquatting/phishing domains by scanning the daily newly-registered-domains list for permutations of a keyword.
input: Domain patterns or keywords
output: List of newly registered matching domains
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
- metadata-exif
status: live
pricing: free
costNote: Open-source Python (hnrd.py); free. Consumes the free daily Whoisds new-domains list. A VirusTotal API key is optional for detection enrichment.
opsec: passive
opsecNote: Works from the public Whoisds daily list plus lookups (DNS, whois, SSL, VirusTotal); it does not contact the suspect domain's owner. Enrichment lookups (whois/DNS/VT) go out from your IP and are logged by those services — use API keys and, if needed, a proxy for the enrichment stage.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source tool (gfek, hundreds of GitHub stars); relies on the third-party Whoisds daily feed for completeness.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- hnrd
- Hunting New Registered Domains
tags:
- phishing
- typosquatting
- Domain/IP investigation
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# Hunting-New-Registered-Domains

> A CLI that pulls the day's newly-registered-domains list and flags permutations of your keyword (bitsquatting, hyphenation, typos), enriching each hit with DNS, whois, SSL, ASN and VirusTotal data — early warning for phishing look-alikes.

## When to use
You have a brand, name, or `domain` you care about and want to catch impersonation domains the day they appear — typosquats, homoglyphs, hyphenated variants that phishers register to target a person or organization. Given a date and a keyword, it scans that day's global new-domains feed and returns matches with rich context so you can triage which look-alikes are active and hostile. Relevant when a missing person's identity/brand is being spoofed, or to map infrastructure a suspect is standing up.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo and install requirements (Python 2.7 or 3): `pip install -r requirements.txt`.
2. (Optional) add a VirusTotal API key in the config for detection enrichment.
3. Run: `python hnrd.py -f 2026-07-29 -s paypal` — `-f` a date (YYYY-MM-DD, must have a Whoisds list), `-s` your keyword.
4. Read the output: matching new domains with DNS records, IP→ASN, whois, SSL certs, VirusTotal detections, QUAD9 block status, entropy and string-similarity scores.
5. Pivot: a hostile look-alike's resolved IP/ASN → hosting/infrastructure mapping; its SSL cert → certificate-transparency pivots; whois → registrant leads.

## Inputs → Outputs
- **In:** a date + keyword/`domain` pattern
- **Out:** list of newly registered matching `domain`s, each with `ip-address`/ASN, whois, SSL, VT detections and similarity/entropy scores (`metadata-exif`-style enrichment)
- **Empty/negative result looks like:** zero matches for that date+keyword (no look-alikes registered that day), or a fetch error if the Whoisds list for that date isn't available yet.

## Gotchas & OpSec
- Coverage is bounded by the Whoisds daily list — it does not see every TLD or registrar, so absence isn't proof.
- OpSec: the scan itself is passive, but per-domain enrichment (whois/DNS/VT) leaves queries in those services' logs from your IP; use API keys and a proxy for sensitive work.
- Run it daily and diff results — it's a monitor, not a one-shot.

## Overlaps ("do both")
- Complements certstream-based watchers (which catch new SSL certs in near-real-time) — this uses the registration feed instead; run both to cover domains that get certs late or never.

## Trust & verifiability
`trust: community` — widely-used open-source tool; completeness depends on the third-party Whoisds feed, so treat it as high-signal early warning rather than an exhaustive census.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hunting-new-registered-domains |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
