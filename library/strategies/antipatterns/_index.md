---
name: antipatterns-index
description: The tempting wrong moves and why they fail — the cognitive and opsec failures that sink missing-persons investigations more often than missing tools do.
kind: group-index
---

# Antipatterns

In missing-persons OSINT the failure modes are almost always cognitive or opsec, not tooling. These are the moves that *feel* right and aren't. Each names the temptation, explains why it fails, and gives the fix.

## Children
- **[[antipattern-forcing-the-match]]** — promoting a candidate to "confirmed" on thin evidence because you want it to be them; the most damaging error, since it produces confident false reports about real people.
- **[[antipattern-tunnel-vision]]** — committing depth-first to one platform/lead before exhausting cheap breadth; effort without expansion.
- **[[antipattern-contaminating-the-subject]]** — any detectable engagement (follow/message/view/contact) that tips off the subject or network; the gravest opsec failure because the harm lands on a vulnerable person.
- **[[antipattern-trusting-stripped-metadata]]** — reading "no EXIF" as "no data" (platforms strip it), or trusting present metadata as gospel (it can be wrong/spoofed).
- **[[antipattern-paywall-rabbit-hole]]** — burning time and money chasing people-search teasers when free passive pivots would answer the same question.

## The pattern behind the antipatterns
Three are cognitive (forcing-the-match, tunnel-vision, trusting-metadata), one is opsec (contaminating-the-subject), one is resource-management (paywall-rabbit-hole). Their fixes all live in the phases and patterns: verification, breadth-before-depth, opsec, and selector discipline. The antipatterns matter as much as the pivots — knowing the right move isn't enough if the wrong one feels better in the moment.
