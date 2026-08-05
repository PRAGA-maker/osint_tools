---
id: password-safe
name: Password Safe
description: Use when you need to store the many sock-puppet logins and credentials of an investigation in one encrypted local vault — returns secure, offline password management (investigator OpSec).
url: https://pwsafe.org/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Keeping investigation sock-puppet accounts and credentials in a single encrypted, offline vault.
selectorsIn: []
selectorsOut:
- password
status: live
pricing: free
costNote: Free and open source (originally designed by Bruce Schneier's team); no account or cloud dependency.
opsec: passive
opsecNote: A local, offline vault — nothing syncs to a third party by default, which is exactly what you want for sensitive credentials. Its safety rests on a strong master passphrase and securing the .psafe3 database file; if that file and passphrase leak, every sock puppet is exposed at once.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Long-standing open-source password manager conceived by Bruce Schneier; auditable code, no cloud, widely trusted for offline credential storage.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- pwsafe
- pwsafe.org
tags:
- toddington
- curated-directory
- proxy-servers-online-privacy-security-tools
- password-manager
- opsec
source: toddington-resources
lastVerified: '2026-08-05'
enrichment: full
---

# Password Safe

> A free, offline, open-source password manager (a Bruce Schneier design): one encrypted local database holds all the throwaway logins an investigation accumulates, so you never reuse or lose a sock-puppet credential.

## When to use
Any real investigation spawns a pile of sock-puppet accounts — emails, social logins, forum handles, disposable numbers — and reusing passwords or storing them in a browser is an OpSec failure waiting to happen. Password Safe keeps them in a single encrypted, offline vault, generating strong unique passwords per account. It protects *your* tradecraft; it returns no subject data.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download Password Safe from https://pwsafe.org/ (Windows native; Linux/macOS ports and compatible apps exist) and install on your investigation machine/VM.
2. Create a new database (`.psafe3`) protected by a strong master passphrase — this is the one secret you must never lose or reuse.
3. Add an entry per sock-puppet account (username, generated password, URL, notes). Use the built-in generator for each password.
4. Keep the database file backed up securely and offline; unlock it only on a trusted machine.
5. Pivot: consistent per-persona credentials keep sock puppets from colliding and make it easy to retire an identity cleanly.

## Inputs → Outputs
- **In:** your own account credentials to store (no subject data)
- **Out:** an encrypted local vault of `password`s and account metadata
- **Empty/negative result looks like:** a forgotten master passphrase means the vault is unrecoverable by design — there is no backdoor, so passphrase hygiene is non-negotiable.

## Gotchas & OpSec
- Human-in-the-loop: none beyond unlocking.
- OpSec: passive and offline — nothing leaves your machine, which is the point. The whole vault's security collapses to one master passphrase plus physical control of the `.psafe3` file; protect both.
- Offline by default means no cross-device sync unless you deliberately (and carefully) move the file — a feature for sensitive work, an inconvenience otherwise.

## Overlaps ("do both")
- Pairs with [[tor-browser]] and disposable-account tooling like [[smstome-com]] — those create and carry the sock-puppet identities, this remembers their credentials securely; do both to run puppets without cross-contamination.

## Trust & verifiability
`trust: trusted` — a mature, open-source manager from a respected lineage, with no cloud component to compromise. The code is auditable; the risk model is entirely local (master passphrase + file security).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | password-safe |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  → password |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
