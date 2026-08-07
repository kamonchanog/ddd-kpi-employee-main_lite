# คู่มือการเขียน PRESENTATION_SPEC.md

---

## 1. ภาพรวม

`PRESENTATION_SPEC.md` คือเอกสาร P1 ที่กำหนด specification สำหรับ **2 Presentation** ที่พนักงานต้องนำเสนอในแต่ละไตรมาส ได้แก่ (1) **Q-Start Presentation** ต้นไตรมาส — นำเสนอแผน KPI ว่าจะทำอะไร มี KR อะไร มีแผนอย่างไร และ (2) **Q-End Presentation** ปลายไตรมาส — นำเสนอผลลัพธ์จริง บทเรียนที่ได้ และ preview ไตรมาสถัดไป เอกสารนี้ไม่ใช่ตัว slide เอง แต่เป็น blueprint ที่บอกว่าแต่ละ slide ควรมีเนื้อหาอะไรบ้าง

**depends_on:** `key_results`, `key_activities`
**downstream:** (leaf document — เป็นเอกสารสุดท้ายใน Phase 3)
**ผู้เขียน:** พนักงานเอง โดยอ้างอิงจาก KEY_RESULTS.md, KEY_ACTIVITIES.md, KPI_CHARTER.md, CONTEXT_MAP.md
**ผู้อ่าน:** พนักงาน (ใช้เป็น guide สร้าง slides จริง), Line Manager (ใช้ review structure)

**Dependency Diagram:**

```
CONTEXT_MAP.md ──────────────────────────────┐
KPI_CHARTER.md ──────────────────────────────┤
KEY_RESULTS.md ──────────────────────────────┤──▶ PRESENTATION_SPEC.md
KEY_ACTIVITIES.md ───────────────────────────┘       (leaf — ไม่มี downstream)
```

**Priority:** P1

> ⚠️ **ข้อบังคับ:** เอกสารนี้ต้องมีครบ **ทั้ง Q-Start และ Q-End** — ขาดอันใดอันหนึ่งถือว่าเอกสารไม่สมบูรณ์

---

## 2. ก่อนเริ่มเขียน (Prerequisites)

ก่อนเขียน `PRESENTATION_SPEC.md` ต้องมีเอกสารเหล่านี้พร้อมก่อน:

1. **KEY_RESULTS.md** — ต้องรู้ KR ทุกข้อ (target, unit, scoring rubric, data source) เพราะต้อง reference ใน Q-Start และใส่ actual vs target ใน Q-End
2. **KEY_ACTIVITIES.md** — ต้องรู้ activities ต่อเดือน และ milestones เพื่อสร้าง Quarterly Roadmap slide ใน Q-Start
3. **KPI_CHARTER.md** — ต้องรู้ KPI weight และ Company KPI linkage เพื่อ Strategic Alignment slide
4. **CONTEXT_MAP.md** — ต้องรู้ Company Goal, Strategic Theme, และ Company KPI เพื่อเล่า narrative ใน Slide 2 (alignment cascade)

**ข้อมูลที่ต้องรวบรวมก่อนเขียน Q-End:**
- วันนำเสนอ Q-End (ปกติสัปดาห์แรกหลังสิ้นไตรมาส)
- Actual results จาก data sources ที่ระบุใน KEY_RESULTS.md
- Root cause analysis สำหรับ KR ที่ต่ำกว่า target

---

## 3. วิธีเขียนทีละ Section

### Section 1: Q-Start Presentation Spec

**จุดประสงค์:** กำหนด structure ของ deck ที่ใช้นำเสนอต้นไตรมาส ให้ผู้ฟังเห็นว่าพนักงานจะทำอะไร เพราะอะไร และวางแผนอย่างไร

**วิธีเขียน:**
- ระบุ audience, duration, วันนำเสนอ ก่อนเสมอ
- Slide 2 ต้องแสดง cascade 3-4 ชั้นจาก Company Goal → Strategic Theme → Company KPI → Personal KPI
- สร้าง 1 slide ต่อ KPI (ไม่รวม title และ alignment slide) — แต่ละ slide มีครบ: KPI name, weight, KR list + targets, Key Activities, Company KPI link
- Slide สุดท้ายต้องเป็น Quarterly Roadmap แบบ Gantt-style

**ตัวอย่างที่ดี:**

```markdown
## Q-Start Presentation Spec

**ชื่อ Deck:** KPI Plan Q3/2026 — วีรชัย อินทรสุวรรณ · Digital Marketing TL
**Audience:** Line Manager (Head of Marketing), Marketing & Growth Team, HR
**Duration:** 12 นาที + 3 นาที Q&A
**วันนำเสนอ:** 3 กรกฎาคม 2026

| Slide | หัวข้อ | เนื้อหาหลัก |
|---|---|---|
| 1 | Title | ชื่อ / ตำแหน่ง / ทีม / Quarter |
| 2 | Strategic Alignment | Company Goal → ST-2/ST-3 → C-KPI-2/C-KPI-3 → KPI-1/2/3 |
| 3 | KPI-1: Inbound Lead Gen (40%) | KR-1.1/1.2/1.3/1.4 + targets + M1/M2/M3 activities |
| 4 | KPI-2: Content ROI (35%) | KR-2.1/2.2/2.3 + targets + M1/M2/M3 activities |
| 5 | KPI-3: Brand Visibility (25%) | KR-3.1/3.2/3.3 + targets + M1/M2/M3 activities |
| 6 | Quarterly Roadmap | Gantt chart: activities M1→M2→M3 + milestones |
```

**ตัวอย่างที่ผิด:**

```markdown
❌ Q-Start: นำเสนอ KPI ของตัวเองให้ผู้จัดการรับทราบ
   - KPI 1: Lead Generation
   - KPI 2: Content
   - KPI 3: Brand
```

> ❌ ไม่ระบุ slide structure, ไม่มี KR targets, ไม่มี Company KPI linkage — ผู้ฟังไม่เห็นว่า KPI เชื่อมกับ Company Strategy อย่างไร

---

### Section 2: Q-End Presentation Spec

**จุดประสงค์:** กำหนด structure ของ deck ที่ใช้รายงานผลปลายไตรมาส ต้องแสดง actual vs target ทุก KR พร้อม evidence และ root cause สำหรับ KR ที่พลาด

**วิธีเขียน:**
- Duration ยาวกว่า Q-Start เพราะต้องมี deep dive ทุก KPI
- Slide 2 ต้องเป็น KPI Scorecard ตาราง (KPI# | Weight | Target | Actual | Achievement% | Weighted Score | Overall)
- แต่ละ KPI ต้องมี Deep Dive slide แยก — แสดง actual vs target per KR + variance + root cause + evidence
- Key Learnings slide ต้องมี 3 ข้อ ที่ specific และ actionable (ไม่ใช่ generic)
- Next Quarter Preview ต้องมี rationale ว่าทำไมถึงตั้ง target นั้น

**ตัวอย่างที่ดี:**

```markdown
## Q-End Presentation Spec

**ชื่อ Deck:** KPI Results Q3/2026 — วีรชัย อินทรสุวรรณ · Digital Marketing TL
**Audience:** Line Manager, Marketing & Growth Team, HR
**Duration:** 18 นาที + 5 นาที Q&A
**วันนำเสนอ:** 9 ตุลาคม 2026

| Slide | หัวข้อ | เนื้อหาหลัก |
|---|---|---|
| 1 | Title | ชื่อ / ไตรมาส / สรุป Overall Score |
| 2 | KPI Scorecard | ตาราง: KPI# / Weight / Target / Actual / Achievement% / Score |
| 3 | KPI-1 Deep Dive | actual vs target per KR-1.1/1.2/1.3/1.4, variance%, root cause, HubSpot screenshot |
| 4 | KPI-2 Deep Dive | actual vs target per KR-2.1/2.2/2.3, variance%, GA4 screenshot |
| 5 | KPI-3 Deep Dive | actual vs target per KR-3.1/3.2/3.3, variance%, GSC + LinkedIn screenshot |
| 6 | Key Learnings | 3 specific learnings + แผนปรับปรุง Q4 |
| 7 | Next Quarter Preview | Q4 KPI Objectives เบื้องต้น + rationale |
```

**ตัวอย่างที่ผิด:**

```markdown
❌ Q-End: รายงานว่าทำ KPI ได้ 85% โดยรวม บางข้อได้ บางข้อไม่ได้
   เพราะงานเยอะและทีมมีน้อย จะพยายามทำให้ดีขึ้นในไตรมาสหน้า
```

> ❌ ไม่มีตัวเลข actual vs target ต่อ KR, ไม่มี evidence, root cause ไม่ specific, Key Learnings เป็น generic — ผู้ฟังไม่สามารถ evaluate ผลงานจริงได้

---

### Section 3: Slide Templates

**จุดประสงค์:** template มาตรฐานสำหรับแต่ละ slide type เพื่อให้ consistent ทุกไตรมาส

**วิธีเขียน:**
- ระบุ KPI Overview Slide template (Q-Start) และ KPI Deep Dive Slide template (Q-End)
- ใช้ ASCII diagram หรือตาราง placeholder เพื่อแสดง layout
- ระบุว่า field ใด fill in จาก document ใด

**ตัวอย่างที่ดี:**

```markdown
### KPI Overview Slide (Q-Start)
┌──────────────────────────────────────────────┐
│ KPI-[N]: [KPI Name TH]          Weight: [X]% │
│ Linked to: [Company KPI ID + Name]            │
├─────────────────┬────────────────────────────┤
│ Key Results     │ Key Activities              │
│ KR-N.1: [X unit]│ M1: [activity name]        │
│ KR-N.2: [X unit]│ M2: [activity name]        │
│ KR-N.3: [X unit]│ M3: [activity name]        │
└─────────────────┴────────────────────────────┘
```

```markdown
### KPI Deep Dive Slide (Q-End)
┌──────────────────────────────────────────────────────────┐
│ KPI-[N]: [KPI Name TH]                   Score: [X%]     │
├────────┬──────────┬──────────┬──────────┬────────────────┤
│ KR     │ Target   │ Actual   │ Ach%     │ Evidence       │
│ N.1    │ [value]  │ [value]  │ [X%]     │ [tool name]    │
│ N.2    │ [value]  │ [value]  │ [X%]     │ [tool name]    │
├────────┴──────────┴──────────┴──────────┴────────────────┤
│ Variance: [Delta%] | Root Cause: [2 sentences max]       │
└──────────────────────────────────────────────────────────┘
```

---

### Section 4: Storytelling Guide

**จุดประสงค์:** guide การเล่าเรื่องทั้ง Q-Start และ Q-End ให้ผู้บริหารเข้าใจ และเห็น impact ต่อ Company Strategy

**วิธีเขียน:**
- ระบุ narrative arc ของ Q-Start และ Q-End แยกกัน
- ระบุ Data Storytelling Rule อย่างน้อย 2-3 ข้อ
- ให้ตัวอย่าง opening sentence ทั้งสองแบบ

**ตัวอย่างที่ดี:**

```markdown
### Q-Start Narrative Arc
Company Goal → Strategic Theme → Company KPI ที่ contribute → KPI ส่วนตัว → แผน 3 เดือน

เปิด: "ไตรมาสนี้ Ragnar ต้องการลูกค้าใหม่ 80 ราย ทีมเรารับผิดชอบ
สร้าง inbound pipeline ซึ่งเป็น 60% ของ lead ที่ Sales ใช้ปิดการขาย
KPI 3 ข้อที่ออกแบบไว้วัดสิ่งเดียวกันจากมุม volume, quality และ efficiency"

### Q-End Narrative Arc
สิ่งที่ทำ → ผลจริง → impact ต่อ Company KPI → บทเรียน → Q4 preview
```

---

## 4. ตัวอย่างเต็ม

> ตัวละครสมมติ: **วีรชัย อินทรสุวรรณ**, Digital Marketing Team Leader, Q3/2026

```markdown
# PRESENTATION_SPEC — วีรชัย อินทรสุวรรณ | Q3/2026

---

## Q-Start Presentation Spec

**ชื่อ Deck:** KPI Plan Q3/2026 — วีรชัย อินทรสุวรรณ · Digital Marketing TL
**Audience:** Head of Marketing, Marketing & Growth Team, HR Business Partner
**Duration:** 12 นาที + 3 นาที Q&A
**วันนำเสนอ:** 3 กรกฎาคม 2026

| Slide | หัวข้อ | เนื้อหาหลัก |
|---|---|---|
| 1 | Title | วีรชัย อินทรสุวรรณ / Digital Marketing TL / KPI Plan Q3/2026 |
| 2 | Strategic Alignment | Company Goal (MRR 20M) → ST-2 + ST-3 → C-KPI-2 + C-KPI-3 → KPI-1/2/3 |
| 3 | KPI-1: Inbound Lead Gen (40%) | KR: 150 MQLs / 70% MQL-to-SAL / ≤800 THB CPL / 32% open rate; M1-M3 activities |
| 4 | KPI-2: Content ROI (35%) | KR: 25,000 sessions / 55 content MQLs / pos ≤12.0; M1-M3 activities |
| 5 | KPI-3: Brand Visibility (25%) | KR: 1,500 branded searches / 50K LinkedIn reach / 8 PR mentions; M1-M3 activities |
| 6 | Quarterly Roadmap | Gantt: activities M1→M2→M3 + milestones (31 ก.ค., 31 ส.ค., 30 ก.ย.) |

---

## Q-End Presentation Spec

**ชื่อ Deck:** KPI Results Q3/2026 — วีรชัย อินทรสุวรรณ · Digital Marketing TL
**Audience:** Head of Marketing, Marketing & Growth Team, HR Business Partner
**Duration:** 18 นาที + 5 นาที Q&A
**วันนำเสนอ:** 9 ตุลาคม 2026

| Slide | หัวข้อ | เนื้อหาหลัก |
|---|---|---|
| 1 | Title | วีรชัย / ไตรมาส Q3/2026 / Overall Score: [X%] |
| 2 | KPI Scorecard | KPI# / Weight / Target / Actual / Achievement% / Weighted Score / Overall |
| 3 | KPI-1 Deep Dive | actual vs target per KR-1.1~1.4, variance, HubSpot + Google Ads evidence |
| 4 | KPI-2 Deep Dive | actual vs target per KR-2.1~2.3, variance, GA4 + Search Console evidence |
| 5 | KPI-3 Deep Dive | actual vs target per KR-3.1~3.3, variance, GSC + LinkedIn + PR log evidence |
| 6 | Key Learnings | (1) Industry-specific lead magnet > generic 2.3x / (2) Data-driven posts reach +40% / (3) PR ต้องเริ่มล่วงหน้า 6 สัปดาห์ |
| 7 | Next Quarter Preview | Q4: 200 MQLs / 80 content MQLs / 2,500 branded searches + rationale |

---

## Slide Templates

### KPI Overview Slide (Q-Start)
┌──────────────────────────────────────────────┐
│ KPI-[N]: [KPI Name TH]          Weight: [X]% │
│ Linked to: [Company KPI ID] [Company KPI Name]│
├──────────────────┬───────────────────────────┤
│ Key Results      │ Key Activities             │
│ KR-N.1: [X unit] │ M1: [activity]             │
│ KR-N.2: [X unit] │ M2: [activity]             │
│ KR-N.3: [X unit] │ M3: [activity]             │
└──────────────────┴───────────────────────────┘

### KPI Deep Dive Slide (Q-End)
┌────────────────────────────────────────────────────────┐
│ KPI-[N]: [Name]                        Score: [X%]     │
├──────┬──────────┬──────────┬──────────┬────────────────┤
│ KR   │ Target   │ Actual   │ Ach%     │ Evidence       │
│ N.1  │ [value]  │ [value]  │ [X%]     │ HubSpot report │
│ N.2  │ [value]  │ [value]  │ [X%]     │ GA4 screenshot │
├──────┴──────────┴──────────┴──────────┴────────────────┤
│ Variance: [Delta%] Root Cause: [2 sentences]           │
└────────────────────────────────────────────────────────┘

---

## Storytelling Guide

### Q-Start Narrative Arc
```
Company Goal ที่ Ragnar ต้องบรรลุ
    → Strategic Theme ที่ Marketing & Growth ดูแล
    → Company KPI ที่ role นี้ contribute หลัก
    → KPI ส่วนตัวที่ออกแบบมา support
    → แผน 3 เดือนที่จะ execute
```

ตัวอย่างการเปิด Q-Start: "ไตรมาสนี้ Ragnar ต้องการลูกค้าใหม่ที่จ่ายเงิน 80 ราย ผมและทีมรับผิดชอบสร้าง inbound pipeline ซึ่งเป็น 60% ของ lead ที่ Sales ใช้ปิดการขาย KPI 3 ข้อที่ผมออกแบบไว้วัดสิ่งเดียวกันจาก 3 มุม คือ volume, quality และ brand momentum"

### Q-End Narrative Arc
```
สิ่งที่วางแผนไว้ vs ทำได้จริง
    → ผลลัพธ์จริง (ตัวเลข + evidence)
    → Impact ต่อ Company KPI
    → บทเรียนที่ได้ + จะปรับอะไร Q4
```

ตัวอย่างการเปิด Q-End: "Q3 เราได้ [X] MQLs จากเป้า 150 — [X%] ของเป้า โดย content MQLs เกินเป้า แต่ paid campaign ต่ำกว่าคาดเพราะ landing page ปัญหาที่พบในเดือน 2 วันนี้จะพาทุกคนดูตัวเลขจริงทีละ KPI"

### Data Storytelling Rules
- **Rule 1:** ทุก claim ต้องมี evidence — screenshot, report link, หรือตัวเลขที่ verify ได้ ห้าม narrative เดี่ยว
- **Rule 2:** compare กับ baseline เสมอ ไม่ใช่แค่ target ("organic traffic เติบโต 38% QoQ แม้ต่ำกว่า target 40%")
- **Rule 3:** KR ที่ต่ำกว่า target ต้องอธิบาย root cause ใน 2 ประโยค ไม่ใช่แค่ตัวเลข
```

---

## 5. Validation Checklist

**Q-Start Deck**
- [ ] ระบุ audience, duration, วันนำเสนอก่อนเสมอ
- [ ] Slide 2 แสดง cascade ครบ: Company Goal → Strategic Theme → Company KPI → Personal KPI
- [ ] มี 1 slide ต่อ KPI ทุกข้อ (ไม่ขาด)
- [ ] ทุก KPI slide มี: KR list + targets, Key Activities M1/M2/M3, Company KPI link
- [ ] Slide สุดท้ายเป็น Quarterly Roadmap ที่แสดง activities ทั้ง 3 เดือน
- [ ] KR targets ตรงกับ KEY_RESULTS.md (ไม่ใช้ตัวเลขอื่น)

**Q-End Deck**
- [ ] ระบุ audience, duration, วันนำเสนอก่อนเสมอ
- [ ] Slide 2 เป็น KPI Scorecard ที่มีครบ: Target, Actual, Achievement%, Weighted Score, Overall
- [ ] มี Deep Dive slide สำหรับทุก KPI — ไม่ข้ามแม้แต่ KPI เดียว
- [ ] ทุก Deep Dive slide แสดง actual vs target **ต่อ KR** (ไม่ใช่ต่อ KPI รวม)
- [ ] มี evidence ระบุสำหรับทุก KR (tool name + screenshot/report)
- [ ] Key Learnings มีครบ 3 ข้อ และ specific (ไม่ generic)
- [ ] Next Quarter Preview มี rationale อธิบายว่าทำไมถึงตั้ง target นั้น

**Slide Templates & Storytelling**
- [ ] มี template ทั้ง KPI Overview (Q-Start) และ KPI Deep Dive (Q-End)
- [ ] Storytelling guide มี narrative arc ทั้งสอง deck
- [ ] Data Storytelling Rules ระบุชัดว่าทุก claim ต้องมี evidence

---

## 6. ข้อผิดพลาดที่พบบ่อย

### ❌ ขาด Q-End Deck — มีแค่ Q-Start

```markdown
❌ PRESENTATION_SPEC.md มีแค่:
   ## Q-Start Presentation Spec
   ...
   (จบ — ไม่มี Q-End)
```

✅ ต้องมีครบ **ทั้ง Q-Start และ Q-End** เสมอ

**ผลกระทบ:** พนักงานไม่มี template สำหรับ Q-End Presentation ทำให้นำเสนอผลปลายไตรมาสแบบ improvise ไม่ consistent ระหว่างไตรมาส

---

### ❌ Q-End ไม่มี actual numbers — ใช้แค่ placeholder

```markdown
❌ | KPI-1 | 40% | [target] | [actual] | [X%] |
   | KPI-2 | 35% | [target] | [actual] | [X%] |
```

✅ Q-End Spec ควรระบุว่า **ต้องหาข้อมูลจากที่ไหน** แม้ spec ยังไม่รู้ actual:

```markdown
✅ | KPI-1 | 40% | 150 MQLs | → จาก HubSpot Q3 MQL Report | Achievement: คำนวณ Actual/Target × 100 |
```

**ผลกระทบ:** พนักงานไม่รู้ว่าต้องไปหาข้อมูลจากไหน ทำให้เตรียม Q-End ช้า และ data อาจไม่ครบ

---

### ❌ Key Learnings เป็น generic ไม่ actionable

```markdown
❌ Key Learnings:
   1. ควรวางแผนให้ดีกว่านี้
   2. ต้องสื่อสารกับทีมให้มากขึ้น
   3. จะพยายามทำ KPI ให้ได้ใน Q4
```

✅ ต้องระบุให้ specific — สิ่งที่เรียนรู้ + สิ่งที่จะเปลี่ยนใน Q4:

```markdown
✅ Key Learnings:
   1. Lead magnet เฉพาะ industry (เช่น "KPI สำหรับโรงงาน ISO") ได้ conversion 2.3x เทียบ generic ebook
      → Q4: สร้าง 3 industry-specific lead magnets (Manufacturing, Healthcare, Retail)
   2. LinkedIn posts ที่ใช้ Ragnar platform data ได้ reach +40% กว่า thought leadership ทั่วไป
      → Q4: เพิ่ม data-driven posts เป็น 50% ของ content calendar
   3. PR pitching ต้องเริ่มล่วงหน้า ≥6 สัปดาห์ — Q3 pitch ในเดือน 3 ไม่ทันลงก่อนสิ้นไตรมาส
      → Q4: pitch Q4 publications ตั้งแต่ต้น Q3 (สิงหาคม)
```

**ผลกระทบ:** ผู้บริหารไม่เห็น maturity ของพนักงาน, บทเรียน generic ไม่นำไปสู่การปรับปรุง KPI จริง

---

### ❌ ไม่มี Company KPI link ใน Q-Start Slides

```markdown
❌ Slide 3 — KPI-1: Inbound Lead Generation (40%)
   KR-1.1: 150 MQLs
   KR-1.2: 70% conversion
   Activities: รัน campaigns, สร้าง content
```

✅ ทุก KPI slide ต้องแสดง Company KPI ที่ contribute:

```markdown
✅ Slide 3 — KPI-1: Inbound Lead Generation (40%)
   Linked to: C-KPI-2 New Paid Customers (target: 80 ราย)
   KR-1.1: MQLs ≥ 150 leads/quarter
   KR-1.2: MQL-to-SAL rate ≥ 70%
   KR-1.3: Cost per MQL ≤ 800 THB
   M1: ปรับ lead scoring model | M2: Launch 2 campaigns | M3: A/B test landing pages
```

**ผลกระทบ:** ผู้บริหารไม่เห็น connection ระหว่าง KPI ส่วนตัวกับเป้าหมายบริษัท ทำให้ดูเหมือน KPI ลอย ไม่ได้ support Company Strategy
