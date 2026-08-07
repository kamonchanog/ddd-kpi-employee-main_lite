# คู่มือการเขียน CONTEXT_MAP.md

---

## 1. ภาพรวม

CONTEXT_MAP.md คือเอกสารเริ่มต้นของ DDD-KPI Employee Edition ทำหน้าที่เชื่อมโยง Strategy ระดับบริษัทลงมาสู่ระดับบุคคล เป็นเอกสาร P0 ที่ทุกเอกสารอื่นในชุดนี้ต้องอ้างอิง เนื้อหาหลักคือการแสดงให้เห็นว่า Company KPI ในไตรมาสนี้เชื่อมกับ Strategic Theme ใด และบทบาทของพนักงานคนนี้มีความเกี่ยวข้องกับ KPI ระดับบริษัทอย่างไร เอกสารนี้ป้องกันปัญหา "KPI ลอย" ที่ไม่มีรากฐานมาจากทิศทางองค์กร

- **depends_on:** ไม่มี (เป็น root document)
- **downstream:** ROLE_PROFILE.md, KPI_CHARTER.md, KEY_RESULTS.md, KEY_ACTIVITIES.md
- **ผู้เขียน:** HR/PM หรือพนักงานร่วมกับผู้จัดการ (ต้องมีข้อมูล Company Strategy และ Company KPI ก่อน)
- **ผู้อ่าน:** พนักงาน, ผู้จัดการโดยตรง, HR Business Partner
- **Output ที่คาดหวัง:** ตารางแสดง Role-KPI Alignment ที่ระบุว่าแต่ละ Company KPI มีความเกี่ยวข้องกับบทบาทนี้ในระดับ Primary / Secondary / None พร้อมเหตุผลชัดเจน

**Dependency Diagram:**

```
[Company Strategy & Vision]
         |
         v
 [Company KPI This Quarter]
         |
         v
+------------------+
|  CONTEXT_MAP.md  |  <-- คุณอยู่ที่นี่
+------------------+
         |
    +---------+----------+----------+
    v         v          v          v
ROLE_PROFILE  KPI_CHARTER KEY_RESULTS KEY_ACTIVITIES
```

**Priority: P0**

---

## 2. ก่อนเริ่มเขียน (Prerequisites)

1. อ่านเอกสาร Company Strategy อย่างน้อย 1 รอบ — ระบุ Vision, Mission, และ Strategic Themes ให้ครบ
2. รวบรวม Company KPI ของไตรมาสปัจจุบันจากระบบ PMS หรือเอกสาร OKR ระดับบริษัท
3. ระบุ Quarter และ Year ที่ชัดเจน เช่น Q3/2026 (กรกฎาคม–กันยายน 2569)
4. ทำความเข้าใจ Job Description (JD) ของตนเองในเบื้องต้น เพื่อประเมิน alignment ได้อย่างสมเหตุสมผล
5. ตรวจสอบว่า Company KPI มีอยู่กี่ตัว และแต่ละตัวมีหน่วยวัดอะไร (%, THB, count)
6. ถามผู้จัดการหรือ HR ว่าบทบาทของตนเองอยู่ใน Value Chain ขององค์กรในส่วนใด (Revenue Generation / Support / Compliance)
7. ห้ามคาดเดา Company KPI — ต้องมาจากแหล่งข้อมูลทางการเท่านั้น

---

## 3. วิธีเขียนทีละ Section

### Company Strategy Summary

**วัตถุประสงค์:** ย่อ Vision, Mission, และ Strategic Themes ของบริษัทในรูปแบบที่กระชับ เพื่อให้ผู้อ่านเข้าใจบริบทก่อนดู KPI

**วิธีเขียน:** ดึงข้อมูลจากเอกสาร Company Strategy โดยตรง ไม่ตีความหรือปรับแต่ง ใช้ bullet point แยก Vision / Mission / Strategic Themes อย่างละ 1-2 ประโยค

**ตัวอย่างที่ดี:**

```markdown
## Company Strategy Summary

**Vision:** Ragnar เป็นแพลตฟอร์ม QMS และ Performance Management ที่ SME ไทยเลือกใช้มากที่สุด ภายในปี 2028

**Mission:** ทำให้การจัดการคุณภาพและประสิทธิภาพองค์กรเป็นเรื่องง่าย ผ่าน SaaS ที่ใช้งานได้จริงโดยไม่ต้องมีที่ปรึกษาภายนอก

**Strategic Themes Q3/2026:**
- ST-1: Revenue Growth — เพิ่ม MRR และลด Churn Rate
- ST-2: Product Excellence — เพิ่ม Feature Adoption และลด Support Ticket
- ST-3: Brand Authority — สร้างการรับรู้แบรนด์ในกลุ่ม HR Tech ไทย
- ST-4: Operational Efficiency — ลด CAC และปรับปรุง Gross Margin
```

**ตัวอย่างที่ผิด ❌:**

```markdown
## Company Strategy Summary

บริษัทต้องการเติบโตและมีกำไรมากขึ้น โดยพัฒนาผลิตภัณฑ์ให้ดีขึ้นและลูกค้าพอใจ
ทีม Marketing ควรช่วยสร้างรายได้ให้บริษัท
```

**เหตุผลที่ผิด:** ไม่มีการอ้างอิง Vision/Mission จริง ไม่ระบุ Strategic Theme ที่ชัดเจน และมีการตีความเพิ่มเติมที่ไม่มีในต้นฉบับ ส่งผลให้ KPI ที่ตามมาขาดรากฐาน

---

### KPI Company This Quarter

**วัตถุประสงค์:** แสดงรายการ Company KPI ทั้งหมดของไตรมาสนี้พร้อม Target และหน่วยวัด เป็นแหล่งอ้างอิงที่ KPI_CHARTER.md จะต้อง link กลับมา

**วิธีเขียน:** ใช้ตาราง 4 คอลัมน์: KPI ID / KPI Name / Target / Strategic Theme ที่เชื่อมโยง ห้ามเพิ่ม KPI ที่ไม่มีในระบบ PMS ต้นทาง

**ตัวอย่างที่ดี:**

```markdown
## KPI Company This Quarter (Q3/2026)

| KPI ID | Company KPI | Target | Strategic Theme |
|--------|-------------|--------|-----------------|
| C-KPI-01 | MRR Growth Rate | +15% QoQ | ST-1 |
| C-KPI-02 | Churn Rate | ≤ 2.5% | ST-1 |
| C-KPI-03 | New Customer Acquisition | 80 accounts | ST-1, ST-3 |
| C-KPI-04 | Feature Adoption Rate | 60% of active users | ST-2 |
| C-KPI-05 | NPS Score | ≥ 45 | ST-2 |
| C-KPI-06 | Brand Awareness Score | +20% YoY | ST-3 |
| C-KPI-07 | Customer Acquisition Cost (CAC) | ≤ 8,500 THB | ST-4 |
```

**ตัวอย่างที่ผิด ❌:**

```markdown
## KPI Company This Quarter

- เพิ่มยอดขาย
- ลูกค้าพอใจ
- ทีมทำงานได้ดี
- รายได้เพิ่มขึ้น 20%
```

**เหตุผลที่ผิด:** ไม่มี KPI ID, ไม่มีหน่วยวัดที่ชัดเจน, บาง item เป็นเป้าหมายที่คลุมเครือ และไม่เชื่อมกับ Strategic Theme — ทำให้ KPI_CHARTER.md ไม่สามารถ link กลับมาได้

---

### Role-KPI Alignment Matrix

**วัตถุประสงค์:** แสดงให้เห็นชัดเจนว่าบทบาทของพนักงานคนนี้มีผลต่อ Company KPI ตัวใด และมากน้อยแค่ไหน พร้อมคำอธิบายเหตุผล

**วิธีเขียน:** ใช้ตาราง 3 คอลัมน์: Company KPI / Alignment Level / เหตุผล (1-2 ประโยค) โดย Alignment Level มี 3 ระดับ:
- **Primary:** บทบาทนี้มีผลโดยตรงและวัดได้ต่อ KPI นี้
- **Secondary:** บทบาทนี้มีส่วนสนับสนุนแต่ไม่ใช่ผู้รับผิดชอบหลัก
- **None:** บทบาทนี้ไม่มีความเกี่ยวข้องกับ KPI นี้อย่างมีนัยสำคัญ

**ตัวอย่างที่ดี:**

```markdown
## Role-KPI Alignment Matrix
**Role:** Digital Marketing Team Leader | **Quarter:** Q3/2026

| Company KPI | Alignment Level | เหตุผล |
|-------------|-----------------|--------|
| C-KPI-01: MRR Growth Rate | Primary | Digital Marketing สร้าง Pipeline โดยตรงผ่าน Inbound & Paid campaigns ซึ่งแปลงเป็น MRR |
| C-KPI-02: Churn Rate | Secondary | Content และ Email campaigns ช่วย Onboarding และ Engagement แต่ Churn หลักอยู่ที่ CS |
| C-KPI-03: New Customer Acquisition | Primary | Demand Generation เป็น Core Function ของ Digital Marketing |
| C-KPI-04: Feature Adoption Rate | None | Feature Adoption อยู่ในความรับผิดชอบของ Product & CS team |
| C-KPI-05: NPS Score | Secondary | Review campaigns และ Success Stories ช่วย Sentiment แต่ไม่ใช่ผู้ขับเคลื่อนหลัก |
| C-KPI-06: Brand Awareness Score | Primary | Brand Content, SEO, และ Social Media เป็นงานหลักของทีม |
| C-KPI-07: CAC | Primary | Digital Marketing เป็นผู้กำหนด Channel Mix และ Budget Efficiency โดยตรง |
```

**ตัวอย่างที่ผิด ❌:**

```markdown
## Role-KPI Alignment Matrix

| Company KPI | Alignment Level |
|-------------|-----------------|
| MRR Growth Rate | Primary |
| Churn Rate | Primary |
| New Customer Acquisition | Primary |
| Feature Adoption Rate | Primary |
| NPS Score | Primary |
| Brand Awareness Score | Primary |
| CAC | Primary |
```

**เหตุผลที่ผิด:** ทุก KPI เป็น Primary ไม่มีเหตุผลประกอบ และไม่สมเหตุสมผลเลย — Digital Marketing ไม่สามารถรับผิดชอบ Feature Adoption ได้โดยตรง การไม่แยก Level ทำให้ KPI_CHARTER.md ตั้ง KPI ซ้อนทับกับทีมอื่น

---

### Quarter Context

**วัตถุประสงค์:** ระบุบริบทพิเศษของไตรมาสนี้ที่อาจส่งผลต่อการตั้ง KPI หรือความยากในการบรรลุเป้าหมาย

**วิธีเขียน:** เขียนเป็น bullet point สั้นๆ 3-6 ข้อ ครอบคลุม: ช่วงเวลา, งบประมาณที่ได้รับ, ปัจจัยภายนอก, ทรัพยากรพิเศษ หรือข้อจำกัดที่รู้ล่วงหน้า

**ตัวอย่างที่ดี:**

```markdown
## Quarter Context (Q3/2026: กรกฎาคม–กันยายน 2569)

- **ช่วงเวลา:** Q3 ตรงกับฤดูกาล Slow Season ของ B2B SaaS ในไทย (ส.ค. มีวันหยุดยาว)
- **งบประมาณ:** Digital Marketing Budget Q3 = 450,000 THB (เพิ่มจาก Q2 15%)
- **Launch ใหม่:** Ragnar Performance Module v2.0 จะ Launch ปลาย ก.ค. — เป็นโอกาสสำหรับ PR Campaign
- **ทีม:** มีพนักงานใหม่ 1 คน (Content Specialist) เริ่มงาน 1 ก.ค. — ต้อง Onboard ก่อนมอบงานเต็มรูปแบบ
- **ข้อจำกัด:** ระบบ CRM (HubSpot) จะมี Migration ปลาย ส.ค. อาจส่งผลต่อ Reporting 1-2 สัปดาห์
```

**ตัวอย่างที่ผิด ❌:**

```markdown
## Quarter Context

ไตรมาส 3 เป็นไตรมาสที่สำคัญ ทีมต้องทำงานหนักเพื่อบรรลุเป้าหมาย
```

**เหตุผลที่ผิด:** ไม่มีข้อมูลที่ใช้ประโยชน์ได้จริง — ไม่ระบุช่วงเวลา งบประมาณ หรือปัจจัยเสี่ยง ทำให้ KEY_ACTIVITIES.md ไม่สามารถวางแผนรับมือปัจจัยเหล่านี้ได้

---

## 4. ตัวอย่างเต็ม

> **พนักงาน:** วีรชัย อินทรสุวรรณ | **ตำแหน่ง:** Digital Marketing Team Leader | **ทีม:** Marketing & Growth | **ไตรมาส:** Q3/2026

```markdown
# CONTEXT_MAP.md
**Employee:** วีรชัย อินทรสุวรรณ | **Role:** Digital Marketing Team Leader
**Department:** Marketing & Growth | **Quarter:** Q3/2026 (ก.ค.–ก.ย. 2569)
**Created:** 2026-06-25 | **Version:** 1.0

---

## Company Strategy Summary

**Vision:** Ragnar เป็นแพลตฟอร์ม QMS และ Performance Management ที่ SME ไทยเลือกใช้มากที่สุด ภายในปี 2028

**Mission:** ทำให้การจัดการคุณภาพและประสิทธิภาพองค์กรเป็นเรื่องง่าย ผ่าน SaaS ที่ใช้งานได้จริง โดยไม่ต้องพึ่งที่ปรึกษาภายนอก

**Strategic Themes Q3/2026:**
- ST-1: Revenue Growth — เร่ง MRR และรักษาฐานลูกค้าเดิม
- ST-2: Product Excellence — เพิ่ม Adoption และคุณภาพประสบการณ์การใช้งาน
- ST-3: Brand Authority — สร้างการรับรู้และความน่าเชื่อถือในตลาด HR Tech ไทย
- ST-4: Operational Efficiency — เพิ่ม ROI ของทุก Function และลดต้นทุนต่อหน่วย

---

## KPI Company This Quarter (Q3/2026)

| KPI ID | Company KPI | Target | Strategic Theme |
|--------|-------------|--------|-----------------|
| C-KPI-01 | MRR Growth Rate | +15% QoQ | ST-1 |
| C-KPI-02 | Churn Rate | ≤ 2.5% | ST-1 |
| C-KPI-03 | New Customer Acquisition | 80 new accounts | ST-1, ST-3 |
| C-KPI-04 | Feature Adoption Rate (Performance Module) | 60% of active users | ST-2 |
| C-KPI-05 | NPS Score | ≥ 45 | ST-2 |
| C-KPI-06 | Brand Awareness Score (aided recall) | +20% YoY | ST-3 |
| C-KPI-07 | Customer Acquisition Cost (CAC) | ≤ 8,500 THB/account | ST-4 |

---

## Role-KPI Alignment Matrix
**Role:** Digital Marketing Team Leader | **Quarter:** Q3/2026

| Company KPI | Alignment Level | เหตุผล |
|-------------|-----------------|--------|
| C-KPI-01: MRR Growth Rate | Primary | Inbound และ Paid campaigns ของทีมสร้าง Pipeline ที่แปลงเป็น Subscription โดยตรง — Marketing Attribution ครอบ 60% ของ New MRR |
| C-KPI-02: Churn Rate | Secondary | Email Nurturing และ Success Story content ช่วยรักษา Engagement แต่การตัดสินใจ Renew อยู่ที่ CS Team |
| C-KPI-03: New Customer Acquisition | Primary | Demand Generation, Lead Nurturing, และ Conversion Optimization เป็น Core Deliverable ของ Digital Marketing |
| C-KPI-04: Feature Adoption Rate | None | Feature Adoption ขึ้นอยู่กับ Onboarding Flow และ In-app Guidance ซึ่งอยู่ในความรับผิดชอบของ Product & CS |
| C-KPI-05: NPS Score | Secondary | Customer Review Campaign และ Social Proof Content ช่วย Sentiment แต่ Promoter/Detractor หลักมาจากประสบการณ์ใช้งาน Product |
| C-KPI-06: Brand Awareness Score | Primary | SEO, Content Marketing, Social Media, และ PR Campaign เป็นงานหลักที่ทีมนี้ขับเคลื่อนโดยตรง |
| C-KPI-07: CAC | Primary | Digital Marketing กำหนด Channel Mix, Bid Strategy, และ Conversion Funnel ซึ่งเป็นตัวแปรหลักของ CAC |

---

## Quarter Context (Q3/2026: กรกฎาคม–กันยายน 2569)

- **ช่วงเวลา:** Q3 ตรงกับ Slow Season B2B ในไทย — ส.ค. มีวันหยุดยาวหลายวัน ควรเร่ง Pipeline ใน ก.ค.
- **งบประมาณ:** Digital Marketing Budget Q3/2026 = 450,000 THB (เพิ่ม 15% จาก Q2)
- **Product Launch:** Ragnar Performance Module v2.0 จะ Go-Live ปลาย ก.ค. — โอกาสทำ Launch Campaign ใหญ่
- **ทีมใหม่:** Content Specialist เริ่มงาน 1 ก.ค. — ต้องใช้เวลา 2-3 สัปดาห์ Onboard ก่อนเต็มประสิทธิภาพ
- **ข้อจำกัดระบบ:** HubSpot CRM Migration ปลาย ส.ค. — Reporting อาจมี Gap 1-2 สัปดาห์
- **งบประมาณเพิ่มเติม:** PR Budget 80,000 THB สำหรับ Product Launch (ไม่รวมใน Budget หลัก)
```

---

## 5. Validation Checklist

**โครงสร้างและ Header:**
- [ ] ระบุ Quarter และ Year ใน Header อย่างชัดเจน (เช่น Q3/2026)
- [ ] ระบุชื่อพนักงาน ตำแหน่ง และทีม
- [ ] มีวันที่สร้างและ Version

**Company Strategy Summary:**
- [ ] มี Vision ที่มาจากเอกสารทางการ ไม่ใช่แต่งเอง
- [ ] มี Mission ที่ชัดเจน
- [ ] ระบุ Strategic Themes อย่างน้อย 3 ข้อพร้อม ID (ST-1, ST-2, ...)
- [ ] ไม่มีการตีความหรือเพิ่มเนื้อหาที่ไม่มีในต้นฉบับ

**KPI Company This Quarter:**
- [ ] ทุก KPI มี KPI ID (C-KPI-XX)
- [ ] ทุก KPI มี Target ที่เป็นตัวเลขหรือค่าที่วัดได้
- [ ] ทุก KPI เชื่อมกับ Strategic Theme ที่ระบุใน Strategy Summary
- [ ] จำนวน KPI ตรงกับที่ระบบ PMS กำหนด — ไม่เพิ่ม ไม่ลด

**Role-KPI Alignment Matrix:**
- [ ] ทุก Company KPI มีการระบุ Alignment Level (Primary/Secondary/None)
- [ ] ทุก item ที่เป็น Primary หรือ Secondary มีเหตุผลอธิบาย ไม่ใช่แค่ระบุ Level
- [ ] ไม่มี KPI ที่ "ควรเป็น None" ถูกทำให้เป็น Primary เพื่อเอาใจผู้จัดการ
- [ ] มี KPI ที่ระดับ None อย่างน้อย 1 ตัว (เพื่อแสดงว่าวิเคราะห์จริง)
- [ ] Alignment สอดคล้องกับ Job Description ที่มีอยู่จริง

**Quarter Context:**
- [ ] ระบุช่วงเวลาของไตรมาส (เดือนเริ่ม–เดือนจบ)
- [ ] ระบุงบประมาณที่ได้รับ (ถ้ามีข้อมูล)
- [ ] ระบุปัจจัยเสี่ยงหรือข้อจำกัดที่รู้ล่วงหน้า
- [ ] ระบุโอกาสพิเศษของไตรมาส (Product Launch, Event, ฯลฯ)

**Cross-reference:**
- [ ] KPI ID ใน Alignment Matrix ตรงกับ KPI ID ใน KPI Company This Quarter
- [ ] Strategic Theme ที่ใช้ใน KPI table ตรงกับ Strategic Theme ใน Strategy Summary

---

## 6. ข้อผิดพลาดที่พบบ่อย

### ข้อผิดพลาดที่ 1: สร้าง Company KPI ขึ้นเอง

❌ **ผิด:**
```
| C-KPI-08 | Employee Engagement Score | ≥ 75% | ST-4 |
```
(ไม่มีใน PMS ต้นทาง แต่ใส่เข้ามาเพราะคิดว่าน่าจะมี)

✅ **ถูก:**
ใช้เฉพาะ KPI ที่มีอยู่ใน PMS หรือเอกสาร Company OKR อย่างเป็นทางการ ถ้าพบ KPI ที่คิดว่าควรมีแต่ไม่มี ให้บันทึกใน Quarter Context แทน

**ผลกระทบ:** KPI_CHARTER.md จะ link ไปหา Company KPI ที่ไม่มีจริง ทำให้ระบบ Validation ล้มเหลวและตัวเลขรายงานไม่ได้

---

### ข้อผิดพลาดที่ 2: ทุกอย่างเป็น Primary

❌ **ผิด:**
```
| C-KPI-04: Feature Adoption Rate | Primary | ทีม Marketing ช่วยโปรโมท Feature |
```

✅ **ถูก:**
```
| C-KPI-04: Feature Adoption Rate | None | Feature Adoption ขึ้นอยู่กับ In-app Experience และ CS Onboarding ซึ่งไม่อยู่ในขอบเขตของ Digital Marketing |
```

**ผลกระทบ:** ถ้า Marketing รับ Primary ใน Feature Adoption โดยไม่มีอำนาจควบคุม KPI นั้นจะกลายเป็น Vanity KPI ที่วัดไม่ได้ และทีม Product กับ CS จะ confused ว่าใครต้องรับผิดชอบ

---

### ข้อผิดพลาดที่ 3: ไม่ระบุ Quarter ใน Header

❌ **ผิด:**
```
# CONTEXT_MAP.md
**Employee:** วีรชัย อินทรสุวรรณ
```

✅ **ถูก:**
```
# CONTEXT_MAP.md
**Employee:** วีรชัย อินทรสุวรรณ | **Quarter:** Q3/2026 (ก.ค.–ก.ย. 2569)
```

**ผลกระทบ:** เอกสารชุดนี้จะถูกสร้างทุกไตรมาส ถ้าไม่ระบุ Quarter จะเกิดความสับสนว่าเอกสารนี้เป็นของ Q ใด โดยเฉพาะเมื่อดู Historical Records

---

### ข้อผิดพลาดที่ 4: ใส่เหตุผลใน Alignment Matrix แบบ Copy-Paste ทุกแถว

❌ **ผิด:**
```
| C-KPI-01: MRR Growth Rate | Primary | ทีม Digital Marketing รับผิดชอบ KPI นี้ |
| C-KPI-03: New Customer Acquisition | Primary | ทีม Digital Marketing รับผิดชอบ KPI นี้ |
| C-KPI-06: Brand Awareness | Primary | ทีม Digital Marketing รับผิดชอบ KPI นี้ |
```

✅ **ถูก:** เหตุผลของแต่ละแถวต้องอธิบาย Mechanism ที่แตกต่างกัน — MRR มาจาก Pipeline Conversion, Acquisition มาจาก Lead Generation, Brand มาจาก Content & SEO

**ผลกระทบ:** เหตุผล Generic ไม่ช่วยให้ KPI_CHARTER.md สร้าง KPI ที่ถูกต้อง และไม่แสดงให้เห็นว่าผู้เขียนเข้าใจ Value Chain จริงๆ
