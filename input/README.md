# input/ — โฟลเดอร์สำหรับ Context Files

วางไฟล์ Input Context ทั้งหมดที่นี่ก่อนใช้งาน DDD-KPI

> โฟลเดอร์นี้ถูก **gitignore** แล้ว — ไฟล์ที่วางไว้จะไม่ถูก push ขึ้น GitHub

---

## ไฟล์ที่ต้องมี (5 ไฟล์)

| ชื่อไฟล์ (แนะนำ) | เนื้อหา | ได้จากไหน |
|---|---|---|
| `company-context.md` | Goal, Vision, Mission, Strategic Theme ขององค์กร | HR / ผู้บริหาร |
| `kpi-policy.md` | นโยบายการกำหนด KPI — weight rules, scoring rubric, จำนวน KPI | HR |
| `job-description.md` | Job Description ของคุณ | HR / ต้นสังกัด |
| `job-landscape.md` | Job Landscape ของแผนกที่สังกัด | หัวหน้าแผนก |
| `kpi-company-Q[N]-[YEAR].md` | KPI Company ของไตรมาสนี้ | ผู้บริหาร / ประชุม KPI |

---

## Format แนะนำ

ไฟล์ทุกไฟล์ใช้ Markdown (`.md`) เนื้อหาเป็นภาษาไทยหรืออังกฤษก็ได้ AI จะอ่านได้ทั้งสองภาษา

ตัวอย่าง `kpi-company-Q3-2026.md`:

```markdown
# KPI Company Q3/2026

## KPI 1 — รายได้รวม
- Target: 50 ล้านบาท
- Owner: Sales Team
- Strategic Theme: Revenue Growth

## KPI 2 — Customer Satisfaction Score
- Target: NPS >= 45
- Owner: Customer Success
- Strategic Theme: Customer Excellence
```
