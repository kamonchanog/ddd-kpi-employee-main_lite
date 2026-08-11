# คู่มือการเขียน KEY_ACTIVITIES.md

---

## 1. ภาพรวม

KEY_ACTIVITIES.md คือเอกสารปิดท้ายของ DDD-KPI Employee Edition ทำหน้าที่แปลง Key Results ให้กลายเป็นแผนปฏิบัติการที่เป็นรูปธรรม โดยจัดกิจกรรมตาม 3 เดือนของไตรมาส (Month 1/2/3) แต่ละกิจกรรมระบุ KR ที่รองรับ, เจ้าของ (Owner), Deadline, Effort ในหน่วย Man-Day (MD), และ Dependency เอกสารนี้ยังครอบคลุม Activity-KR Mapping เพื่อพิสูจน์ว่าไม่มี KR ใดถูกทิ้งไว้โดยไม่มีกิจกรรมรองรับ และ Dependencies & Risks ที่ระบุ Top 3 Risks พร้อม Probability/Impact Rating และ Mitigation Plan

- **depends_on:** KEY_RESULTS.md
- **downstream:** ไม่มี (เป็น leaf document)
- **ผู้เขียน:** พนักงาน (ต้องมี KEY_RESULTS.md ที่ Approved แล้ว)
- **ผู้อ่าน:** พนักงาน, ผู้จัดการ, และ Peer ที่เป็น Dependency
- **Output ที่คาดหวัง:** แผนกิจกรรม 3 เดือนที่ครอบคลุมทุก KR พร้อม Dependency Map และ Risk Register ที่ใช้ได้จริง

**Dependency Diagram:**

```
[KEY_RESULTS.md]
      |
      v
+--------------------+
|  KEY_ACTIVITIES.md |  <-- คุณอยู่ที่นี่ (leaf document)
+--------------------+
      |
   (ไม่มี downstream — นำไปปฏิบัติจริง)
```

**Priority: P0**

---

## 2. ก่อนเริ่มเขียน (Prerequisites)

1. อ่าน KEY_RESULTS.md ให้ครบ — สร้าง List ของ KR ID ทั้งหมดและ Deadline ของแต่ละตัว
2. แยก KR ออกเป็น Lead KR (ต้องทำกิจกรรมต้น Quarter) และ Lag KR (ผลปลาย Quarter แต่กิจกรรมต้องเริ่มต้น Quarter)
3. ระบุ Dependency ของแต่ละกิจกรรมก่อน — กิจกรรมใดต้องรอใคร หรือรอทรัพยากรอะไร
4. ประเมิน Effort (MD = Man-Day = วันทำงานของ 1 คน 8 ชั่วโมง) อย่างสมเหตุสมผล — ห้ามใส่ Effort ต่ำเกินจริง
5. Month 1 (ก.ค.) ต้องเป็นกิจกรรม Foundational เช่น วางแผน, Setup เครื่องมือ, รวบรวมข้อมูล ห้ามใส่ Final Deliverable ใน Month 1
6. ทำ Coverage Check — เขียน Mapping ว่า KR แต่ละตัวมีกิจกรรมรองรับกี่ข้อ ก่อน Finalize
7. ระบุ Top 3 Risks ที่อาจทำให้ KR ล้มเหลว พร้อม Probability (H/M/L) และ Impact (H/M/L)

---

## 3. วิธีเขียนทีละ Section

### Month 1 Activities (กิจกรรมเดือน 1)

**วัตถุประสงค์:** วางรากฐานสำหรับ Quarter ทั้งหมด — ต้องเป็นกิจกรรม Setup, Planning, และ Baseline Measurement

**วิธีเขียน:** ใช้ตาราง 7 คอลัมน์: Activity ID / Activity Description / KR Support / Owner / Deadline / Effort (MD) / Dependency แยกกลุ่มกิจกรรมตาม Cluster (เช่น Paid Media, SEO, People)

**ตัวอย่างที่ดี:**

```markdown
## Month 1 Activities (กรกฎาคม 2026)
**Theme:** วางรากฐาน — Setup, Onboard, และ Baseline

| Act ID | กิจกรรม | KR Support | Owner | Deadline | Effort (MD) | Dependency |
|--------|---------|------------|-------|----------|------------|------------|
| A1-01 | จัดทำ Q3 Campaign Brief และ Channel Plan ฉบับสมบูรณ์ | KR-01-A, KR-01-B, KR-02-A | วีรชัย | 5 ก.ค. | 2 MD | — |
| A1-02 | Onboard Content Specialist ใหม่ + มอบหมายงาน Content Calendar | KR-03-C, KR-05-B | วีรชัย | 7 ก.ค. | 1 MD | รมย์ สิริมงคล เริ่มงาน 1 ก.ค. |
| A1-03 | Setup A/B Test บน Landing Page หลัก 3 หน้า (Homepage, Pricing, Blog CTA) | KR-01-A | กานต์ + ปริม | 15 ก.ค. | 3 MD | IT Tracking Setup |
| A1-04 | รวบรวม Baseline Data ทุก KR (GA4, HubSpot, SEMrush) | ทุก KR | ปริม วงศ์ทอง | 10 ก.ค. | 1 MD | Tool Access |
| A1-05 | จัดทำ Individual Development Plan (IDP) กับสมาชิก 4 คน | KR-05-B | วีรชัย | 15 ก.ค. | 2 MD | — |
| A1-06 | ทำ Keyword Research + SEO Content Plan Q3 (9 บทความ) | KR-03-B, KR-03-C | ปริม วงศ์ทอง | 10 ก.ค. | 2 MD | — |
| A1-07 | ประชุม Sales-Marketing SLA Review — ตกลง MQL Criteria ใหม่ | KR-01-D | วีรชัย + Sales | 20 ก.ค. | 0.5 MD | ธนา วิชัย (Sales) |
| A1-08 | Launch Paid Campaign Q3 Wave 1 (Google + Meta) | KR-01-B, KR-02-A | กานต์ ชัยกุล | 8 ก.ค. | 1.5 MD | A1-01 |
```

**ตัวอย่างที่ผิด ❌:**

```markdown
## Month 1 Activities

- ส่งแคมเปญ Q3 ทั้งหมด ✓
- ปิด Lead 90 ตัว ✓
- ทำ Content 9 ชิ้น ✓
```

**เหตุผลที่ผิด:** Month 1 ไม่ใช่เวลาสำหรับ Final Deliverable ทั้งหมด การ "ปิด Lead 90 ตัว" ใน ก.ค. เพียงเดือนเดียวเป็นไปไม่ได้ในทางปฏิบัติ และไม่มี Owner, Effort, หรือ Dependency

---

### Month 2 Activities (กิจกรรมเดือน 2)

**วัตถุประสงค์:** ดำเนินการหลัก (Execution) และ Optimize จากผลลัพธ์ Month 1 — เป็นเดือนที่สร้าง Momentum มากที่สุด

**วิธีเขียน:** เช่นเดียวกับ Month 1 แต่กิจกรรมควรเป็น Execution, Optimization, และ Mid-Quarter Review

**ตัวอย่างที่ดี:**

```markdown
## Month 2 Activities (สิงหาคม 2026)
**Theme:** Execute & Optimize — ดำเนินการและปรับแต่ง

| Act ID | กิจกรรม | KR Support | Owner | Deadline | Effort (MD) | Dependency |
|--------|---------|------------|-------|----------|------------|------------|
| A2-01 | วิเคราะห์ผล A/B Test Wave 1 และ Implement Winning Variant | KR-01-A | กานต์ + ปริม | 10 ส.ค. | 1.5 MD | A1-03 ครบ 3 สัปดาห์ |
| A2-02 | Publish SEO Blog Posts ชุดแรก 4 บทความ | KR-03-C | แพร + รมย์ | 20 ส.ค. | 4 MD | A1-06 Approved |
| A2-03 | ปรับ Paid Campaign Targeting ตาม M1 Performance Data | KR-01-B, KR-02-A | กานต์ ชัยกุล | 7 ส.ค. | 1 MD | A2-01 |
| A2-04 | Launch Product Launch Campaign (Performance Module v2.0) | KR-01-B, KR-04-A | วีรชัย + กานต์ | 28 ก.ค. | 3 MD | Product Brief จาก ชนิดา |
| A2-05 | Mid-Quarter KR Review กับ Manager (31 ส.ค.) | ทุก KR | วีรชัย | 31 ส.ค. | 0.5 MD | Data Export HubSpot |
| A2-06 | ปิด Budget Low-ROI Channels และ Reallocate | KR-04-B | วีรชัย + กานต์ | 15 ส.ค. | 1 MD | A2-03 |
| A2-07 | เตรียม Manual Export Backup ก่อน HubSpot Migration | ทุก KR | วีรชัย | 22 ส.ค. | 1 MD | แจ้ง IT Migration Date |
| A2-08 | จัด 1-on-1 สำหรับสมาชิกทั้ง 4 คน (รอบ ส.ค.) | KR-05-A, KR-05-C | วีรชัย | 29 ส.ค. | 2 MD | IDP ใน A1-05 |
```

**ตัวอย่างที่ผิด ❌:**

```markdown
## Month 2 Activities

- ทำเหมือน Month 1 แต่มากขึ้น
- รอดูผลก่อนแล้วค่อยตัดสินใจ
```

**เหตุผลที่ผิด:** "รอดูผลก่อน" ไม่ใช่กิจกรรม และ "ทำเหมือน Month 1" แสดงว่าไม่ได้วางแผน Optimization ซึ่งเป็นหัวใจของ Month 2

---

### Month 3 Activities (กิจกรรมเดือน 3)

**วัตถุประสงค์:** Finalize Deliverables, รวบรวมหลักฐาน, และเตรียม Quarter-End Review

**วิธีเขียน:** กิจกรรม Month 3 ต้องเน้น Closing, Reporting, และ Evidence Collection ไม่ใช่เริ่ม Initiative ใหม่ขนาดใหญ่

**ตัวอย่างที่ดี:**

```markdown
## Month 3 Activities (กันยายน 2026)
**Theme:** Finalize & Close — ปิด KR และเตรียม Review

| Act ID | กิจกรรม | KR Support | Owner | Deadline | Effort (MD) | Dependency |
|--------|---------|------------|-------|----------|------------|------------|
| A3-01 | Publish SEO Blog Posts ชุดที่ 2-3 รวม 5 บทความที่เหลือ | KR-03-C | แพร + รมย์ | 20 ก.ย. | 5 MD | A2-02 |
| A3-02 | Final Campaign Push — เพิ่ม Budget 10% ใน Top Channels | KR-01-B, KR-02-A | กานต์ ชัยกุล | 15 ก.ย. | 0.5 MD | M2 Performance Data |
| A3-03 | Export และ Archive ข้อมูล KR ทุกตัว (Final Snapshot) | ทุก KR | วีรชัย | 27 ก.ย. | 1 MD | HubSpot Migration เสร็จ |
| A3-04 | รวบรวมผล Sales Rejection Rate รายเดือน + สรุป Q3 | KR-01-D | วีรชัย + Sales | 28 ก.ย. | 0.5 MD | ธนา วิชัย (Sales) |
| A3-05 | จัด 1-on-1 รอบ ก.ย. พร้อมรวบรวม Development Score | KR-05-A, KR-05-C | วีรชัย | 26 ก.ย. | 2 MD | — |
| A3-06 | จัดทำ Q3 Performance Summary Deck สำหรับ Manager Review | ทุก KR | วีรชัย | 29 ก.ย. | 2 MD | A3-03 |
| A3-07 | Final KR Review กับ Manager (Quarter-End) | ทุก KR | วีรชัย + นลิน | 30 ก.ย. | 1 MD | A3-06 |
```

**ตัวอย่างที่ผิด ❌:**

```markdown
## Month 3 Activities

- เริ่ม Rebranding Campaign ใหม่
- ออกแบบ Website ใหม่ทั้งหมด
- วางแผน Q4 Strategy
```

**เหตุผลที่ผิด:** ทุกกิจกรรมเป็นการเริ่มต้นใหม่ ไม่มีกิจกรรมที่ Finalize KR ที่มีอยู่ — การ Rebranding ใน Month 3 ของ Quarter จะไม่มีผลต่อ KR ปัจจุบัน และจะรบกวน Execution ที่ต้องปิดให้เสร็จ

---

### Activity-KR Mapping

**วัตถุประสงค์:** พิสูจน์ว่าทุก KR มีกิจกรรมรองรับ และไม่มี KR ใดถูกทิ้งไว้โดยไม่มีแผน

**วิธีเขียน:** ใช้ตาราง Matrix หรือ List ที่แสดง KR ID → Activity IDs ที่รองรับ พร้อม Coverage Status

**ตัวอย่างที่ดี:**

```markdown
## Activity-KR Mapping

| KR ID | KR Statement (ย่อ) | Activity IDs | Coverage |
|-------|-------------------|--------------|---------|
| KR-01-A | Landing Page Conversion Rate 3.0% | A1-03, A2-01 | ✓ Covered |
| KR-01-B | MQL Paid ≥ 90 | A1-08, A2-03, A2-04, A3-02 | ✓ Covered |
| KR-01-C | MQL Organic ≥ 70 | A1-06, A2-02, A3-01 | ✓ Covered |
| KR-01-D | Sales Rejection Rate ≤ 15% | A1-07, A3-04 | ✓ Covered |
| KR-02-A | CPL ≤ 330 THB | A1-08, A2-03, A3-02 | ✓ Covered |
| KR-02-B | Lead-to-Customer ≥ 4.5% | A1-07, A2-03 | ✓ Covered |
| KR-02-C | Budget Variance ≤ ±5% | A2-06, A3-03 | ✓ Covered |
| KR-03-A | Organic Sessions 33,000/month | A1-06, A2-02, A3-01 | ✓ Covered |
| KR-03-B | Top 10 Keywords 70 | A1-06, A2-02 | ✓ Covered |
| KR-03-C | Blog Posts 9 ชิ้น | A2-02, A3-01 | ✓ Covered |
| KR-04-A | Attributed Revenue 1.44M THB | A2-04, A3-02 | ✓ Covered |
| KR-04-B | Low-ROI Spend ≤ 30% | A2-06 | ⚠ Single Activity — ติดตามใกล้ชิด |
| KR-05-A | 1-on-1 Completion ≥ 90% | A1-02, A2-08, A3-05 | ✓ Covered |
| KR-05-B | IDP Completion 4 คน | A1-02, A1-05 | ✓ Covered |
| KR-05-C | Avg Dev Score ≥ 4.0 | A2-08, A3-05 | ✓ Covered |

**KR ที่มี Single Activity Coverage (ต้องติดตามพิเศษ):**
- KR-04-B: มีแค่ A2-06 รองรับ — ถ้า A2-06 ล่าช้า KR นี้จะไม่มีแผน Backup
```

**ตัวอย่างที่ผิด ❌:**

```markdown
## Activity-KR Mapping

ทุก Activity รองรับ KR ทั้งหมด
```

**เหตุผลที่ผิด:** ไม่มี Mapping จริง ไม่รู้ว่า KR ตัวไหนขาด Coverage — ถ้าไม่ตรวจก็ไม่รู้ว่ามี KR ที่ถูกลืม

---

### Dependencies & Risks

**วัตถุประสงค์:** ระบุ External Dependencies และ Top 3 Risks ที่อาจทำให้ KR ล้มเหลว พร้อม Mitigation Plan

**วิธีเขียน:** แบ่งเป็น 2 ส่วน: (1) External Dependencies ที่ต้องติดตาม (2) Risk Register ด้วยตาราง: Risk / Probability / Impact / Mitigation

**ตัวอย่างที่ดี:**

```markdown
## Dependencies & Risks

### External Dependencies ที่ต้องติดตาม

| Dependency | เกี่ยวกับ KR | ต้องพร้อมเมื่อ | ผู้ประสาน |
|-----------|-------------|---------------|----------|
| Product Brief (Performance Module v2.0) | KR-01-B, KR-04-A | 20 ก.ค. | ชนิดา สุวรรณ (PM) |
| Sales-Marketing SLA ที่ตกลงร่วมกัน | KR-01-D | 20 ก.ค. | ธนา วิชัย (Sales Lead) |
| HubSpot Migration Date (IT) | ทุก Lag KR | ภายใน ส.ค. | อนุพร เตชะ (IT/Ops) |
| LinkedIn Ads Account Upgrade (Tier ใหม่) | KR-01-B, KR-02-A | 7 ก.ค. | กานต์ ชัยกุล + Finance |

---

### Risk Register — Top 3 Risks

| # | Risk | Probability | Impact | Risk Level | Mitigation Plan |
|---|------|-------------|--------|------------|----------------|
| R-01 | HubSpot Migration ล่าช้า / Data Loss ทำให้รายงาน KR ไม่ได้ | M | H | HIGH | เตรียม Manual Export Backup (A2-07) ก่อน Migration; ตั้ง Alert กับ IT 2 สัปดาห์ล่วงหน้า |
| R-02 | Content Specialist ใหม่ Ramp-up ช้ากว่า 3 สัปดาห์ ทำให้ Blog Posts ล่าช้า | M | M | MEDIUM | วีรชัยเขียน 2 บทความแรกเองในกรณีฉุกเฉิน; Freelance Writer Backup รายชื่อพร้อม |
| R-03 | Product Launch Campaign ของ Performance Module v2.0 ล่าช้า | L | H | MEDIUM | Campaign Brief ออกแบบให้ Launch ได้อิสระจาก Product — ถ้า Product ล่าช้า ใช้ "Coming Soon" Campaign แทน |
```

**ตัวอย่างที่ผิด ❌:**

```markdown
## Risk

- อาจมีความเสี่ยงด้านงบประมาณ
- ทีมอาจทำงานหนักเกินไป
- เครื่องมืออาจมีปัญหา
```

**เหตุผลที่ผิด:** Risk คลุมเครือ ไม่มี Probability/Impact Rating และไม่มี Mitigation Plan — ไม่สามารถใช้เป็นแนวทางปฏิบัติได้เมื่อ Risk เกิดขึ้นจริง

---

## 4. ตัวอย่างเต็ม

> **พนักงาน:** วีรชัย อินทรสุวรรณ | **ตำแหน่ง:** Digital Marketing Team Leader | **ทีม:** Marketing & Growth | **ไตรมาส:** Q3/2026

```markdown
# KEY_ACTIVITIES.md
**Employee:** วีรชัย อินทรสุวรรณ | **Role:** Digital Marketing Team Leader
**Department:** Marketing & Growth | **Quarter:** Q3/2026 (ก.ค.–ก.ย. 2569)
**Created:** 2026-06-30 | **Version:** 1.0 | **Depends on:** KEY_RESULTS.md v1.0

---

## Month 1 Activities (กรกฎาคม 2026)
**Theme:** วางรากฐาน — Setup, Plan, Baseline
**Total Effort: ~17.5 MD**

| Act ID | กิจกรรม | KR Support | Owner | Deadline | Effort (MD) | Dependency |
|--------|---------|------------|-------|----------|------------|------------|
| A1-01 | จัดทำ Q3 Campaign Brief + Channel Plan ฉบับสมบูรณ์ | KR-01-A, KR-01-B, KR-02-A | วีรชัย | 5 ก.ค. | 2 | — |
| A1-02 | Onboard Content Specialist ใหม่ (รมย์) + มอบหมาย Content Calendar | KR-03-C, KR-05-B | วีรชัย | 7 ก.ค. | 1 | รมย์ เริ่มงาน 1 ก.ค. |
| A1-03 | Setup A/B Test Landing Pages (Homepage, Pricing, Blog CTA) | KR-01-A | กานต์ + ปริม | 15 ก.ค. | 3 | IT Tracking Setup |
| A1-04 | รวบรวม Q3 Baseline Data ทุก KR จาก GA4 / HubSpot / SEMrush | ทุก KR | ปริม วงศ์ทอง | 10 ก.ค. | 1 | Tool Access |
| A1-05 | จัดทำ Individual Development Plan (IDP) กับสมาชิก 4 คน | KR-05-B, KR-05-C | วีรชัย | 15 ก.ค. | 2 | — |
| A1-06 | Keyword Research + SEO Content Plan Q3 (9 บทความ) | KR-03-B, KR-03-C | ปริม วงศ์ทอง | 10 ก.ค. | 2 | — |
| A1-07 | Sales-Marketing SLA Workshop: ตกลง MQL Criteria ใหม่ | KR-01-D, KR-02-B | วีรชัย | 20 ก.ค. | 0.5 | ธนา วิชัย พร้อม |
| A1-08 | Launch Paid Campaign Q3 Wave 1 (Google Ads + Meta) | KR-01-B, KR-02-A | กานต์ ชัยกุล | 8 ก.ค. | 1.5 | A1-01 |
| A1-09 | Setup LinkedIn Ads Campaign สำหรับ Enterprise Segment | KR-01-B, KR-02-A | กานต์ ชัยกุล | 12 ก.ค. | 1 | Account Upgrade |
| A1-10 | จัด 1-on-1 รอบ ก.ค. กับสมาชิกทั้ง 4 คน | KR-05-A, KR-05-C | วีรชัย | 25 ก.ค. | 2 | IDP A1-05 |
| A1-11 | ประสานงาน Product Team ขอ Launch Brief (Performance Module v2.0) | KR-01-B, KR-04-A | วีรชัย | 20 ก.ค. | 0.5 | ชนิดา สุวรรณ (PM) |

---

## Month 2 Activities (สิงหาคม 2026)
**Theme:** Execute & Optimize — ดำเนินการหลักและปรับปรุง
**Total Effort: ~17 MD**

| Act ID | กิจกรรม | KR Support | Owner | Deadline | Effort (MD) | Dependency |
|--------|---------|------------|-------|----------|------------|------------|
| A2-01 | วิเคราะห์ A/B Test Wave 1 + Implement Winning Variant | KR-01-A | กานต์ + ปริม | 10 ส.ค. | 1.5 | A1-03 (3 สัปดาห์ Run) |
| A2-02 | Publish SEO Blog Posts ชุดแรก 4 บทความ (รมย์ + แพร) | KR-03-A, KR-03-C | แพร + รมย์ | 20 ส.ค. | 4 | A1-06 Approved |
| A2-03 | ปรับ Paid Campaign Targeting + Bidding ตาม M1 Data | KR-01-B, KR-02-A | กานต์ ชัยกุล | 7 ส.ค. | 1 | M1 Performance Data |
| A2-04 | Launch Product Launch Campaign: Ragnar Performance v2.0 | KR-01-B, KR-04-A | วีรชัย + กานต์ | 28 ก.ค. | 3 | A1-11 Brief Ready |
| A2-05 | Mid-Quarter KR Review Meeting กับ Manager | ทุก KR | วีรชัย | 31 ส.ค. | 0.5 | HubSpot Export Ready |
| A2-06 | ปิด / ลด Budget Low-ROI Channels + Reallocate | KR-04-B | วีรชัย + กานต์ | 15 ส.ค. | 1 | A2-03 |
| A2-07 | เตรียม Manual Export Backup ก่อน HubSpot Migration (25 ส.ค.) | ทุก Lag KR | วีรชัย | 22 ส.ค. | 1 | IT แจ้ง Migration Date |
| A2-08 | จัด 1-on-1 รอบ ส.ค. + Update IDP Progress | KR-05-A, KR-05-C | วีรชัย | 29 ส.ค. | 2 | IDP A1-05 |
| A2-09 | Email Nurture Campaign: ส่ง Lead Magnet (ebook) ถึง Cold MQL | KR-01-C | แพร มาลีวรรณ | 18 ส.ค. | 2 | A1-06 Content |
| A2-10 | SEMrush Position Check + Technical SEO Audit ครึ่งปี | KR-03-B | ปริม วงศ์ทอง | 25 ส.ค. | 1 | — |

---

## Month 3 Activities (กันยายน 2026)
**Theme:** Finalize & Close — ปิด KR และเตรียม Quarter-End Review
**Total Effort: ~15.5 MD**

| Act ID | กิจกรรม | KR Support | Owner | Deadline | Effort (MD) | Dependency |
|--------|---------|------------|-------|----------|------------|------------|
| A3-01 | Publish SEO Blog Posts ชุด 2 (5 บทความที่เหลือ) | KR-03-A, KR-03-C | แพร + รมย์ | 20 ก.ย. | 5 | A2-02 Draft Ready |
| A3-02 | Final Campaign Push — เพิ่ม Budget 10% ใน Top-ROI Channels | KR-01-B, KR-02-A | กานต์ ชัยกุล | 15 ก.ย. | 0.5 | M2 ROI Data |
| A3-03 | Export และ Archive ข้อมูล KR Final Snapshot (HubSpot + GA4 + Ads) | ทุก KR | วีรชัย | 27 ก.ย. | 1.5 | HubSpot Migration เสร็จ |
| A3-04 | รวบรวม Sales Rejection Report Q3 + Debrief กับ Sales Team | KR-01-D | วีรชัย | 28 ก.ย. | 0.5 | ธนา วิชัย |
| A3-05 | จัด 1-on-1 รอบ ก.ย. + รวบรวม Development Score Final | KR-05-A, KR-05-C | วีรชัย | 26 ก.ย. | 2 | — |
| A3-06 | จัดทำ Q3 Performance Summary Deck (KR Actuals + Learnings) | ทุก KR | วีรชัย | 29 ก.ย. | 2.5 | A3-03 |
| A3-07 | Final KR Review + Quarter-End Score กับ Manager | ทุก KR | วีรชัย + นลิน | 30 ก.ย. | 1 | A3-06 |
| A3-08 | สรุป A/B Test Learnings สำหรับ Q4 Planning | KR-01-A | ปริม + กานต์ | 28 ก.ย. | 1 | — |
| A3-09 | Submit Q3 KPI Score ผ่านระบบ PMS | ทุก KR | วีรชัย | 30 ก.ย. | 0.5 | A3-07 Approved |

---

## Activity-KR Mapping

| KR ID | KR (ย่อ) | Activities | Coverage |
|-------|---------|------------|---------|
| KR-01-A | Conversion Rate 3.0% | A1-03, A2-01, A3-08 | ✓ |
| KR-01-B | MQL Paid 90 | A1-08, A1-09, A2-03, A2-04, A3-02 | ✓ |
| KR-01-C | MQL Organic 70 | A1-06, A2-02, A2-09, A3-01 | ✓ |
| KR-01-D | Rejection Rate ≤ 15% | A1-07, A3-04 | ✓ |
| KR-02-A | CPL ≤ 330 THB | A1-08, A1-09, A2-03, A3-02 | ✓ |
| KR-02-B | Lead-to-Customer ≥ 4.5% | A1-07, A2-03 | ✓ |
| KR-02-C | Budget Variance ≤ ±5% | A2-06, A3-03 | ✓ |
| KR-03-A | Organic Sessions 33,000 | A1-06, A2-02, A2-10, A3-01 | ✓ |
| KR-03-B | Top 10 Keywords 70 | A1-06, A2-10 | ✓ |
| KR-03-C | Blog Posts 9 ชิ้น | A2-02, A3-01 | ✓ (4+5) |
| KR-04-A | Attributed Revenue 1.44M | A2-04, A3-02 | ✓ |
| KR-04-B | Low-ROI Spend ≤ 30% | A2-06 | ⚠ Single |
| KR-05-A | 1-on-1 Completion ≥ 90% | A1-10, A2-08, A3-05 | ✓ |
| KR-05-B | IDP 4 คน | A1-02, A1-05 | ✓ |
| KR-05-C | Avg Dev Score 4.0 | A1-10, A2-08, A3-05 | ✓ |

---

## Dependencies & Risks

### External Dependencies

| Dependency | KR ที่เกี่ยวข้อง | ต้องพร้อมเมื่อ | ผู้ประสาน | สถานะ |
|-----------|----------------|---------------|----------|--------|
| Product Brief: Performance Module v2.0 | KR-01-B, KR-04-A | 20 ก.ค. | ชนิดา สุวรรณ (PM) | รอยืนยัน |
| Sales-Marketing SLA Revision | KR-01-D, KR-02-B | 20 ก.ค. | ธนา วิชัย (Sales) | Pending |
| HubSpot Migration Date (IT) | ทุก Lag KR | ยืนยันก่อน 15 ส.ค. | อนุพร เตชะ (IT) | รอ IT |
| LinkedIn Ads Tier Upgrade Approval | KR-01-B, KR-02-A | 5 ก.ค. | กานต์ + Finance | Approved |

### Risk Register — Top 3 Risks

| # | Risk | P | I | Level | Mitigation |
|---|------|---|---|-------|------------|
| R-01 | HubSpot Migration ทำให้ Data Loss / Report หาย | M | H | HIGH | A2-07: Manual Export ก่อน Migration; ตั้ง Alert กับ IT 14 วันล่วงหน้า; มี Backup Google Sheet |
| R-02 | Content Specialist ใหม่ Ramp-up ช้า Blog Posts ล่าช้า | M | M | MEDIUM | วีรชัยเขียน Backup 2 บทความเอง; มี Freelance Writer Backup 1 คน (กานดา พรหม) พร้อมรับงาน |
| R-03 | Product v2.0 Launch ล่าช้า → Campaign Brief ไม่มี | L | H | MEDIUM | ออกแบบ Campaign ให้ Launch ได้อิสระ; ถ้าล่าช้า ใช้ "Coming Soon" Campaign แทน — ปรับ Brief ใน A2-04 |

**P = Probability: H=High M=Medium L=Low**
**I = Impact: H=High M=Medium L=Low**
```

---

## 5. Validation Checklist

**โครงสร้างและ Header:**
- [ ] ระบุ Quarter และ Year ใน Header
- [ ] ระบุ Depends on KEY_RESULTS.md version

**Month 1 Activities:**
- [ ] กิจกรรม Month 1 เป็น Foundational (Setup/Plan/Baseline) ไม่ใช่ Final Deliverable
- [ ] ทุกกิจกรรมมี Activity ID (A1-XX)
- [ ] ทุกกิจกรรมมี Owner ที่เฉพาะเจาะจง (ไม่ใช่ "ทีม")
- [ ] ทุกกิจกรรมมี Deadline ที่อยู่ในเดือน ก.ค.
- [ ] ทุกกิจกรรมระบุ Effort (MD) และ Dependency

**Month 2 Activities:**
- [ ] กิจกรรม Month 2 เป็น Execution และ Optimization
- [ ] มีกิจกรรม Mid-Quarter Review
- [ ] Activity ที่ Depend on Month 1 ระบุ Dependency ID ชัดเจน

**Month 3 Activities:**
- [ ] กิจกรรม Month 3 เน้น Finalize, Archive, และ Review
- [ ] มีกิจกรรม Final KR Review กับ Manager
- [ ] มีกิจกรรม Submit Score ผ่านระบบ PMS
- [ ] Deadline ทุกกิจกรรม ≤ 30 ก.ย. 2026

**Activity-KR Mapping:**
- [ ] ทุก KR จาก KEY_RESULTS.md มีอยู่ในตาราง Mapping
- [ ] ไม่มี KR ที่ Coverage = ไม่มี Activity เลย
- [ ] KR ที่มี Single Activity ถูก Flag ⚠ และมีแผน Monitor

**Dependencies & Risks:**
- [ ] ระบุ External Dependencies ที่อยู่นอกการควบคุมของพนักงาน
- [ ] มี Risk Register อย่างน้อย 3 Risks
- [ ] ทุก Risk มี Probability, Impact, และ Mitigation Plan
- [ ] Mitigation Plan ผูกกับ Activity ID ที่มีอยู่จริง

**Cross-reference กับ KEY_RESULTS.md:**
- [ ] Activity-KR Mapping ครอบคลุม KR ทุกตัวจาก KEY_RESULTS.md
- [ ] Deadline ของ Activity ที่รองรับ Lag KR ≤ Deadline ของ KR นั้น

---

## 6. ข้อผิดพลาดที่พบบ่อย

### ข้อผิดพลาดที่ 1: Month 1 เต็มไปด้วย Final Deliverables

❌ **ผิด:**
```
| A1-01 | ปิด MQL 90 ตัว ภายใน ก.ค. | KR-01-B | วีรชัย | 31 ก.ค. | — |
| A1-02 | Publish Blog Posts ครบ 9 ชิ้น | KR-03-C | แพร | 31 ก.ค. | — |
```

✅ **ถูก:**
Month 1 ควรเป็น A1-06 "Keyword Research + SEO Content Plan" (เตรียม) ไม่ใช่ A1-02 "Publish ครบ 9 ชิ้น" (ผลลัพธ์สุดท้าย)

**ผลกระทบ:** ถ้าบีบ Final Deliverable ทั้งหมดไปไว้ Month 1 จะทำให้แผน Unrealistic และเมื่อไม่ได้ตาม Plan จะไม่รู้ว่าต้อง Adjust อะไรใน Month 2-3

---

### ข้อผิดพลาดที่ 2: Activity-KR Mapping ไม่ครบ

❌ **ผิด:**
```
Activity-KR Mapping:
- A1-01 → KR-01-A
- A1-02 → KR-03-C
(ไม่ได้ Map KR-04-B, KR-02-C ไว้เลย)
```

✅ **ถูก:** ทำ Mapping เป็นตาราง โดยเริ่มจาก KR ทุกตัวก่อน แล้วหา Activity ที่รองรับ ไม่ใช่เริ่มจาก Activity แล้วระบุว่า Support KR ไหน (ทำให้ KR ที่ไม่มี Activity หลุดออกไป)

**ผลกระทบ:** KR ที่ไม่มี Activity จะถูกลืมจนกว่าจะถึง M2 หรือ M3 Review — เมื่อถึงตอนนั้นก็ไม่มีเวลาแก้ไข

---

### ข้อผิดพลาดที่ 3: Risk ไม่มี Mitigation ที่ปฏิบัติได้

❌ **ผิด:**
```
R-01: ถ้า HubSpot มีปัญหา จะแก้ไขตามสถานการณ์
```

✅ **ถูก:**
```
R-01: HubSpot Migration ทำให้ Data Loss | P: M | I: H
Mitigation: A2-07 เตรียม Manual Export 22 ส.ค. + ตั้ง IT Alert 14 วันล่วงหน้า + Backup Google Sheet
```

**ผลกระทบ:** "แก้ตามสถานการณ์" ไม่ใช่แผน — เมื่อ Risk เกิดขึ้นจริงจะเสียเวลาคิดในสถานการณ์กดดัน ทำให้แก้ช้าและ KR ได้รับผลกระทบ

---

### ข้อผิดพลาดที่ 4: Owner ของ Activity ไม่ชัดเจน

❌ **ผิด:**
```
| A2-04 | Launch Product Campaign | KR-01-B | Marketing Team | 28 ก.ค. | — |
```

✅ **ถูก:**
```
| A2-04 | Launch Product Campaign | KR-01-B | วีรชัย + กานต์ | 28 ก.ค. | 3 MD | A1-11 Brief Ready |
```
ระบุชื่อ Primary Owner 1 คน + Supporter ได้ แต่ต้องมีคนรับผิดชอบหลักที่ชัดเจน

**ผลกระทบ:** ถ้า Owner คือ "ทีม" ทุกคนจะคิดว่าคนอื่นทำ (Diffusion of Responsibility) — Activity จะถูกทิ้งจนถึง Deadline
