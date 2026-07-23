---
id: cyberbro
name: Cyberbro
description: Use when you have a messy blob of indicators (`ip-address`, `domain`, hashes, URLs) and want bulk reputation/enrichment — returns aggregated CTI verdicts and reverse-DNS/geolocation context.
url: https://github.com/stanfrbd/cyberbro
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Bulk-extracting IoCs from garbage input and scoring them across 30+ threat-intel services at once.
selectorsIn:
- ip-address
- domain
selectorsOut:
- ip-address
- domain
- geolocation
status: live
pricing: free
costNote: Free and open-source (MIT). Self-host with Docker/Python at no cost; some upstream CTI services it queries need your own free API keys to unlock full data.
opsec: passive
opsecNote: Reputation lookups are passive against the target, but Cyberbro forwards your indicators to third-party CTI providers (VirusTotal, Shodan, AbuseIPDB, etc.). Those providers log and may retain what you submit, so treat any indicator you paste as disclosed to them. Self-hosting keeps the app itself off a shared cloud.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: docker
trust: community
trustNote: Actively maintained open-source project (stanfrbd) with an MIT license and public issue tracker; it is a query aggregator, so data quality is inherited from the upstream services, not Cyberbro itself.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- cyberbro CTI
- stanfrbd/cyberbro
tags:
- other-tools
- ioc-enrichment
- threat-intel
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Cyberbro

> A self-hosted IoC scrubber-and-scorer: paste raw text, it extracts the indicators and checks each against 30+ threat-intel services in parallel.

## When to use
You have a pile of unstructured indicators — an `ip-address` list, `domain`s, file hashes, URLs, or Chrome extension IDs buried in log lines or an email header — and you want a single de-duplicated table of reputation verdicts instead of pasting each one into a dozen web forms. Most relevant for infrastructure/attribution work; only marginally useful for missing-persons cases (an `ip-address` or `domain` tied to a subject can be geolocated and reverse-resolved here).

## How to use it (`bestInteractionPattern`: docker)
1. Clone the repo: `git clone https://github.com/stanfrbd/cyberbro && cd cyberbro`.
2. Copy `secrets-sample.json` to `secrets.json` and paste in whatever free CTI API keys you have (VirusTotal, AbuseIPDB, Shodan, etc.). Missing keys just disable those specific engines.
3. Launch with `docker compose up -d` (or the Python path) and open the local web UI.
4. Paste your garbage input into the box and submit; Cyberbro regex-extracts the IoCs, queries the enabled services multithreaded, and shows a filterable table with reverse DNS/RDAP and geolocation.
5. Export to CSV/Excel, or pivot a flagged `ip-address`/`domain` into a dedicated passive-DNS or geolocation tool.

## Inputs → Outputs
- **In:** `ip-address`, `domain` (also hashes, URLs, extension IDs) — as free text
- **Out:** per-indicator reputation across 30+ services, reverse DNS/RDAP, `geolocation`, exportable CSV/Excel
- **Empty/negative result looks like:** an indicator row with every engine returning "not found"/clean — means no listed reputation data, not proof the indicator is benign.

## Gotchas & OpSec
- Human-in-the-loop: you must supply your own API keys; engines without a key are silently skipped, so "clean" can just mean "not queried."
- OpSec: every indicator you paste is forwarded to third-party CTI providers who log it. Don't submit sensitive/private indicators you don't want VirusTotal & co. to retain.
- It only reports what upstream services already know; a fresh/obscure indicator will look clean everywhere.

## Overlaps ("do both")
- Pairs with dedicated passive-DNS and IP-geolocation tools like [[dns-dumpster]] and [[ipinfo-map]] — Cyberbro triages a bulk list fast, then you drill into a single flagged indicator with a specialist tool.

## Trust & verifiability
`trust: community` — maintained open-source project with a transparent codebase; because it aggregates other services, verify any critical verdict against the originating provider rather than trusting the summary cell.
