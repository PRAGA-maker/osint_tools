---
id: prowler
name: Prowler
description: Use when you control a cloud account (AWS/Azure/GCP/K8s) and want a security & compliance baseline of its config — returns findings mapped to controls. A defensive audit tool, not a lookup.
url: https://github.com/prowler-cloud/prowler
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- cloud-configuration-analysis
bestFor: Running hundreds of security/compliance checks against a cloud account you own to baseline its posture.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Open-source CLI is free (Apache-2.0); Prowler Cloud/App (hosted SaaS) is a paid add-on. The CLI alone covers full assessments.
opsec: active
opsecNote: Prowler authenticates to a cloud account and calls its management APIs — it must only be run against accounts you own or are explicitly authorized to assess, and those calls are logged in the target account's audit trail (e.g. CloudTrail). It is not a covert or third-party recon tool.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Widely-used open-source cloud-security tool (prowler-cloud) with an active maintainer community and large check library.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
invitationOnly: false
relatedTools: []
aliases:
- prowler-cloud
- Prowler CLI
tags:
- cloud-security
- compliance
- defensive
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# Prowler

> An open-source cloud-security scanner: point it at an AWS/Azure/GCP/Kubernetes account you own and it runs hundreds of checks, mapping findings to compliance frameworks. Defensive posture assessment, not subject research.

## When to use
This is a **defensive/authorized-audit** tool, low relevance to person-finding. Reach for it when you administer a cloud account (your own investigative infrastructure, or a client's with permission) and want to baseline its security and compliance — misconfigurations, exposed resources, IAM weaknesses — against frameworks like CIS, PCI-DSS, or GDPR. It assesses *your* environment; it returns no data about any external subject.

## How to use it (`bestInteractionPattern`: cli)
1. Install from https://github.com/prowler-cloud/prowler (e.g. `pip install prowler` or the container image).
2. Authenticate to the target account with credentials you are authorized to use (AWS profile, Azure/GCP service principal, kubeconfig).
3. Run a scan: `prowler aws` (or `azure`/`gcp`/`kubernetes`), optionally `-c <compliance>` to target a framework.
4. Review the findings, grouped by check/control with severity and remediation, and export (CSV/JSON/HTML) for reporting.
5. Remediate and re-run to confirm; schedule periodic scans for drift.

## Inputs → Outputs
- **In:** cloud credentials/profile for an account you own (not a personal selector)
- **Out:** security & compliance findings per control, with severity and framework mapping (not a harvested selector)
- **Empty/negative result looks like:** all checks pass / no findings for a scoped service — a clean baseline, not an error.

## Gotchas & OpSec
- **Authorization required:** only run against accounts you own or are explicitly permitted to assess — it uses real, authenticated API calls, and unauthorized scanning is abuse.
- Every call is logged in the account's audit trail; this is transparent by design, not stealthy.
- Broad scans are read-heavy and can be noisy/slow on large accounts; scope by service or region when iterating.

## Overlaps ("do both")
- Pairs with other cloud-configuration analysis tools in this category: run Prowler for the broad compliance baseline, then a focused tool (e.g. a policy linter) for deep single-domain checks it summarizes.

## Trust & verifiability
`trust: community` — a mature, widely-adopted open-source project (prowler-cloud) with a large, auditable check library. Trust the code; the findings are only as scoped as the credentials and services you point it at.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | prowler |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
