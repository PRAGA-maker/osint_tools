#!/usr/bin/env python3
"""Merge a batch of enrichment metadata into public/arf.json by matching tool `name`.

Historical helper from the domain-enrichment batches. Archived here alongside the
batch data it operates on. Paths are resolved relative to the repo root, so it can
be run from anywhere:

    python library/ledger/enrich-batches/merge_enrichments.py [enrichment.json]

`enrichment.json` defaults to the batch4 domains file in this directory. The file
must be `{"enrichments": {"<Tool Name>": {<fields to merge>}, ...}}`.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[2]  # library/ledger/enrich-batches -> repo root
ARF_PATH = REPO_ROOT / "public" / "arf.json"
DEFAULT_ENRICHMENT = HERE / "enrichment-batch4-domains.json"


def merge_enrichment_into_node(node, enrichments):
    """Recursively search and merge enrichment data into matching nodes."""
    if isinstance(node, dict):
        if node.get("name") in enrichments:
            node.update(enrichments[node["name"]])
        for child in node.get("children", []):
            merge_enrichment_into_node(child, enrichments)


def main():
    enrichment_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_ENRICHMENT

    enrichments = json.loads(enrichment_path.read_text(encoding="utf-8"))["enrichments"]
    arf_data = json.loads(ARF_PATH.read_text(encoding="utf-8"))

    merge_enrichment_into_node(arf_data, enrichments)

    # Match upstream arf.json serialization exactly: indent=2, ensure_ascii, trailing newline.
    ARF_PATH.write_text(
        json.dumps(arf_data, indent=2, ensure_ascii=True) + "\n", encoding="utf-8"
    )

    print(f"Merged enrichment data for {len(enrichments)} tools into {ARF_PATH}")


if __name__ == "__main__":
    main()
