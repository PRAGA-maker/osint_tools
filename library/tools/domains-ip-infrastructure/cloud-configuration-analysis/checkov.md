---
id: checkov
name: Checkov
description: Use when you have a `domain`/org's infrastructure-as-code repo and want to find its cloud misconfigurations — returns policy violations with severity and remediation.
url: https://github.com/bridgecrewio/checkov
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- cloud-configuration-analysis
bestFor: Statically scanning Terraform/CloudFormation/Kubernetes IaC for insecure cloud settings.
selectorsIn:
- domain
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free and open source (Apache-2.0). A managed SaaS tier (Prisma Cloud / former Bridgecrew) exists but the CLI scanner is fully free.
opsec: passive
opsecNote: Passive — it parses local IaC files (e.g. a target org's public GitHub repo you have cloned) and never touches the live cloud environment, so the target sees nothing. Only analyse code you are authorised to review.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Widely-adopted open-source scanner (bridgecrewio/checkov, now under Palo Alto/Prisma Cloud) with thousands of built-in policies and an active community.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- checkov
- bridgecrew checkov
tags:
- iac-security
- cloud-misconfiguration
- static-analysis
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# Checkov

> A static analysis scanner for infrastructure-as-code — point it at Terraform/CloudFormation/Kubernetes/ARM files and it flags insecure cloud configurations before they deploy.

## When to use
You are assessing an organisation's (`employer-org` / `domain`) security posture and have access to its infrastructure-as-code — e.g. a public IaC repo on GitHub. Checkov statically evaluates that code against thousands of policies (open S3 buckets, permissive security groups, unencrypted volumes, exposed secrets) to reveal how the org's cloud is likely misconfigured, without ever probing the live environment.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install checkov`.
2. Clone or download the target's IaC (only what you are authorised to review).
3. Run: `checkov -d .` over the directory (or `-f main.tf` for a single file); add `-o json` for machine-readable output.
4. Read the report: each finding has a check ID, severity, the offending resource, and remediation guidance.
5. Pivot: exposed resource names, bucket names, and hardcoded endpoints in the code feed domain/asset-mapping of the org's cloud footprint.

## Inputs → Outputs
- **In:** `domain`/org infrastructure-as-code files (Terraform, CloudFormation, K8s, ARM, Helm, Dockerfile)
- **Out:** policy violations (misconfigurations) mapped to the owning `employer-org`, plus any secrets embedded in the code
- **Empty/negative result looks like:** "Passed" for all checks — the IaC is clean by Checkov's ruleset, which says nothing about resources provisioned outside IaC.

## Gotchas & OpSec
- It only sees what's in the code — infrastructure created manually or by other tooling is invisible to it.
- A clean scan is not a clean cloud; it validates the templates, not the deployed reality.
- Only analyse code you have a legitimate basis to review (public repos, authorised engagements).
- Custom policies may be needed for org-specific concerns beyond the built-in set.

## Overlaps ("do both")
- Pairs with cloud-asset enumeration (bucket/subdomain finders) — Checkov shows how the IaC is misconfigured, while enumeration shows what is actually exposed live; together they map intended vs real posture.

## Trust & verifiability
`trust: trusted` — a mature, heavily-used open-source scanner with transparent, versioned policies; findings are reproducible by re-running the same version.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | checkov |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
