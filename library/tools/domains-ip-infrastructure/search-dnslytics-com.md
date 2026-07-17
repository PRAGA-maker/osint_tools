---
id: search-dnslytics-com
name: DNSlytics Tools
description: Use when you have a `domain` or `ip-address` and want to find everything connected to it — reverse-IP neighbours, reverse-whois, shared AdSense/Analytics IDs and DNS history — returns related `domain`s and `ip-address`es.
url: https://search.dnslytics.com/tools
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Pivoting a domain/IP into the network of sites and infrastructure that share ownership, hosting or tracking IDs.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: Free tier gives limited lookups/results per day; a paid subscription unlocks full result sets, history and higher volume.
opsec: passive
opsecNote: Queries run against DNSlytics' own datasets, not the target's servers, so the subject sees nothing. You are querying a third party about the target's infrastructure — fine for OSINT; use a research browser if you want to avoid tying lookups to yourself.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: trusted
trustNote: Well-established, widely-cited domain/IP intelligence service; its reverse and historical datasets are respected in the OSINT community.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- dnslytics-com
- tcp-ip-utils-domain-neighbors
- viewdns-info
aliases:
- DNSlytics legacy tools
- search.dnslytics.com
tags:
- domainsandips
- reverse-ip
- reverse-whois
- dns
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# DNSlytics Tools

> The legacy toolbox of DNSlytics' investigation suite — reverse-IP, reverse-whois, reverse-NS/MX, shared-tracker-ID and DNS-history lookups that turn one domain/IP into its whole infrastructure cluster.

## When to use
You have a `domain` or `ip-address` tied to your subject (a personal site, a business, a scam page, a mail server) and want to expand it: what other domains sit on the same IP/subnet, who registered them (reverse-whois), which sites share the same Google AdSense/Analytics ID (a strong ownership link), and how the DNS/hosting has changed over time. This "domain neighbours + shared trackers" pivot is one of the most reliable ways to connect a person to *other* sites they run.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://search.dnslytics.com/tools — the legacy tools index.
2. Pick the pivot you need:
   - **Reverse IP** — enter an IP to list other domains hosted on it/its subnet.
   - **Reverse Whois** — enter a name/email/org to find domains registered with it.
   - **Reverse NS / MX** — find domains sharing a name/mail server.
   - **Reverse AdSense / Analytics ID** — enter a `pub-XXXX`/`UA-`/`G-` ID (or a domain to reveal it) to find co-owned sites — the strongest signal.
   - **History tools** — see a domain's historical IPs/DNS.
3. Read the related `domain`/`ip-address` list; treat shared tracker IDs as high-confidence common-ownership.
4. Mind the free-tier limits — results are truncated and rate-limited until you sign in/subscribe.
5. Pivot: new domains feed whois/registration lookups and content review; the shared-ID cluster maps a person's whole web presence.

## Inputs → Outputs
- **In:** `domain` or `ip-address` (or a whois name/email, or an AdSense/Analytics ID)
- **Out:** related `domain`s, co-hosted `ip-address`es, shared-tracker clusters, DNS/hosting history
- **Empty/negative result looks like:** few/no neighbours (dedicated IP or privacy hosting) or a truncated free-tier list — absence of neighbours isn't proof of no other sites; corroborate with `[[viewdns-info]]`.

## Gotchas & OpSec
- Free tier truncates results and rate-limits — you may be seeing only the top slice; note this before concluding "only N domains."
- Reverse-whois is weakened by GDPR redaction and privacy services; shared AdSense/Analytics IDs are the more durable ownership signal.
- Shared IP on cheap shared hosting ≠ same owner — weight IP-only links lightly; weight tracker-ID links heavily.

## Overlaps ("do both")
- Pairs with `[[viewdns-info]]` and `[[tcp-ip-utils-domain-neighbors]]` — run the same reverse pivots on both; their datasets differ and each surfaces neighbours the other misses. `[[dnslytics-com]]` is the main site's front-end for the same data.

## Trust & verifiability
`trust: trusted` — DNSlytics is a long-standing, widely-referenced domain/IP intelligence provider. Its reverse and historical datasets are respected, though (as with all reverse-whois) registration data quality is limited by redaction; verify ownership claims across a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-dnslytics-com |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
