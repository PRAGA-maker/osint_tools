---
id: filevault
name: FileVault
description: Use when you need to encrypt your own investigator macOS device at rest so seized/lost hardware cannot leak case data — a defensive opsec control, not a selector lookup.
url: https://support.apple.com/en-us/HT204837
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Full-disk encryption of the investigator's own Mac to protect stored case material.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Built into macOS at no cost; no download or account required.
opsec: passive
opsecNote: This protects YOUR data, not a target's. Enabling it encrypts the whole startup disk with a key tied to your login/recovery key — store the recovery key offline; losing it means permanent data loss. It leaks nothing about anyone and is purely defensive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: First-party Apple full-disk encryption (XTS-AES-128) documented on Apple Support; the reference standard for Mac at-rest protection.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Apple FileVault
- macOS full-disk encryption
tags:
- privacy-and-encryption-tools
- opsec
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# FileVault

> Apple's built-in macOS full-disk encryption — an investigator opsec control that keeps stored case data unreadable if the Mac is lost, stolen, or seized.

## When to use
You store OSINT case material on a Mac and want at-rest protection so a lost, stolen, or legally seized device does not expose subjects' data or your sources. This is a defensive hygiene step for the operator; it returns no intelligence about any target.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Open **System Settings → Privacy & Security → FileVault** (older macOS: System Preferences → Security & Privacy → FileVault).
2. Click **Turn On FileVault**.
3. Choose how to unlock/recover: an iCloud account unlock or a locally stored recovery key. For opsec prefer the **recovery key** and store it offline, away from the machine.
4. Let the initial encryption complete; thereafter the disk is encrypted whenever powered off.
5. No pivot — this is a terminal defensive step, not an investigative lead.

## Inputs → Outputs
- **In:** none (a configuration action on your own device)
- **Out:** none (an encrypted disk state)
- **Empty/negative result looks like:** N/A — success is simply "FileVault: On"; failure is being unable to enable it (unsupported hardware/OS).

## Gotchas & OpSec
- Lose the recovery key **and** your password → data is unrecoverable by design. Escrow the key securely.
- Protection applies at rest (powered off); a running, unlocked Mac is still exposed — combine with screen-lock and a strong login password.
- OpSec: **passive**; it touches no external service and reveals nothing about anyone.

## Overlaps ("do both")
- Pairs with encrypted external evidence volumes and a password manager so case data is protected both on-disk and in transit/backup.

## Trust & verifiability
`trust: trusted` — first-party Apple feature (XTS-AES-128) documented on Apple Support; verify state in Settings, no third-party involved.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | filevault |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
