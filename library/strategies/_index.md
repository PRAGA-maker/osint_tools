---
name: strategies-index
description: Root of the Strategies tree — the reasoning of good missing-persons investigators, organized as a pivot graph over investigation phases.
kind: group-index
---

# Strategies

How a good investigator *thinks* — not just what tools exist. A strategy answers: "given selector X, what's the highest-yield move to reach selector Y, and how do I avoid fooling myself?" Tools are the *what*; strategies are the *when, why, and in what order*.

This tree pairs 1:1 with `tools/` through the shared **selector vocabulary** (`schema/taxonomy.md`): a strategy's `pivotFrom`/`pivotTo` line up with a tool's `selectorsIn`/`selectorsOut`.

## Structure
- **`00-phases/`** — the arc of an investigation: `intake → triage → pivot → enrichment → verification → reporting`, plus cross-cutting `opsec`. Read these first; they frame everything else.
- **`pivots/`** — the heart: `<from-selector>/<to-selector>/<technique>.md`. The directed edges of the investigation graph.
- **`patterns/`** — reusable good moves that aren't tied to one pivot (selector discipline, network triangulation, timeline anchoring).
- **`antipatterns/`** — the tempting wrong moves and *why they fail* (tunnel vision, forcing a match, contaminating the subject).
- **`playbooks/`** — ordered sequences for a situation type ("runaway teen, social-first"; "single photo, unknown subject").
- **`platforms/`** — per-platform technique notes (what's publicly enumerable, the good pivots, the gotchas).
- **`case-studies/`** — what actually worked in solved cases / CTFs (harvested from writeups).

## The one-paragraph doctrine
Missing-persons OSINT is **selector expansion under verification**. You start with a thin set of selectors, expand breadth-first into new selectors via pivots, and *continuously verify* that each new selector still refers to the same person. Social media is where most hackathon/CTF cases break, because people leak `geolocation`, `associate`, and `face` selectors there constantly. The failure modes are almost always cognitive (tunnel vision, confirmation bias), not tooling — which is why the `antipatterns/` branch matters as much as `pivots/`.
