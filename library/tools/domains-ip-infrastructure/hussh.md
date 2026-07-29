---
id: hussh
name: Hussh
description: Use when you have a `domain` and want a one-shot recon sweep — returns subdomains, live hosts, historical URLs, and basic vuln checks compiled into an HTML report.
url: https://github.com/harshnandwana/hussh
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: A wrapper shell script that chains subdomain enumeration, host probing, Wayback URL collection, and spidering into a single automated domain-recon report.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source shell script; no account. Wraps other free tools (sublist3r, subfinder, httprobe, gospider) which must be installed — easiest via the recommended Docker/Kali setup.
opsec: active
opsecNote: Parts are passive (Wayback/CT queries) but httprobe and gospider actively connect to the target's hosts, generating traffic and logs and possibly tripping WAF/IDS. Run only against domains you're authorised to test, and from a sock-puppet host.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A small personal GitHub project (low stars, Kali-oriented) that orchestrates well-known tools; convenient but lightly maintained — verify the underlying tools' output rather than trusting the report blindly.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- owasp-amass
- subfinder
- waybackurls
aliases:
- hussh
- harshnandwana/hussh
tags:
- Domain/IP/Links
- recon-automation
- subdomain-enumeration
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Hussh

> A convenience shell script that stitches several well-known recon tools into one pass over a domain — subdomains, live hosts, archived URLs, and quick vuln checks, output as an HTML report.

## When to use
You have a `domain` and want a fast, hands-off first recon sweep without running each tool by hand. Hussh chains subdomain enumeration (sublist3r, subfinder), liveness probing (httprobe), Wayback URL harvesting, spidering (gospider), and basic checks (e.g. CORS misconfig) into an organised HTML report. Good for a quick orientation on a target's footprint; for depth/accuracy you'll still run the underlying tools directly. Infrastructure recon, so missing-persons relevance is indirect.

## How to use it (`bestInteractionPattern`: cli)
1. Clone: `git clone https://github.com/harshnandwana/hussh` (it's built for Kali; use the recommended Docker image on other distros so the dependencies are present).
2. Ensure the wrapped tools (sublist3r, subfinder, httprobe, gospider) are installed.
3. Run against a target you're authorised to test: `./hussh target.com`.
4. Read the generated report under `/target/hussh-<date>/` — an HTML summary of discovered subdomains, live hosts, URLs, and flagged issues.
5. Pivot: take the subdomains/URLs into `[[owasp-amass]]` for deeper enumeration and into `[[waybackurls]]`/an endpoint tool for more archived paths; validate any flagged vuln manually.

## Inputs → Outputs
- **In:** `domain` (a single target).
- **Out:** `domain`/host inventory — subdomains, live hosts, historical URLs, and basic vuln flags in an HTML report.
- **Empty/negative result looks like:** a sparse report — a small footprint, or (more often) a missing dependency so a stage silently produced nothing. Check that each wrapped tool ran.

## Gotchas & OpSec
- Human-in-the-loop: none, but dependency setup is the main friction — use Docker/Kali to avoid missing-tool gaps.
- OpSec: **active** — httprobe/gospider hit the target directly (logs, possible WAF alerts). Only test authorised domains; run from a sock-puppet host.
- Lightly maintained wrapper: it's only as good as the tools it calls and can break as they change — don't trust the report over the underlying tools' direct output.

## Overlaps ("do both")
- Overlaps with `[[owasp-amass]]` / `[[subfinder]]` — Hussh calls lightweight enumerators; run Amass separately for far more thorough subdomain discovery and cross-check.
- Feeds/overlaps `[[waybackurls]]` — for exhaustive archived-URL collection beyond Hussh's Wayback step.

## Trust & verifiability
`trust: community` — a small personal orchestration script over reputable tools. Treat its HTML report as a convenient summary, and verify anything important against the wrapped tools' own output.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hussh |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
