<<<<<<< HEAD
# MyTCAS_Dashboard
=======
# โครงการวิเคราะห์ค่าเล่าเรียน TCAS

โปรเจกต์นี้จัดทำขึ้นเพื่อรวบรวมข้อมูลค่าเล่าเรียนของหลักสูตรที่เกี่ยวข้องกับคอมพิวเตอร์จากเว็บไซต์ https://course.mytcas.com แล้วนำข้อมูลมาแสดงผลในรูปแบบแดชบอร์ด เพื่อให้ผู้สนใจสามารถเปรียบเทียบและดูข้อมูลได้สะดวกขึ้น

scripts/
│ └── collect_fees.py # โค้ดสำหรับดึงข้อมูลจากเว็บไซต์
│
├── data/
│ └── tcas_results.xlsx # ไฟล์ข้อมูลที่ได้จากการดึงข้อมูล
│
├── dashboard/
│ └── dashboard.py # ไฟล์สำหรับแสดงผลด้วย Streamlit
│
└── README.md 


## วิธีใช้งาน

1. ติดตั้งไลบรารีที่จำเป็น
```bash
pip install pandas beautifulsoup4 requests streamlit openpyxl

โดยการใช้งานเริ่มจาก 
1.รันไฟล์เพื่อดึงข้อมูลจากเว็บไซต์ python scripts/collect_fees.py 
2.เปิดแดชบอร์ดเพื่อดูข้อมูล streamlit run dashboard/dashboard.py

เครื่องมือที่ใช้

Python 3
pandas
BeautifulSoup
Streamlit
ผู้จัดทำ

รหัสนักศึกษา: 6510110059
ชื่อ: จักรภัทร บูรณ์พงษ์ทอง


>>>>>>> ecdcf31 (เพิ่มโปรเจกต์ระบบเก็บค่าเล่าเรียนจาก MyTCAS)
