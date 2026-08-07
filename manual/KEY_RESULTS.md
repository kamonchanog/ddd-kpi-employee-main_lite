# คู่มือการเขียน KEY_RESULTS.md

---

## 1. ภาพรวม

KEY_RESULTS.md คือเอกสารที่แปลง KPI Objectives ใน KPI_CHARTER.md ให้กลายเป็น Key Results (KR) ที่วัดได้และปฏิบัติได้จริง แต่ละ KPI Objective จะมี KR อย่างน้อย 2 ตัว ซึ่งระบุ Numeric Target, Baseline, หน่วยวัด, Deadline, และ Lead/Lag Tag ชัดเจน เอกสารนี้ยังรวม KR Scoring Rubric ที่อธิบายวิธีคำนวณคะแนนจาก Actual vs Target รวมถึงการคำนวณแบบ Inverse Proportional สำหรับ KR ที่ "ยิ่งต่ำยิ่งดี" เช่น Error Rate หรือ Cost per Lead

- **depends_on:** KPI_CHARTER.md
- **downstream:** KEY_ACTIVITIES.md
- **ผู้เขียน:** พนักงานร่วมกับผู้จัดการ (ต้องมี KPI_CHARTER.md ที่ Approved แล้ว)
- **ผู้อ่าน:** พนักงาน, ผู้จัดการ, HR Business Partner
- **Output ที่คาดหวัง:** รายการ KR ที่ครอบคลุมทุก KPI Objective ในรูปแบบ SMART พร้อม Scoring Rubric และ Data Source ที่ชัดเจน

**Dependency Diagram:**

```
[KPI_CHARTER.md]
      |
      v
+------------------+
|  KEY_RESULTS.md  |  <-- คุณอยู่ที่นี่
+------------------+
      |
      v
[KEY_ACTIVITIES.md]
```

**Priority: P0**

---

## 2. ก่อนเริ่มเขียน (Prerequisites)

1. อ่าน KPI_CHARTER.md ที่ Approved แล้ว — บันทึก KPI ID, Weight, และเกณฑ์ 100% ของแต่ละ KPI
2. สำหรับแต่ละ KPI Objective ให้คิดว่า "ทำอะไรได้บ้างเพื่อให้ KPI นี้บรรลุ" — KR คือ Output ที่วัดได้ ไม่ใช่ Activity
3. ตรวจสอบ Baseline ของทุก KR ก่อนกำหนด Target — ถ้าไม่มี Baseline ต้องวัดในเดือนแรก (ก.ค.) แล้วค่อยตั้ง Target เดือน ส.ค. ขึ้นไป
4. ระบุว่า KR แต่ละตัวเป็น Lead Indicator (วัดได้ก่อนที่ผลจะเกิด) หรือ Lag Indicator (วัดได้หลังผลเกิด) เพื่อวางแผน Review ให้ถูกต้อง
5. ทำความเข้าใจ Inverse Proportional Scoring สำหรับ KR ที่วัด Cost, Rate, หรือ Error — สูตรและตัวอย่างอยู่ใน Section 3
6. ตรวจสอบว่า Deadline ทุกตัวอยู่ภายใน Quarter (ไม่เกิน 30 ก.ย. สำหรับ Q3)
7. ทุก KPI ต้องมี KR อย่างน้อย 2 ตัว — ถ้า KPI ไหนมีแค่ 1 ตัวหมายความว่า Decompose ยังไม่เพียงพอ

---

## 3. วิธีเขียนทีละ Section

### Key Results per Objective

**วัตถุประสงค์:** แสดง KR ที่ผ่านการตรวจสอบ SMART สำหรับแต่ละ KPI Objective พร้อมข้อมูลครบถ้วน

**วิธีเขียน:** เขียน subsection แยกต่อ KPI Objective หนึ่ง subsection ในแต่ละ KPI จะมีตาราง KR พร้อมคอลัมน์: KR ID / KR Statement / Baseline / Target / หน่วย / Deadline / Lead/Lag

**ตัวอย่างที่ดี — E-KPI-01 (MQL):**

```markdown
### E-KPI-01: Marketing Qualified Leads (MQL) — Weight 30%
**KPI Target (100%):** 180–199 MQL รายไตรมาส

| KR ID | KR Statement | Baseline | Target | หน่วย | Deadline | Lead/Lag |
|-------|-------------|----------|--------|-------|----------|----------|
| KR-01-A | เพิ่ม Website Conversion Rate (Visitor→Lead) จาก Landing Pages | 2.1% | 3.0% | % | 31 ส.ค. 2026 | Lead |
| KR-01-B | สร้าง MQL จาก Paid Campaigns ≥ 90 MQL ต่อไตรมาส | 78 | 90 | MQL | 30 ก.ย. 2026 | Lag |
| KR-01-C | สร้าง MQL จาก Organic (SEO + Content) ≥ 70 MQL | 52 | 70 | MQL | 30 ก.ย. 2026 | Lag |
| KR-01-D | ลด Lead-to-MQL Rejection Rate (Sales Reject) ≤ 15% | 22% | 15% | % | 30 ก.ย. 2026 | Lead |

**หมายเหตุ:** KR-01-D เป็น Inverse KR (ยิ่งต่ำยิ่งดี) — ดูวิธี Scoring ใน Section KR Scoring Rubric
```

**ตัวอย่างที่ผิด ❌:**

```markdown
### E-KPI-01: MQL

KR ของ E-KPI-01:
- สร้าง Content ที่ดีเพื่อดึง Lead
- ปรับปรุง Landing Page
- ทำ A/B Test
- เพิ่มงบ Paid Ads
```

**เหตุผลที่ผิด:** ทุกข้อเป็น Activity ไม่ใช่ Key Result ไม่มีตัวเลข Baseline หรือ Target — KR ต้องเป็น Output ที่วัดได้ ไม่ใช่สิ่งที่ทำ ถ้าเขียนแบบนี้ KEY_ACTIVITIES.md จะกลายเป็นเอกสารที่ซ้ำซ้อนกันทั้งหมด

---

### KR Scoring Rubric

**วัตถุประสงค์:** อธิบายวิธีแปลง Actual Result เป็น Score สำหรับทั้ง KR ปกติและ Inverse KR

**วิธีเขียน:** อธิบายสูตรและยกตัวอย่างเชิงตัวเลขอย่างน้อย 2 กรณี (Higher is Better และ Lower is Better)

**ตัวอย่างที่ดี:**

```markdown
## KR Scoring Rubric

### สูตรที่ 1: Higher is Better (Standard)
```
Score = (Actual ÷ Target) × 100
ถ้า Score > 120 → ปรับเป็น 120 (Cap)
ถ้า Score < 0 → ปรับเป็น 0
```

**ตัวอย่าง:** KR-01-B Target = 90 MQL, Actual = 81 MQL
Score = (81 ÷ 90) × 100 = **90 คะแนน**

---

### สูตรที่ 2: Lower is Better (Inverse Proportional)
```
Score = (Target ÷ Actual) × 100
ถ้า Score > 120 → ปรับเป็น 120 (Cap)
ถ้า Score < 0 → ปรับเป็น 0
```

**ตัวอย่าง:** KR-01-D Target = 15% Rejection Rate, Actual = 12% (ดีกว่า Target)
Score = (15 ÷ 12) × 100 = **125 → ปรับเป็น 120 คะแนน** (ใช้ Cap)

**ตัวอย่าง:** KR-01-D Target = 15%, Actual = 18% (แย่กว่า Target)
Score = (15 ÷ 18) × 100 = **83 คะแนน**

---

### วิธีคำนวณ KPI Score รวมจาก KR

KPI Score = Average ของ KR Score ทั้งหมดภายใต้ KPI นั้น (เว้นแต่ระบุ Weight ของ KR แยกไว้)

**ตัวอย่าง E-KPI-01:**
- KR-01-A Score: 95
- KR-01-B Score: 90
- KR-01-C Score: 107
- KR-01-D Score: 120

**E-KPI-01 Score = (95 + 90 + 107 + 120) ÷ 4 = 103 คะแนน**
```

**ตัวอย่างที่ผิด ❌:**

```markdown
## KR Scoring Rubric

ให้คะแนนตามผลงานจริง ถ้าทำได้ตาม Target ได้ 100 คะแนน ถ้าทำได้มากกว่าได้มากกว่า
```

**เหตุผลที่ผิด:** ไม่มีสูตรที่ชัดเจน ไม่มีตัวอย่างเชิงตัวเลข และไม่ได้กล่าวถึง Inverse Scoring เลย — ทำให้ Review Score ผิดพลาดสำหรับ KR ที่วัด CAC หรือ Error Rate

---

### KR Data Sources

**วัตถุประสงค์:** ระบุแหล่งข้อมูลสำหรับแต่ละ KR พร้อมผู้รับผิดชอบและ Access Method

**วิธีเขียน:** ใช้ตาราง 5 คอลัมน์: KR ID / แหล่งข้อมูล / ระบบ/URL / ผู้รับผิดชอบ / รูปแบบ Export

**ตัวอย่างที่ดี:**

```markdown
## KR Data Sources

| KR ID | Metric | แหล่งข้อมูล | ผู้รับผิดชอบ | Export Format |
|-------|--------|------------|--------------|---------------|
| KR-01-A | Conversion Rate | GA4 → Goals Report + HubSpot Forms | ปริม วงศ์ทอง | CSV รายเดือน |
| KR-01-B | Paid MQL | HubSpot CRM (Source = Paid) | กานต์ ชัยกุล | HubSpot Report |
| KR-01-C | Organic MQL | HubSpot CRM (Source = Organic/Social) | ปริม วงศ์ทอง | HubSpot Report |
| KR-01-D | Sales Rejection Rate | HubSpot Deal Stage → Disqualified | วีรชัย | Manual Count |
| KR-02-A | Total Ad Spend | Google Ads + Meta Ads + LinkedIn Ads | กานต์ ชัยกุล | Platform Export |
| KR-02-B | New Customers (Paid) | HubSpot Deals (Closed Won + Source=Paid) | วีรชัย | HubSpot Report |
| KR-03-A | Organic Sessions | Google Search Console + GA4 | ปริม วงศ์ทอง | GSC Export |
| KR-03-B | Keyword Ranking | SEMrush Position Tracking | ปริม วงศ์ทอง | SEMrush Report |
| KR-04-A | Attributed Revenue | HubSpot Revenue Attribution | วีรชัย | HubSpot Report |
| KR-05-A | Team Dev Score | Google Form Score Sheet | วีรชัย | Form Response |
```

**ตัวอย่างที่ผิด ❌:**

```markdown
## KR Data Sources

ดูจาก Dashboard ของบริษัท
```

**เหตุผลที่ผิด:** ไม่ระบุว่า Dashboard ไหน ไม่มีผู้รับผิดชอบ — ถ้าข้อมูลหาย Reviewer จะไม่รู้จะไปหาที่ไหน

---

### Review Schedule

**วัตถุประสงค์:** กำหนดตารางเวลาการ Review KR ตลอดไตรมาส เพื่อให้มีการ Track Progress อย่างสม่ำเสมอ

**วิธีเขียน:** ใช้ตาราง Timeline แสดง Monthly Progress Check และ Quarter-End Final Review พร้อมระบุว่า Review แต่ละครั้งดูอะไร และมีผลอย่างไร

**ตัวอย่างที่ดี:**

```markdown
## Review Schedule

| รอบ | วันที่ | ประเภท | สิ่งที่ Review | ผู้เข้าร่วม | ผลลัพธ์ |
|-----|--------|--------|----------------|------------|---------|
| M1 | 31 ก.ค. 2026 | Progress Check | KR Actual ทั้งหมด + Lead KR | วีรชัย + Manager | Midpoint Adjustment (ถ้าจำเป็น) |
| M2 | 31 ส.ค. 2026 | Progress Check | KR Actual ทั้งหมด + Forecast Q3 | วีรชัย + Manager | Action Plan ถ้าต่ำกว่า 80% |
| M3 | 30 ก.ย. 2026 | Final Review | KR Final Score + KPI Score | วีรชัย + Manager + HR | Score Submission |

**KR ที่ต้องดูเป็นพิเศษ:**
- KR-01-A (Conversion Rate): ดู Weekly เพราะเป็น Lead Indicator — ถ้าต่ำกว่า 2.5% ใน ก.ค. ต้องแก้ไขก่อน ส.ค.
- KR-01-D (Rejection Rate): ดู Bi-weekly ร่วมกับ Sales Team — เป็น KR ที่ต้องประสานงานข้ามทีม
- KR ทุกตัว: เดือนที่ HubSpot Migration (ส.ค.) ใช้ Manual Backup Data
```

**ตัวอย่างที่ผิด ❌:**

```markdown
## Review Schedule

Review ทุกเดือน
```

**เหตุผลที่ผิด:** ไม่ระบุวันที่ชัดเจน ไม่ระบุใครเข้าร่วม และไม่ระบุว่า Review แล้วทำอะไร — ทำให้ Review เกิดขึ้นหรือไม่เกิดขึ้นก็ได้โดยไม่มีผลกระทบ

---

## 4. ตัวอย่างเต็ม

> **พนักงาน:** วีรชัย อินทรสุวรรณ | **ตำแหน่ง:** Digital Marketing Team Leader | **ทีม:** Marketing & Growth | **ไตรมาส:** Q3/2026

```markdown
# KEY_RESULTS.md
**Employee:** วีรชัย อินทรสุวรรณ | **Role:** Digital Marketing Team Leader
**Department:** Marketing & Growth | **Quarter:** Q3/2026 (ก.ค.–ก.ย. 2569)
**Created:** 2026-06-28 | **Version:** 1.0 | **Depends on:** KPI_CHARTER.md v1.0

---

## Key Results per Objective

### E-KPI-01: Marketing Qualified Leads (MQL) — Weight 30%
**KPI Target (100%):** 180–199 MQL Q3/2026

| KR ID | KR Statement | Baseline | Target | หน่วย | Deadline | Lead/Lag |
|-------|-------------|----------|--------|-------|----------|----------|
| KR-01-A | เพิ่ม Landing Page Conversion Rate (Visitor→Form Submit) | 2.1% | 3.0% | % | 31 ส.ค. 2026 | Lead |
| KR-01-B | สร้าง MQL จาก Paid Campaigns (Google + Meta + LinkedIn) | 78 | 90 | MQL | 30 ก.ย. 2026 | Lag |
| KR-01-C | สร้าง MQL จาก Organic (SEO + Content + Email) | 52 | 70 | MQL | 30 ก.ย. 2026 | Lag |
| KR-01-D | ลด Sales Rejection Rate (MQL ที่ Sales ปฏิเสธ) | 22% | 15% | % | 30 ก.ย. 2026 | Lead ★Inverse |

### E-KPI-02: Customer Acquisition Cost (CAC) — Weight 25%
**KPI Target (100%):** ≤ 8,500 THB/account
**สูตร:** Total Marketing Spend ÷ New Customers from Marketing

| KR ID | KR Statement | Baseline | Target | หน่วย | Deadline | Lead/Lag |
|-------|-------------|----------|--------|-------|----------|----------|
| KR-02-A | ลด Cost per Lead (CPL) ของ Paid Campaigns | 450 | 330 | THB/Lead | 30 ก.ย. 2026 | Lead ★Inverse |
| KR-02-B | เพิ่ม Lead-to-Customer Conversion Rate (Paid) | 3.2% | 4.5% | % | 30 ก.ย. 2026 | Lead |
| KR-02-C | ปิด Budget Variance ≤ ±5% ของ Quarterly Budget | — | ≤5% | % variance | 30 ก.ย. 2026 | Lag ★Inverse |

### E-KPI-03: Organic Search Traffic Growth — Weight 20%
**KPI Target (100%):** 32,000–35,999 Sessions/month avg

| KR ID | KR Statement | Baseline | Target | หน่วย | Deadline | Lead/Lag |
|-------|-------------|----------|--------|-------|----------|----------|
| KR-03-A | เพิ่ม Monthly Organic Sessions เฉลี่ย Q3 | 28,000 | 33,000 | Sessions/month | 30 ก.ย. 2026 | Lag |
| KR-03-B | เพิ่ม Keywords ที่ติด Top 10 ใน Google.co.th | 42 | 70 | Keywords | 31 ส.ค. 2026 | Lead |
| KR-03-C | Publish Blog Posts ที่ SEO-Optimized ≥ 9 ชิ้น | 0 | 9 | Posts | 30 ก.ย. 2026 | Lead |

### E-KPI-04: Campaign Blended ROI — Weight 15%
**KPI Target (100%):** 3.2–3.7x ROI

| KR ID | KR Statement | Baseline | Target | หน่วย | Deadline | Lead/Lag |
|-------|-------------|----------|--------|-------|----------|----------|
| KR-04-A | บรรลุ Marketing Attributed Revenue Q3 | — | 1,440,000 | THB | 30 ก.ย. 2026 | Lag |
| KR-04-B | ลด Spend บน Low-ROI Channels (< 2x ROI) ลง | 100% | ≤30% | % of Total Spend | 31 ส.ค. 2026 | Lead ★Inverse |

### E-KPI-05: Team Development Score — Weight 10%
**KPI Target (100%):** 4.0–4.4/5.0 avg

| KR ID | KR Statement | Baseline | Target | หน่วย | Deadline | Lead/Lag |
|-------|-------------|----------|--------|-------|----------|----------|
| KR-05-A | จัด 1-on-1 รายสัปดาห์ครบตามกำหนดสำหรับสมาชิก 4 คน | 0% | ≥ 90% | % completion | 30 ก.ย. 2026 | Lead |
| KR-05-B | สมาชิกทีมทุกคนมี Individual Development Plan (IDP) | 0 | 4 | คน | 31 ก.ค. 2026 | Lead |
| KR-05-C | Average Development Score จาก 1-on-1 (เฉลี่ยทั้ง Quarter) | — | 4.0 | /5.0 | 30 ก.ย. 2026 | Lag |

---

## KR Scoring Rubric

### สูตรที่ 1: Higher is Better (Standard)
```
Score = (Actual ÷ Target) × 100
Cap ≤ 120 | Floor ≥ 0
```
**ตัวอย่าง:** KR-01-B Target = 90 MQL, Actual = 85 MQL → Score = (85÷90)×100 = **94 คะแนน**

---

### สูตรที่ 2: Lower is Better (Inverse Proportional) — ★Inverse
```
Score = (Target ÷ Actual) × 100
Cap ≤ 120 | Floor ≥ 0
```
**ตัวอย่าง A (ดีกว่า Target):** KR-01-D Target = 15%, Actual = 11%
Score = (15÷11)×100 = 136 → ปรับเป็น **120 คะแนน** (ใช้ Cap)

**ตัวอย่าง B (แย่กว่า Target):** KR-01-D Target = 15%, Actual = 20%
Score = (15÷20)×100 = **75 คะแนน**

---

### วิธีรวม KPI Score จาก KR
**E-KPI-01 ตัวอย่าง (ถ้า KR ไม่มี Weight แยก = Average เท่าๆ กัน):**
KR-01-A: 110, KR-01-B: 94, KR-01-C: 100, KR-01-D: 120
E-KPI-01 Score = (110+94+100+120)÷4 = **106 คะแนน** → อยู่ในระดับ 100–119 = On Target+

---

## KR Data Sources

| KR ID | Metric | ระบบ | ผู้รับผิดชอบ | Export Format |
|-------|--------|------|--------------|---------------|
| KR-01-A | Landing Page Conversion Rate | GA4 Goals + HubSpot Forms | ปริม วงศ์ทอง | CSV รายเดือน |
| KR-01-B | Paid MQL Count | HubSpot CRM (Source Filter) | กานต์ ชัยกุล | HubSpot List Export |
| KR-01-C | Organic MQL Count | HubSpot CRM (Source Filter) | ปริม วงศ์ทอง | HubSpot List Export |
| KR-01-D | Sales Rejection Rate | HubSpot Deal Stage Log | วีรชัย | Manual Count |
| KR-02-A | CPL Paid | Google Ads + Meta Ads Manager | กานต์ ชัยกุล | Platform Export |
| KR-02-B | Lead-to-Customer Rate | HubSpot Funnel Report | วีรชัย | HubSpot Report |
| KR-02-C | Budget Variance | Finance Budget Sheet + Ad Platforms | วีรชัย | Manual Calculation |
| KR-03-A | Organic Sessions | Google Search Console + GA4 | ปริม วงศ์ทอง | GSC Export |
| KR-03-B | Top 10 Keyword Count | SEMrush Position Tracking | ปริม วงศ์ทอง | SEMrush Export |
| KR-03-C | Blog Post Count | CMS (WordPress) Content Calendar | แพร มาลีวรรณ | Manual Count |
| KR-04-A | Attributed Revenue | HubSpot Revenue Attribution (First Touch) | วีรชัย | HubSpot Report |
| KR-04-B | Low-ROI Channel Spend % | Ad Platform Reports | กานต์ ชัยกุล | Manual Calculation |
| KR-05-A | 1-on-1 Completion Rate | Calendar + Meeting Log (Notion) | วีรชัย | Manual Count |
| KR-05-B | IDP Completion | HR System + Google Drive | วีรชัย | HR Form |
| KR-05-C | Avg Dev Score | Google Form (1-on-1 Template) | วีรชัย | Form Export |

---

## Review Schedule

| รอบ | วันที่ | ประเภท | Focus KR | ผู้เข้าร่วม | Action |
|-----|--------|--------|----------|------------|--------|
| M1 Check | 31 ก.ค. 2026 | Progress | KR-01-A, KR-01-D, KR-03-B, KR-05-B (Lead KRs) | วีรชัย + นลิน | Midpoint Adjustment |
| M2 Check | 29 ส.ค. 2026 | Progress + Forecast | ทุก KR + Q3 Projection | วีรชัย + นลิน | Action Plan ถ้า < 80% |
| M3 Final | 30 ก.ย. 2026 | Final Scoring | ทุก KR (Final Actual) | วีรชัย + นลิน + HR | Score Lock + Submission |

**หมายเหตุ ส.ค.:** HubSpot Migration ปลายเดือน — ใช้ Manual Export Backup สำหรับ KR-01-B, KR-01-C, KR-04-A
```

---

## 5. Validation Checklist

**โครงสร้างและ Header:**
- [ ] ระบุ Depends on KPI_CHARTER.md version
- [ ] ทุก E-KPI-XX มี Section ใน Key Results per Objective

**Key Results per Objective:**
- [ ] ทุก KPI Objective มี KR อย่างน้อย 2 ตัว
- [ ] ทุก KR มีตัวเลข Baseline และ Target
- [ ] ทุก KR ระบุ Deadline ที่อยู่ภายใน Quarter
- [ ] ทุก KR ระบุ Lead หรือ Lag
- [ ] KR ที่เป็น Inverse ระบุ ★Inverse อย่างชัดเจน
- [ ] ทุก KR เป็น Output/Result ไม่ใช่ Activity

**KR Scoring Rubric:**
- [ ] มีสูตร Standard (Higher is Better) พร้อมตัวอย่างตัวเลข
- [ ] มีสูตร Inverse (Lower is Better) พร้อมตัวอย่างตัวเลข 2 กรณี (เกิน/ต่ำกว่า Target)
- [ ] ระบุ Cap ที่ 120 และ Floor ที่ 0
- [ ] อธิบายวิธีรวม KPI Score จาก KR หลายตัว

**KR Data Sources:**
- [ ] ทุก KR ระบุระบบ/แหล่งข้อมูลที่เฉพาะเจาะจง
- [ ] ทุก KR ระบุผู้รับผิดชอบ Pull Data
- [ ] ระบุรูปแบบ Export

**Review Schedule:**
- [ ] มีอย่างน้อย 3 รอบ Review ใน Quarter (M1/M2/M3)
- [ ] ระบุวันที่ชัดเจน
- [ ] ระบุผู้เข้าร่วมและ Action ที่เกิดขึ้นหลัง Review

**Cross-reference กับ KPI_CHARTER.md:**
- [ ] KPI ID ใน KEY_RESULTS.md ตรงกับ KPI_CHARTER.md ทุกตัว
- [ ] Target ของ Lag KR สอดคล้องกับเกณฑ์ 100% ใน Success Criteria
- [ ] ไม่มี KR ที่ Deadline เกินวันสิ้นสุด Quarter

---

## 6. ข้อผิดพลาดที่พบบ่อย

### ข้อผิดพลาดที่ 1: KR คือ Activity ไม่ใช่ Result

❌ **ผิด:**
```
KR-01-A: จัดทำ A/B Test Landing Page 3 ชุด
KR-01-B: เพิ่มงบ Paid Ads 20%
KR-01-C: ทำ Content Marketing รายสัปดาห์
```

✅ **ถูก:**
```
KR-01-A: เพิ่ม Landing Page Conversion Rate จาก 2.1% เป็น 3.0% ภายใน 31 ส.ค.
KR-01-B: สร้าง MQL จาก Paid Campaigns ≥ 90 MQL ภายใน 30 ก.ย.
KR-01-C: Publish SEO-Optimized Blog Posts ≥ 9 ชิ้น ภายใน 30 ก.ย.
```

**ผลกระทบ:** ถ้า KR เป็น Activity จะไม่สามารถวัดความสำเร็จที่แท้จริงได้ ทำ A/B Test ครบ 3 ชุดแต่ Conversion ไม่เพิ่มขึ้นเลย — ได้ 100 คะแนน KR แต่ KPI ล้มเหลว

---

### ข้อผิดพลาดที่ 2: Inverse KR ไม่มีทิศทางที่ชัดเจน

❌ **ผิด:**
```
KR-02-A: CAC ≤ 8,500 THB ได้ Score 100
```
(ไม่ระบุว่าเป็น Inverse และไม่มีสูตรคำนวณ Score สำหรับค่าที่อยู่ระหว่าง)

✅ **ถูก:** ระบุ ★Inverse ทั้งในตาราง KR และ Scoring Rubric พร้อมตัวอย่างคำนวณ 2 กรณีที่เป็นตัวเลข

**ผลกระทบ:** ถ้าไม่มี Rubric ชัดเจน Reviewer จะคำนวณ Score ผิด เช่น ใช้ Standard Formula กับ CAC ทำให้ยิ่ง CAC สูงยิ่งได้คะแนนสูง

---

### ข้อผิดพลาดที่ 3: Deadline ของ KR เกิน Quarter

❌ **ผิด:**
```
KR-03-C: Publish Blog Posts ≥ 9 ชิ้น | Deadline: 31 ต.ค. 2026
```
(Q3 สิ้นสุด 30 ก.ย. แต่ Deadline อยู่ใน Q4)

✅ **ถูก:**
```
KR-03-C: Publish Blog Posts ≥ 9 ชิ้น | Deadline: 30 ก.ย. 2026
```

**ผลกระทบ:** KR ที่ Deadline เกิน Quarter จะไม่ถูกนับใน Q3 Score ทำให้ E-KPI-03 ขาด KR ที่ใช้คำนวณ และพนักงานทำงานโดยไม่รู้ว่าผลงานจะไม่ถูกวัด

---

### ข้อผิดพลาดที่ 4: ไม่มี Lead KR เลย มีแต่ Lag KR

❌ **ผิด:**
```
KR-01-B: MQL Paid 90 ตัว (Lag) | Deadline: 30 ก.ย.
KR-01-C: MQL Organic 70 ตัว (Lag) | Deadline: 30 ก.ย.
```
(ทั้งสอง KR รู้ผลแค่ปลาย Quarter — ไม่มี Early Warning Signal)

✅ **ถูก:** เพิ่ม Lead KR เช่น Conversion Rate (วัดได้รายสัปดาห์) เพื่อให้รู้ก่อนว่าจะบรรลุหรือไม่ ถ้าต่ำกว่าเป้าสัปดาห์ที่ 3 ยังแก้ได้ทัน

**ผลกระทบ:** ถ้ามีแต่ Lag KR จะรู้ว่าล้มเหลวก็ต่อเมื่อสิ้น Quarter แล้ว ไม่มีโอกาสปรับแผนกลางทาง
