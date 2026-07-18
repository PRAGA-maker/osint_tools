---
id: coeus-osint-toolbox
name: Coeus-OSINT-ToolBox
description: Use when you have a `username`, `email`, `phone`, or `domain` and want a GUI to run several OSINT lookups at once — returns `social-profile`s, `email`s, and `phone` leads.
url: https://github.com/AnonCatalyst/Coeus-OSINT-ToolBox
category: people-search
path:
- people-search
bestFor: GUI-driven multi-selector OSINT lookups bundled into one Python app.
selectorsIn:
- username
- email
- phone
- domain
selectorsOut:
- social-profile
- email
- phone
status: live
pricing: free
costNote: Free and open-source (GitHub); you run it locally, so the only cost is setup and any API keys individual modules need.
opsec: passive
opsecNote: Mostly passive — it queries public sources — but it's a bundle of modules with varying behavior, and some may make requests that touch a target's infrastructure. Run from a sock-puppet environment/VPN and review what each module does before firing it at a real subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: Community project by AnonCatalyst (few hundred GitHub stars); convenient aggregator, but module reliability varies and the code is unaudited.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- ominis-osint
- webhound-anoncatalyst
aliases:
- coeus
- Coeus OSINT ToolBox
tags:
- toolbox
- gui
- multi-tool
source: gh-topic-osint-framework
lastVerified: '2026-07-18'
enrichment: full
---

# Coeus-OSINT-ToolBox

> A locally-run Python GUI that bundles multiple OSINT modules so you can pivot a username, email, phone, or domain across several sources from one window.

## When to use
Early-stage enrichment when you have one or more selectors — a `username`, `email`, `phone`, or `domain` — and want to run a batch of common lookups without wiring up separate scripts. Good for quickly widening a thin lead into candidate `social-profile`s, related `email`s/`phone`s, and other pivots; treat its output as leads to verify in authoritative tools.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Clone `https://github.com/AnonCatalyst/Coeus-OSINT-ToolBox` and install the Python requirements per the README.
2. Launch the GUI application.
3. Choose a module for your selector (username / email / phone / domain) and enter the value; supply any API keys a module needs.
4. Run the lookup and read the aggregated results; export or note the candidate profiles/contacts.
5. Pivot: feed the returned handles/emails/phones into dedicated, verifiable people-search and breach tools to confirm.

## Inputs → Outputs
- **In:** `username`, `email`, `phone`, or `domain`.
- **Out:** candidate `social-profile`s, associated `email`s and `phone`s, and related pivots.
- **Empty/negative result looks like:** a module returns no hits or errors out (dead upstream source/blocked request) — expected as third-party endpoints change; don't read a blank result as "nothing exists."

## Gotchas & OpSec
- Module drift: it wraps third-party sources that break over time — verify each module still works before trusting its silence.
- Local setup: needs Python and dependencies; some modules require their own API keys.
- Unaudited: community code — review a module's behavior before pointing it at a real target.
- OpSec: mostly passive, but run behind a VPN/sock-puppet in case a module makes attributable requests.

## Overlaps ("do both")
- Pairs with `[[ominis-osint]]` and `[[webhound-anoncatalyst]]` (same author's ecosystem) and with maintained aggregators — cross-check Coeus's leads against tools with more reliable, current data.

## Trust & verifiability
`trust: community` — a handy unofficial aggregator whose value depends on its wrapped sources; always confirm findings in an authoritative, verifiable tool before acting on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | coeus-osint-toolbox |
| category | people-search |
| selectorsIn → selectorsOut | username, email, phone, domain → social-profile, email, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
