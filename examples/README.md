# Examples — DDD-KPI Employee Edition

เอกสารตัวอย่างที่ generate จาก `ddd-kpi-employee-v1.0.0.json` สำหรับพนักงานสมมติ **"วีรชัย อินทรสุวรรณ"** Team Leader ฝ่าย Digital Marketing ไตรมาส Q3/2026

ไฟล์เหล่านี้แสดงให้เห็นว่า **format และโครงสร้าง** ที่ AI ควรสร้างออกมามีหน้าตาอย่างไร — ไม่ใช่เอกสารจริงของพนักงานจริง

---

## Fictional Context

| Field | Value |
|---|---|
| **Employee** | วีรชัย อินทรสุวรรณ (Weerachai Intharasuwan) |
| **Position** | Digital Marketing Team Leader |
| **Team** | Marketing & Growth |
| **Level** | Team Leader (มีสมาชิกทีม 3 คน) |
| **Quarter** | Q3/2026 (1 ก.ค. — 30 ก.ย. 2026) |

---

## Example Documents

| ไฟล์ | Phase | Document ID | สิ่งที่แสดง |
|---|---|---|---|
| `CONTEXT_MAP.md` | Phase 1 · Context | `context_map` | Company Strategy → KPI Company → Role alignment |
| `KEY_RESULTS.md` | Phase 2 · KPI Design | `key_results` | SMART KRs ต่อทุก Objective + scoring rubric |
| `PRESENTATION_SPEC.md` | Phase 3 · Communication | `presentation_spec` | Q-Start + Q-End deck spec |

โปรเจกต์จริงจะ generate ครบทั้ง 6 เอกสารใน `docs/` ตาม `meta.generation_order[]`
