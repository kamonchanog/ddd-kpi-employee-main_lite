# DDD-KPI — KPI Documentation Framework (Employee Edition)

**DDD-KPI** คือ framework สำหรับพนักงาน Ragnar ในการกำหนด KPI ประจำไตรมาสอย่างเป็นระบบ โดยใช้ AI (Claude Code) เป็นผู้ช่วยสร้างเอกสาร KPI ชุดสมบูรณ์จาก context ที่พนักงานให้มา

---

## Input Context ที่ต้องเตรียม (5 ไฟล์)

วางไฟล์ทั้งหมดใน `input/` — โฟลเดอร์นี้ถูก gitignore แล้ว ข้อมูลจะไม่ถูก push ขึ้น GitHub

| ไฟล์ | เนื้อหา |
|---|---|
| `input/company-context.md` | Goal, Vision, Mission, Strategic Theme ขององค์กร |
| `input/kpi-policy.md` | นโยบายการกำหนด KPI ขององค์กร |
| `input/job-description.md` | Job Description ของพนักงานคนนี้ |
| `input/job-landscape.md` | Job Landscape ของแผนกที่สังกัด |
| `input/kpi-company-[quarter].md` | KPI Company ของไตรมาสนี้ที่ได้รับจากผู้บริหาร |

---

## Output ที่จะได้รับ (6 เอกสาร ใน `docs/`)

```
Phase 1 · Context & Alignment
  CONTEXT_MAP.md      → แผนที่บริบท: Company Strategy → KPI Company → Role
  ROLE_PROFILE.md     → สรุปบทบาท, collaboration map, KPI constraints

Phase 2 · KPI Design  ← ผลลัพธ์หลัก
  KPI_CHARTER.md      → KPI Objectives + weight (รวม 100%) + success criteria
  KEY_RESULTS.md      → Key Results SMART ต่อทุก Objective + scoring rubric
  KEY_ACTIVITIES.md   → กิจกรรม Month 1/2/3 + milestone + risk mitigation

Phase 3 · Communication Spec
  PRESENTATION_SPEC.md → Q-Start (ต้นไตรมาส) + Q-End (ปลายไตรมาส) slide spec
```

---

## วิธีใช้งาน

### วิธีที่ 1 — `/doc-coauthoring` (แนะนำ)

```bash
# 1. Clone repo นี้
git clone <repo-url>
cd ddd-kpi-employee

# 2. วาง Input Context ใน input/
#    (ดูรายการไฟล์ด้านบน)

# 3. เปิด Claude Code แล้วพิมพ์
/doc-coauthoring
```

AI จะถามข้อมูลทีละส่วนและ generate เอกสารแบบ interactive — ได้เนื้อหาที่ตรงกับ context จริงมากกว่า

### วิธีที่ 2 — Prompt ตรง

```
Read ddd-kpi-employee-v1.0.0.json and generate all 6 documents
in meta.generation_order[] into docs/.
Input context files are in input/:
  - input/company-context.md
  - input/kpi-policy.md
  - input/job-description.md
  - input/job-landscape.md
  - input/kpi-company-[quarter].md
Follow agent_hints.instruction for each document.
```

---

## Validation

```bash
# Validate blueprint (default)
python3 validate.py

# JSON output สำหรับ CI
python3 validate.py --format json
```

ติดตั้ง `jsonschema` เพื่อเปิด Level 2 schema check:

```bash
pip install jsonschema
```

---

## Priority Guide

ถ้าเวลาจำกัด generate เฉพาะ P0 ก่อน:

```
P0 (ต้องมี): CONTEXT_MAP, ROLE_PROFILE, KPI_CHARTER, KEY_RESULTS, KEY_ACTIVITIES
P1 (ควรมี): PRESENTATION_SPEC
```

---

## Files

| ไฟล์/โฟลเดอร์ | คำอธิบาย |
|---|---|
| `ddd-kpi-employee-v1.0.0.json` | Blueprint หลัก — AI อ่านไฟล์นี้เพื่อ generate เอกสาร |
| `ddd-schema.json` | JSON Schema สำหรับ validate blueprint |
| `validate.py` | Validator 3 ระดับ |
| `input/` | วาง Input Context ไฟล์ที่นี่ (gitignored) |
| `docs/` | เอกสารที่ AI generate ออกมาจะอยู่ที่นี่ |
