---
id: mailto-analyzer
name: MAILTO ANALYZER
description: Use when you have access to an `email` account's mailbox (.mbox export) and want to map which services that address is registered on — returns the list of sites/services (`social-profile`s) tied to the email, analyzed locally.
url: https://github.com/soxoj/mailto_analyzer
category: email
path:
- email
bestFor: Parsing an .mbox export to reveal every service an email address is registered with (from its received notifications/newsletters).
selectorsIn:
- email
selectorsOut:
- social-profile
- email
status: live
pricing: free
costNote: Free and open-source (Python). Runs entirely locally — the author notes it does not transfer data to third-party servers.
opsec: passive
opsecNote: Requires you to already have the mailbox export (.mbox) — i.e. lawful access to that account — and analyzes it locally, sending nothing externally. This is account/consented analysis, not remote reconnaissance; only run on mailboxes you own or are authorized to examine.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: cli
trust: community
trustNote: An open-source tool by soxoj (author of Maigret), well-regarded in the OSINT community; local-only processing, but review the code as with any tool.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- mailto_analyzer
- MAILTO ANALYZER
tags:
- Emails
- mbox
- account-enumeration
source: cyb-detective
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- 1c-database-converter
- awesome-osint-mcp-servers
- counter-osint-guide-for-russians
- fravia-soxoj
- gitcolombo
- maigret
- maigret-via-socid-extractor-soxoj-ecosystem
- marple
- osint-namecheckers-list
- socid-extractor
- username-generation-guide
---

# MAILTO ANALYZER

> A local Python tool that reads an .mbox mailbox export and maps out every online service the address is registered with — reconstructing a person's account footprint from their own inbox.

## When to use
You have lawful access to a subject's mailbox (an `.mbox` export — e.g. a Google Takeout, a seized/consented account) and want to enumerate which services that email is registered on. Registration confirmations, newsletters, and notification emails betray the accounts a person holds, giving a rich map of their online footprint — all analyzed locally, nothing sent out.

## How to use it (`bestInteractionPattern`: cli)
1. Export the mailbox to `.mbox` (Google Takeout, Thunderbird export, etc.) — you must have authorized access.
2. Clone https://github.com/soxoj/mailto_analyzer and install its Python requirements.
3. Run it against the `.mbox` file; it parses senders/content and identifies the services the address is registered with.
4. Review the output list of sites/services (a table of the account's exposure).
5. Pivot: each identified service → check for a `social-profile` under the person's usual handle; unexpected services → new leads; combine with breach-search for the same email.

## Inputs → Outputs
- **In:** an `.mbox` mailbox export for the target `email` (authorized access)
- **Out:** a list of services/sites the email is registered with (`social-profile` leads), analyzed locally
- **Empty/negative result looks like:** few services detected — a sparse/new mailbox, or one that's been cleaned. Thin output reflects the mailbox contents, not the person's full footprint; supplement with breach-search and username enumeration.

## Gotchas & OpSec
- **Requires the mailbox** — this is consented/authorized account analysis, not remote recon on someone else's live account.
- Fully local (no third-party transfer), but handle the mailbox securely — it contains sensitive data.
- Only surfaces services that emailed the address; account-less or notification-off services won't appear.

## Overlaps ("do both")
- Pairs with account-existence checkers (`[[account-live-com]]`), breach-search (HIBP/Dehashed), and `[[whatsmyname-python]]` — the mailbox reveals registered services from the inside; those probe for accounts from the outside.

## Trust & verifiability
`trust: community` — an open-source tool by a respected OSINT author, processing data locally. The service list is derived from real received mail, but confirm each account independently before treating it as the subject's.
