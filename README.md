# MyTCAS Dashboard

โปรเจกต์นี้เป็นระบบสำหรับดึงข้อมูลค่าเล่าเรียนจากเว็บไซต์ MyTCAS  
และแสดงผลข้อมูลผ่านแดชบอร์ดด้วย Streamlit  

---

## โครงสร้างไฟล์
scripts/
│ └── collect_fees.py # โค้ดสำหรับดึงข้อมูลจากเว็บไซต์ (scrapping)
│
├── data/
│ └── tcas_results.xlsx # ไฟล์ข้อมูลที่ได้จากการดึงข้อมูล (results)
│
├── dashboard/
│ └── dashboard.py # ไฟล์สำหรับแสดงผลด้วย Streamlit
│
└── README.md 


---

## วิธีใช้งาน

1. รันไฟล์เพื่อดึงข้อมูลจากเว็บไซต์  
   ```bash
   python scripts/collect_fees.py

เครื่องมือที่ใช้
Python 3
pandas
BeautifulSoup
Streamlit


ผู้จัดทำ
รหัสนักศึกษา: 6510110059
ชื่อ: จักรภัทร บูรณ์พงษ์ทอง
