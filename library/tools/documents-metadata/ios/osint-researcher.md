---
id: osint-researcher
name: OSINT Researcher (iOS)
description: Use when you have a GitHub `username`, org or repo URL and want members, repos and contribution history on the go — returns linked accounts, project metadata and `associate` (team) leads.
url: https://apps.apple.com/us/app/osint-researcher/id6747302251
category: documents-metadata
path:
- documents-metadata
- ios
bestFor: Mobile GitHub reconnaissance — mapping an organization's members, repositories, and contribution history from an iPhone/iPad.
selectorsIn:
- username
- employer-org
selectorsOut:
- username
- associate
- employer-org
status: live
pricing: free
costNote: Free iOS app on the US App Store; requires an Apple device to install (no web version).
opsec: passive
opsecNote: It queries GitHub's public API/data, so it doesn't alert the target. But it runs on your personal device via your App Store account — install from a research device/account if attribution matters, and be aware it's a third-party app whose data handling is unverified.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: mobile-app
trust: unverified
trustNote: A third-party iOS app of unknown developer provenance; it surfaces public GitHub data, which you can independently verify on github.com.
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
- OSINT Researcher app
tags:
- github
- code-osint
- ios
- mobile-app
source: arf-seed
lastVerified: '2026-07-21'
enrichment: full
---

# OSINT Researcher (iOS)

> An iOS app for GitHub reconnaissance — organization structure, member lists, and contribution history in your pocket.

## When to use
You have a GitHub `username`, organization, or repository URL and want to map the people and projects around it — who the members are, what they contribute to, and how an org's repos connect. GitHub footprints expose real names, emails (in commits), collaborators, and interests. This app packages that recon for mobile use when you're away from a desk. On a workstation, a browser or the GitHub API does the same and more; this shines for on-the-go lookups.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Install "OSINT Researcher" from the US App Store on a research iPhone/iPad.
2. Enter an organization name, GitHub profile, or repository URL.
3. Review the output: organization members, repository lists, contribution history, project metadata.
4. Note co-contributors and linked accounts as `associate` leads; pull real names/emails from commit history in the browser.
5. Pivot: GitHub usernames feed cross-platform username-search; commit emails feed email OSINT; org membership maps a professional network.

## Inputs → Outputs
- **In:** GitHub `username`, `employer-org` (org name), or repo URL
- **Out:** members, repos, contribution history → linked `username`s, co-contributor `associate`s, `employer-org` structure
- **Empty/negative result looks like:** an org/user with no public repos or members returns little — GitHub activity is optional, so absence isn't proof of no coding presence.

## Gotchas & OpSec
- iOS-only: needs an Apple device; no web fallback in-app (use github.com/API on desktop).
- Third-party app of unknown provenance: verify anything material directly on github.com, and mind that it runs under your App Store account.
- Public-data only: it can't see private repos/members; results reflect what GitHub exposes publicly.
- OpSec: passive toward the target; the exposure is your own device/account.

## Overlaps ("do both")
- Pairs with browser/API-based GitHub OSINT and commit-email harvesting — the app is the mobile front end; deeper enumeration (commit emails, cross-repo graphs) is easier on desktop tooling.

## Trust & verifiability
`trust: unverified` — an unvetted third-party app, but it presents public GitHub data you can confirm yourself on github.com; treat the app as a convenience layer over verifiable sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-researcher |
| category | documents-metadata |
| selectorsIn → selectorsOut | username, employer-org → username, associate, employer-org |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | mobile-app |
| opsec | passive |
| human-in-loop | no |
