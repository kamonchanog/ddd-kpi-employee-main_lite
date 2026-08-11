# คู่มือการเขียนเอกสาร DDD-KPI Employee Edition

คู่มือทีละเอกสาร สำหรับใช้ประกอบการเขียนเอกสาร KPI แต่ละชิ้น แต่ละไฟล์อธิบาย: ภาพรวม, prerequisites, วิธีเขียนทีละ section, ตัวอย่างเต็ม, validation checklist, และข้อผิดพลาดที่พบบ่อย

---

## Phase 1 · Context & Alignment

| ไฟล์ | Document ID | Priority | คำอธิบาย |
|---|---|---|---|
| [CONTEXT_MAP.md](CONTEXT_MAP.md) | `context_map` | P0 | เชื่อมโยง Company Strategy → KPI Company → Role |
| [ROLE_PROFILE.md](ROLE_PROFILE.md) | `role_profile` | P0 | สรุปบทบาท, collaboration map, KPI constraints |

## Phase 2 · KPI Design

| ไฟล์ | Document ID | Priority | คำอธิบาย |
|---|---|---|---|
| [KPI_CHARTER.md](KPI_CHARTER.md) | `kpi_charter` | P0 | KPI Objectives + weight (รวม 100%) + success criteria |
| [KEY_RESULTS.md](KEY_RESULTS.md) | `key_results` | P0 | SMART KRs ต่อทุก Objective + scoring rubric |
| [KEY_ACTIVITIES.md](KEY_ACTIVITIES.md) | `key_activities` | P0 | กิจกรรม Month 1/2/3 + milestone + risk |

## Phase 3 · Communication Spec

| ไฟล์ | Document ID | Priority | คำอธิบาย |
|---|---|---|---|
| [PRESENTATION_SPEC.md](PRESENTATION_SPEC.md) | `presentation_spec` | P1 | Q-Start (ต้นไตรมาส) + Q-End (ปลายไตรมาส) |

---

## Generation Order

```
context_map → role_profile → kpi_charter → key_results → key_activities → presentation_spec
```

---

## Format ของทุกไฟล์คู่มือ (6 Sections)

| Section | เนื้อหา |
|---|---|
| 1. ภาพรวม | จุดประสงค์, dependency diagram, priority, ผู้เขียน/ผู้อ่าน |
| 2. ก่อนเริ่มเขียน | ข้อมูลที่ต้องเตรียม, upstream docs ที่ต้องอ่านก่อน |
| 3. วิธีเขียนทีละ Section | คำแนะนำต่อ section + ตัวอย่างดี/ผิด |
| 4. ตัวอย่างเต็ม | เอกสารตัวอย่างสมบูรณ์ (ใช้ตัวละครสมมติ "วีรชัย อินทรสุวรรณ") |
| 5. Validation Checklist | รายการตรวจสอบก่อน submit |
| 6. ข้อผิดพลาดที่พบบ่อย | ❌ ผิด → ✅ ถูก + ผลกระทบ |
