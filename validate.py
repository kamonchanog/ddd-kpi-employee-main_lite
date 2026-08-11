#!/usr/bin/env python3
"""
validate.py — Three-level validator for DDD files

Level 1: JSON syntax
Level 2: Schema validation (requires jsonschema; skipped with warning if absent)
Level 3: Semantic checks (pure stdlib)
"""

import json
import sys
import argparse

ERRORS = []
WARNINGS = []
CHECKS = []
FORMAT = "text"


def fail(msg):
    ERRORS.append(msg)
    CHECKS.append({"level": "error", "message": msg})
    if FORMAT == "text":
        print(f"  ✗ {msg}")


def warn(msg):
    WARNINGS.append(msg)
    CHECKS.append({"level": "warning", "message": msg})
    if FORMAT == "text":
        print(f"  ⚠ {msg}")


def ok(msg):
    CHECKS.append({"level": "ok", "message": msg})
    if FORMAT == "text":
        print(f"  ✓ {msg}")


# ---------------------------------------------------------------------------
# Level 1 — JSON syntax
# ---------------------------------------------------------------------------

def level1_json_syntax(ddd_path, schema_path):
    if FORMAT == "text":
        print("\nLevel 1 — JSON syntax")
    data, schema = None, None

    try:
        with open(ddd_path) as f:
            data = json.load(f)
        ok(f"{ddd_path} is valid JSON")
    except FileNotFoundError:
        fail(f"{ddd_path} not found")
    except json.JSONDecodeError as e:
        fail(f"{ddd_path} JSON parse error: {e}")

    try:
        with open(schema_path) as f:
            schema = json.load(f)
        ok(f"{schema_path} is valid JSON")
    except FileNotFoundError:
        fail(f"{schema_path} not found")
    except json.JSONDecodeError as e:
        fail(f"{schema_path} JSON parse error: {e}")

    return data, schema


# ---------------------------------------------------------------------------
# Level 2 — Schema validation
# ---------------------------------------------------------------------------

def level2_schema(data, schema):
    if FORMAT == "text":
        print("\nLevel 2 — Schema validation")
    if data is None or schema is None:
        warn("Skipping schema validation (JSON parse failed above)")
        return

    try:
        import jsonschema  # type: ignore[import-untyped]
        jsonschema.validate(data, schema)
        ok("Schema validation passed")
    except ImportError:
        warn("jsonschema not installed — skipping (pip install jsonschema to enable)")
    except Exception as e:
        fail(f"Schema validation failed: {e}")


# ---------------------------------------------------------------------------
# Level 3 — Semantic checks
# ---------------------------------------------------------------------------

def level3_semantic(data):
    if FORMAT == "text":
        print("\nLevel 3 — Semantic checks")
    if data is None:
        warn("Skipping semantic checks (JSON parse failed)")
        return

    # Collect all document IDs from phases
    all_doc_ids = []
    all_docs = {}  # id -> document dict
    for phase in data.get("phases", []):
        for doc in phase.get("documents", []):
            doc_id = doc.get("id")
            if doc_id:
                all_doc_ids.append(doc_id)
                all_docs[doc_id] = doc

    generation_order = data.get("meta", {}).get("generation_order", [])

    # Check generation_order has exactly the same IDs as all_doc_ids
    gen_set = set(generation_order)
    doc_set = set(all_doc_ids)
    missing_from_order = doc_set - gen_set
    extra_in_order = gen_set - doc_set

    if missing_from_order or extra_in_order:
        if missing_from_order:
            fail(f"generation_order missing IDs: {sorted(missing_from_order)}")
        if extra_in_order:
            fail(f"generation_order has unknown IDs: {sorted(extra_in_order)}")
    else:
        ok(f"generation_order has {len(generation_order)}/{len(all_doc_ids)} document IDs")

    # Check topological order: all depends_on must appear before this doc
    seen = set()
    topo_ok = True
    for doc_id in generation_order:
        doc = all_docs.get(doc_id)
        if doc is None:
            continue
        for dep in doc.get("depends_on", []):
            if dep not in doc_set:
                fail(f"'{doc_id}.depends_on' references unknown ID '{dep}'")
                topo_ok = False
            elif dep not in seen:
                fail(f"Topological violation: '{doc_id}' depends on '{dep}' which appears later in generation_order")
                topo_ok = False
        seen.add(doc_id)

    if topo_ok and not ERRORS:
        ok("Topological order valid")
    elif topo_ok:
        ok("Topological order valid (other errors above)")

    # Check all refs[] entries resolve to valid doc IDs
    refs_ok = True
    sections_refs_ok = True
    for doc_id, doc in all_docs.items():
        for section in doc.get("sections", []):
            if "refs" not in section:
                fail(f"'{doc_id}' section '{section.get('id', '?')}' is missing 'refs' key")
                sections_refs_ok = False
            else:
                for ref in section["refs"]:
                    if ref not in doc_set:
                        fail(f"'{doc_id}' section '{section.get('id', '?')}' refs unknown ID '{ref}'")
                        refs_ok = False

    if refs_ok:
        ok("All refs[] resolve to valid document IDs")
    if sections_refs_ok:
        ok("All sections have refs[] key")

    # Check document order within each phase matches generation_order
    gen_set = set(generation_order)
    for phase in data.get("phases", []):
        phase_ids = [d["id"] for d in phase.get("documents", []) if d.get("id")]
        gen_filtered = [x for x in generation_order if x in set(phase_ids)]
        if phase_ids != gen_filtered:
            warn(f"Phase '{phase['id']}' document order doesn't match generation_order")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    global FORMAT
    parser = argparse.ArgumentParser(description="Validate a DDD file")
    parser.add_argument("--file", default="ddd-kpi-employee-v1.0.0.json", help="Path to DDD file (default: ddd-kpi-employee-v1.0.0.json)")
    parser.add_argument("--schema", default="ddd-schema.json", help="Path to schema file (default: ddd-schema.json)")
    parser.add_argument("--format", choices=["text", "json"], default="text", help="Output format (default: text)")
    args = parser.parse_args()
    FORMAT = args.format

    if FORMAT == "text":
        print(f"Validating {args.file} against {args.schema}")

    data, schema = level1_json_syntax(args.file, args.schema)
    level2_schema(data, schema)
    level3_semantic(data)

    passed = len(ERRORS) == 0
    if FORMAT == "json":
        import json as _json
        print(_json.dumps({"passed": passed, "errors": ERRORS, "warnings": WARNINGS, "checks": CHECKS}))
    else:
        print()
        if ERRORS:
            print(f"FAILED — {len(ERRORS)} error(s), {len(WARNINGS)} warning(s)")
        else:
            print(f"PASSED — {len(WARNINGS)} warning(s)")
    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
