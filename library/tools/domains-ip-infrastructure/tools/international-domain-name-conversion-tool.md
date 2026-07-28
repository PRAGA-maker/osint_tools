---
id: international-domain-name-conversion-tool
name: International Domain Name Conversion Tool
description: Use when you have a `domain` in Unicode/IDN or Punycode form and want its equivalent — returns the converted form so you can spot look-alike/homograph domains.
url: https://mct.verisign-grs.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- tools
bestFor: Converting between a Unicode internationalized domain (IDN) and its ASCII Punycode (xn--) form to unmask homograph/look-alike domains.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free public tool from Verisign; no account required.
opsec: passive
opsecNote: Conversion happens in the tool without contacting the target domain, so it is passive — the domain owner sees nothing. You do type the domain into Verisign's site.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Verisign (the .com/.net registry operator); the IDN↔Punycode conversion follows the published IDNA standard, so output is authoritative.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- who-is
aliases:
- Verisign IDN Conversion Tool
- Punycode converter
- IDN converter
tags:
- Domain/IP investigation
- idn
- punycode
- arf-seed
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# International Domain Name Conversion Tool

> Verisign's IDN ↔ Punycode converter — turn a Unicode domain into its `xn--` ASCII form (and back) to reveal look-alike and homograph domains used for spoofing.

## When to use
You have a `domain` that either contains non-ASCII characters (an internationalized domain name, e.g. Cyrillic/Greek/accented letters) or an unfamiliar `xn--…` Punycode string, and you need its true equivalent. This is the standard move for **homograph attacks**: `аpple.com` (Cyrillic а) and `apple.com` look identical but are different domains — converting to Punycode exposes the deception. Also use it to normalize IDNs before WHOIS/DNS lookups that expect the ASCII form.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://mct.verisign-grs.com/.
2. Paste the domain — either the Unicode form (e.g. `café.com`) or the Punycode form (e.g. `xn--caf-dma.com`).
3. Run the conversion; the tool returns the counterpart form (Unicode → Punycode, or Punycode → Unicode).
4. Compare against the legitimate brand/domain you expected — a mismatch or unexpected script signals a spoof/look-alike.
5. Pivot: take the true ASCII (`xn--`) form into `[[who-is]]`, DNS and reputation tools to see who registered the look-alike and where it points.

## Inputs → Outputs
- **In:** `domain` (Unicode IDN or Punycode `xn--` string)
- **Out:** `domain` (the converted equivalent form)
- **Empty/negative result looks like:** a plain ASCII domain with no international characters converts to itself (nothing hidden); an error means malformed input — check for stray spaces or invalid characters.

## Gotchas & OpSec
- This only converts encoding — it does **not** tell you if a domain is malicious; a valid conversion of a spoof domain still needs WHOIS/reputation follow-up.
- Rendering of the Unicode form depends on your fonts; rely on the `xn--` output, not on how the Unicode looks on screen.
- Fully passive; the target domain is never contacted.

## Overlaps ("do both")
- Pairs with `[[who-is]]` — convert the look-alike to its ASCII form here, then run WHOIS/DNS on that form to identify the registrant and hosting behind a suspected spoof.

## Trust & verifiability
`trust: trusted` — provided by Verisign, operator of the .com/.net registries; the conversion implements the standardized IDNA algorithm, so the ASCII/Unicode mapping is authoritative and reproducible with any conformant Punycode library.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | international-domain-name-conversion-tool |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
