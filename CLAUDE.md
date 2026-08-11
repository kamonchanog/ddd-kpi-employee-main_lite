# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## What This Repo Is

**DDD-KPI Employee Edition** — a single-template DDD framework for Ragnar employees to set quarterly KPIs. Claude reads `ddd-kpi-employee-v1.0.0.json` and generates 6 documents into `docs/`.

## Input Context Files

All input context files are in `input/`. Read these files before generating any document:

| File | Content |
|---|---|
| `input/company-context.md` | Company Goal, Vision, Mission, Strategic Theme |
| `input/kpi-policy.md` | KPI Policy — rules, weight constraints, scoring rubric |
| `input/job-description.md` | Employee's Job Description |
| `input/job-landscape.md` | Department Job Landscape |
| `input/kpi-company-[quarter].md` | Company KPIs for this quarter from management |
| `input/employee-kpi-preference.md` | Employee's pre-defined KPI/iKPI/OKR (created during pre-generation check) |

If any required input file is missing, ask the employee to provide it before generating dependent documents.

## PDF Auto-Conversion

When a `.pdf` file is found in `input/` (e.g. `job-description.pdf`, `job-landscape.pdf`), convert it to `.md` automatically **before** reading:

```bash
python3 scripts/pdf_to_md.py input/<filename>.pdf
```

The script replaces the PDF with a `.md` file of the same name. If no PDF library is installed, print the install hint from the script and ask the employee to install one.

## Pre-Generation KPI Check

**Before generating any document (before step 1 in Generation Order)**, ask the employee:

> "คุณมี KPI / iKPI / OKR ที่ต้องการกำหนดไว้แล้วหรือยัง?"

**ถ้ามี** → ขอให้ผู้ใช้พิมพ์รายการ KPI/iKPI/OKR ทั้งหมด → บันทึกลง `input/employee-kpi-preference.md` → ใช้รายการนี้เป็นฐานในการสร้าง KEY_RESULTS.md และ KEY_ACTIVITIES.md ให้สอดคล้อง

**ถ้าไม่มี** → สร้าง KPI/iKPI/OKR ที่เหมาะสมให้ผู้ใช้โดยอิงจาก role, company context และ kpi-policy → นำเสนอให้ผู้ใช้อนุมัติหรือแก้ไข → บันทึกผลลัพธ์ที่อนุมัติแล้วลง `input/employee-kpi-preference.md` → ใช้เป็นฐานต่อไป

## Generation Order

Generate documents strictly in this order (topological dependency):

```
1. CONTEXT_MAP.md        — no dependencies
2. ROLE_PROFILE.md       — depends on: context_map
3. KPI_CHARTER.md        — depends on: context_map, role_profile
4. KEY_RESULTS.md        — depends on: kpi_charter
5. KEY_ACTIVITIES.md     — depends on: key_results
6. PRESENTATION_SPEC.md  — depends on: key_results, key_activities   → output: Markdown (.md)
```

Never generate a document before its dependencies are complete.

## Output Format Rules

| Document | Format | Notes |
|---|---|---|
| CONTEXT_MAP.md → KEY_ACTIVITIES.md | Markdown | Standard spec docs |
| PRESENTATION_SPEC.md | Markdown | Q-Start and Q-End presentation specification |

### PRESENTATION_SPEC.md
Generate a Markdown presentation specification immediately from the available context and upstream docs. Do not ask the employee for a presentation theme. Must include:
- Both Q-Start deck and Q-End deck in one file
- Slide objective, key message, content blocks, visual guidance, and speaker notes where useful
- All slides populated with real data — no placeholders allowed

## Critical Rules

1. **Never fabricate KPIs or targets** — all KPIs must trace back to input context files.
2. **KPI weights must sum to 100%** — verify before generating KEY_RESULTS.md.
3. **Every KR must have a numeric target** — qualitative-only KRs are not acceptable.
4. **KEY_ACTIVITIES.md must cover Month 1, 2, and 3** — never leave a month empty.
5. **PRESENTATION_SPEC.md must have both Q-Start and Q-End** — neither section can be omitted.

## Validation

```bash
python3 validate.py
```

Run after any change to `ddd-kpi-employee-v1.0.0.json`.

## Output

All generated documents go into `docs/`. Use the filename from each document's `filename` field:
- Markdown docs → `docs/CONTEXT_MAP.md`, `docs/ROLE_PROFILE.md`, `docs/KPI_CHARTER.md`, `docs/KEY_RESULTS.md`, `docs/KEY_ACTIVITIES.md`, `docs/PRESENTATION_SPEC.md`.
