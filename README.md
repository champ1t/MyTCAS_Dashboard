
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

โดยการใช้งานเริ่มจาก 
1.รันไฟล์เพื่อดึงข้อมูลจากเว็บไซต์ python scripts/collect_fees.py 
2.เปิดแดชบอร์ดเพื่อดูข้อมูล streamlit run dashboard/dashboard.py

เครื่องมือที่ใช้
-Python 3
-pandas
-BeautifulSoup
-Streamlit

ผู้จัดทำ
รหัสนักศึกษา: 6510110059
ชื่อ: จักรภัทร บูรณ์พงษ์ทอง

ไลบรารีที่จำเป็น
```bash
pip install pandas beautifulsoup4 requests streamlit openpyxl 



