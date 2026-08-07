# AGENTS.md

This file provides guidance to AI coding agents (OpenAI Codex, Gemini, etc.) when working with this repository.

## What This Repo Is

A single-template DDD framework for Ragnar employees to set quarterly KPIs. The blueprint file `ddd-kpi-employee-v1.0.0.json` defines all 6 documents an employee needs. Your job is to read input context files and generate those documents into `docs/`.

## Setup

```bash
pip install jsonschema
```

No other dependencies.

## Validation

```bash
python3 validate.py
```

Run after any change to `ddd-kpi-employee-v1.0.0.json`. Exit code 0 = pass.

## Input Context Files

All input files are in `input/` (gitignored). Read ALL of them before generating any document:

| File | Content |
|---|---|
| `input/company-context.md` | Goal, Vision, Mission, Strategic Theme |
| `input/kpi-policy.md` | KPI Policy — weight rules, scoring rubric |
| `input/job-description.md` | Employee's Job Description |
| `input/job-landscape.md` | Department Job Landscape |
| `input/kpi-company-[quarter].md` | Company KPIs for this quarter |

If any file is missing, stop and report which file is needed before proceeding.

## How to Generate Documents

Read these fields from `ddd-kpi-employee-v1.0.0.json` for each document:

| Field | How to use it |
|---|---|
| `id` | Unique document identifier for cross-referencing |
| `filename` | Output filename to write in `docs/` |
| `depends_on[]` | Read these upstream documents first — their content is input |
| `sections[]` | Each section maps to a `##` heading in the output |
| `sections[].refs[]` | Document IDs to cross-reference in this section |
| `sections[].items[]` | Bullet points and sub-topics to cover |
| `agent_hints.instruction` | Primary generation instruction for this document |
| `agent_hints.input_context` | Which input files and upstream docs to read |
| `agent_hints.validation` | Post-generation checklist — verify before writing the file |
| `output_format.suggested_headings[]` | `##` headings to use in the output |

## Generation Order

Generate strictly in this sequence (topological dependency order):

```
1. CONTEXT_MAP.md         — input: company-context.md, kpi-company-[Q].md
2. ROLE_PROFILE.md        — input: job-description.md, job-landscape.md, kpi-policy.md, CONTEXT_MAP.md
3. KPI_CHARTER.md         — input: CONTEXT_MAP.md, ROLE_PROFILE.md, kpi-policy.md
4. KEY_RESULTS.md         — input: KPI_CHARTER.md
5. KEY_ACTIVITIES.md      — input: KEY_RESULTS.md, ROLE_PROFILE.md
6. PRESENTATION_SPEC.md   — input: KEY_RESULTS.md, KEY_ACTIVITIES.md, KPI_CHARTER.md, CONTEXT_MAP.md
```

Never generate a document before its dependencies are complete.

## Critical Rules

1. **Never fabricate KPIs or targets** — all values must trace back to input context files.
2. **KPI weights must sum to exactly 100%** — verify before writing KPI_CHARTER.md.
3. **Every KR must have a numeric target** — qualitative descriptions alone are not acceptable.
4. **KEY_ACTIVITIES.md must have content for Month 1, 2, and 3** — no empty months.
5. **PRESENTATION_SPEC.md must include both Q-Start and Q-End** — omitting either is an error.

## Language Convention

- Narrative sections: Thai
- Identifiers, field names, column headers, metric names, code: English
- KPI names: bilingual (Thai name + English name)

## Output

Write all generated documents to `docs/` using the `filename` field value.
