---
id: stormspotter
name: Stormspotter
description: Use when you have authorized access to an Azure tenant and want to map its attack surface — returns an interactive graph of Azure/AAD identities, resources, roles and privilege-escalation paths.
url: https://github.com/Azure/Stormspotter
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- azure-gcp-discovery
bestFor: Red-team/assessment mapping of an Azure subscription and Azure AD — visualising identities, resources and attack edges as a Neo4j graph.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
- associate
status: live
pricing: free
costNote: Free and open-source (Microsoft/Azure GitHub). Requires you to run Neo4j (free community edition) locally.
opsec: active
opsecNote: The collection phase (Stormcollector) makes AUTHENTICATED queries against Azure APIs using credentials you supply — this is active, logged by Azure, and must only be run against a tenant you are authorized to assess. It is not a passive external-recon tool.
humanInLoop: true
humanInLoopReason:
- account-login
- legal-gate
bestInteractionPattern: docker
trust: trusted
trustNote: Published under Microsoft's official Azure GitHub organization; it reads live Azure/AAD data, so the graph is authoritative for the tenant at collection time.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- Stormspotter
- Azure Stormspotter
tags:
- azure
- attack-graph
- cloud-recon
- arf-seed
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# Stormspotter

> Microsoft's own Azure attack-graph tool: collect a tenant's identities and resources with supplied credentials, then explore the privilege-escalation paths as an interactive Neo4j graph.

## When to use
This is an **authorized-assessment** tool, not open-source people-finding. Reach for it during a sanctioned red-team/cloud-security review of an Azure environment you have credentials for: it enumerates Azure Resource Manager resources and Azure AD objects (users, groups, service principals, roles) and renders how they connect, exposing attack paths and over-privileged identities. Think BloodHound-for-Azure. It has little relevance to missing-persons work and cannot be run against a tenant you don't control.

## How to use it (`bestInteractionPattern`: docker)
1. Confirm you are authorized to assess the target Azure tenant (this step is not optional — the collection is intrusive and logged).
2. Deploy with Docker Compose (recommended): it spins up the frontend, backend and a Neo4j container.
3. Run **Stormcollector** with your Azure creds (`az login` session or a service principal client ID/secret) to enumerate the subscription(s) — this produces a data package.
4. Upload the collected package into the Stormspotter UI; it loads into Neo4j.
5. Explore the graph: pivot from an identity to the resources and roles it can reach; identify privilege-escalation edges. Query Neo4j directly for custom paths.

## Inputs → Outputs
- **In:** authorized Azure credentials for a tenant (`employer-org` you're assessing)
- **Out:** a graph of Azure/AAD `employer-org` structure — identities, resources, roles, and their relationships (`associate` edges between principals)
- **Empty/negative result looks like:** a sparse graph usually means the credentials lack read scope over parts of the tenant, not that the resources don't exist — collection only sees what the identity can enumerate.

## Gotchas & OpSec
- **Active + legal gate:** collection authenticates to Azure and is logged; only run it against tenants you are contractually authorized to test.
- Requires standing up Neo4j; version/dependency drift (Python 3.8, Node, Neo4j) can complicate the manual install — Docker is the smoother path.
- The graph is a point-in-time snapshot; re-collect for current state.

## Overlaps ("do both")
- Complements broader cloud-enumeration tooling in the Azure/GCP discovery set — Stormspotter focuses on the identity/permission attack graph once you're inside a tenant, whereas external discovery finds the tenant's exposed assets first.

## Trust & verifiability
`trust: trusted` — an official Microsoft/Azure open-source project reading live Azure/AAD APIs, so the graph is authoritative for the tenant at collection time. Verify specific edges against the Azure portal/CLI, since collection reflects only what the supplied identity could see.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | stormspotter |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | employer-org → employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | docker |
| opsec | active |
| human-in-loop | yes (account-login, legal-gate) |
