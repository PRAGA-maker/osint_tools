---
id: scoutsuite
name: ScoutSuite
description: Use when you have credentials to a cloud account (AWS/Azure/GCP/etc.) and want a read-only security-posture audit — returns an HTML report of misconfigurations across the `employer-org`'s cloud estate.
url: https://github.com/nccgroup/ScoutSuite
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- cloud-configuration-analysis
bestFor: Read-only multi-cloud configuration audits of an account you control, flagging exposed/misconfigured resources.
selectorsIn:
- employer-org
selectorsOut: []
status: live
pricing: free
costNote: Free and open source (Python) from NCC Group; no account. Requires cloud credentials for the estate you are auditing.
opsec: active
opsecNote: ScoutSuite authenticates to the cloud provider's APIs with credentials you supply and reads configuration metadata — it does not modify resources, but the API calls are logged in the account's audit trail (CloudTrail/Activity Log). Run it only against accounts you are authorized to assess.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Maintained by NCC Group, a major security firm; a widely-used, auditable open-source cloud-audit tool.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- microburst
aliases:
- nccgroup/ScoutSuite
- Scout Suite
tags:
- cloud-audit
- multi-cloud
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# ScoutSuite

> A read-only, multi-cloud security-auditing tool: give it credentials to an AWS/Azure/GCP/Oracle/Alibaba account you control and it produces an offline HTML report of misconfigurations and exposures.

## When to use
This is a defensive/audit tool, not external OSINT recon. You have legitimate credentials to an `employer-org`'s cloud environment — your own, a client's during an authorized engagement — and you want a fast, categorized snapshot of what's misconfigured or publicly exposed: open storage buckets, permissive security groups, unencrypted resources, weak IAM. It reads configuration only; it never changes anything.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install scoutsuite` (or from the repo).
2. Configure provider credentials the normal way (AWS profile, `az login`, GCP service-account key, etc.).
3. Run for the provider, e.g. `scout aws --profile <name>` / `scout azure` / `scout gcp`.
4. Open the generated local HTML report — findings grouped by service and severity, each linking to the offending resource.
5. Pivot: exposed storage/endpoints become items to lock down (defensive) or, in an authorized red-team, leads for further testing.

## Inputs → Outputs
- **In:** cloud credentials for the `employer-org` estate you're authorized to audit
- **Out:** an interactive HTML report of misconfigurations/exposures by service and severity (no external selector)
- **Empty/negative result looks like:** a report with no high-severity findings — meaning nothing tripped ScoutSuite's rules for the permissions your credentials had; blind spots exist where the credential lacks read access.

## Gotchas & OpSec
- Authorization is the whole game: run it ONLY against accounts you own or are explicitly engaged to assess. It uses real credentials against real provider APIs.
- It's read-only but not invisible — every enumeration call lands in the account's audit log.
- Coverage is bounded by the permissions of the credential you supply; a low-privilege key yields an incomplete picture.

## Overlaps ("do both")
- Pairs with `[[microburst]]` — ScoutSuite gives a broad multi-cloud read-only posture audit of accounts you control, while MicroBurst adds Azure-specific external enumeration and exposure testing.

## Trust & verifiability
`trust: community` — open-source and maintained by NCC Group; the ruleset and code are auditable, and it's a standard tool in professional cloud-security reviews.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scoutsuite |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | employer-org → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
