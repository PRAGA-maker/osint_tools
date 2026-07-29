---
id: certgraph
name: certgraph
description: Use when you have a `domain` and want to discover related/sibling domains an operator controls — returns a graph of linked `domain`s via shared TLS certificate SANs.
url: https://github.com/lanrat/certgraph
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- certificate-search
bestFor: Crawling the graph of certificate Subject Alternative Names to surface an operator's related domains.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Open-source (GPL-2.0); free binaries, Docker image, and source. Optional Censys driver needs free API keys.
opsec: passive
opsecNote: The default HTTP/SMTP drivers open direct TLS connections to the target's hosts, which those hosts can log. To stay fully passive, use the `--driver crtsh` (Certificate Transparency via crt.sh) or Censys driver so you never touch the target infrastructure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Maintained by lanrat on GitHub; packaged in Kali and BlackArch. Mechanism (CT logs / live cert SANs) is verifiable and deterministic, not a proprietary black box.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools: []
aliases:
- CertGraph
tags:
- certificate-search
- domain-recon
- Code
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# certgraph

> A CLI that crawls certificate Subject Alternative Names outward from a seed domain, mapping the web of domains an operator ties together on shared TLS certs.

## When to use
You have a `domain` (a person's personal site, a scam/phishing domain, a small business tied to a subject) and want to find the *other* domains the same operator controls. Because a single TLS certificate often lists many hostnames in its SAN field, certgraph pivots from one domain to all the domains sharing certs with it, then repeats — surfacing infrastructure a WHOIS lookup alone would miss.

## How to use it (`bestInteractionPattern`: cli)
1. Install: grab a pre-built binary from the [releases page](https://github.com/lanrat/certgraph/releases), pull the Docker image, or `go install github.com/lanrat/certgraph@latest` (Go 1.23+).
2. Run a passive crawl against a seed domain:
   `certgraph -depth 2 -driver crtsh example.com`
   (`crtsh` queries Certificate Transparency logs, so you never connect to the target.)
3. For a machine-readable graph, add `-json > graph.json`; certgraph also ships an HTML/D3 viewer to render the adjacency graph visually.
4. Read the output: each node is a `domain`, each edge is a shared-certificate relationship, annotated with depth and cert fingerprint.
5. Pivot: feed newly discovered domains back into WHOIS, `[[whois-search]]`, DNS, and content review to confirm they belong to the same subject.

## Inputs → Outputs
- **In:** one or more seed `domain`s
- **Out:** a directed graph of related `domain`s (with cert fingerprints, depth, and status)
- **Empty/negative result looks like:** the seed returns only itself with no edges — the domain uses a dedicated single-host cert (or the CT driver has no records), so there is nothing to pivot on.

## Gotchas & OpSec
- Human-in-the-loop: none — it is fully scriptable.
- OpSec: the **default** HTTP and SMTP drivers make live TLS handshakes to the target's servers, which can be logged. Prefer `-driver crtsh` (or Censys with keys) to keep the crawl passive.
- Depth is exponential: `-depth 3+` on a large hosting provider can explode into thousands of unrelated nodes. Start shallow and raise depth deliberately.
- Shared-cert linkage can produce false positives when domains sit behind a shared CDN/host that bundles unrelated sites onto one cert — verify ownership before asserting a link.

## Overlaps ("do both")
- Pairs with a raw CT-log search like `[[whois-search]]` and crt.sh directly: certgraph *automates the recursive pivot* across certs, whereas a single crt.sh query only shows one hop. Run certgraph to map the neighborhood, then confirm each node's registration separately.

## Trust & verifiability
`trust: community` — open-source and reproducible: anyone can re-run the same crawl and get the same graph from public CT logs, and it is shipped in mainstream pentest distros (Kali, BlackArch).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | certgraph |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
