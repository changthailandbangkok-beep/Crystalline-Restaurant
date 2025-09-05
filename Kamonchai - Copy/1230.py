# ฟังก์ชันสำหรับคำนวณรายได้ของพนักงาน
def calculate_income(name_employ, personal_number, address_employ, employ_number,
                     dept_employ, age_employ, tel_number, salary, total_hours_worked):
    
    # ชั่วโมงทำงานปกติใน 25 วัน = 25*8 = 200 ชั่วโมง
    normal_hours = 25 * 8
    hrs_ot = max(0, total_hours_worked - normal_hours)  # OT ถ้าทำเกิน 200 ชม.
    ot_money = hrs_ot * 50
    all_money = salary + ot_money
    social_sec = salary * 0.05
    net_income = all_money - social_sec

    # แสดงผลข้อมูล
    print("========== ข้อมูลพนักงาน ==========")
    print(f"ชื่อ: {name_employ}")
    print(f"รหัสประจำตัวประชาชน: {personal_number}")
    print(f"ที่อยู่: {address_employ}")
    print(f"รหัสพนักงาน: {employ_number}")
    print(f"แผนก: {dept_employ}")
    print(f"อายุ: {age_employ}")
    print(f"เบอร์โทร: {tel_number}")
    print(f"เงินเดือน: {salary:.2f} บาท")
    print(f"จำนวนชั่วโมงทำงานทั้งหมด: {total_hours_worked} ชั่วโมง")
    print(f"จำนวนชั่วโมง OT: {hrs_ot} ชั่วโมง")
    print(f"ค่าล่วงเวลา OT: {ot_money:.2f} บาท")
    print(f"รายได้รวม: {all_money:.2f} บาท")
    print(f"เงินประกันสังคม (5%): {social_sec:.2f} บาท")
    print(f"รายได้สุทธิ: {net_income:.2f} บาท")
    print("====================================\n")


# ตัวอย่างข้อมูลพนักงาน 3 คน
employees = [
    {
        "name_employ": "สมชาย ใจดี",
        "personal_number": "1234567890123",
        "address_employ": "123 ถนนสุขใจ กรุงเทพฯ",
        "employ_number": "EMP001",
        "dept_employ": "แคชเชียร์",
        "age_employ": 28,
        "tel_number": "0812345678",
        "salary": 15000,
        "total_hours_worked": 210  # ทำเกิน 10 ชม.
    },
    {
        "name_employ": "สมหญิง ใจงาม",
        "personal_number": "2345678901234",
        "address_employ": "456 ถนนพระราม2 กรุงเทพฯ",
        "employ_number": "EMP002",
        "dept_employ": "จัดสินค้า",
        "age_employ": 32,
        "tel_number": "0898765432",
        "salary": 16500,
        "total_hours_worked": 198  # ไม่ถึงเกณฑ์ OT
    },
    {
        "name_employ": "วิชัย แรงดี",
        "personal_number": "3456789012345",
        "address_employ": "789 ซอยดินแดง กรุงเทพฯ",
        "employ_number": "EMP003",
        "dept_employ": "ส่งของ",
        "age_employ": 25,
        "tel_number": "0901234567",
        "salary": 17000,
        "total_hours_worked": 215  # OT 15 ชั่วโมง
    }
]

# เรียกใช้งานฟังก์ชันกับข้อมูลพนักงาน
for emp in employees:
    calculate_income(**emp)
