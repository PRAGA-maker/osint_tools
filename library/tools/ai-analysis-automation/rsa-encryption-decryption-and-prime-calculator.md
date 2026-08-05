---
id: rsa-encryption-decryption-and-prime-calculator
name: RSA Encryption, Decryption and Prime Calculator
description: Use when you have RSA key parameters (n, e, d, p, q) or ciphertext from a CTF/crypto artifact and want to encrypt, decrypt, or factor small keys in-browser — an analysis utility, not a data source.
url: https://canihavesomecoffee.github.io/js-rsa-tool/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: In-browser RSA encrypt/decrypt and small-key prime factoring for CTF/crypto exercises.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, open-source static web tool hosted on GitHub Pages; no account required.
opsec: passive
opsecNote: It's a client-side JavaScript tool (runs in your browser), so parameters you enter aren't sent to a server — safe for scratch crypto work. Even so, never paste real private keys/secrets into any web tool; use it for CTF/test values.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A small open-source JS RSA tool; fine for learning/CTF and small numbers, but not a substitute for a vetted crypto library on anything real.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- js-rsa-tool
- RSA prime calculator
tags:
- crypto
- ctf
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# RSA Encryption, Decryption and Prime Calculator

> A client-side RSA playground — encrypt, decrypt, and factor small RSA keys right in the browser, handy for CTF crypto challenges.

## When to use
Crypto/CTF support, not a person lookup. You've got RSA parameters from a challenge or artifact — a modulus `n`, exponent `e`, maybe a `d`, or a ciphertext — and want to compute quickly: derive `d` from `p`/`q`, factor a small `n`, or encrypt/decrypt a test value. This tool does that interactively without setting up a Python/SageMath environment.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://canihavesomecoffee.github.io/js-rsa-tool/.
2. Enter your known parameters (n, e, d, p, q as available) or ciphertext.
3. Use the prime/factoring function for small moduli, or the encrypt/decrypt function with your key.
4. Read the computed result (recovered key components or plaintext).
5. Pivot: recovered plaintext may contain a flag, a message, or embedded selectors to feed onward.

## Inputs → Outputs
- **In:** RSA key parameters / ciphertext (no person selector)
- **Out:** computed keys, factors, or decrypted text
- **Empty/negative result looks like:** factoring stalls or returns nothing — the modulus is too large for browser-side factoring; move to proper tooling (e.g. `yafu`, `RsaCtfTool`, SageMath).

## Gotchas & OpSec
- **Small numbers only:** browser-side factoring handles toy/CTF-sized moduli, not real 2048-bit keys.
- **Never enter real secrets** into any web tool — reserve it for CTF/test values.
- It's a learning/CTF aid, not a production crypto library; don't rely on it for anything security-critical.

## Overlaps ("do both")
- For anything beyond small CTF values, step up to `RsaCtfTool`, `yafu`, or SageMath; use this only for quick interactive checks.

## Trust & verifiability
`trust: community` — a small open-source client-side tool; results for small inputs are easy to verify by recomputation, and you should never trust any web tool with real key material.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rsa-encryption-decryption-and-prime-calculator |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
