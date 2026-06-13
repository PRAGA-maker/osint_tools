---
name: pivots-email-index
description: Pivots that start from an email — near-unique, and a key into both account discovery and breach data.
kind: group-index
---

# Pivots from `email`

An email is close to unique and forks into account discovery, breach/leak mining, and a username candidate (the local-part). One of the highest-yield seeds to hold.

## Sub-pivots
- **`social-profile/`** → [[pivot-email-to-accounts]] — passive account-discovery + breach/leak mining + local-part-as-handle enumeration.

## Watch
Prefer passive discovery — registration probes that email the subject are a contamination risk (`[[antipattern-contaminating-the-subject]]`).
