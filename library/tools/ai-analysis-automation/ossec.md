---
id: ossec
name: OSSEC
description: Use when you control a host and want defensive log-based intrusion detection, file-integrity monitoring, and IOC alerting on it — provides host telemetry, not a lookup on an external subject.
url: https://ossec.github.io
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Host-based intrusion detection and file-integrity monitoring on systems you own — defensive telemetry and compliance auditing.
selectorsIn:
- ip-address
selectorsOut:
- ip-address
status: live
pricing: free
costNote: Core OSSEC is free and open-source. Atomicorp sells an enhanced "Atomic OSSEC" (extra rules, ML, GUI, support) from ~$5/device/month, but that upgrade is optional.
opsec: passive
opsecNote: Runs entirely on infrastructure you own to watch your own hosts — it is not a query against a third party and reveals nothing to an external target. Its OSINT/DFIR value is defensive: detecting intrusions and preserving log evidence on your own or a client's systems.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: cli
trust: trusted
trustNote: Long-standing, widely deployed open-source HIDS now maintained by Atomicorp; source is public and the project has a large operational track record.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- OSSEC HIDS
- Open Source SECurity
tags:
- hids
- log-analysis
- file-integrity
- defensive
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# OSSEC

> An open-source host-based intrusion detection system (HIDS): log analysis, file-integrity monitoring, rootkit/malware detection, and active response on machines you run.

## When to use
OSSEC is a **defensive** tool, not a people-finder. Reach for it when you operate a host or fleet and need to know if it's being tampered with: it watches logs for suspicious events, alerts on changed system files (FIM), detects malware/rootkits, and can auto-respond. In an investigative context its relevance is the DFIR/blue-team side — instrumenting a honeypot or a subject-owned system you have lawful access to, and mining its alerts for attacker `ip-address`es and indicators. It does not take a `name` or `email` and return records.

## How to use it (`bestInteractionPattern`: cli)
1. Download a precompiled binary (Windows, Linux, FreeBSD, macOS, Unix) from the official downloads page, or compile from source.
2. Install in local mode (single host) or manager/agent mode (central `ossec-server` collecting from `ossec-agent`s).
3. Configure `ossec.conf`: point log-analysis at your log sources, set the `syscheck` (FIM) directories, and tune the rule set.
4. Start the service; review alerts (files/syslog, or forward to a SIEM). Tune rules to cut false positives.
5. Pivot: extract attacker `ip-address`es, filenames, and timestamps from alerts as indicators for further infrastructure OSINT.

## Inputs → Outputs
- **In:** `ip-address` context of the hosts you monitor (your own infrastructure)
- **Out:** alerts containing attacker `ip-address`es, changed-file paths, and IOCs
- **Empty/negative result looks like:** a quiet alert stream — either genuinely no suspicious activity or under-tuned rules/log sources; verify agents are reporting before concluding "clean."

## Gotchas & OpSec
- Human-in-the-loop: alert triage is `manual-review`; OSSEC generates signals, you interpret them.
- Only deploy on systems you own or are authorised to monitor — installing an HIDS on someone else's host is not OSINT, it's intrusion.
- Initial rule tuning is significant; expect noise until baselined.

## Overlaps ("do both")
- Complements network-side monitoring and malware-analysis tools: OSSEC covers the host view (logs, file integrity), while a disassembler like `[[ghidra]]` dissects any sample it flags — do both when investigating a compromise.

## Trust & verifiability
`trust: trusted` — a mature, heavily deployed open-source HIDS with public source and a long operational history; the free core is fully functional and the paid tier is an optional enhancement, not a gate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ossec |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | ip-address → ip-address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (manual-review) |
