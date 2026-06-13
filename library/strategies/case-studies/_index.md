---
name: case-studies-index
description: Real solved cases and CTF writeups — what actually worked — harvested from external sources. Populated by a separate harvest pass, not hand-authored.
kind: group-index
---

# Case studies

What actually broke real cases. Where the rest of the tree is the *general method*, this branch is the *evidence*: solved missing-persons cases, Trace Labs-style CTF writeups, and documented investigations, each distilled into the pivot chain that worked and the lesson it teaches.

## Status
**Empty by design — pending harvest.** This folder is populated by a separate harvest pass that mines writeups and case reports, not by hand-authoring. The deliberate split keeps the method tree (transferable reasoning) free of invented specifics, and keeps real-case facts traceable to their `source`.

## What goes here (for the harvest pass)
Each case study should:
- Use `type: case-study` and carry an `evidence[]` block citing the writeup/case/article it's drawn from (with `url` and `note`), plus a `source` id.
- Distill the **pivot chain that worked** — which selectors, in what order, through which pivots — and cross-link the relevant `pivots/`, `patterns/`, and `playbooks/` with `[[id]]`.
- Name the **lesson**: the pattern it confirms or the antipattern it illustrates (e.g. a case where reverse-image-everything cracked it, or where forcing-the-match sent investigators wrong).
- Respect the safety bar — real cases involving real (often vulnerable) people; cite responsibly and avoid re-publishing sensitive personal data.

## Until then
The transferable reasoning lives in `[[phases-index]]`, `[[pivots-index]]`, `[[patterns-index]]`, `[[antipatterns-index]]`, and `[[playbooks-index]]`. Case studies will ground that reasoning in what demonstrably worked.
