---
name: pivots-index
description: The directed edges of the investigation graph — <from-selector>/<to-selector>/<technique>. The heart of the strategies tree.
kind: group-index
---

# Pivots

A pivot is a tool-driven conversion of one selector into another — an edge in the investigation graph. Folders are `<from-selector>/<to-selector>/`, mirroring the `pivotFrom`/`pivotTo` vocabulary and pairing 1:1 with the Tools tree's `selectorsIn`/`selectorsOut`.

Run the cheap, passive, high-yield edges first (see `[[phase-triage]]` and `[[pattern-breadth-before-depth]]`), and gate every new selector through `[[phase-verification]]`.

## By starting selector

### from `username`
- **[[username-reuse-enumeration]]** (`username → social-profile`) — handle-reuse across platforms; usually the highest-yield early pivot.

### from `image` / `face`
- **[[pivot-image-to-geolocation]]** (`image → geolocation`) — reverse image + read signs, architecture, terrain, sun to place a photo.
- **[[pivot-image-to-face]]** (`image → face → name`) — face-search engines to find the person; verification-heavy, high-risk.
- **[[pivot-exif-and-chronolocation]]** (`image → metadata-exif`) — pull EXIF GPS/time; chronolocate from shadows/season when stripped.

### from `name`
- **[[pivot-name-to-accounts]]** (`name → social-profile`) — search + disambiguate a real name down to one person's accounts.

### from `phone`
- **[[pivot-phone-to-identity]]** (`phone → name`) — caller-ID, messaging-app presence, records; passive-vs-active is the key choice.

### from `email`
- **[[pivot-email-to-accounts]]** (`email → social-profile`) — account discovery + breach/leak mining; local-part as a handle.

### from `social-profile` / `associate`
- **[[pivot-network-triangulation]]** (`social-profile → associate`) — reach a private subject through their network's public content.

## The cross-cutting rule
Every pivot ends the same way: the new selector is a **candidate** until two independent signals confirm it. Convergence between pivots IS the verification — see `[[phase-verification]]` and `[[antipattern-forcing-the-match]]`.
