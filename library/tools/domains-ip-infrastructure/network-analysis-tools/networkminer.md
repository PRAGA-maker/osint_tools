---
id: networkminer
name: NetworkMiner
description: Use when you have a captured PCAP and want to carve out files, images, credentials and host details from the traffic — returns `email`, `password`, `image` and `ip-address` artifacts.
url: https://www.netresec.com/?page=Networkminer
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- network-analysis-tools
bestFor: Passive network forensics — extracting transferred files, images, emails and cleartext credentials from a PCAP without touching the wire.
selectorsIn:
- ip-address
selectorsOut:
- email
- password
- image
- ip-address
status: live
pricing: freemium
costNote: NetworkMiner Free Edition covers PCAP parsing, file/image/credential extraction and live sniffing at no cost; the Professional edition (~$1,300) adds OSINT hash/IP lookups, OS fingerprinting, CLI scripting and browser tracing.
opsec: passive
opsecNote: Analysis is fully offline against a capture you already hold — nothing is sent to any subject or third party. The only exposure is if you enable Pro's online OSINT lookups, which query external services; keep those off for air-gapped work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Flagship tool from Netresec (Sweden), widely used in DFIR and law enforcement training; long track record and reproducible output.
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
- Netresec NetworkMiner
tags:
- network-forensics
- pcap
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# NetworkMiner

> A passive network-forensics tool that reassembles a PCAP into human artifacts — the files, images, emails, certificates and cleartext passwords that crossed the wire.

## When to use
You have a packet capture (PCAP/PcapNG) relevant to an investigation — from a seized device, a honeypot, or a monitored connection you are lawfully permitted to analyse — and you need the *content*, not the packets: which files and images were transferred, which email addresses and credentials appeared in cleartext, and which hosts (`ip-address`) talked to which. NetworkMiner carves all of that out automatically and organises it by host.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download NetworkMiner Free Edition from https://www.netresec.com/?page=Networkminer (portable — no install; runs on Windows, and on Linux via Mono/.NET).
2. File → Open and select your `.pcap`/`.pcapng` (or start a live capture on an interface you are authorised to monitor).
3. Work the tabs: **Hosts** (per-IP inventory with OS guesses), **Files**/**Images** (carved artifacts saved to the assembled-files folder), **Credentials** (cleartext logins seen), **Messages** (emails/chat), **Parameters** (form fields, cookies).
4. Export the carved files for hashing and your evidence log.
5. Pivot: `email`s and `ip-address`es found feed email/IP OSINT; use a full protocol dissector like Wireshark for anything NetworkMiner does not reassemble.

## Inputs → Outputs
- **In:** a PCAP/PcapNG capture (hosts appear as `ip-address`)
- **Out:** carved files and `image`s, `email` addresses, cleartext `password`s/credentials, certificates, per-host OS fingerprints
- **Empty/negative result looks like:** a fully TLS-encrypted capture yields certificates and metadata but no cleartext files or credentials — that reflects encryption, not a tool failure.

## Gotchas & OpSec
- It only recovers what was unencrypted or extractable; modern HTTPS/TLS hides payloads, so expect metadata over content on encrypted traffic.
- The Free Edition omits the online OSINT lookups and CLI scripting of Pro.
- OpSec: passive and offline — safe for air-gapped forensic use. Disable Pro's external lookups if the case must stay off the network.

## Overlaps ("do both")
- Pairs with Wireshark/tshark — NetworkMiner is content-first (artifacts and hosts), Wireshark is packet-first (protocol detail); use NetworkMiner to triage what was transferred, Wireshark to reconstruct exactly how.

## Trust & verifiability
`trust: trusted` — an established DFIR tool from Netresec; every carved artifact can be hashed and re-derived from the source PCAP, so findings are fully reproducible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | networkminer |
