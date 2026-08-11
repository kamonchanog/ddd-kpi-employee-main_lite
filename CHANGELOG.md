# Changelog

All notable changes to DDD-KPI Employee Edition are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
Versions follow [Semantic Versioning](https://semver.org/).

---

## [Unreleased] — Lite Edition

### Added

- `ddd-kpi-employee-v1.0.0_lite.json` — reduced 6-document variant of the blueprint for Operation-level / individual-contributor employees
  - Phase 1 · Context & Alignment: `context_map`, `role_profile`
  - Phase 2 · KPI Design: `kpi_charter`, `key_results`, `key_activities`
  - Phase 3 · Communication Spec: `presentation_spec`

### Removed (relative to the 9-document full edition)

- `cascade_plan` — team-cascade planning is only relevant for Team Leaders; use the full edition (`ddd-kpi-employee-v1.0.0.json`) if this is needed
- `report_spec` — standalone progress-report format spec; not required for initial quarterly KPI planning
- `dashboard_spec` — standalone tracking-dashboard spec; not required for initial quarterly KPI planning

**Note:** Phase 2's description text and the "cascade" content inside `PRESENTATION_SPEC.md` (Slide 2 — Strategic Alignment) still reference the *cascade concept* (Company Goal → Strategic Theme → Company KPI → Personal KPI), but no longer imply a separate `CASCADE_PLAN.md` deliverable in this lite edition.

---

## [1.0.0] — 2026-05-28

### Added

**DDD-KPI Employee Edition — Initial Release**

- `ddd-kpi-employee-v1.0.0.json` — KPI Planning blueprint (9 documents, 3 phases)
  - Phase 1 · Context & Alignment: `context_map`, `role_profile`
  - Phase 2 · KPI Design: `kpi_charter`, `key_results`, `key_activities`, `cascade_plan`
  - Phase 3 · Communication Specs: `report_spec`, `dashboard_spec`, `presentation_spec`
  - 32 dependency edges, 3 readiness gates
- `ddd-schema.json` — JSON Schema (draft-07) for blueprint validation
- `validate.py` — 3-level validator (JSON syntax, schema, semantic checks)
- `manual/` — 9 Thai-language user guides (one per document, 6-section format)
- `examples/` — 3 sample output documents using fictional employee "วีรชัย อินทรสุวรรณ"
- `input/` — gitignored folder for employee context files (with README)
- `docs/` — output directory placeholder
- `README.md`, `CLAUDE.md`, `AGENTS.md` — usage documentation
- `.github/workflows/validate.yml` — CI validation on push and PR

**Design decisions:**
- `input/` is gitignored — employees can store confidential context files locally without risk of pushing to GitHub
- `CASCADE_PLAN.md` is generated for all employees; Operation-level employees write "ไม่เกี่ยวข้อง" and skip
- `PRESENTATION_SPEC.md` covers both Q-Start (planning) and Q-End (review) in a single document
- Bilingual schema throughout: Thai narrative, English identifiers

---

[1.0.0]: https://github.com/ragnar-co/ddd-kpi-employee/releases/tag/v1.0.0
