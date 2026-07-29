---
id: hacking-the-cloud
name: Hacking the Cloud
description: Use when you're assessing cloud infrastructure and need attack/technique references — returns an encyclopedia of AWS/Azure/GCP offensive tactics.
url: https://hackingthe.cloud/
category: search-engines
path:
- search-engines
bestFor: Looking up offensive-security techniques for AWS, Azure, and GCP during authorised cloud assessments.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, open, community-maintained knowledge base (open-source on GitHub); no account.
opsec: passive
opsecNote: Reading the encyclopedia touches no target. The techniques it documents are active by nature — only apply them to cloud environments you own or are explicitly authorised to test.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-known community/open-source cloud-security knowledge base with contributions from practitioners. Reference material — validate techniques in your own authorised lab.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- hacktricks
- pacu
- mitre-attack
aliases:
- hackingthe.cloud
tags:
- cloud-security
- pentest
- reference
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Hacking the Cloud

> An encyclopedia of cloud attack techniques — practical, referenced tactics for AWS, Azure, GCP, and Terraform that offensive-security professionals use during authorised assessments.

## When to use
Reference tool for the cloud-infrastructure side of an engagement: when you've identified that a subject/organisation runs on AWS/Azure/GCP and you need to understand relevant attack paths, misconfigurations, enumeration methods, and privilege-escalation techniques. It maps techniques to concrete commands and to defensive context — a "how do I test this cloud safely and thoroughly" lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://hackingthe.cloud/.
2. Browse by provider (AWS/Azure/GCP) and category (enumeration, initial access, privilege escalation, persistence, defence evasion).
3. Read the technique page: prerequisites, step-by-step commands, and detection/defence notes.
4. Apply only within an authorised scope; use the defensive notes to understand what will be logged.
5. Pivot: technique names map to MITRE ATT&CK (`[[mitre-attack]]`) and to tooling like `[[pacu]]` for AWS exploitation.

## Inputs → Outputs
- **In:** none (a knowledge base — you bring the target context)
- **Out:** documented cloud attack techniques with commands and defensive notes
- **Empty/negative result looks like:** the specific service/technique isn't covered — check a broader hacking wiki or the provider's own security docs.

## Gotchas & OpSec
- **Authorised testing only:** the techniques are active and intrusive; applying them without authorisation is unlawful.
- Cloud providers change fast — verify a technique still works and check current detection behaviour before relying on it.
- It's reference material, not a scanner; pair it with actual tooling to execute (in scope).

## Overlaps ("do both")
- Pairs with `[[hacktricks]]` (broad pentest wiki) and `[[mitre-attack]]` (technique taxonomy), plus tools like `[[pacu]]`. Do both: Hacking the Cloud for cloud-specific depth, the others for cross-domain breadth and structured mapping.

## Trust & verifiability
`trust: community` — a respected, open community knowledge base. Techniques are practitioner-contributed; validate each in your own authorised environment before use, and confirm current provider behaviour.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hacking-the-cloud |
