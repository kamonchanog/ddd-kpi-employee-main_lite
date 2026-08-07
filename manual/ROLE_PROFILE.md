# คู่มือการเขียน ROLE_PROFILE.md

---

## 1. ภาพรวม

ROLE_PROFILE.md คือเอกสารที่สังเคราะห์บทบาทของพนักงานจากแหล่งข้อมูลสามแหล่ง ได้แก่ Job Description (JD), Job Landscape (ภาพรวมของแผนกและตำแหน่งเทียบเคียง), และ KPI Policy ขององค์กร เอกสารนี้ทำหน้าที่เป็น "กรอบขอบเขต" ที่ KPI_CHARTER.md จะใช้ในการตั้ง KPI — ถ้า ROLE_PROFILE.md ไม่ชัดเจน KPI ที่ได้จะออกมาผิดขอบเขต เอกสารนี้แยกแยะความแตกต่างระหว่าง "สิ่งที่พนักงานทำ" กับ "สิ่งที่ผู้อื่นรับผิดชอบ" อย่างชัดเจน ซึ่งเป็นรากฐานของการ Link ระหว่าง Role กับ Company KPI ที่ถูกต้อง

- **depends_on:** CONTEXT_MAP.md
- **downstream:** KPI_CHARTER.md, KEY_RESULTS.md, KEY_ACTIVITIES.md
- **ผู้เขียน:** HR Business Partner ร่วมกับพนักงานและผู้จัดการโดยตรง
- **ผู้อ่าน:** พนักงาน, ผู้จัดการ, HR, และ Reviewer ของ KPI_CHARTER.md
- **Output ที่คาดหวัง:** เอกสารที่ระบุ Core Responsibilities, ตำแหน่งในแผนก, ผู้มีส่วนได้ส่วนเสีย (Stakeholders), และข้อจำกัดจาก KPI Policy ที่ต้องนำมาพิจารณาในการตั้ง KPI

**Dependency Diagram:**

```
[CONTEXT_MAP.md]  +  [Job Description]  +  [KPI Policy]
         |                  |                    |
         +------------------+--------------------+
                            |
                            v
                  +--------------------+
                  |  ROLE_PROFILE.md   |  <-- คุณอยู่ที่นี่
                  +--------------------+
                            |
                  +---------+----------+
                  v                    v
           KPI_CHARTER.md      (KEY_RESULTS.md)
```

**Priority: P0**

---

## 2. ก่อนเริ่มเขียน (Prerequisites)

1. อ่าน CONTEXT_MAP.md ให้จบ โดยเฉพาะ Role-KPI Alignment Matrix — ทำให้รู้ว่า KPI ตัวใดเป็น Primary ของบทบาทนี้
2. รวบรวม Job Description (JD) ฉบับปัจจุบัน — ถ้าไม่มีให้ขอจาก HR ก่อน ห้ามเขียนจากความจำ
3. อ่าน Job Landscape ของแผนก เพื่อเข้าใจว่าบทบาทนี้อยู่ตรงไหนในโครงสร้างทีม และต่างจาก Senior/Junior Position อย่างไร
4. ดาวน์โหลด KPI Policy เวอร์ชันล่าสุดจาก HR และอ่าน Section ที่เกี่ยวกับ Managerial/Team Leader Position
5. ระบุ Stakeholders ที่ทำงานด้วยบ่อย ทั้ง upstream (ทีมที่ส่งข้อมูลให้เรา) และ downstream (ทีมที่เราส่งผลงานให้)
6. ตรวจสอบว่า Job Title ปัจจุบันตรงกับ Job Grade ใน KPI Policy — เพราะ Policy อาจกำหนดจำนวน KPI, น้ำหนัก KPI ต่ำสุด/สูงสุด แตกต่างกันตาม Grade
7. บันทึกข้อจำกัดพิเศษที่เกิดจากบริบท Quarter นี้ (เช่น มีพนักงานใหม่ในทีม, ระบบ IT กำลัง Migrate)

---

## 3. วิธีเขียนทีละ Section

### Core Responsibilities

**วัตถุประสงค์:** สรุปหน้าที่รับผิดชอบหลักจาก JD ในรูปแบบที่กระชับและ Actionable เพื่อใช้เป็นฐานในการตั้ง KPI

**วิธีเขียน:** ดึงข้อมูลจาก JD โดยตรง จัดกลุ่มตาม Function Area (เช่น Strategy, Execution, People Management, Reporting) ใช้ Verb ที่ชัดเจน (วางแผน, ดำเนินการ, ตรวจสอบ, รายงาน) ห้ามเพิ่มหน้าที่ที่ไม่มีใน JD

**ตัวอย่างที่ดี:**

```markdown
## Core Responsibilities
*(มาจาก JD version 2.1, อัปเดต: มีนาคม 2026)*

**Strategy & Planning:**
- วางแผน Digital Marketing Strategy รายไตรมาส ครอบคลุม SEO, Paid Media, Social Media, Email Marketing
- กำหนด Channel Mix และ Budget Allocation ตาม ROI Target ที่ได้รับมอบหมาย

**Execution & Management:**
- ดูแลและบริหารทีม 4 คน (SEO Specialist, Paid Media Specialist, Content Specialist × 2)
- ตรวจสอบและอนุมัติ Content Calendar รายสัปดาห์
- บริหาร Ad Spend Budget ประจำไตรมาส

**Analytics & Reporting:**
- รายงาน Campaign Performance ต่อ VP Marketing ทุก 2 สัปดาห์
- วิเคราะห์ Attribution Model และ Marketing Funnel Metrics รายเดือน

**Collaboration:**
- ประสานงานกับ Sales Team เพื่อ Lead Handoff Process
- ทำงานร่วมกับ Product Team สำหรับ Launch Campaign
```

**ตัวอย่างที่ผิด ❌:**

```markdown
## Core Responsibilities

- ดูแลงาน Marketing ทั้งหมด
- ทำให้บริษัทมีลูกค้าเพิ่มขึ้น
- จัดการทีม
- วิเคราะห์ข้อมูล
- ประสานงานกับทีมอื่นๆ
- รับผิดชอบ Budget ของทีม
- รับผิดชอบ Customer Experience ของลูกค้า (ไม่มีใน JD)
```

**เหตุผลที่ผิด:** ใช้ภาษากว้างเกินไป ไม่มี Function Area ที่จัดกลุ่ม และบางข้อ (Customer Experience) ไม่มีใน JD — ถ้าใส่เข้ามาจะทำให้ KPI_CHARTER.md ตั้ง KPI ที่เกินขอบเขต

---

### Department Landscape

**วัตถุประสงค์:** แสดงให้เห็นว่าตำแหน่งนี้อยู่ตรงไหนในโครงสร้างของแผนก รายงานต่อใคร และมีทีมอะไรอยู่ข้างเคียง

**วิธีเขียน:** ใช้ Org Chart แบบ text art และคำอธิบาย 3-4 ประโยค ระบุ Direct Manager, Peer Positions, และทีมที่ดูแล

**ตัวอย่างที่ดี:**

```markdown
## Department Landscape

**แผนก:** Marketing & Growth | **รายงานต่อ:** VP Marketing (นลิน พรรัตน์)

```
VP Marketing
├── Digital Marketing Team Leader  ← [วีรชัย] ตำแหน่งนี้
│   ├── SEO Specialist (1)
│   ├── Paid Media Specialist (1)
│   └── Content Specialist (2)
├── Brand & PR Manager (Peer)
└── Marketing Operations (Peer)
```

**ตำแหน่งนี้ในบริบทแผนก:**
Digital Marketing Team Leader รับผิดชอบ Performance Marketing และ Organic Growth ซึ่งเป็นช่องทางหลักในการสร้าง Inbound Pipeline ตำแหน่งนี้แตกต่างจาก Brand & PR Manager ที่เน้น Awareness และ Reputation Management ไม่ใช่ Conversion

**ขอบเขตที่ชัดเจน:**
- IN SCOPE: Paid Ads, SEO/SEM, Email Marketing, Social Media Performance
- OUT OF SCOPE: Event Marketing (อยู่ที่ Brand & PR), Customer Success Content (อยู่ที่ CS Team)
```

**ตัวอย่างที่ผิด ❌:**

```markdown
## Department Landscape

อยู่ในทีม Marketing รายงานต่อหัวหน้า มีลูกน้อง 4 คน ทำงานร่วมกับทุกทีมในบริษัท
```

**เหตุผลที่ผิด:** ไม่มี Org Chart, ไม่ระบุชื่อ Manager, ไม่แยก IN/OUT SCOPE — ทำให้ KPI_CHARTER.md ไม่รู้ว่าควรหยุดตั้ง KPI ตรงไหน

---

### Collaboration Map

**วัตถุประสงค์:** ระบุ Stakeholders ที่ทำงานด้วย โดยแยกอย่างชัดเจนระหว่าง Upstream (คนที่ส่งข้อมูล/ทรัพยากรให้เรา) และ Downstream (คนที่รับผลงานจากเรา)

**วิธีเขียน:** ใช้ตาราง 4 คอลัมน์: ทีม/บุคคล / ทิศทาง / สิ่งที่แลกเปลี่ยน / ความถี่

**ตัวอย่างที่ดี:**

```markdown
## Collaboration Map

| ทีม / บุคคล | ทิศทาง | สิ่งที่แลกเปลี่ยน | ความถี่ |
|-------------|---------|-------------------|---------|
| VP Marketing | Upstream | OKR, Budget, Strategic Direction | รายเดือน |
| Sales Team | Downstream | Qualified Leads, MQL Handoff | รายสัปดาห์ |
| Product Team | Upstream | Feature Roadmap, Launch Brief | รายเดือน |
| Customer Success | Downstream/Upstream | Win/Loss Stories, Customer Quotes | รายเดือน |
| Finance | Upstream | Budget Approval, Spend Reports | รายไตรมาส |
| Brand & PR (Peer) | Lateral | Campaign Alignment, Asset Sharing | รายสัปดาห์ |

**Critical Dependency:**
Sales Team คือ Downstream ที่สำคัญที่สุด — ถ้า Lead Quality ต่ำ Pipeline จะไม่ Convert และ MRR Growth จะไม่บรรลุ แม้ว่า Marketing จะทำ Volume ได้ตามเป้า
```

**ตัวอย่างที่ผิด ❌:**

```markdown
## Collaboration Map

ทำงานร่วมกับ: Sales, Product, CS, Finance, Brand, HR, Legal, IT
```

**เหตุผลที่ผิด:** ไม่แยก Upstream/Downstream, ไม่ระบุสิ่งที่แลกเปลี่ยน, และรายการกว้างเกินจนไม่มีประโยชน์ — ทำให้ KEY_ACTIVITIES.md ไม่รู้ว่าต้องประสานงานกับใครเมื่อไหร่

---

### KPI Constraints & Policy Notes

**วัตถุประสงค์:** สรุปข้อกำหนดจาก KPI Policy ที่ส่งผลต่อการออกแบบ KPI ของบทบาทนี้โดยตรง

**วิธีเขียน:** อ้างอิง Section ของ KPI Policy อย่างชัดเจน ระบุข้อจำกัดที่เป็นตัวเลขหรือกฎที่ต้องปฏิบัติตาม

**ตัวอย่างที่ดี:**

```markdown
## KPI Constraints & Policy Notes

**อ้างอิง:** Ragnar KPI Policy v3.2 (มีนาคม 2026)

**ข้อกำหนดสำหรับ Team Leader Level (Grade M2):**

| ข้อกำหนด | รายละเอียด | Policy Reference |
|----------|------------|------------------|
| จำนวน KPI | 3–5 ตัว | Section 4.2 |
| น้ำหนัก KPI แต่ละตัว | 10%–40% | Section 4.3 |
| สัดส่วน KPI ที่ Link กับ Company KPI | ≥ 80% ของ Weight ทั้งหมด | Section 5.1 |
| KPI ด้าน People Management | ต้องมีอย่างน้อย 1 ตัว | Section 6.4 (Team Leader) |
| Measurement Period | Quarterly (วัดทุกเดือน, Finalize รายไตรมาส) | Section 3.1 |

**ข้อควรระวัง:**
- Section 7.2: KPI ที่วัดผลจาก "ความพยายาม" (เช่น จำนวนชั่วโมงทำงาน) ไม่ได้รับการยอมรับ — ต้องเป็น Output-based เท่านั้น
- Section 8.1: KPI ที่ใช้ข้อมูลจากระบบภายนอก (เช่น Google Ads, Facebook Ads) ต้องระบุ Data Source และผู้รับผิดชอบ Verify ข้อมูลชัดเจน
```

**ตัวอย่างที่ผิด ❌:**

```markdown
## KPI Constraints & Policy Notes

ต้องทำ KPI ตาม Policy ของบริษัท ดูได้ที่ HR
```

**เหตุผลที่ผิด:** ไม่ได้อ้างอิง Section ใดเลย ไม่ระบุตัวเลขข้อจำกัด — ทำให้ KPI_CHARTER.md อาจตั้ง KPI ที่ผิด Policy โดยไม่รู้ตัว

---

## 4. ตัวอย่างเต็ม

> **พนักงาน:** วีรชัย อินทรสุวรรณ | **ตำแหน่ง:** Digital Marketing Team Leader | **ทีม:** Marketing & Growth | **ไตรมาส:** Q3/2026

```markdown
# ROLE_PROFILE.md
**Employee:** วีรชัย อินทรสุวรรณ | **Role:** Digital Marketing Team Leader
**Department:** Marketing & Growth | **Quarter:** Q3/2026 (ก.ค.–ก.ย. 2569)
**Created:** 2026-06-25 | **Version:** 1.0 | **Depends on:** CONTEXT_MAP.md v1.0

---

## Core Responsibilities
*(มาจาก JD Digital Marketing Team Leader v2.1, อัปเดต: มีนาคม 2026)*

**Strategy & Planning:**
- วางแผน Digital Marketing Strategy รายไตรมาส ครอบคลุม SEO, Paid Media (Google/Meta), Social Media, และ Email Marketing
- กำหนด Channel Mix และ Budget Allocation ตาม ROI Target ที่ได้รับมอบหมายจาก VP Marketing

**Campaign Management:**
- ดูแลและบริหาร Paid Campaigns บน Google Ads, Meta Ads, และ LinkedIn Ads
- อนุมัติ Content Calendar รายสัปดาห์และ Creative Briefs
- บริหาร Ad Spend Budget ทั้ง Quarter — ต้องใช้ไม่เกิน ±5% ของงบที่ได้รับ

**Analytics & Reporting:**
- รายงาน Campaign Performance (CTR, CPL, MQL, CAC) ต่อ VP Marketing ทุก 2 สัปดาห์
- วิเคราะห์ Full-Funnel Attribution และ Channel ROI รายเดือน
- รับผิดชอบ Marketing Dashboard ใน HubSpot และ Google Analytics 4

**People Management:**
- บริหารและ Coach ทีม 4 คน: SEO Specialist (1), Paid Media Specialist (1), Content Specialist (2)
- ทำ 1-on-1 รายสัปดาห์และ Performance Review รายไตรมาส

**Collaboration:**
- ประสานงานกับ Sales Team เพื่อกำหนด Lead Scoring และ MQL Handoff Criteria
- ทำงานร่วมกับ Product Team สำหรับ Product Launch Campaign Brief

---

## Department Landscape

**แผนก:** Marketing & Growth | **รายงานต่อ:** VP Marketing (นลิน พรรัตน์) | **Grade:** M2 (Team Leader)

```
VP Marketing (นลิน พรรัตน์)
├── Digital Marketing Team Leader  ← [วีรชัย] ตำแหน่งนี้
│   ├── SEO Specialist (ปริม วงศ์ทอง)
│   ├── Paid Media Specialist (กานต์ ชัยกุล)
│   ├── Content Specialist (รมย์ สิริมงคล)  — ใหม่ 1 ก.ค. 2026
│   └── Content Specialist (แพร มาลีวรรณ)
├── Brand & PR Manager (ศิริ ภักดีสกุล)  — Peer
└── Marketing Operations (อนุพร เตชะ)  — Peer
```

**ขอบเขตที่ชัดเจน:**

| IN SCOPE | OUT OF SCOPE |
|----------|--------------|
| Paid Ads (Google, Meta, LinkedIn) | Event Marketing (อยู่ที่ Brand & PR) |
| SEO / SEM / Organic Search | Trade Show / Offline Marketing |
| Email Marketing & Automation | Customer Success Content / Knowledge Base |
| Social Media Performance Campaigns | Product Documentation |
| Lead Generation & Nurturing | Customer Support Communications |

---

## Collaboration Map

| ทีม / บุคคล | ทิศทาง | สิ่งที่แลกเปลี่ยน | ความถี่ |
|-------------|---------|-------------------|---------|
| VP Marketing (นลิน พรรัตน์) | Upstream | OKR, Budget, Strategy Direction, Performance Review | รายเดือน |
| Sales Team (ผู้จัดการ: ธนา วิชัย) | Downstream | MQL List, Lead Quality Report, Win/Loss Feedback | รายสัปดาห์ |
| Product Team (PM: ชนิดา สุวรรณ) | Upstream | Feature Roadmap, Launch Brief, Product Messaging | รายเดือน |
| Customer Success (CS Lead: วิภา นาค) | Bi-directional | Customer Stories (รับ), Onboarding Email Content (ส่ง) | รายเดือน |
| Finance (AP: ประภา สมิต) | Upstream | Budget Report, Invoice Approval, Spend Reconciliation | รายเดือน |
| Brand & PR (ศิริ ภักดีสกุล) | Lateral | Campaign Alignment, Brand Asset, PR Calendar | รายสัปดาห์ |
| IT / Marketing Ops (อนุพร เตชะ) | Upstream | HubSpot Access, GA4 Setup, Tracking Implementation | ตามต้องการ |

**Critical Dependency:**
Sales Team เป็น downstream ที่สำคัญที่สุดสำหรับ MRR KPI — ถ้า Lead Quality ต่ำ Sales จะ Reject และ Pipeline Conversion จะล้มเหลว ต้องมี SLA ร่วมกันว่า MQL ต้องมีคุณสมบัติอะไร

---

## KPI Constraints & Policy Notes

**อ้างอิง:** Ragnar KPI Policy v3.2 (มีนาคม 2026) — Grade M2: Team Leader

| ข้อกำหนด | รายละเอียด | Policy Reference |
|----------|------------|------------------|
| จำนวน KPI ทั้งหมด | 3–5 ตัว | Section 4.2, Table 3 |
| น้ำหนักต่ำสุดต่อ KPI | 10% | Section 4.3 |
| น้ำหนักสูงสุดต่อ KPI | 40% | Section 4.3 |
| สัดส่วน Link กับ Company KPI | ≥ 80% ของ Weight รวม | Section 5.1 |
| KPI People Management | บังคับ ≥ 1 ตัว สำหรับ Grade M2+ | Section 6.4 |
| การวัดผล | Quarterly Final + Monthly Progress Check | Section 3.1 |
| Data Source | ต้องระบุระบบและผู้ Verify สำหรับ External Data | Section 8.1 |

**ข้อห้ามเพิ่มเติม (Section 7.x):**
- ห้ามตั้ง KPI ที่วัดจาก Input/Effort (เช่น จำนวน Posts, จำนวนชั่วโมงทำงาน) — ต้อง Output/Outcome-based
- ห้ามตั้ง KPI ที่มีข้อมูลวัดผลจาก Subjective Assessment เพียงอย่างเดียว (Section 7.3)
- ถ้าใช้ External Platform (Google Ads, Meta) เป็น Data Source ต้องมี Monthly Screenshot + Export เก็บไว้ (Section 8.2)
```

---

## 5. Validation Checklist

**โครงสร้างและ Header:**
- [ ] ระบุ Quarter และ Year ใน Header
- [ ] ระบุ Version ของ JD ที่ใช้อ้างอิง
- [ ] ระบุว่า Depends on CONTEXT_MAP.md version ใด

**Core Responsibilities:**
- [ ] ทุกข้อมาจาก JD จริง ไม่ได้คิดเพิ่มเอง
- [ ] มีการจัดกลุ่มตาม Function Area
- [ ] ใช้ Action Verb ที่ชัดเจน (ไม่ใช่ "ดูแลงาน" แต่เป็น "วางแผน/อนุมัติ/รายงาน/บริหาร")
- [ ] ไม่มีหน้าที่ที่อยู่นอก JD แทรกเข้ามา

**Department Landscape:**
- [ ] มี Org Chart (text art) ที่แสดง Direct Manager, Peers, และ Direct Reports
- [ ] ระบุชื่อ Manager จริง
- [ ] มีตาราง IN SCOPE / OUT OF SCOPE
- [ ] OUT OF SCOPE ระบุว่าสิ่งนั้นอยู่ที่ทีมใด

**Collaboration Map:**
- [ ] แยก Upstream / Downstream / Lateral อย่างชัดเจน
- [ ] ระบุสิ่งที่แลกเปลี่ยนในแต่ละความสัมพันธ์
- [ ] ระบุความถี่การประสานงาน
- [ ] ระบุ Critical Dependency ที่ส่งผลต่อ KPI หลัก

**KPI Constraints & Policy Notes:**
- [ ] อ้างอิง Policy Version และ Section อย่างเฉพาะเจาะจง
- [ ] ระบุจำนวน KPI min/max สำหรับ Grade นี้
- [ ] ระบุน้ำหนัก KPI min/max
- [ ] ระบุว่าต้องมี People Management KPI หรือไม่

**Cross-reference กับ CONTEXT_MAP.md:**
- [ ] Core Responsibilities สอดคล้องกับ Primary KPI ใน Role-KPI Alignment Matrix
- [ ] OUT OF SCOPE ตรงกับ None ใน Alignment Matrix
- [ ] ไม่มีความขัดแย้งระหว่าง Scope ที่นี่กับ Alignment ใน CONTEXT_MAP.md

---

## 6. ข้อผิดพลาดที่พบบ่อย

### ข้อผิดพลาดที่ 1: เพิ่ม Responsibilities ที่ไม่มีใน JD

❌ **ผิด:**
```
**Core Responsibilities:**
- รับผิดชอบ Customer Experience ทั้งหมดของ Ragnar
- กำหนด Product Roadmap ร่วมกับ CTO
```
(ทั้งสองข้อนี้ไม่มีใน JD Digital Marketing Team Leader)

✅ **ถูก:**
ใส่เฉพาะสิ่งที่ระบุใน JD หากอยากเพิ่มเติม ให้ใส่ใน Quarter Context ของ CONTEXT_MAP.md แทนว่า "ได้รับมอบหมายพิเศษ" สำหรับไตรมาสนี้

**ผลกระทบ:** KPI_CHARTER.md จะตั้ง KPI ที่เกินขอบเขต เช่น NPS หรือ Product Adoption ซึ่งทำให้เกิดความขัดแย้งกับทีม Product และ CS ว่าใครรับผิดชอบ

---

### ข้อผิดพลาดที่ 2: ไม่อ้างอิง Section ใน KPI Policy

❌ **ผิด:**
```
## KPI Constraints & Policy Notes
ต้องมี KPI ไม่เกิน 5 ตัว และน้ำหนักต้องรวมกันได้ 100%
```

✅ **ถูก:**
```
| จำนวน KPI ทั้งหมด | 3–5 ตัว | Section 4.2, Table 3 |
| น้ำหนักรวม | = 100% | Section 4.1 |
```

**ผลกระทบ:** ถ้า Policy เปลี่ยน (เช่น จาก 5 เป็น 6 ตัว) และไม่มีการอ้างอิง Section ชัดเจน จะไม่รู้ว่าต้องไปอ่านที่ไหนเพื่ออัปเดต และอาจใช้กฎเก่าที่ผิดอยู่นาน

---

### ข้อผิดพลาดที่ 3: Collaboration Map ไม่แยก Upstream/Downstream

❌ **ผิด:**
```
ทำงานร่วมกับ: Sales, Product, CS, Finance, IT, Brand, HR
```

✅ **ถูก:**
แยกเป็นตารางที่ระบุทิศทาง สิ่งที่แลกเปลี่ยน และความถี่ — Sales เป็น Downstream (รับ Lead), Product เป็น Upstream (ส่ง Brief)

**ผลกระทบ:** KEY_ACTIVITIES.md จะไม่สามารถระบุ Dependencies ที่ถูกต้องได้ เช่น ไม่รู้ว่าต้องรอ Product Brief ก่อนทำ Launch Campaign ทำให้ Timeline ผิดพลาด

---

### ข้อผิดพลาดที่ 4: Org Chart ไม่แสดง Peer Positions

❌ **ผิด:**
```
รายงานต่อ VP Marketing มีลูกน้อง 4 คน
```

✅ **ถูก:**
```
VP Marketing (นลิน พรรัตน์)
├── Digital Marketing Team Leader ← [วีรชัย]
│   ├── SEO Specialist (1)
│   └── ...
├── Brand & PR Manager (Peer)
└── Marketing Operations (Peer)
```

**ผลกระทบ:** ถ้าไม่เห็น Peer Positions KPI_CHARTER.md อาจตั้ง KPI ซ้อนกับ Brand & PR Manager เช่น ทั้งคู่ตั้ง Brand Awareness เป็น Primary ซึ่งจะสร้างความขัดแย้งใน Review
