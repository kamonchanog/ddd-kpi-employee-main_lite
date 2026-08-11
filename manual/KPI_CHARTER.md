# คู่มือการเขียน KPI_CHARTER.md

---

## 1. ภาพรวม

KPI_CHARTER.md คือหัวใจของ DDD-KPI Employee Edition เป็นเอกสารที่กำหนด KPI Objectives อย่างเป็นทางการ พร้อมน้ำหนัก (Weight) ที่รวมกันได้ 100% เกณฑ์ความสำเร็จ 3 ระดับ (70/100/120%) และ Measurement Method ที่ชัดเจน เอกสารนี้ตอบคำถามว่า "วัดอะไร, วัดอย่างไร, และผ่านเกณฑ์ระดับไหน" เนื้อหาทุกส่วนต้องอ้างอิงกลับไปยัง CONTEXT_MAP.md (Company KPI) และ ROLE_PROFILE.md (Scope + Policy Constraints) เสมอ

- **depends_on:** CONTEXT_MAP.md, ROLE_PROFILE.md
- **downstream:** KEY_RESULTS.md, KEY_ACTIVITIES.md
- **ผู้เขียน:** พนักงานร่วมกับผู้จัดการโดยตรง และ HR Business Partner (Review)
- **ผู้อ่าน:** พนักงาน, ผู้จัดการ, HR, VP/C-Level (ในกรณี Review Cycle)
- **Output ที่คาดหวัง:** ตาราง KPI Objectives 3-5 ตัว น้ำหนักรวม = 100% แต่ละตัวมีเกณฑ์ 3 ระดับที่เป็นตัวเลข, Data Source ที่ระบุได้, และ Policy Compliance ที่ตรวจสอบได้

**Dependency Diagram:**

```
[CONTEXT_MAP.md]      [ROLE_PROFILE.md]
       |                      |
       +----------+-----------+
                  |
                  v
        +------------------+
        |  KPI_CHARTER.md  |  <-- คุณอยู่ที่นี่
        +------------------+
                  |
         +--------+--------+
         v                 v
   KEY_RESULTS.md    KEY_ACTIVITIES.md
```

**Priority: P0**

---

## 2. ก่อนเริ่มเขียน (Prerequisites)

1. อ่าน CONTEXT_MAP.md ให้จบ — โดยเฉพาะ Role-KPI Alignment Matrix เพื่อรู้ว่าต้องใส่ Company KPI ID ใดบ้างใน Link
2. อ่าน ROLE_PROFILE.md ให้จบ — โดยเฉพาะ KPI Constraints & Policy Notes เพื่อรู้ว่า KPI จำนวนกี่ตัว, น้ำหนักแต่ละตัวเท่าไหร่, และต้องมี KPI ประเภทใดบ้าง
3. วาง Draft น้ำหนัก KPI ก่อนเขียนรายละเอียด — ตรวจว่ารวมกัน = 100% เสมอ
4. ตรวจสอบข้อมูล Baseline ของแต่ละ Metric ที่จะวัด — ถ้าไม่มี Baseline ห้ามกำหนดเกณฑ์เป้าหมาย
5. ระบุ Data Source สำหรับทุก KPI ก่อนเขียน — ถ้าข้อมูลวัดไม่ได้ KPI นั้นใช้ไม่ได้
6. สำหรับ KPI ที่วัดแบบ Inverse (ต่ำกว่าดีกว่า เช่น CAC, Error Rate) ให้กำหนดทิศทางการให้คะแนนไว้ก่อน
7. ประชุมกับผู้จัดการเพื่อยืนยัน Target ก่อน Finalize — ห้ามตั้ง Target ฝ่ายเดียวโดยไม่มี Sign-off

---

## 3. วิธีเขียนทีละ Section

### KPI Objectives Summary

**วัตถุประสงค์:** ภาพรวมของ KPI ทั้งหมดในรูปแบบตารางสรุป เพื่อให้เห็น Portfolio ของ KPI และตรวจสอบน้ำหนักรวมได้ในทันที

**วิธีเขียน:** ใช้ตาราง 5 คอลัมน์: KPI ID / KPI Name / Weight / Link to Company KPI / Type (Primary Metric หรือ Supporting Metric)

**ตัวอย่างที่ดี:**

```markdown
## KPI Objectives Summary
**Quarter:** Q3/2026 | **Total Weight: 100%** ✓

| KPI ID | KPI Objective | Weight | Company KPI Link | Type |
|--------|---------------|--------|------------------|------|
| E-KPI-01 | Marketing Qualified Leads (MQL) Generated | 30% | C-KPI-03 | Primary |
| E-KPI-02 | Customer Acquisition Cost (CAC) | 25% | C-KPI-07 | Primary |
| E-KPI-03 | Brand Organic Search Traffic Growth | 20% | C-KPI-06 | Primary |
| E-KPI-04 | Campaign ROI (Blended) | 15% | C-KPI-01, C-KPI-07 | Primary |
| E-KPI-05 | Team Performance Score (Direct Reports) | 10% | — (People Mgmt) | Supporting |
| | **รวม** | **100%** | | |
```

**ตัวอย่างที่ผิด ❌:**

```markdown
## KPI Objectives Summary

KPI ของวีรชัยมี 4 ตัวดังนี้:
1. สร้าง Lead ให้ได้มาก
2. ลด Cost
3. เพิ่ม Traffic
4. ดูแลทีม
```

**เหตุผลที่ผิด:** ไม่มี Weight, ไม่มี Link กับ Company KPI, ชื่อ KPI คลุมเครือ และไม่มีตารางที่ตรวจสอบยอดรวม 100% ได้

---

### Success Criteria per KPI

**วัตถุประสงค์:** กำหนดเกณฑ์ตัวเลขสำหรับ 3 ระดับ: 70% (Minimum Acceptable), 100% (On Target), 120% (Stretch/Exceptional) สำหรับทุก KPI

**วิธีเขียน:** เขียน subsection แยกสำหรับแต่ละ KPI ใช้ตาราง 4 คอลัมน์: ระดับ / เกณฑ์ / Score / คำอธิบาย โดยทุกเกณฑ์ต้องเป็นตัวเลข ห้ามใช้คำเช่น "ดี", "ยอดเยี่ยม", "ตามที่คาดหวัง"

**ตัวอย่างที่ดี — E-KPI-01 (MQL):**

```markdown
### E-KPI-01: Marketing Qualified Leads (MQL) Generated
**Baseline Q2/2026:** 145 MQL | **Direction:** Higher is Better

| ระดับ | เกณฑ์ | Score | หมายเหตุ |
|-------|-------|-------|----------|
| 70% (Minimum) | 140–159 MQL | 70 | ต่ำกว่า Q2 baseline เล็กน้อย |
| 100% (On Target) | 180–199 MQL | 100 | +24% จาก Q2, สอดคล้องกับ Budget ที่เพิ่ม 15% |
| 120% (Stretch) | ≥ 200 MQL | 120 | เกิน Target 11%+ |
| Below Minimum | < 140 MQL | 0–69 | ต่ำกว่า Baseline — ต้องมี Root Cause Analysis |
```

**ตัวอย่างที่ดี — E-KPI-02 (CAC) ซึ่งเป็น Inverse KPI:**

```markdown
### E-KPI-02: Customer Acquisition Cost (CAC)
**Baseline Q2/2026:** 9,200 THB/account | **Direction:** Lower is Better (Inverse)
**Company Target:** ≤ 8,500 THB/account

| ระดับ | เกณฑ์ | Score | หมายเหตุ |
|-------|-------|-------|----------|
| 120% (Exceptional) | ≤ 7,500 THB | 120 | ลด 18%+ จาก Baseline |
| 100% (On Target) | 7,501–8,500 THB | 100 | บรรลุ Company Target |
| 70% (Minimum) | 8,501–9,500 THB | 70 | ยังสูงกว่า Company Target แต่ลดลงจาก Baseline |
| Below Minimum | > 9,500 THB | 0–69 | สูงกว่า Baseline Q2 — ไม่ยอมรับ |

**หมายเหตุ Inverse Scoring:** ยิ่ง CAC ต่ำ คะแนนยิ่งสูง ผู้อ่านต้องไม่สับสนทิศทางนี้
```

**ตัวอย่างที่ผิด ❌:**

```markdown
### E-KPI-01: MQL

- ระดับดีเยี่ยม: สร้าง Lead ได้มากกว่าที่คาดหวัง
- ระดับผ่าน: สร้าง Lead ได้ตามเป้า
- ระดับต้องปรับปรุง: สร้าง Lead ได้น้อยกว่าเป้า
```

**เหตุผลที่ผิด:** ไม่มีตัวเลขเลย คำเช่น "มากกว่าที่คาดหวัง" ตีความได้แตกต่างกัน — ทำให้ Review Score ขึ้นอยู่กับ Subjective Judgment ของผู้จัดการ ซึ่งผิด KPI Policy Section 7.3

---

### Measurement Method

**วัตถุประสงค์:** ระบุวิธีการวัดผล แหล่งข้อมูล ความถี่ในการวัด และผู้รับผิดชอบ Data Verification สำหรับแต่ละ KPI

**วิธีเขียน:** ใช้ตาราง 5 คอลัมน์: KPI ID / Data Source / ความถี่ / ผู้ Pull Data / ผู้ Verify

**ตัวอย่างที่ดี:**

```markdown
## Measurement Method

| KPI ID | Data Source | ความถี่ | ผู้ Pull Data | ผู้ Verify |
|--------|-------------|---------|--------------|-----------|
| E-KPI-01 | HubSpot CRM (MQL Stage) | ทุกสิ้นเดือน | วีรชัย | VP Marketing |
| E-KPI-02 | HubSpot CRM + Google Ads + Meta Ads Manager | ทุกสิ้นเดือน | กานต์ ชัยกุล (Paid Media) | วีรชัย |
| E-KPI-03 | Google Search Console + GA4 | ทุกสิ้นเดือน | ปริม วงศ์ทอง (SEO) | วีรชัย |
| E-KPI-04 | HubSpot Revenue Attribution + Ad Platforms | ทุกสิ้นเดือน | วีรชัย | VP Marketing |
| E-KPI-05 | 1-on-1 Score Sheet + Performance Form | รายไตรมาส | วีรชัย | HR Business Partner |

**หมายเหตุสำคัญ:**
- E-KPI-02 ใช้ข้อมูลจากหลาย Platform — ต้องมี Reconciliation Sheet รายเดือนเพื่อรวม Ad Spend ทุก Channel ก่อนคำนวณ CAC
- ช่วง HubSpot Migration (ปลาย ส.ค.): ใช้ Manual Export จาก Google Ads + Meta Ads โดยตรง และบันทึกเป็น Supplementary Data
```

**ตัวอย่างที่ผิด ❌:**

```markdown
## Measurement Method

วัดผลจากระบบของบริษัท ทุกสิ้นเดือน โดยวีรชัยเป็นผู้รายงาน
```

**เหตุผลที่ผิด:** ไม่ระบุระบบที่ใช้ ไม่แยกรายการต่อ KPI และไม่มีผู้ Verify — ถ้าข้อมูลผิดไม่มีใครจับได้

---

### KPI Policy Compliance Check

**วัตถุประสงค์:** ตรวจสอบ self-check ว่า KPI ที่ออกแบบสอดคล้องกับ KPI Policy ทุกข้อก่อน Submit

**วิธีเขียน:** ใช้ Checklist format แบบ checkbox พร้อมค่าที่ตรวจสอบได้จริง

**ตัวอย่างที่ดี:**

```markdown
## KPI Policy Compliance Check

| ข้อกำหนด (Policy Ref) | ค่าที่กำหนด | ค่าจริงในเอกสารนี้ | ผ่าน/ไม่ผ่าน |
|-----------------------|------------|-------------------|--------------|
| จำนวน KPI (Sec 4.2) | 3–5 ตัว | 5 ตัว | ✓ |
| น้ำหนักรวม (Sec 4.1) | = 100% | 30+25+20+15+10 = 100% | ✓ |
| น้ำหนักต่ำสุด (Sec 4.3) | ≥ 10% | ต่ำสุด = 10% (E-KPI-05) | ✓ |
| น้ำหนักสูงสุด (Sec 4.3) | ≤ 40% | สูงสุด = 30% (E-KPI-01) | ✓ |
| Link Company KPI (Sec 5.1) | ≥ 80% Weight | 30+25+20+15 = 90% | ✓ |
| People Mgmt KPI (Sec 6.4) | ≥ 1 ตัว | 1 ตัว (E-KPI-05) | ✓ |
| Output-based only (Sec 7.2) | ทุกตัว | ตรวจแล้ว — ทุกตัวเป็น Outcome | ✓ |
| Data Source ระบุชัด (Sec 8.1) | ทุกตัว | ระบุครบทุก KPI | ✓ |
```

**ตัวอย่างที่ผิด ❌:**

```markdown
## KPI Policy Compliance Check

ตรวจสอบแล้ว ผ่านทุกข้อ ✓
```

**เหตุผลที่ผิด:** ไม่มีการแสดงค่าที่ตรวจสอบ — Reviewer ไม่สามารถ Verify ได้ และถ้ามีข้อผิดพลาดจะตรวจไม่เจอจนกว่าจะถึง Performance Review

---

## 4. ตัวอย่างเต็ม

> **พนักงาน:** วีรชัย อินทรสุวรรณ | **ตำแหน่ง:** Digital Marketing Team Leader | **ทีม:** Marketing & Growth | **ไตรมาส:** Q3/2026

```markdown
# KPI_CHARTER.md
**Employee:** วีรชัย อินทรสุวรรณ | **Role:** Digital Marketing Team Leader
**Department:** Marketing & Growth | **Quarter:** Q3/2026 (ก.ค.–ก.ย. 2569)
**Created:** 2026-06-25 | **Version:** 1.0
**Approved by:** นลิน พรรัตน์ (VP Marketing) | **Date:** 2026-06-28

---

## KPI Objectives Summary
**Total Weight: 100%** ✓

| KPI ID | KPI Objective | Weight | Company KPI Link | Type |
|--------|---------------|--------|------------------|------|
| E-KPI-01 | Marketing Qualified Leads (MQL) | 30% | C-KPI-03 | Primary |
| E-KPI-02 | Customer Acquisition Cost (CAC) | 25% | C-KPI-07 | Primary |
| E-KPI-03 | Organic Search Traffic Growth | 20% | C-KPI-06 | Primary |
| E-KPI-04 | Campaign Blended ROI | 15% | C-KPI-01, C-KPI-07 | Primary |
| E-KPI-05 | Team Development Score | 10% | — (People Mgmt) | Supporting |
| | **รวม** | **100%** | | |

---

## Success Criteria per KPI

### E-KPI-01: Marketing Qualified Leads (MQL)
**Baseline Q2/2026:** 145 MQL | **Direction:** Higher is Better
**คำนิยาม MQL:** Lead ที่ผ่าน Lead Scoring ≥ 50 คะแนนใน HubSpot และ Job Title ตรงกับ ICP (HR Manager, CEO, COO ใน SME 50–500 คน)

| ระดับ | เกณฑ์ | Score | หมายเหตุ |
|-------|-------|-------|----------|
| 120% | ≥ 200 MQL | 120 | +38% YoY, บรรลุ Stretch Target |
| 100% | 180–199 MQL | 100 | +24–37% จาก Q2 Baseline |
| 70% | 140–179 MQL | 70 | Maintain ระดับ Q2 หรือดีกว่าเล็กน้อย |
| < 70% | < 140 MQL | 0–69 | ต่ำกว่า Baseline — ต้อง Root Cause Analysis |

### E-KPI-02: Customer Acquisition Cost (CAC)
**Baseline Q2/2026:** 9,200 THB/account | **Direction:** Lower is Better (Inverse)
**Company Target:** ≤ 8,500 THB/account
**สูตรคำนวณ:** Total Marketing Spend ÷ New Customers Acquired

| ระดับ | เกณฑ์ | Score | หมายเหตุ |
|-------|-------|-------|----------|
| 120% | ≤ 7,500 THB | 120 | ลด 18%+ จาก Baseline, เกิน Company Target |
| 100% | 7,501–8,500 THB | 100 | บรรลุ Company Target ≤ 8,500 THB |
| 70% | 8,501–9,500 THB | 70 | ลดลงจาก Q2 แต่ยังไม่ถึง Company Target |
| < 70% | > 9,500 THB | 0–69 | สูงกว่า Q2 Baseline — ต้องทบทวน Channel Mix |

### E-KPI-03: Organic Search Traffic Growth
**Baseline Q2/2026 avg:** 28,000 Sessions/month | **Direction:** Higher is Better

| ระดับ | เกณฑ์ | Score | หมายเหตุ |
|-------|-------|-------|----------|
| 120% | ≥ 36,000 Sessions/month avg | 120 | +29%+ จาก Baseline |
| 100% | 32,000–35,999 Sessions/month avg | 100 | +14–28% Growth |
| 70% | 28,001–31,999 Sessions/month avg | 70 | Maintain + Growth เล็กน้อย |
| < 70% | ≤ 28,000 Sessions/month avg | 0–69 | Flat หรือลด — ตรวจสอบ Technical SEO |

### E-KPI-04: Campaign Blended ROI
**Baseline Q2/2026:** 2.8x | **Direction:** Higher is Better
**สูตรคำนวณ:** (Revenue Attributed to Marketing) ÷ (Total Marketing Spend)

| ระดับ | เกณฑ์ | Score | หมายเหตุ |
|-------|-------|-------|----------|
| 120% | ≥ 3.8x ROI | 120 | +36%+ จาก Baseline |
| 100% | 3.2–3.7x ROI | 100 | +14–32% จาก Baseline |
| 70% | 2.8–3.1x ROI | 70 | Maintain ระดับ Q2 |
| < 70% | < 2.8x ROI | 0–69 | ต่ำกว่า Baseline — ต้องทบทวน Spend Allocation |

### E-KPI-05: Team Development Score
**Baseline:** — (ไตรมาสแรกที่วัดแบบ Formal) | **Direction:** Higher is Better
**วิธีวัด:** Average ของ Monthly 1-on-1 Development Score (1–5 scale) × 4 คน

| ระดับ | เกณฑ์ | Score | หมายเหตุ |
|-------|-------|-------|----------|
| 120% | ≥ 4.5/5.0 avg | 120 | ทีมมี Clear Development Path และ Progress |
| 100% | 4.0–4.4/5.0 avg | 100 | On Track ทุกคน |
| 70% | 3.5–3.9/5.0 avg | 70 | ส่วนใหญ่ On Track มี 1-2 คนที่ต้องติดตาม |
| < 70% | < 3.5/5.0 avg | 0–69 | มีปัญหา People Management ที่ต้องแก้ไข |

---

## Measurement Method

| KPI ID | Data Source | ความถี่ | ผู้ Pull Data | ผู้ Verify |
|--------|-------------|---------|--------------|-----------|
| E-KPI-01 | HubSpot CRM (MQL Stage Filter) | ทุกสิ้นเดือน | วีรชัย | VP Marketing |
| E-KPI-02 | HubSpot + Google Ads + Meta + LinkedIn | ทุกสิ้นเดือน | กานต์ (Paid Media) | วีรชัย |
| E-KPI-03 | Google Search Console + GA4 (Organic Sessions) | ทุกสิ้นเดือน | ปริม (SEO) | วีรชัย |
| E-KPI-04 | HubSpot Revenue Attribution Report | ทุกสิ้นเดือน | วีรชัย | VP Marketing |
| E-KPI-05 | 1-on-1 Score Sheet (Google Form) + HR Records | รายไตรมาส | วีรชัย | HR Business Partner |

**ข้อควรระวังพิเศษ Q3:**
HubSpot Migration ปลาย ส.ค. — เตรียม Manual Export Backup สำหรับ E-KPI-01 และ E-KPI-04 ในช่วง 25–31 ส.ค.

---

## KPI Policy Compliance Check

| ข้อกำหนด (Policy Ref) | ค่าที่กำหนด | ค่าจริงในเอกสารนี้ | สถานะ |
|-----------------------|------------|-------------------|--------|
| จำนวน KPI (Sec 4.2) | 3–5 ตัว | 5 ตัว | ✓ Pass |
| น้ำหนักรวม (Sec 4.1) | = 100% | 100% | ✓ Pass |
| น้ำหนักต่ำสุด (Sec 4.3) | ≥ 10% | 10% (E-KPI-05) | ✓ Pass |
| น้ำหนักสูงสุด (Sec 4.3) | ≤ 40% | 30% (E-KPI-01) | ✓ Pass |
| Link Company KPI (Sec 5.1) | ≥ 80% Weight | 90% (E-KPI-01~04) | ✓ Pass |
| People Mgmt KPI (Sec 6.4) | ≥ 1 ตัว | 1 ตัว (E-KPI-05) | ✓ Pass |
| Output-based (Sec 7.2) | ทุกตัว | ตรวจแล้ว ทุกตัวเป็น Outcome | ✓ Pass |
| Data Source ระบุ (Sec 8.1) | ทุกตัว | ระบุครบทุก KPI | ✓ Pass |
```

---

## 5. Validation Checklist

**โครงสร้างและ Header:**
- [ ] ระบุ Quarter และ Year ใน Header
- [ ] มี Approval Sign-off จากผู้จัดการ
- [ ] ระบุ Depends on CONTEXT_MAP.md และ ROLE_PROFILE.md version ใด

**KPI Objectives Summary:**
- [ ] น้ำหนัก KPI รวมกันได้ = 100% พอดี (ตรวจด้วยเครื่องคิดเลข ไม่ใช่แค่อ่าน)
- [ ] ทุก KPI มี Company KPI Link (ยกเว้น People Management KPI ที่อาจไม่มี)
- [ ] KPI ID ใช้รูปแบบ E-KPI-XX อย่างสม่ำเสมอ
- [ ] จำนวน KPI อยู่ในช่วงที่ Policy กำหนด (3–5 ตัวสำหรับ Grade M2)

**Success Criteria:**
- [ ] ทุก KPI มีเกณฑ์ครบ 3 ระดับ (70%, 100%, 120%)
- [ ] ทุกเกณฑ์เป็นตัวเลข — ห้ามมีคำเชิงคุณลักษณะ เช่น "ดี", "พอใจ"
- [ ] KPI ที่เป็น Inverse ระบุทิศทาง "Lower is Better" ชัดเจน
- [ ] ระบุ Baseline ของทุก KPI ก่อนกำหนดเกณฑ์

**Measurement Method:**
- [ ] ทุก KPI ระบุ Data Source ที่เฉพาะเจาะจง (ชื่อระบบ)
- [ ] ทุก KPI ระบุผู้ Pull Data และผู้ Verify แยกกัน
- [ ] ระบุความถี่การวัดผล

**Policy Compliance:**
- [ ] มี Compliance Check Table ที่แสดงค่าจริงเทียบกับ Policy
- [ ] ทุกแถวใน Compliance Check มีสถานะ ✓ Pass
- [ ] ถ้ามี ✗ Fail ต้องมีหมายเหตุและแผนแก้ไขก่อน Submit

**Cross-reference:**
- [ ] ทุก Company KPI Link ใน KPI Objectives ตรงกับ Primary/Secondary ใน CONTEXT_MAP.md
- [ ] ไม่มี KPI ที่ Link ไปหา Company KPI ที่ CONTEXT_MAP.md ระบุว่า None

---

## 6. ข้อผิดพลาดที่พบบ่อย

### ข้อผิดพลาดที่ 1: น้ำหนัก KPI รวมไม่ได้ 100%

❌ **ผิด:**
```
| E-KPI-01 | MQL | 30% |
| E-KPI-02 | CAC | 25% |
| E-KPI-03 | Traffic | 20% |
| E-KPI-04 | ROI | 20% |
| E-KPI-05 | Team Score | 10% |
รวม = 105% ❌
```

✅ **ถูก:** ตรวจสอบยอดรวม = 100% ก่อน Finalize เสมอ ถ้าผลรวมไม่ตรงให้ปรับ Weight ของ KPI ที่ยืดหยุ่นได้ (มักเป็น Supporting KPI)

**ผลกระทบ:** ระบบ PMS จะ Reject เอกสารทันที และ Score ที่คำนวณออกมาจะผิดทั้งหมด พนักงานอาจได้ Score สูง/ต่ำเกินจริง

---

### ข้อผิดพลาดที่ 2: เกณฑ์ 3 ระดับไม่เป็นตัวเลข

❌ **ผิด:**
```
| 100% (On Target) | บรรลุเป้า MQL ตามที่ตกลงกัน | 100 |
| 70% (Minimum) | บรรลุเป้าบางส่วน | 70 |
```

✅ **ถูก:**
```
| 100% (On Target) | 180–199 MQL | 100 |
| 70% (Minimum) | 140–179 MQL | 70 |
```

**ผลกระทบ:** เมื่อถึง Review ผู้จัดการและพนักงานจะเถียงกันว่า "บรรลุเป้าบางส่วน" หมายถึง 60% หรือ 90% — เป็นต้นเหตุของ Review Conflict ที่พบบ่อยที่สุด

---

### ข้อผิดพลาดที่ 3: ไม่ระบุทิศทางสำหรับ Inverse KPI

❌ **ผิด:**
```
### E-KPI-02: CAC
| 120% | ≥ 10,000 THB | 120 |  ← สับสนทิศทาง
| 100% | 8,500 THB | 100 |
| 70% | 7,000 THB | 70 |
```
(ยิ่ง CAC สูง Score ยิ่งสูง — ผิดทิศทาง)

✅ **ถูก:** ระบุ **Direction: Lower is Better (Inverse)** ชัดเจนใน Header ของ KPI นั้น และเกณฑ์ระดับ 120% ต้องเป็นค่าที่ต่ำที่สุด

**ผลกระทบ:** ถ้าทิศทางผิด พนักงานจะได้รับแรงจูงใจให้เพิ่ม CAC แทนที่จะลด — ซึ่งขัดแย้งกับ Company KPI C-KPI-07 โดยตรง

---

### ข้อผิดพลาดที่ 4: Link Company KPI ที่ CONTEXT_MAP บอกว่า None

❌ **ผิด:**
```
| E-KPI-06 | Feature Adoption Rate | 15% | C-KPI-04 | Primary |
```
(CONTEXT_MAP.md ระบุว่า Digital Marketing มี Alignment = None สำหรับ C-KPI-04)

✅ **ถูก:** ห้าม Link ไปหา Company KPI ที่ Alignment = None — ถ้าอยากมี KPI นี้ ต้องกลับไปแก้ CONTEXT_MAP.md และขออนุมัติจาก Manager ก่อน

**ผลกระทบ:** จะเกิด Ownership Conflict กับ Product Team ที่เป็นเจ้าของ Feature Adoption จริงๆ และเมื่อทีมอื่น Score ต่ำ พนักงาน Marketing จะได้รับผลกระทบจาก KPI ที่ตัวเองไม่สามารถควบคุมได้
