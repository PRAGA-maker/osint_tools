---
id: cloud-custodian
name: Cloud Custodian
description: Use when you have access to a cloud account (AWS/Azure/GCP) and want to inventory and query its resources by policy — returns matched resources and configuration findings, optionally with remediation.
url: https://github.com/cloud-custodian/cloud-custodian
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- cloud-configuration-analysis
bestFor: Policy-driven inventory and configuration auditing of a cloud account you control.
selectorsIn: []
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free and open-source (Apache-2.0), maintained under the CNCF/Stacklet; you pay only for the cloud API calls it makes.
opsec: active
opsecNote: This authenticates to a real cloud account with your credentials and calls provider APIs directly; those calls are logged in the account's audit trail (CloudTrail etc.), and misconfigured policies can trigger enforcement/remediation actions. Only run it against accounts you are authorized to assess.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: A mature, widely-adopted open-source cloud-governance engine (CNCF sandbox / Stacklet); used in production by many enterprises.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- c7n
- custodian
tags:
- cloud
- cloud-security
- configuration-audit
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# Cloud Custodian

> An open-source rules engine for cloud governance: write YAML policies and it queries your AWS/Azure/GCP account to find, report and (optionally) fix resources that match.

## When to use
You have legitimate access to a cloud account and want to inventory or audit it against declarative rules — find public S3 buckets, exposed security groups, untagged assets, resources in unexpected regions. In an investigative/defensive context it's for infrastructure you're authorized to assess, not for probing someone else's cloud (which you can't query without their credentials anyway). Output can surface `domain`s and `ip-address`es tied to the account's resources.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install c7n` (plus `c7n-azure`/`c7n-gcp` for those clouds).
2. Configure provider credentials in your environment (an authorized read-only role is ideal).
3. Write a policy YAML — a `resource:` type plus `filters:` describing what to match.
4. Dry-run: `custodian run --dryrun -s out policy.yml` to see matched resources without acting.
5. Read `out/` for matched resources and metadata; remove `--dryrun` only when you intend actions. Pivot: feed discovered endpoints/IPs into infrastructure-mapping tooling.

## Inputs → Outputs
- **In:** cloud credentials + a YAML policy (no OSINT selector query)
- **Out:** matched resources, config findings, resource metadata including `domain`s/`ip-address`es; optional remediation
- **Empty/negative result looks like:** a run with zero matched resources — meaning nothing in the account meets the policy's filters, not that the account is empty. Re-check the filter logic.

## Gotchas & OpSec
- Human-in-the-loop: none at runtime, but authoring correct policies (and scoping credentials) is on you.
- OpSec: **active** — it makes authenticated, logged API calls; always `--dryrun` first and only run against authorized accounts. A bad policy can delete/modify resources.
- It governs accounts you control; it is not a remote-recon tool for third-party cloud assets.

## Overlaps ("do both")
- Complements external cloud-asset discovery (bucket finders, cert-transparency) — those find exposed assets from outside; Cloud Custodian audits from inside with credentials.

## Trust & verifiability
`trust: trusted` — a mature, community-governed open-source project used widely in production; findings reflect authoritative provider API data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cloud-custodian |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut |  → domain, ip-address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
